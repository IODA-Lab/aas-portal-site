# -*- coding: utf-8 -*-
"""Stage 1: 장비개발계획서(HWPX) → 정규화 매핑표(JSON).

계획서 표준 양식(참조모델 개발계획서)을 결정론적으로 파싱한다.
- 큰 폼 표(table[0])의 행을 순회해 장비명·서브모델 구간(#01..#0N)·담당자로 분절
- 각 서브모델의 '2.3 개발방법'에서 템플릿 종류(IDTA/자체/외부)와 IDTA 번호 추출
- 각 서브모델의 '2.4 프로퍼티 목록' 셀에서 헤딩(그룹) + 중첩표(프로퍼티 행) → 요소 계층 복원
- 프로퍼티 행: [SME Type, idShort, 정의(ko), 예시, semanticId] → valueType·unit 추론

에이전트/LLM 없음. HWP는 한컴 COM으로 HWPX 변환 후 이 파서를 태운다(convert 참고).
"""
import re, json, zipfile
from lxml import etree

HP = '{http://www.hancom.co.kr/hwpml/2011/paragraph}'
def q(t): return HP + t
def _txt(e): return ''.join(e.itertext())

# ---------------- valueType / unit 추론 ----------------
_UNITS = r'(kg|mm/s2|mm/s|mm|m/s2|m/min|cm/min|cm|µm|um|deg/s|deg|°/s|°|kVA|VA|kW|W|MPa|kPa|Pa|bar|V|A|Hz|%RH|%|Cel|℃|s|h|N|cycle|rpm)'
_UNIT_RE = re.compile(r'(-?±?\d[\d,\.]*)\s*' + _UNITS + r'(?![\w/])', re.I)
# 예시값 '전체'가 "숫자 [단위]"일 때만 수치로 본다(문장 속 숫자·단위를 수치로 오인하지 않도록).
_UNIT_FULL = re.compile(r'^\s*(-?±?\s*\d[\d,]*(?:\.\d+)?)\s*' + _UNITS + r'?\s*$', re.I)
_UNIT_NORM = {'℃':'Cel','°':'deg','°/s':'deg/s','um':'um','µm':'um'}
_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
_DTIME = re.compile(r'^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}')
_NUMONLY = re.compile(r'^-?±?\s*\d[\d,]*(\.\d+)?$')
_COUNT_HINT = re.compile(r'(축|axes|axis|개|ea\b|매|블레이드|blade|hand|count|번|회|대)', re.I)

def infer_unit(example):
    if not example: return None
    m = _UNIT_FULL.match(example)
    if not m or not m.group(2): return None
    u = m.group(2)
    return _UNIT_NORM.get(u, u)

def infer_valuetype(sme_type, example):
    """SME Type + 예시값으로 basyx valueType 문자열 반환."""
    st = (sme_type or '').strip()
    if st in ('MLP', 'File', 'Range', 'SMC', 'SML'):
        return st
    ex = (example or '').strip()
    if not ex:
        return 'String'
    low = ex.lower()
    if low in ('true', 'false', 'yes', 'no', 'on', 'off'):
        return 'Boolean'
    if _DTIME.match(ex): return 'dateTime'
    if _DATE.match(ex): return 'Date'
    # 숫자? (예시 전체가 "숫자 [단위]"인 단일 수치만. "8/12/16 mm 피더"처럼 문장 속 수치는 문자열)
    um = _UNIT_FULL.match(ex)
    if um is None:
        return 'String'
    num = um.group(1)
    has_unit = bool(um.group(2))
    if _NUMONLY.match(num.strip()):
        # 정수 & 단위없음/카운트힌트 → Int, 그 외 → Float
        is_int = ('.' not in num)
        if is_int and (not has_unit or _COUNT_HINT.search(ex)):
            return 'Int'
        return 'Float'
    return 'String'

# ---------------- 헤딩 파싱 ----------------
_HEAD = re.compile(r'^\s*\d+\.\s*(.+?)\s*$')
def parse_heading(text):
    """'3. TechnicalProperties / MechanicalStructure' -> ['TechnicalProperties','MechanicalStructure']
       '1. GeneralInformation' -> ['GeneralInformation']. 아니면 None."""
    t = text.strip().replace('\n', ' ')
    m = _HEAD.match(t)
    if not m: return None
    body = m.group(1).strip()
    # '[0]'은 SML(반복 목록) 익명 항목의 위치 표기(idShort 아님). 반복 항목은 _slot()이 복원하므로 경로에서 뺀다.
    parts = [p.strip() for p in body.split('/') if not re.fullmatch(r'\s*\[\d+\]\s*', p)]
    # idShort 형태(영문/숫자) 인지 최소 확인
    if not parts or not re.match(r'^[A-Za-z][\w]*$', parts[-1]):
        return None
    return parts

# ---------------- 표(프로퍼티) 파싱 ----------------
def parse_prop_table(tb):
    """프로퍼티 표 → [{sme,idShort,def_ko,example,semanticId}] (헤더행 제외)."""
    rows = tb.findall(q('tr'))
    out = []
    for tr in rows:
        cells = {}
        for tc in tr.findall(q('tc')):
            ca = tc.find(q('cellAddr'))
            if ca is None: continue
            cells[int(ca.get('colAddr'))] = _txt(tc).strip()
        c0 = cells.get(0, '')
        if c0 in ('SME Type', '') or c0.startswith('SME'):
            continue  # 헤더 또는 빈 행
        out.append({
            'sme': c0,
            'idShort': cells.get(1, '').replace('\n', ' ').strip(),
            'def_ko': cells.get(2, '').strip(),
            'example': cells.get(3, '').strip(),
            'semanticId': cells.get(4, '').strip(),
        })
    return out

def _leaf_node(r):
    st = (r['sme'] or '').strip()
    if st in ('Ref', 'ReferenceElement'):
        return {'type': 'Ref', 'idShort': r['idShort'], 'valueType': 'Ref',
                'def_ko': r['def_ko'], 'example': r['example'],
                'semanticId': r['semanticId'], 'unit': None}
    vt = infer_valuetype(r['sme'], r['example'])
    return {
        'type': vt if vt in ('MLP', 'File', 'Range') else 'Prop',
        'idShort': r['idShort'], 'valueType': vt,
        'def_ko': r['def_ko'], 'example': r['example'],
        'semanticId': r['semanticId'], 'unit': infer_unit(r['example']),
    }

# SML(반복 목록)의 반복 항목 이름. 계획서는 반복 항목을 평탄화해 항목의 필드만 보여 주므로
# 파서가 항목(래퍼 SMC)을 복원한다. 생성기에서 항목 idShort는 비워진다(AASd-120).
_SML_ITEM = {"ProductImages": "ProductImage", "ProductClassifications": "ProductClassification",
             "TechnicalPropertyAreas": "TechnicalPropertyArea", "SpecificDescriptions": "SpecificDescription",
             "ListRULBoundaryConditions": "RULCondition", "ListPreAlerts": "PreAlert",
             "Markings": "Marking", "Documents": "Document"}
_CONTAINERS = ('SMC', 'SML', 'Entity')

def _key(s):
    """표 셀 idShort → 경로 키(끝의 '(MLP)' 같은 주석 제거)."""
    return re.sub(r'\s*\([^)]*\)\s*$', '', (s or '').replace('\n', ' ')).strip()

def _item_name(sml):
    if sml in _SML_ITEM:
        return _SML_ITEM[sml]
    n = sml[4:] if (sml.startswith('List') and len(sml) > 4) else sml
    return n[:-1] if (n.endswith('s') and len(n) > 1) else n + 'Item'

def _new_container(st, idshort, def_ko='', sem=''):
    node = {'type': st, 'idShort': idshort, 'def_ko': def_ko, 'semanticId': sem, 'children': []}
    if st == 'SML':
        node['children'] = [{'type': 'SMC', 'idShort': _item_name(_key(idshort)), 'def_ko': '',
                             'semanticId': '', 'children': [], 'list_item': True}]
    return node

def _slot(node):
    """노드의 자식이 들어갈 리스트. SML이면 반복 항목(래퍼)의 children."""
    ch = node['children']
    if node.get('type') == 'SML' and ch and ch[0].get('list_item'):
        return ch[0]['children']
    return ch

def parse_property_cell(cell):
    """서브모델 2.4 셀 subList → 요소 계층(list of nodes). 세 가지 표기를 모두 처리:
      (1) 헤딩 'N. A' / 'N. A / B' (idShort형) → 그룹 계층(경로)
      (2) 표 안 SME Type='SMC'/'SML'/'Entity' 행 → 컨테이너.
          - 뒤에 그 경로의 헤딩이 나오면(선박·FPD 최종 계획서 형식) 컨테이너는 형제로만 등록되고
            내용은 그 헤딩의 표에서 채워진다(같은 경로 = 같은 노드, 중복 생성 없음).
          - 헤딩이 없으면(초기 계획서 형식) 이후 leaf 행이 그 컨테이너의 자식이 된다.
      (3) SML은 반복 항목(래퍼 SMC)을 하나 두고, 계획서에 평탄화된 항목 필드를 그 안에 넣는다.
    번호가 붙었지만 idShort형이 아닌 제목(예: '0. 최상위 구성')은 최상위로 되돌린다.
    node = {type:'SMC'|'SML'|'Entity', idShort, children:[...]} 또는 leaf {type,idShort,valueType,def_ko,example,semanticId,unit}
    """
    sub = cell.find(q('subList'))
    if sub is None:
        return [], ''
    items, intro = [], ''
    for ch in sub:
        if etree.QName(ch).localname != 'p':
            continue
        tb = ch.find('.//' + q('tbl'))
        text = _txt(ch).strip()
        if tb is None:
            if text.startswith('※') and not intro:
                intro = text
            head = parse_heading(text) if text else None
            if head:
                items.append(('head', tuple(head)))
            elif text and re.match(r'^\s*\d+\.\s', text):
                items.append(('label', None))
            continue
        items.append(('table', parse_prop_table(tb)))
    # 헤딩 경로의 모든 접두 경로(= 뒤에서 내용이 채워질 컨테이너)
    head_prefixes = set()
    for kind, val in items:
        if kind == 'head':
            for k in range(1, len(val) + 1):
                head_prefixes.add(val[:k])

    top, index = [], {}
    def slot_for(path):
        return top if not path else _slot(index[path])
    cur_path, cur_list, scope = (), top, None
    for kind, val in items:
        if kind == 'label':
            cur_path, cur_list, scope = (), top, None
            continue
        if kind == 'head':
            parent = ()
            for part in val:
                key = parent + (part,)
                if key not in index:
                    # 제목으로만 생기는 컨테이너: 공식 템플릿에서 SML로 정해진 이름이면 SML(반복 항목 포함)로
                    node = _new_container('SML' if part in _SML_ITEM else 'SMC', part)
                    slot_for(parent).append(node)
                    index[key] = node
                parent = key
            cur_path, cur_list, scope = val, slot_for(val), None
            continue
        for r in val:
            st = (r['sme'] or '').strip()
            if st in _CONTAINERS:
                key = cur_path + (_key(r['idShort']),)
                if key in index:                      # 헤딩이 먼저 만든 노드 → 종류·의미 정보 보강
                    node = index[key]
                    if node['type'] != st:
                        kids = _slot(node)
                        repl = _new_container(st, node['idShort'])
                        _slot(repl).extend(kids)
                        node.clear(); node.update(repl)
                    node['def_ko'] = node.get('def_ko') or r['def_ko']
                    node['semanticId'] = node.get('semanticId') or r['semanticId']
                else:
                    node = _new_container(st, r['idShort'], r['def_ko'], r['semanticId'])
                    cur_list.append(node)
                    index[key] = node
                # 뒤에 이 경로의 헤딩이 있으면 형제로만 등록, 없으면 이후 leaf 행의 부모(초기 형식)
                scope = None if key in head_prefixes else _slot(node)
            else:
                (scope if scope is not None else cur_list).append(_leaf_node(r))
    return top, intro

# ---------------- 개발방법(템플릿) 파싱 ----------------
_IDTA_NUM = re.compile(r'(\d{5}(?:-\d+){0,3})')
def parse_dev_method(text):
    """'2.3 개발 방법' 텍스트 → {template:'IDTA|self|external', template_name, idta_no}"""
    t = text.replace('\n', ' ')
    checked = None
    if '☑ IDTA' in t or '☑IDTA' in t or ('IDTA 서브모델 템플릿' in t and '☑' in t.split('IDTA')[0][-3:]):
        checked = 'IDTA'
    if '자체 제작' in t and '☑ 자체' in t:
        checked = 'self'
    if '외부 서브모델' in t and '☑ 외부' in t:
        checked = 'external'
    # 체크 표식이 애매하면 키워드로 보정
    if checked is None:
        if '자체 제작 사유' in t: checked = 'self'
        elif 'IDTA 서브모델 템플릿 활용 이유' in t: checked = 'IDTA'
    name = None
    mn = re.search(r'서브모델 템플릿 명[:：]\s*([^\n버]+)', text)
    if mn: name = mn.group(1).strip()
    no = None
    # 템플릿 번호는 '추가 계획' 문장 이전에서만 찾는다(예: 'AGV 전용 템플릿(IDTA 02047)은 사용하지 않음' 오인 방지)
    head_part = t.split('대상 장비/공정 특화')[0]
    mnum = _IDTA_NUM.search(head_part)
    if mnum: no = mnum.group(1)
    return {'template': checked or 'unknown', 'template_name': name, 'idta_no': no}

# ---------------- 메인 파싱 ----------------
def _split_outside_parens(s):
    """괄호 밖의 '/'로만 나눈다. 예: 'SMD 마운터(SMD Mounter / Chip Mounter) / 장착 공정'."""
    parts, depth, cur = [], 0, ''
    for chx in s:
        if chx in '(（': depth += 1
        elif chx in ')）': depth = max(0, depth - 1)
        if chx == '/' and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += chx
    parts.append(cur)
    return parts

def _camel(en):
    words = re.findall(r'[A-Za-z0-9]+', en or '')
    return ''.join(w[:1].upper() + w[1:] for w in words) or 'Equipment'

def parse_plan_hwpx(hwpx_path):
    try:
        with zipfile.ZipFile(hwpx_path) as z:
            xml = z.read('Contents/section0.xml')
        root = etree.fromstring(xml)
    except Exception:
        raise ValueError("한글 계획서(.hwpx)를 열지 못했습니다. 파일이 손상됐거나 hwpx 형식이 아닙니다.")
    tbl0 = None
    for tb in root.iter(q('tbl')):
        tbl0 = tb; break  # 첫(최외곽) 표 = 폼 표
    if tbl0 is None:
        raise ValueError("계획서 양식의 표를 찾지 못했습니다. 장비개발계획서(.hwp/.hwpx)가 맞는지 확인하세요.")
    rows = tbl0.findall(q('tr'))

    def row_text(i): return _txt(rows[i]).replace('\n', ' ').strip()
    def row_cell(i, col):
        for tc in rows[i].findall(q('tc')):
            ca = tc.find(q('cellAddr'))
            if ca is not None and int(ca.get('colAddr')) == col:
                return _txt(tc).strip()
        return ''

    equip = {'name_ko': '', 'name_en': '', 'manager': ''}
    submodels = []
    cur = None
    field = None  # 현재 어떤 2.x 필드를 읽는 중인지
    for i, tr in enumerate(rows):
        label = _txt(tr.findall(q('tc'))[0]).replace('\n', ' ').strip() if tr.findall(q('tc')) else ''
        full = _txt(tr).replace('\n', ' ').strip()
        # 장비명
        if '장비/공정 명' in label or (i+1 < len(rows) and False):
            val = row_cell(i, 1) or row_text(i+1)
        if label.startswith('1.') and '장비' in label and not equip['name_ko']:
            # 장비명은 처음 한 번만 설정(서브모델 내부에도 '1. ...장비...' 헤딩이 있어 덮어쓰기 방지).
            # 다음 행이 장비명 값. 영어명은 "이름 부분(/앞)"에서만 찾는다
            # (설명 문장 안의 괄호 영문, 예: 수직전기동도금/...(PCB)...을 장비명으로 오인하지 않도록)
            if i+1 < len(rows):
                nm = _txt(rows[i+1]).strip()
                name_part = _split_outside_parens(nm)[0].strip()   # 괄호 밖 첫 '/' 앞 = 장비명
                # 짧은 영문 괄호만 영어명으로(이름 부분 내, 40자 이내)
                men = re.search(r'\(([^)]*[A-Za-z][^)]*)\)', name_part)
                if men and len(men.group(1)) <= 40:
                    # 괄호 안에 별칭이 '/'로 이어지면 첫 이름만(예: 'SMD Mounter / Chip Mounter' → 'SMD Mounter')
                    equip['name_en'] = men.group(1).split('/')[0].strip()
                # 한글명은 영문 괄호를 떼어 깔끔하게(파일명용). 예: '선박 용접용 로봇(Ship..)'→'선박 용접용 로봇'
                equip['name_ko'] = re.sub(r'\s*\([^)]*\)\s*', '', name_part).strip() or name_part
            continue
        # 서브모델 시작
        m08 = re.search(r'서브모델\s*\(#(\d+)\)', full) or re.search(r'서브모델\(#(\d+)\)', label)
        if m08:
            cur = {'no': int(m08.group(1)), 'idShort': '', 'necessity': '',
                   'dev': {}, 'elements': [], 'intro': ''}
            submodels.append(cur)
            # 같은 행 오른쪽 셀에 '2.1 서브모델 명' 라벨, 다음 행에 이름
            field = 'name'
            continue
        if cur is not None:
            if label.startswith('2.1') or '서브모델(Submodel) 명' in full:
                field = 'name'; continue
            if label.startswith('2.2') or '서브모델 필요성' in label:
                field = 'necessity'; continue
            if label.startswith('2.3') or '서브모델 개발 방법' in label:
                field = 'dev'; continue
            if label.startswith('2.4') or '프로퍼티' in label and '목록' in label:
                field = 'prop'; continue
            if label.startswith('2.5') or '데이터 수집' in label:
                field = 'data'; continue
            if label.startswith('3.') and '담당자' in label:
                # 담당자 정보 섹션: 바로 다음 행이 담당자 이름(예: '서영건'). 처음 한 번만.
                if not equip['manager'] and i+1 < len(rows):
                    mnm = _txt(rows[i+1]).strip().split('\n')[0].strip()
                    if (':' in mnm) or ('：' in mnm):
                        mnm = re.split(r'[:：]', mnm)[-1].strip()
                    parts = mnm.split()
                    equip['manager'] = parts[0] if parts else mnm
                cur = None; field = None; continue
            # 값 행(라벨 셀이 아닌 내용 행)
            if field == 'name' and not cur['idShort'] and full:
                cur['idShort'] = full
                field = None
            elif field == 'necessity':
                cur['necessity'] = (cur['necessity'] + ' ' + full).strip()
            elif field == 'dev':
                cur['dev'] = parse_dev_method(_txt(tr))
                field = None
            elif field == 'prop':
                cell = tr.findall(q('tc'))[0]
                els, intro = parse_property_cell(cell)
                if els:
                    cur['elements'] = els; cur['intro'] = intro
                    field = None
    aas_name = _camel(equip['name_en'])
    return {'equipment': equip, 'aas_name': aas_name, 'submodels': submodels}


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.exit("사용: python parse_plan.py <계획서.hwpx> [mapping.json]")
    path = sys.argv[1]
    data = parse_plan_hwpx(path)
    out = sys.argv[2] if len(sys.argv) > 2 else 'mapping.json'
    json.dump(data, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('장비:', data['equipment'], '| aas_name:', data['aas_name'])
    print('서브모델 수:', len(data['submodels']))
    def count_leaves(nodes):
        n = 0
        for nd in nodes:
            if nd.get('children'): n += count_leaves(nd['children'])
            else: n += 1
        return n
    for s in data['submodels']:
        print(f"  #{s['no']:02} {s['idShort']:24} tmpl={s['dev'].get('template'):8} idta={s['dev'].get('idta_no')} "
              f"요소(leaf)={count_leaves(s['elements'])}")
    print('-> 저장:', out)
