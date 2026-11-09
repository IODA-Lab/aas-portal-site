# -*- coding: utf-8 -*-
"""Stage 2: 매핑표(JSON) → 검증통과 AASX(.aasx/.json/.xml).

- 요소·값·semanticId는 계획서(매핑표)에 적힌 그대로 사용
- 서브모델 semanticId: 표준 IDTA 서브모델 → IDTA 표준 semanticId(idta_semantics.json),
  자체 제작 → smart-factory.kr IRI 자체정의 (가장 흔한 오류 방지)
- KOSMO/IDTA 통과용 수정 내장: assetKind=Type·kind=Template, IEC61360 CD(dataType+단위),
  측정형은 단위 필수(없으면 COUNT로 대체), SML 원소 id_short=None(semanticId 유지),
  File 값 비움, 대표 이미지(thumbnail) 패키징
- 표준 서브모델인데 계획서에 프로퍼티가 없으면(DN·HD: '변경없이 추가') IDTA 템플릿 요소를 그대로 복사

에이전트/LLM 없음. basyx는 anaconda python으로 실행.
"""
import os, sys, json, re, copy, base64, datetime as _dtm
from basyx.aas import model as m
import basyx.aas.model.datatypes as dt
from basyx.aas.model import DictObjectStore, Submodel, ConceptDescription
from basyx.aas.adapter.json import write_aas_json_file
from basyx.aas.adapter.xml import write_aas_xml_file
from basyx.aas.adapter.aasx import AASXWriter, AASXReader, DictSupplementaryFileContainer
import contextlib as _ctx, logging as _logging


@_ctx.contextmanager
def _quiet_basyx():
    """공식 템플릿 원본을 읽을 때만 basyx 오류 로그를 숨긴다. 원본 자체의 id 중복(IDTA 02031 서브모델 id = CD id,
    IDTA 02048 RULCondition CD 2개) 때문에 'duplicate identifier ... skipping it'이 찍혀 사용자 창에 오류처럼 보이기 때문.
    생성한 AASX를 다시 읽는 검사(round-trip·validate)에는 쓰지 않는다."""
    lg = _logging.getLogger("basyx"); old = lg.level; lg.setLevel(_logging.CRITICAL)
    try:
        yield
    finally:
        lg.setLevel(old)

HERE = os.path.dirname(os.path.abspath(__file__))
def _res(rel):
    """번들 리소스 경로. PyInstaller(.exe)에서는 sys._MEIPASS, 아니면 소스 폴더."""
    base = getattr(sys, "_MEIPASS", HERE)
    return os.path.join(base, rel)
NS = "https://www.smart-factory.kr/ids"
_IEC = "https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/0"

IDTA_SEM = json.load(open(_res("idta_semantics.json"), encoding="utf-8"))["standard_submodels"]
# 재사용 한글 설명 사전(표준 IDTA 요소 + 상세 한글). idShort -> 한글 설명.
try:
    KO_STD = json.load(open(_res("ko_descriptions.json"), encoding="utf-8"))
except (OSError, ValueError):
    KO_STD = {}
# alias(소문자·공백제거) -> 표준키
_ALIAS = {}
for k, info in IDTA_SEM.items():
    for a in [k] + info.get("aliases", []):
        _ALIAS[re.sub(r"\s+", "", a).lower()] = k

_VT = {"String": dt.String, "Float": dt.Double, "Int": dt.Int, "Long": dt.Long, "Boolean": dt.Boolean,
       "dateTime": dt.DateTime, "Date": dt.Date, "Range": dt.Double, "MLP": None, "File": None}
IEC_DT = {"String": "STRING", "Float": "REAL_MEASURE", "Int": "INTEGER_COUNT", "Long": "INTEGER_COUNT", "Boolean": "BOOLEAN",
          "Date": "DATE", "dateTime": "TIMESTAMP", "Range": "REAL_MEASURE", "MLP": "STRING", "File": "STRING"}

_PLACEHOLDER_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==")

# ---------------- 값 파싱 ----------------
_NUM = re.compile(r"-?\d[\d,]*\.?\d*")
def _num(ex):
    if ex is None: return None
    s = str(ex).replace("±", "").replace(",", "")
    mm = _NUM.search(s)
    return mm.group(0) if mm else None

def _range(ex):
    if ex is None: return (None, None)
    s = str(ex)
    nums = _NUM.findall(s.replace(",", ""))
    if "±" in s and nums:
        v = abs(float(nums[0])); return (-v, v)
    if len(nums) >= 2:
        return (float(nums[0]), float(nums[1]))
    if len(nums) == 1:
        return (float(nums[0]), float(nums[0]))
    return (None, None)

def _cast(vt, ex):
    if ex is None or ex == "": return None
    try:
        if vt is dt.DateTime: return _dtm.datetime.fromisoformat(str(ex).replace("Z", "+00:00"))
        if vt is dt.Date:
            y, mo, d = [int(x) for x in re.findall(r"\d+", str(ex))[:3]]; return dt.Date(y, mo, d)
        if vt is dt.Boolean: return str(ex).strip().lower() in ("true", "1", "yes", "on")
        if vt is dt.Int or vt is dt.Long:
            n = _num(ex); return (dt.Long(int(float(n))) if vt is dt.Long else int(float(n))) if n is not None else None
        if vt is dt.Double:
            n = _num(ex); return float(n) if n is not None else None
        return str(ex)
    except Exception:
        return None

_LANG_TAG = re.compile(r"@([a-z]{2}(?:-[A-Za-z]{2})?)\s*$")
def _mlp_value(ex):
    """계획서 다국어 예시 → MultiLanguageTextType.
    'Text@en', 'A@en; B@ko'(모든 조각에 언어 태그가 있을 때만 분리). 태그가 없으면 한글 포함 시 ko, 아니면 en."""
    if ex is None or str(ex).strip() == "":
        return None
    s = str(ex).strip()
    parts = [p.strip() for p in s.split(";")]
    if not (len(parts) > 1 and all(_LANG_TAG.search(p) for p in parts)):
        parts = [s]
    d = {}
    for p in parts:
        mm = _LANG_TAG.search(p)
        if mm:
            lang, text = mm.group(1), p[:mm.start()].strip()
        else:
            lang, text = ("ko" if re.search("[가-힣]", p) else "en"), p
        if text and lang not in d:
            d[lang] = text
    return m.MultiLanguageTextType(d) if d else None

def clean_idshort(s):
    s = re.sub(r"\s*\([^)]*\)\s*$", "", (s or "").strip())   # 끝의 '(MLP)' 등 제거
    s = re.sub(r"[^0-9A-Za-z_]", "", s)                       # idShort 허용문자만
    if not s: return "Item"
    if not re.match(r"[A-Za-z_]", s): s = "C_" + s            # idShort는 문자/밑줄로 시작
    return s

def _camel(en):
    return "".join(w[:1].upper() + w[1:] for w in re.findall(r"[A-Za-z0-9]+", en or "")) or "Equipment"

# ---------------- semanticId / CD ----------------
class Gen:
    def __init__(self, aas_name, equip_en):
        self.aas_name = aas_name; self.equip_en = equip_en or aas_name
        self.used = {}   # sid -> dict(idShort, iec, unit, def_ko)
        self.needs_review = []

    def semref(self, sid, idShort, iec="STRING", unit=None, def_ko=""):
        if not sid:
            sid = f"{NS}/cd/{clean_idshort(idShort)}/1/0"
            self.needs_review.append(f"{idShort}: semanticId 비어 자체정의로 대체")
        self.used.setdefault(sid, {"idShort": clean_idshort(idShort), "iec": iec, "unit": unit, "def_ko": def_ko})
        return m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, sid),))

    def desc(self, en, ko=None):
        d = {"en": en}
        if ko: d["ko"] = ko
        return m.MultiLanguageTextType(d)

    def _dedup(self, elements):
        """같은 레벨 idShort 중복 시 접미사(2,3..)로 유일화 (AASd-022). id_short=None은 건너뜀."""
        seen = {}
        for el in elements:
            ish = getattr(el, "id_short", None)
            if ish is None: continue
            if ish in seen:
                seen[ish] += 1
                el.id_short = f"{ish}{seen[ish]}"
                self.needs_review.append(f"{ish}: 같은 레벨 중복 → {el.id_short}로 유일화")
            else:
                seen[ish] = 1
        return elements

    # ---- 요소(leaf/컨테이너) 빌드 ----
    def leaf(self, node, no_ids=False):
        ish = clean_idshort(node["idShort"])
        vt_str = node.get("valueType", "String")
        iec = IEC_DT.get(vt_str, "STRING")
        unit = node.get("unit")
        sem = self.semref(node.get("semanticId"), ish, iec, unit, node.get("def_ko", ""))
        d = self.desc(f"{ish} of the {self.equip_en}", node.get("def_ko") or None)
        ex = node.get("example")
        if vt_str == "MLP":
            val = _mlp_value(ex)
            el = m.MultiLanguageProperty(id_short=ish, value=val, semantic_id=sem, description=d)
        elif vt_str == "Ref" or node.get("type") == "Ref":
            # ReferenceElement: Type 수준에서는 참조 대상이 없으므로 값 없이 구조만 둔다.
            el = m.ReferenceElement(id_short=ish, value=None, semantic_id=sem, description=d)
        elif vt_str == "File":
            el = m.File(id_short=ish, content_type="application/octet-stream", value=None, semantic_id=sem, description=d)
        elif vt_str == "Range":
            lo, hi = _range(ex)
            el = m.Range(id_short=ish, value_type=dt.Double,
                         min=(float(lo) if lo is not None else None),
                         max=(float(hi) if hi is not None else None), semantic_id=sem, description=d)
        else:
            vt = _VT.get(vt_str, dt.String)
            val = _cast(vt, ex)
            if val is None and ex not in (None, ""):
                vt, val = dt.String, str(ex)
            el = m.Property(id_short=ish, value_type=vt, value=val, semantic_id=sem, description=d)
        if no_ids:
            el.id_short = None
        return el

    def build(self, node, no_ids=False):
        typ = node.get("type")
        if typ == "Entity":
            ish = clean_idshort(node["idShort"])
            sem = self.semref(node.get("semanticId"), ish, "STRING", None, node.get("def_ko", ""))
            kids = self._dedup([self.build(ch, no_ids=False) for ch in node.get("children", [])])
            return m.Entity(id_short=(None if no_ids else ish), entity_type=m.EntityType.CO_MANAGED_ENTITY,
                            statement=kids, semantic_id=sem, description=self.desc(f"{ish} entity"))
        if typ in ("SMC", "SML"):
            ish = clean_idshort(node["idShort"])
            if node.get("list_item") and not node.get("semanticId"):
                # 파서가 복원한 SML 반복 항목(래퍼): 의미는 상위 SML의 list element로 정해지므로 검토 대상 아님
                sid = f"{NS}/cd/{ish}/1/0"
                self.used.setdefault(sid, {"idShort": ish, "iec": "STRING", "unit": None, "def_ko": ""})
                sem = m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, sid),))
            else:
                sem = self.semref(node.get("semanticId"), ish, "STRING", None, node.get("def_ko", ""))
            kids_nodes = node.get("children", [])
            if typ == "SML":
                built = [self.build(ch, no_ids=False) for ch in kids_nodes]
                # AASd-108: SML 원소는 전부 동일 타입(SMC)이어야 함.
                # 자식이 없거나 전부 SMC면 진짜 SML, 아니면(leaf/혼합) SMC로 대체해 유효성 보장.
                if (not built) or all(isinstance(b, m.SubmodelElementCollection) for b in built):
                    child_name = clean_idshort(kids_nodes[0]["idShort"]) if kids_nodes else ish
                    # AASd-107: 자식이 공식 semanticId를 가지면 list_element도 동일값으로(자식 원 sem 보존).
                    child_sid = kids_nodes[0].get("semanticId") if kids_nodes else None
                    if not child_sid and kids_nodes and kids_nodes[0].get("list_item"):
                        child_sid = f"{NS}/cd/{child_name}/1/0"   # 공식 항목 sem은 kosmo_normalize(LIST_ITEM_OFFICIAL)가 복원
                    le_ref = self.semref(child_sid, child_name) if child_sid else self.semref(None, child_name)
                    le_val = le_ref.key[0].value
                    for b in built:
                        b.id_short = None
                        b.semantic_id = m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, le_val),))
                    return m.SubmodelElementList(id_short=(None if no_ids else ish),
                                                 type_value_list_element=m.SubmodelElementCollection,
                                                 value=built, semantic_id=sem,
                                                 semantic_id_list_element=le_ref,
                                                 description=self.desc(f"{ish} list"))
                self.needs_review.append(f"{ish}: SML 자식이 비균질 → SMC로 대체(원 표기는 리스트)")
                return m.SubmodelElementCollection(id_short=(None if no_ids else ish), value=self._dedup(built),
                                                   semantic_id=sem, description=self.desc(f"{ish} collection"))
            kids = self._dedup([self.build(ch, no_ids=False) for ch in kids_nodes])
            smc = m.SubmodelElementCollection(id_short=(None if no_ids else ish), value=kids,
                                              semantic_id=sem, description=self.desc(f"{ish} collection"))
            return smc
        return self.leaf(node, no_ids=no_ids)

    # ---- ConceptDescription 생성 ----
    def make_cds(self, store):
        for sid, info in self.used.items():
            ish = info["idShort"]; iec = info["iec"]; unit = info["unit"]
            if iec.endswith("MEASURE") and not unit:
                iec = iec.replace("MEASURE", "COUNT")
            std = ("admin-shell.io" in sid) or ("0173-1" in sid)
            en = (f"{ish} of the {self.equip_en}." if std
                  else f"Self-defined concept for {ish} of the {self.equip_en} (no standard dictionary match).")
            ddict = {"en": en[:1023]}
            if info.get("def_ko"): ddict["ko"] = info["def_ko"][:1023]
            content = m.DataSpecificationIEC61360(
                preferred_name=m.PreferredNameTypeIEC61360({"en": ish[:255]}),
                data_type=getattr(m.DataTypeIEC61360, iec),
                definition=m.DefinitionTypeIEC61360(ddict))
            if iec.endswith("MEASURE") and unit:
                content.unit = unit
            eds = m.EmbeddedDataSpecification(
                data_specification=m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, _IEC),)),
                data_specification_content=content)
            store.add(m.ConceptDescription(id_=sid, id_short=ish, embedded_data_specifications=[eds]))


def kosmo_normalize(store, aas_name, equip_en, unit_map=None):
    """KOSMO 준수 정규화(최종 패스):
    - 서브모델 semanticId → smart-factory.kr/ids/sm/{AAS}/{SM}/1/0 (표준 IDTA 형식 거부됨)
    - 요소/CD semanticId → IRDI(0173-1)·smart-factory는 유지, 그 외(admin-shell.io 등) → /ids/cd/{idShort}/1/0
    - CD idShort 대문자 시작, 모든 CD에 dataType(valueType 기반), 측정형은 단위 있으면 MEASURE
    - CD 전면 재생성(템플릿의 admin-shell.io·dataType 없는 CD 제거)"""
    VT2K = {dt.String: "STRING", dt.AnyURI: "STRING", dt.Boolean: "BOOLEAN", dt.Date: "DATE",
            dt.DateTime: "TIMESTAMP", dt.Int: "INTEGER_COUNT", dt.Integer: "INTEGER_COUNT",
            dt.Long: "INTEGER_COUNT", dt.Short: "INTEGER_COUNT", dt.Duration: "STRING",
            dt.Double: "REAL_MEASURE", dt.Float: "REAL_MEASURE", dt.Decimal: "REAL_MEASURE"}
    # 공식 IDTA semanticId 오버라이드(검토 #70·#71): 자체 IRI로 남은 표준 컨테이너를 공식값으로 복원.
    # idShort로 매칭(컨테이너/래퍼). 서브모델 자체는 여기서 처리 안 함.
    OFFICIAL = {
        # Technical Data 2.0.1 표준 컨테이너(계획서가 비워도 공식값으로 복원)
        "GeneralInformation": "0173-1#02-ABK161#002/0173-1#01-AHX838#002",
        "ProductClassifications": "0173-1#02-ABK162#002",
        "TechnicalPropertyAreas": "0173-1#02-ABK163#002",
        # Process Parameters 1.0 표준 컨테이너
        "Processes": "https://admin-shell.io/idta/ProcessParameters/Processes/1/0",
        "ProductParameters": "https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0",
        "ProcessParameters": "https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0",
        "ResourceParameters": "https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0",
        "ProcessBoM": "https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0",
    }
    # SML의 list_element(반복 항목) 공식 semanticId (SML idShort → item sem)
    LIST_ITEM_OFFICIAL = {
        "TechnicalPropertyAreas": "0173-1#02-ABL358#002/0173-1#01-AHX773#002",
        "ProductImages": "0173-1#02-ABM220#001/0173-1#01-AHY911#001",
        "ProductClassifications": "0173-1#02-ABK162#002/0173-1#01-AHX839#002",
        "ListRULBoundaryConditions": "https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0",
        "ListPreAlerts": "https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0",
    }
    unit_map = unit_map or {}
    def up(ish):
        ish = clean_idshort(ish)
        return (ish[0].upper() + ish[1:]) if (ish and ish[0].islower()) else ish
    def keep(sid):
        """공식 표준 semanticId는 반드시 보존(IDTA '변경 없이 사용' 원칙, 검토 #71).
        - IRDI 계열: 0173-1#..., 0112/2///..., 0173/1///... 등 (숫자로 시작)
        - IDTA 공식 IRI: admin-shell.io (오타 admin-shell-io 포함)
        - 이미 자체정의된 smart-factory IRI
        그 외(빈 값·비공식)만 /ids/cd/{idShort}로 자체정의."""
        if not sid: return False
        s = sid.strip()
        if s.startswith(NS + "/"): return True
        if "admin-shell.io" in s or "admin-shell-io" in s: return True
        if "eclass-cdp.com" in s: return True          # ECLASS-CDP 공식 IRI(예: Handover OrganizationShortName)
        if re.match(r"^\d{3,4}[-/]", s): return True   # IRDI (0112/2///..., 0173-1#...)
        return False
    used = {}   # sid -> (idShort, dataType, unit)
    def reg(sid, ish, kd, unit):
        used.setdefault(sid, (ish, kd, unit))
    def newref(sid): return m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, sid),))
    def process(el):
        ish = up(el.id_short) if el.id_short else "Item"
        sref = getattr(el, "semantic_id", None)
        old = sref.key[0].value if (sref and sref.key) else None
        if (el.id_short in OFFICIAL):
            sid = OFFICIAL[el.id_short]
        else:
            sid = old if keep(old) else f"{NS}/cd/{ish}/1/0"
        el.semantic_id = newref(sid)
        # dataType
        unit = unit_map.get(ish) or unit_map.get(el.id_short or "")
        if isinstance(el, (m.SubmodelElementCollection, m.SubmodelElementList, m.Entity)):
            kd, unit = "STRING", None
        elif isinstance(el, m.MultiLanguageProperty): kd, unit = "STRING", None
        elif isinstance(el, m.File): kd, unit = "STRING", None
        elif isinstance(el, m.Range):
            kd = "REAL_MEASURE" if unit else "REAL_COUNT"
        elif isinstance(el, m.Property):
            # 공식 템플릿 자료형은 그대로 둔다(선제검토 #63: URIOfTheProduct는 IDTA 원본 xs:anyURI).
            # 예전에는 KOSMO 판정에 맞추려고 anyURI를 string으로 바꿨으나, 공식 원본 변경이라 하지 않는다.
            # #72: PlannedProcessTime은 IDTA 공식 xs:duration으로(값도 ISO8601 duration).
            # 계획서 값(예: PT25S)이 유효하면 그대로 쓰고, 없거나 읽을 수 없을 때만 25초 대표값.
            if el.id_short == "PlannedProcessTime":
                try:
                    from basyx.aas.model.datatypes import from_xsd as _fx
                    cur = el.value
                    if el.value_type is not dt.Duration or cur is None:
                        try:
                            cur = _fx(str(cur).strip(), dt.Duration) if cur not in (None, "") else None
                        except Exception:
                            cur = None
                    el.value_type = dt.Duration
                    el.value = cur if cur is not None else _fx("P0Y0M0DT0H0M25S", dt.Duration)
                except Exception: pass
            kd = VT2K.get(el.value_type, "STRING")
            if kd == "REAL_MEASURE" and not unit: kd = "REAL_COUNT"
            if kd not in ("REAL_MEASURE",): unit = None
        else:
            kd, unit = "STRING", None
        reg(sid, ish, kd, unit)
        if isinstance(el, m.SubmodelElementList):
            le = el.semantic_id_list_element
            lev = le.key[0].value if (le and le.key) else None
            lname = up((lev.split("/")[-1].split("#")[-1]) if lev else (ish + "Element"))
            # 항목(자식)의 기존 공식 sem(템플릿 유래) 확인 — list_element가 비어도 공식값 보존
            _c0 = list(el.value)[0] if el.value else None
            _c0sem = (_c0.semantic_id.key[0].value if (_c0 is not None and getattr(_c0,'semantic_id',None) and _c0.semantic_id.key) else None)
            if el.id_short in LIST_ITEM_OFFICIAL:
                lesid = LIST_ITEM_OFFICIAL[el.id_short]
            elif keep(lev):
                lesid = lev
            elif keep(_c0sem):
                lesid = _c0sem                          # 템플릿 항목의 공식 semanticId 승계
            else:
                lesid = f"{NS}/cd/{lname}/1/0"
            try: el._semantic_id_list_element = None          # 잠시 해제(AASd-107 회피)
            except Exception: pass
            for c in list(el.value):                          # 직속 자식 sem을 list_element로 통일
                try: c.semantic_id = newref(lesid)
                except Exception: pass
                gk = list(c.value) if isinstance(c, (m.SubmodelElementCollection, m.SubmodelElementList)) \
                     else (list(c.statement) if isinstance(c, m.Entity) else [])
                for gc in gk: process(gc)
            try: el._semantic_id_list_element = newref(lesid)
            except Exception: pass
            reg(lesid, lname, "STRING", None)
        elif isinstance(el, m.SubmodelElementCollection):
            for c in list(el.value): process(c)
        elif isinstance(el, m.Entity):
            for c in list(el.statement): process(c)
    # 서브모델 semanticId는 generate()에서 이미 설정(IDTA 표준/자체 IRI) — 여기선 요소·CD만 정규화
    for sm in [o for o in store if isinstance(o, Submodel)]:
        for e in list(sm.submodel_element): process(e)
    # CD 전면 재생성
    for cd in [o for o in store if isinstance(o, ConceptDescription)]:
        store.discard(cd)
    for sid, (ish, kd, unit) in used.items():
        content = m.DataSpecificationIEC61360(
            preferred_name=m.PreferredNameTypeIEC61360({"en": ish[:255]}),
            data_type=getattr(m.DataTypeIEC61360, kd),
            definition=m.DefinitionTypeIEC61360({"en": f"{ish} of the {equip_en}."[:1023]}))
        if kd.endswith("MEASURE") and unit: content.unit = unit
        eds = m.EmbeddedDataSpecification(
            data_specification=m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, _IEC),)),
            data_specification_content=content)
        store.add(m.ConceptDescription(id_=sid, id_short=ish, embedded_data_specifications=[eds]))
    return len(used)


def fill_examples(store, equip_en):
    """R24: 모든 value-bearing leaf에 예시값 필수. 빈 leaf에 타입·idShort 기반 비식별 합성 예시 채움.
    (템플릿 로드된 DN/HD/FS/PdM 등 예시 없는 leaf 대상. File은 Type 템플릿 관례상 value=None 유지.)"""
    import datetime as _d
    def synth(el):
        ish = el.id_short or "Value"; low = ish.lower()
        vt = el.value_type
        if vt is dt.Boolean: return False
        if vt is dt.Int: return 1
        if vt is dt.Double: return 1.0
        if vt is dt.Date: return dt.Date(2026, 1, 1)
        if vt is dt.DateTime: return _d.datetime(2026, 1, 1, 0, 0, 0, tzinfo=_d.timezone(_d.timedelta(hours=9)))
        # String 계열: idShort 힌트
        if "date" in low: return "2026-01-01"
        if "year" in low: return "2026"
        if "version" in low: return "1.0"
        if any(k in low for k in ("uri", "url")): return f"https://www.smart-factory.kr/example/{ish}"
        if any(k in low for k in ("id", "number", "code", "serial")): return f"EXAMPLE-{ish}"
        return f"Example {ish}"
    n = 0
    def visit(el):
        nonlocal n
        if isinstance(el, m.SubmodelElementCollection):
            for c in list(el.value): visit(c)
        elif isinstance(el, m.SubmodelElementList):
            for c in list(el.value): visit(c)
        elif isinstance(el, m.Entity):
            for c in list(el.statement): visit(c)
        elif isinstance(el, m.MultiLanguageProperty):
            if not el.value or len(el.value) == 0:
                ish = el.id_short or "Value"
                el.value = m.MultiLanguageTextType({"en": f"Example {ish}", "ko": f"예시 {ish}"}); n += 1
        elif isinstance(el, m.Range):
            if el.min is None and el.max is None:
                vt = getattr(el, "value_type", None)
                if vt in (dt.Double, dt.Float, dt.Decimal): lo, hi = 0.0, 1.0
                elif vt in (dt.Int, dt.Integer, dt.Long, dt.Short, dt.Byte): lo, hi = 0, 1
                elif vt is dt.Date: lo, hi = dt.Date(2026, 1, 1), dt.Date(2026, 12, 31)
                else: lo = hi = None   # 문자 등 범위에 부적합한 타입은 채우지 않음(크래시 방지)
                if lo is not None:
                    try: el.min, el.max = lo, hi; n += 1
                    except Exception: pass
        elif isinstance(el, m.Property):
            if el.value is None or el.value == "":
                try: el.value = synth(el); n += 1
                except Exception: pass
    for sm in [o for o in store if isinstance(o, Submodel)]:
        for e in sm.submodel_element: visit(e)
    return n


def fill_missing_cds(store, equip_en):
    """참조된 모든 semanticId에 CD가 있도록 누락분을 최소 IEC61360 CD로 생성(댕글링 방지, KOSMO CD-presence)."""
    from basyx.aas.model import SubmodelElementCollection as _SMC, SubmodelElementList as _SML
    have = {o.id for o in store if isinstance(o, ConceptDescription)}
    refs = {}
    def _rec(sid, ish):
        if sid and sid not in refs: refs[sid] = ish
    def visit(el):
        if getattr(el, "semantic_id", None) and el.semantic_id.key:
            _rec(el.semantic_id.key[0].value, getattr(el, "id_short", None) or "Concept")
        if isinstance(el, _SML) and getattr(el, "semantic_id_list_element", None) and el.semantic_id_list_element.key:
            _rec(el.semantic_id_list_element.key[0].value, "Element")
        if isinstance(el, (_SMC, _SML)):
            for c in list(el.value): visit(c)
    # 서브모델 semanticId는 템플릿 개념 참조라 CD 불필요(기존 통과본과 동일) → 요소만 대상
    for sm in [o for o in store if isinstance(o, Submodel)]:
        for e in sm.submodel_element: visit(e)
    n = 0
    for sid, ish in refs.items():
        if sid in have: continue
        if ish and ish.startswith(_HACK): ish = None       # hack placeholder는 이름으로 쓰지 않음
        ishc = clean_idshort(ish) if ish else _clean_from_sid(sid)
        content = m.DataSpecificationIEC61360(
            preferred_name=m.PreferredNameTypeIEC61360({"en": ishc[:255]}),
            data_type=m.DataTypeIEC61360.STRING,
            definition=m.DefinitionTypeIEC61360({"en": f"Concept referenced by {equip_en} model ({ishc})."[:1023]}))
        eds = m.EmbeddedDataSpecification(
            data_specification=m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, _IEC),)),
            data_specification_content=content)
        try:
            store.add(m.ConceptDescription(id_=sid, id_short=ishc, embedded_data_specifications=[eds])); n += 1
        except Exception:
            pass
    return n


def resolve_std(sm_name):
    key = _ALIAS.get(re.sub(r"\s+", "", sm_name or "").lower())
    return (key, IDTA_SEM[key]) if key else (None, None)


_HACK = "generated_submodel_list_hack_"
def _clean_from_sid(sid):
    if not sid: return "Item"
    seg = re.split(r"[\/#]", str(sid).rstrip("/"))[-1]
    return clean_idshort(seg) or "Item"

def sanitize_ids(el, parent_is_sml):
    """basyx가 템플릿 재파싱 시 붙인 'generated_submodel_list_hack_*' id_short 정리.
    SML 직속 원소 → None(AASd-120), 그 외 → semanticId 기반 이름."""
    ish = getattr(el, "id_short", None)
    if ish and ish.startswith(_HACK):
        if parent_is_sml:
            try: el.id_short = None
            except Exception: pass
        else:
            sid = el.semantic_id.key[0].value if (getattr(el, "semantic_id", None) and el.semantic_id.key) else None
            try: el.id_short = _clean_from_sid(sid)
            except Exception: pass
    if isinstance(el, m.SubmodelElementList):
        for c in list(el.value): sanitize_ids(c, True)
    elif isinstance(el, m.SubmodelElementCollection):
        for c in list(el.value): sanitize_ids(c, False)

def strip_sml_child_ids(el):  # 하위호환(템플릿 로드 직후 호출)
    sanitize_ids(el, False)


def load_template_elements(template_rel):
    """IDTA 템플릿 aasx에서 (요소 리스트, CD 리스트) 반환 — 부모 분리해 재사용 가능하게."""
    path = _res(template_rel)
    if not os.path.exists(path):
        return None, None
    st = DictObjectStore()
    with _quiet_basyx(), AASXReader(path) as r:
        r.read_into(object_store=st, file_store=DictSupplementaryFileContainer())
    sms = [o for o in st if isinstance(o, Submodel)]
    if not sms: return None, None
    sm = sms[0]
    els = list(sm.submodel_element)
    for el in els:
        sm.submodel_element.remove(el)   # 부모 분리
    cds = [o for o in st if isinstance(o, ConceptDescription)]
    return els, cds


def _embed_product_image(store, fstore, aas_name, image_path, verbose=True):
    """장비 대표 이미지를 ProductImages/ImageFile(및 유사 슬롯)에 임베드. 규칙: 생성기에서 처리."""
    if not (image_path and os.path.exists(image_path)):
        return 0
    ext = os.path.splitext(image_path)[1].lower()
    ct = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}.get(ext, "image/png")
    # 패키지 파트 경로는 전부 소문자로: OPC relationship 대상이 소문자화되므로 파트명과 일치시켜야
    # 대소문자 구분 검증기(KOSMO)에서 'non-existing target' 오류를 피함.
    pkg_path = f"/aasx/files/{aas_name.lower()}/productimage{ext or '.png'}"
    with open(image_path, "rb") as f:
        fstore.add_file(pkg_path, f, ct)
    n = 0
    def walk(el, ancestors):
        nonlocal n
        for c in _children(el):
            names = ancestors + [c.id_short or ""]
            if isinstance(c, m.File) and any("ProductImage" in a for a in names):
                c.value = pkg_path; c.content_type = ct; n += 1
            walk(c, names)
    for sm in [o for o in store if isinstance(o, Submodel)]:
        walk(sm, [sm.id_short or ""])
    if verbose:
        print(f"제품 이미지 임베드: {n}개 File → {pkg_path}")
    return n


def _children(el):
    if isinstance(el, Submodel): return list(el.submodel_element)
    if isinstance(el, (m.SubmodelElementCollection, m.SubmodelElementList)): return list(el.value)
    if isinstance(el, m.Entity): return list(el.statement)
    return []


# 생성기가 매핑표로 조립하는 IDTA 기반 서브모델(TD/PP/TS)은 공식 템플릿의
# SMT/Cardinality qualifier가 유실됨(템플릿을 통째로 복제하는 DN/HD/FS/PdM은 유지).
# 공고 원본(번들 IDTA 템플릿)에서 요소별 Cardinality qualifier를 semanticId·idShort로
# 대조해 그대로 이식한다(값을 지어내지 않고 공식 원본을 provenance로 사용). #72/#77/#86.
_CARD_TEMPLATES = {
    "TechnicalData": "templates/TechnicalData.aasx",
    "ProcessParameters": "templates/ProcessParametersType.aasx",
    "TimeSeries": "templates/TimeSeriesData.aasx",
    "FunctionalSafety": "templates/FunctionalSafety.aasx",
    "PredictiveMaintenance": "templates/PredictiveMaintenance.aasx",
}
def _card_qual(el):
    for q in (getattr(el, "qualifier", None) or []):
        if "ardinal" in (q.type or ""):
            return q
    return None

def _build_card_map(template_rel):
    """공식 템플릿 → 요소별 qualifier 목록 {semanticId: [q..]}, {idShort: [q..]}, {(부모 sem, sem): [q..]}.
    Cardinality뿐 아니라 AllowedIdShort 등 템플릿이 정한 qualifier 전부(선제검토 #67)."""
    path = _res(template_rel)
    if not os.path.exists(path):
        return {}, {}, {}
    st = DictObjectStore()
    with _quiet_basyx(), AASXReader(path) as r:
        r.read_into(object_store=st, file_store=DictSupplementaryFileContainer())
    by_sem, by_ish, by_pair = {}, {}, {}
    def sem(e):
        s = getattr(e, "semantic_id", None)
        return s.key[0].value if (s and s.key) else None
    def walk(e):
        for c in _children(e):
            qs = list(getattr(c, "qualifier", None) or [])
            if qs:
                s = sem(c)
                if s:
                    by_sem.setdefault(s, qs)
                    # 같은 semanticId가 여러 위치에 나오면(예: TS Metadata/Record=1, Records/Record=0..*) 부모로 구분
                    by_pair.setdefault((sem(e), s), qs)
                if c.id_short: by_ish.setdefault(c.id_short, qs)
            walk(c)
    for s in st:
        if isinstance(s, Submodel): walk(s)
    return by_sem, by_ish, by_pair

def _copy_qualifier(src):
    """공식 템플릿 qualifier를 그대로 복사(type·valueType·value·valueId·kind·semanticId 원문 유지)."""
    return m.Qualifier(type_=src.type, value_type=src.value_type, value=src.value,
                       value_id=getattr(src, "value_id", None), kind=src.kind,
                       semantic_id=getattr(src, "semantic_id", None),
                       supplemental_semantic_id=list(getattr(src, "supplemental_semantic_id", None) or []))

def apply_cardinality(store, verbose=True):
    """TD/PP/TS 등 매핑표로 조립한 서브모델 요소에 공식 템플릿의 qualifier(SMT/Cardinality·AllowedIdShort 등)를
    원문 그대로 이식한다. 요소에 같은 type의 qualifier가 이미 있으면 건드리지 않는다."""
    total = 0
    def sem(e):
        s = getattr(e, "semantic_id", None)
        return s.key[0].value if (s and s.key) else None
    for smx in [o for o in store if isinstance(o, Submodel)]:
        tmpl = _CARD_TEMPLATES.get(smx.id_short)
        if not tmpl:
            continue
        by_sem, by_ish, by_pair = _build_card_map(tmpl)
        if not (by_sem or by_ish):
            continue
        def walk(e):
            nonlocal total
            for c in _children(e):
                src = by_pair.get((sem(e), sem(c))) or by_sem.get(sem(c)) or by_ish.get(c.id_short)
                if src:
                    have = {q.type for q in (getattr(c, "qualifier", None) or [])}
                    for q in src:
                        if q.type in have:
                            continue
                        try:
                            c.qualifier.add(_copy_qualifier(q))
                            have.add(q.type)
                            total += 1
                        except Exception:
                            pass
                walk(c)
        walk(smx)
    if verbose and total:
        print(f"공식 템플릿 qualifier 이식(Cardinality·AllowedIdShort 등, TD/PP/TS): {total}개")
    return total


_TMPL_VT_CACHE = None
def _template_valuetypes():
    """번들 공식 템플릿의 Property semanticId → valueType (공식 자료형 원본, provenance)."""
    global _TMPL_VT_CACHE
    if _TMPL_VT_CACHE is not None:
        return _TMPL_VT_CACHE
    import glob as _glob
    by_sem = {}
    for tmpl in _glob.glob(os.path.join(_res("templates"), "*.aasx")):
        st = DictObjectStore()
        try:
            with _quiet_basyx(), AASXReader(tmpl) as r:
                r.read_into(object_store=st, file_store=DictSupplementaryFileContainer())
        except Exception:
            continue
        def walk(e):
            for c in _children(e):
                if isinstance(c, m.Property) and getattr(c, "semantic_id", None) and c.semantic_id.key:
                    s = c.semantic_id.key[0].value
                    if "sample.com" not in s and "SMT/General/Arbitrary" not in s:
                        by_sem.setdefault(s, c.value_type)
                walk(c)
        for s in st:
            if isinstance(s, Submodel):
                walk(s)
    _TMPL_VT_CACHE = by_sem
    return by_sem


def _convert_value(val, to_vt):
    """값을 목표 xsd 타입의 파이썬 값으로 변환(실패 시 예외)."""
    import datetime as _d
    from basyx.aas.model.datatypes import from_xsd as _fx
    if val is None:
        return None
    if to_vt is dt.String:
        if isinstance(val, (_d.datetime, _d.date)):
            return val.isoformat()
        if isinstance(val, bool):
            return "true" if val else "false"
        return str(val)
    if to_vt in (dt.Long, dt.Int, dt.Integer, dt.Short):
        return int(float(str(val).replace(",", "")))
    if to_vt in (dt.Double, dt.Float, dt.Decimal):
        return float(str(val).replace(",", ""))
    if to_vt is dt.Boolean:
        return str(val).strip().lower() in ("true", "1", "yes", "on")
    if to_vt in (dt.Duration, dt.DateTime, dt.Date):
        if isinstance(val, (int, float)) and to_vt is dt.Duration:
            return _fx(f"PT{val}S", dt.Duration)
        if hasattr(val, "isoformat"):
            return _fx(val.isoformat(), to_vt)
        s = str(val).strip()
        if to_vt is dt.Duration:
            # 이전 계획서에 남은 파이썬 표기 'relativedelta(seconds=+25)'도 읽는다
            mrd = re.match(r"^relativedelta\((.*)\)$", s)
            if mrd:
                kw = {k: int(v) for k, v in re.findall(r"(\w+)=([+-]?\d+)", mrd.group(1))}
                return dt.Duration(**kw)
        if to_vt is dt.DateTime:
            s = re.sub(r"^(\d{4}-\d{2}-\d{2}) (\d{2}:)", r"\1T\2", s)   # '2026-01-01 00:00:00+09:00' 형태 허용
        return _fx(s, to_vt)
    return _fx(str(val), to_vt)


def align_template_valuetypes(store, needs_review=None, verbose=True):
    """공식 템플릿에 정의된 요소(semanticId 일치)는 공식 valueType을 따른다(R13·#72·#73).
    예: TS Time/RecordCount/SamplingRate=xs:long, StartTime=xs:string, TD ClassificationSystemVersion=xs:string,
        PP PlannedProcessTime=xs:duration. 계획서 예시에서 추론한 타입을 공식 원본으로 교정한다."""
    by_sem = _template_valuetypes()
    n = 0
    def walk(e):
        nonlocal n
        for c in _children(e):
            if isinstance(c, m.Property) and getattr(c, "semantic_id", None) and c.semantic_id.key:
                tvt = by_sem.get(c.semantic_id.key[0].value)
                if tvt is not None and tvt is not c.value_type:
                    try:
                        nv = _convert_value(c.value, tvt)
                        c.value_type = tvt
                        c.value = nv
                        n += 1
                    except Exception:
                        if needs_review is not None:
                            needs_review.append(f"{c.id_short}: 공식 자료형({tvt.__name__})으로 값 변환 실패 - 확인 필요")
            walk(c)
    for sm in [o for o in store if isinstance(o, Submodel)]:
        walk(sm)
    if verbose and n:
        print(f"공식 템플릿 자료형 정합: {n}개 요소 valueType 교정")
    return n


def restore_template_container_sems(store, needs_review=None, verbose=True):
    """계획서로 조립하는 표준 서브모델(TD/PP/TS)에서, 계획서에 semanticId가 없어 자체 IRI가 붙은 컨테이너를
    공식 템플릿의 같은 경로(idShort 경로) 컨테이너 semanticId로 복원한다(R13 공식 보존).
    예: 초기 형식 계획서의 TS 'Metadata'·'Segments'(제목으로만 생성) → admin-shell.io 공식 IRI."""
    n = 0
    def sem(e):
        s = getattr(e, "semantic_id", None)
        return s.key[0].value if (s and s.key) else None
    for smx in [o for o in store if isinstance(o, Submodel)]:
        tmpl = _CARD_TEMPLATES.get(smx.id_short)
        if not tmpl or smx.id_short in ("FunctionalSafety", "PredictiveMaintenance"):
            continue
        path = _res(tmpl)
        if not os.path.exists(path):
            continue
        st = DictObjectStore()
        with _quiet_basyx(), AASXReader(path) as r:
            r.read_into(object_store=st, file_store=DictSupplementaryFileContainer())
        tmap = {}
        def twalk(e, p):
            for c in _children(e):
                if isinstance(c, (m.SubmodelElementCollection, m.SubmodelElementList, m.Entity)) and c.id_short \
                        and not str(c.id_short).startswith(_HACK):
                    tmap[p + (c.id_short,)] = sem(c)
                    twalk(c, p + (c.id_short,))
        for s in st:
            if isinstance(s, Submodel): twalk(s, ())
        def walk(e, p):
            nonlocal n
            for c in _children(e):
                if isinstance(c, (m.SubmodelElementCollection, m.SubmodelElementList, m.Entity)):
                    cp = p + ((c.id_short,) if c.id_short else ())
                    cur = sem(c) or ""
                    off = tmap.get(cp)
                    if off and (not cur or cur.startswith(NS + "/cd/")):
                        c.semantic_id = m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, off),))
                        n += 1
                        if needs_review is not None:
                            needs_review[:] = [x for x in needs_review if not x.startswith(f"{c.id_short}: semanticId 비어")]
                    walk(c, cp)
        walk(smx, ())
    if verbose and n:
        print(f"공식 템플릿 컨테이너 semanticId 복원: {n}개")
    return n


# 계획서에 값이 적힌 경우 '공식 템플릿 구조 + 계획서 값'으로 만드는 표준 서브모델(구조 변경 불가 템플릿).
OVERLAY_STD = ("PredictiveMaintenance", "FunctionalSafety", "DigitalNameplate", "HandoverDocumentation")

def overlay_template(tmpl_els, plan_nodes, needs_review=None):
    """공식 템플릿 요소에 계획서 예시값을 idShort(+상위 컨테이너 이름)로 대조해 채운다.
    구조·semanticId·카디널리티는 템플릿 원본을 유지하고, 값만 계획서에서 가져온다."""
    by_pair, by_id = {}, {}
    def idx(nodes, parent):
        for nd in nodes:
            ish = clean_idshort(nd.get("idShort", ""))
            if nd.get("type") in ("SMC", "SML", "Entity"):
                idx(nd.get("children", []), parent if nd.get("list_item") else ish)
            else:
                by_pair.setdefault((parent, ish), nd)
                by_id.setdefault(ish, []).append(nd)
    idx(plan_nodes, None)
    used = set()
    def pick(parent, ish):
        nd = by_pair.get((parent, ish))
        if nd is None and len(by_id.get(ish, [])) == 1:
            nd = by_id[ish][0]
        return nd
    def apply(el, parent):
        for c in _children(el):
            nm = c.id_short if (c.id_short and not str(c.id_short).startswith(_HACK)) else None
            if isinstance(c, (m.SubmodelElementCollection, m.SubmodelElementList, m.Entity)):
                apply(c, nm or parent)        # SML 항목(이름 없음)은 SML 이름을 상위로 유지
                continue
            if not nm:
                continue
            nd = pick(parent, nm)
            if nd is None:
                continue
            ex = nd.get("example")
            if ex in (None, ""):
                continue
            try:
                if isinstance(c, m.MultiLanguageProperty):
                    c.value = _mlp_value(ex)
                elif isinstance(c, m.Range):
                    lo, hi = _range(ex)
                    if lo is not None:
                        c.min = _convert_value(lo, c.value_type)
                        c.max = _convert_value(hi, c.value_type)
                elif isinstance(c, m.Property):
                    raw = ex
                    if c.value_type not in (dt.String,):
                        mnum = re.match(r"^\s*([-±]?\s*\d[\d,]*(?:\.\d+)?)", str(ex))
                        if c.value_type in (dt.Double, dt.Float, dt.Decimal, dt.Long, dt.Int, dt.Integer, dt.Short) and mnum:
                            raw = mnum.group(1).replace("±", "").replace(" ", "")
                    c.value = _convert_value(raw, c.value_type)
                else:
                    continue
                used.add(id(nd))
            except Exception:
                if needs_review is not None:
                    needs_review.append(f"{nm}: 계획서 예시 '{ex}'를 공식 자료형으로 변환 실패")
    for e in tmpl_els:
        if isinstance(e, (m.SubmodelElementCollection, m.SubmodelElementList, m.Entity)):
            apply(e, e.id_short)
        else:
            nm = e.id_short
            nd = pick(None, nm)
            if nd is not None and nd.get("example") not in (None, "") and isinstance(e, m.Property):
                try:
                    e.value = _convert_value(nd["example"], e.value_type); used.add(id(nd))
                except Exception:
                    pass
    if needs_review is not None:
        for lst in by_id.values():
            for nd in lst:
                if id(nd) not in used and nd.get("example") not in (None, ""):
                    needs_review.append(f"{nd.get('idShort')}: 공식 템플릿에 없는 계획서 항목(값 미반영)")
    return len(used)


def refine_std_examples(store, aas_name, verbose=True, equip_ko=None, equip_en=None):
    """표준 템플릿 submodel(HandoverDocumentation/FunctionalSafety/PredictiveMaintenance)의
    비어있거나 일반('Example X') placeholder인 leaf에 의미 있는 대표 예시값을 채운다(모든 예시 채움 요구).
    File은 실제 파일이 없으면 값 없이 유지(경로만 채우면 KOSMO 관계 오류)."""
    welding = ("Welding" in aas_name) or ("Ship" in aas_name)
    fpd = ("FPD" in aas_name) or ("TransferRobot" in aas_name)
    legacy = welding or fpd           # 기존 제출 장비(선박·FPD)는 이전과 같은 대표값 유지
    if welding:
        eq_ko = "선박 용접 로봇"
    elif fpd:
        eq_ko = "FPD 반송 로봇"
    else:
        eq_ko = equip_ko or equip_en or aas_name
    if legacy:
        REP = {  # 문자열 Property 대표값
            "DocumentDomainId": "IODA-HYU", "DocumentIdentifier": "MAN-001", "ClassId": "03-02",
            "ClassificationSystem": "VDI2770 Blatt1:2020", "StatusValue": "Released",
            "OrganizationShortName": "IODA", "OrganizationOfficialName": "IODA Lab, Hanyang University",
            "TypeOfInterlockingDevice": "Safety door interlock switch",
            "OtherOperatingConditions": "Ambient 0-40 C, protection IP54",
            "FunctionalSafetyDeviceType": "Safety controller",
            "IndicationType": "RemainingUsefulLife", "EngineeringUnit": "h", "BoundaryEngineeringUnit": "h",
            "ModelType": "Statistical", "RemainingUsefulLifetime": "5000",
            "SIL": "SIL2", "PL": "d", "Category": "3", "TypeOfVoltage": "DC",
            "ConditionName": ("AccumulatedArcTime" if welding else "AccumulatedOperatingHours"),
            "Description": ("용접 소모품·구동부 마모 기반 잔여수명 예측" if welding else "반송 구동부 마모 기반 잔여수명 예측"),
            "ModelDescription": ("누적 아크가동시간 기반 통계 예측 모델" if welding else "누적 가동시간 기반 통계 예측 모델"),
            "BoundaryDescription": ("컨택트팁 교체 권고 경계" if welding else "감속기 점검 권고 경계"),
            "PreAlertMessage": ("소모품 교체 사전 경보" if welding else "구동부 점검 사전 경보"),
            "AlertMessage": ("소모품 교체 경보" if welding else "구동부 정비 경보"),
        }
    else:  # 그 밖의 장비: 장비명 기반 비식별 대표값(다른 장비 문구가 섞이지 않도록)
        REP = {
            "DocumentDomainId": "EXAMPLE-DMS", "DocumentIdentifier": "MAN-001", "ClassId": "03-02",
            "ClassificationSystem": "VDI2770 Blatt1:2020", "StatusValue": "Released",
            "OrganizationShortName": "ExampleCompany", "OrganizationOfficialName": "ExampleCompany Co., Ltd.",
            "TypeOfInterlockingDevice": "Safety door interlock switch",
            "OtherOperatingConditions": "Indoor use, ambient 15-35 C",
            "FunctionalSafetyDeviceType": "Safety controller",
            "IndicationType": "Time", "EngineeringUnit": "h", "BoundaryEngineeringUnit": "h",
            "ModelType": "ModelTypeDataDriven",
            "SIL": "SIL2", "PL": "d", "Category": "3", "TypeOfVoltage": "AC",
            "ConditionName": "AccumulatedOperatingHours",
            "Description": f"{eq_ko} 주요 마모부 잔여수명 예측",
            "ModelDescription": "누적 가동시간 기반 데이터 기반 예측 모델",
            "BoundaryDescription": "주요 마모부 점검 권고 경계",
            "PreAlertMessage": "주요 마모부 점검 사전 경보",
            "AlertMessage": "주요 마모부 정비 필요 경보",
        }
    MLP_REP = {  # 다국어 Property 대표값
        "ClassName": {"en": "Operation", "ko": "운영"},
        "Title": {"en": "Operation Manual", "ko": f"{eq_ko} 운영 매뉴얼"},
        "Subtitle": {"en": "Installation and Operation Guide", "ko": "설치 및 운전 안내"},
        "Description": {"en": "Operation and maintenance manual", "ko": "운영·정비 매뉴얼"},
        "KeyWords": {"en": "manual, operation, maintenance", "ko": "매뉴얼, 운영, 정비"},
    }
    if not legacy:
        # 선제검토 #65: 실제 매뉴얼이 아니라 구조를 보이는 예시 문서임을 메타데이터에도 밝힌다(첨부 예시 파일과 일치).
        MLP_REP.update({
            "Title": {"en": "Operation Manual (Example)", "ko": f"{eq_ko} 운영 매뉴얼(예시)"},
            "Description": {"en": "Example operation manual for the reference model (not an actual product manual)",
                            "ko": "참조모델 문서 구조를 보이기 위한 예시 운영 매뉴얼(실제 제품 매뉴얼 아님)"},
            "KeyWords": {"en": "manual, operation, maintenance, example", "ko": "매뉴얼, 운영, 정비, 예시"},
        })
    def is_ph(v):  # 비었거나 일반 placeholder인가
        if v is None or v == "": return True
        if isinstance(v, str) and (v.startswith("Example ") or v.startswith("EXAMPLE-")): return True
        return False
    n = 0
    def kids(el):
        if isinstance(el, Submodel): return list(el.submodel_element)
        if isinstance(el, (m.SubmodelElementCollection, m.SubmodelElementList)): return list(el.value)
        if isinstance(el, m.Entity): return list(el.statement)
        return []
    def walk(el):
        nonlocal n
        for c in kids(el):
            ish = c.id_short or ""
            if isinstance(c, m.Property) and is_ph(c.value) and ish in REP:
                c.value = REP[ish]; n += 1
            elif isinstance(c, m.MultiLanguageProperty):
                cur = None
                try: cur = c.value.get("en") if c.value else None
                except Exception: cur = None
                if (not c.value or is_ph(cur)) and ish in MLP_REP:
                    c.value = m.MultiLanguageTextType(MLP_REP[ish]); n += 1
            walk(c)
    for sm in [o for o in store if isinstance(o, Submodel)
               and o.id_short in ("FunctionalSafety", "PredictiveMaintenance", "HandoverDocumentation",
                                  "Nameplate", "DigitalNameplate")]:
        walk(sm)
    n += neutralize_nameplate_samples(store, aas_name, equip_en or aas_name, equip_ko)
    if verbose and n:
        print(f"표준 예시 대표값 채움: {n}개")
    return n


# IDTA Digital Nameplate 3.0.1 템플릿에 들어 있는 견본값(독일 회사·유량계 예시) → 장비 기준 비식별 대표값.
# 견본값과 정확히 같을 때만 바꾼다(계획서·매핑표가 준 값은 건드리지 않음). R24: 비식별 합성 예시 허용.
def neutralize_nameplate_samples(store, aas_name, equip_en, equip_ko=None):
    import datetime as _d
    PROP = {
        "URIOfTheProduct": ("https://www.domain-abc.com/Model-Nr-1234/Serial-Nr-5678", f"{NS}/asset/{aas_name}/1/0"),
        "ManufacturerProductType": ("FM-ABC-1234", "MODEL-1000"),
        "OrderCodeOfManufacturer": ("FMABC1234", "ORDER-1000"),
        "ProductArticleNumberOfManufacturer": ("FM11-ABC22-123456", "ART-1000"),
        "SerialNumber": ("12345678", "SN-0001"),
        "YearOfConstruction": ("2022", "2026"),
        "CountryOfOrigin": ("DE", "KR"),
        "UniqueFacilityIdentifier": ("987654321", "FAC-0001"),
        "DesignationOfCertificateOrApproval": ("KEMA99IECEX1105/128", "CERT-0001"),
        "GuidelineForConformityDeclaration": ("EXAMPLE-GuidelineForConformityDeclaration", "Machinery Directive 2006/42/EC"),
        # 템플릿 견본의 인증기관 번호(실제 기관 번호) → 예시 표기(마킹은 실제 인증이 아닌 예시, #64)
        "MarkingAdditionalText": ("0044", "EXAMPLE"),
    }
    DATES = {"DateOfManufacture": _d.date(2026, 1, 1), "IssueDate": _d.date(2026, 1, 1), "ExpiryDate": _d.date(2031, 1, 1)}
    MLP = {
        "ManufacturerName": ({"Muster AG"}, {"en": "ExampleCompany Co., Ltd."}),
        "ManufacturerProductDesignation": ({"ABC-123"}, {"en": equip_en, **({"ko": equip_ko} if equip_ko else {})}),
        "ManufacturerProductRoot": ({"flow meter"}, {"en": equip_en}),
        "ManufacturerProductFamily": ({"Type ABC"}, {"en": f"{equip_en} series"}),
    }
    n = 0
    def walk(el):
        nonlocal n
        for c in _children(el):
            ish = c.id_short or ""
            if isinstance(c, m.Property):
                if ish in PROP and str(c.value) == PROP[ish][0]:
                    c.value = PROP[ish][1]; n += 1
                elif ish in DATES and c.value is not None and str(c.value).startswith("2022-01-01"):
                    try:
                        c.value = DATES[ish]; n += 1
                    except Exception:
                        pass
            elif isinstance(c, m.MultiLanguageProperty) and ish in MLP and c.value:
                try:   # 템플릿 견본 텍스트는 따옴표를 포함한다(예: "Muster AG")
                    vals = {str(v).strip().strip('"') for v in c.value.values()}
                except Exception:
                    vals = set()
                if vals & MLP[ish][0]:
                    c.value = m.MultiLanguageTextType(MLP[ish][1]); n += 1
            walk(c)
    for sm in [o for o in store if isinstance(o, Submodel) and o.id_short in ("Nameplate", "DigitalNameplate")]:
        walk(sm)
    return n


_OFFICIAL_IEC_CACHE = None
def _load_official_iec():
    """번들 IDTA 템플릿의 ConceptDescription IEC61360 내용을 색인.
    반환: (by_id, by_pn) — {CD id(=공식 semanticId): rec}, {preferredName(en): rec}.
    rec = {pn, sn, def, unit}. 값을 만들지 않고 공고 원본을 그대로 읽어 provenance로 사용."""
    global _OFFICIAL_IEC_CACHE
    if _OFFICIAL_IEC_CACHE is not None:
        return _OFFICIAL_IEC_CACHE
    import glob as _glob
    by_id, by_pn = {}, {}
    for tmpl in _glob.glob(os.path.join(_res("templates"), "*.aasx")):
        st = DictObjectStore()
        try:
            with _quiet_basyx(), AASXReader(tmpl) as r:
                r.read_into(object_store=st, file_store=DictSupplementaryFileContainer())
        except Exception:
            continue
        for cd in st:
            if not isinstance(cd, m.ConceptDescription):
                continue
            for eds in (cd.embedded_data_specifications or []):
                c = eds.data_specification_content
                if not isinstance(c, m.DataSpecificationIEC61360):
                    continue
                dfn = dict(c.definition) if c.definition else {}
                if not dfn:
                    continue
                rec = {"pn": dict(c.preferred_name) if c.preferred_name else {},
                       "sn": dict(c.short_name) if getattr(c, "short_name", None) else {},
                       "def": dfn, "unit": getattr(c, "unit", None)}
                by_id.setdefault(cd.id, rec)
                en_pn = rec["pn"].get("en") or next(iter(rec["pn"].values()), None)
                if en_pn:
                    by_pn.setdefault(en_pn, rec)
    _OFFICIAL_IEC_CACHE = (by_id, by_pn)
    return _OFFICIAL_IEC_CACHE


def enrich_cds(store, equip_en, verbose=True):
    """ConceptDescription의 IEC61360 Content 실질화(PE 'Content' 획일 문제 해소).
    - 표준 요소(IRDI/admin-shell/eclass CD): 번들 IDTA 템플릿의 공식 preferredName/definition/unit/shortName 이식.
    - 자체 요소: 요소의 최종 한글 description을 CD definition(ko)에 주입(영문 자리표시자 유지).
    값을 지어내지 않고 공식 원본 또는 계획서 한글 정의만 사용한다."""
    by_id, by_pn = _load_official_iec()
    el_desc = {}   # semanticId -> {en, ko} (요소 최종 description 대표)
    def collect(el):
        for c in _children(el):
            sref = getattr(c, "semantic_id", None)
            sid = sref.key[0].value if (sref and sref.key) else None
            d = getattr(c, "description", None)
            if sid and d:
                try:
                    en = d.get("en"); ko = d.get("ko")
                except Exception:
                    en = ko = None
                cur = el_desc.get(sid) or {}
                if en and not cur.get("en"): cur["en"] = en
                if ko and not cur.get("ko"): cur["ko"] = ko
                el_desc[sid] = cur
            collect(c)
    for s in store:
        if isinstance(s, m.Submodel):
            collect(s)
    def is_std(sid):
        s = (sid or "").strip()
        return bool(s and (re.match(r"^\d{3,4}[-/]", s) or "admin-shell" in s or "eclass-cdp.com" in s))
    n_std = n_ko = 0
    for cd in [o for o in store if isinstance(o, m.ConceptDescription)]:
        for eds in (cd.embedded_data_specifications or []):
            c = eds.data_specification_content
            if not isinstance(c, m.DataSpecificationIEC61360):
                continue
            sid = cd.id
            off = by_id.get(sid) or (by_pn.get(cd.id_short) if is_std(sid) else None)
            elko = (el_desc.get(sid) or {}).get("ko")
            if off:
                if off["pn"]:
                    c.preferred_name = m.PreferredNameTypeIEC61360(dict(off["pn"]))
                ddict = dict(off["def"])
                if elko and "ko" not in ddict:
                    ddict["ko"] = elko[:1023]
                c.definition = m.DefinitionTypeIEC61360(ddict)
                if off["sn"]:
                    try: c.short_name = m.ShortNameTypeIEC61360(dict(off["sn"]))
                    except Exception: pass
                if off["unit"] and not getattr(c, "unit", None):
                    try: c.unit = off["unit"]
                    except Exception: pass
                n_std += 1
            elif elko:
                ddict = {}
                try:
                    if c.definition: ddict = dict(c.definition)
                except Exception:
                    ddict = {}
                ddict["ko"] = elko[:1023]
                c.definition = m.DefinitionTypeIEC61360(ddict)
                n_ko += 1
    if verbose:
        print(f"CD 내용 실질화: 공식 IEC61360 이식 {n_std}개 · 한글 정의 주입 {n_ko}개")
    return n_std + n_ko


def strip_sample_elements(store, verbose=True):
    """IDTA 템플릿의 샘플/확장 예시 요소 제거(검토 #74): ArbitraryProperty/ArbitraryMLP/ArbitraryFile.
    이들은 실제 장비에 사용되지 않는 템플릿 샘플이므로 최종 참조모델에서 제외한다.
    (컨테이너는 유지하되 그 안의 Arbitrary* leaf만 제거 — 상위 cardinality는 0..*라 안전)"""
    SAMPLE = ("ArbitraryProperty", "ArbitraryMLP", "ArbitraryFile", "ArbitraryProp")
    n = 0
    def prune(container, getlist):
        nonlocal n
        lst = getlist(container)
        for c in list(lst):
            ish = c.id_short or ""
            if ish in SAMPLE:
                lst.remove(c); n += 1
            else:
                if isinstance(c, m.SubmodelElementCollection): prune(c, lambda x: x.value)
                elif isinstance(c, m.SubmodelElementList): prune(c, lambda x: x.value)
                elif isinstance(c, m.Entity): prune(c, lambda x: x.statement)
    for sm in [o for o in store if isinstance(o, Submodel)]:
        prune(sm, lambda x: x.submodel_element)
    if verbose and n:
        print(f"샘플 요소 제거(R/#74): Arbitrary* {n}개")
    return n


def localize_descriptions(store, ko_map, equip_ko, equip_en, verbose=True):
    """모든 description을 영어(en)+한글(ko)로 정규화. de/fr 등 그 외 언어 제거, 한글 상세 채움.
    한글 우선순위: 기존 ko > 계획서/장비 사전(ko_map) > 표준 사전(KO_STD)."""
    n_fix = 0; n_ko = 0
    def gl(d, lang):
        try: return d.get(lang)
        except Exception: return None
    def apply(obj, fb_en=None, fb_ko=None):
        nonlocal n_fix, n_ko
        ish = getattr(obj, "id_short", None)
        # basyx가 SML 직속 원소에 부여하는 내부 합성 id_short는 사람이 읽는 텍스트로 쓰지 않음.
        ish_txt = ish if (ish and not str(ish).startswith("generated_submodel_list_hack")) else None
        d = getattr(obj, "description", None)
        en = gl(d, "en") if d else None
        ko = gl(d, "ko") if d else None
        if not en:
            en = fb_en or ish_txt
        if not ko:
            ko = (ko_map.get(ish) if ish else None) or (KO_STD.get(ish) if ish else None) or fb_ko
        # SML 반복 항목(idShort 없음/합성명): 일반 한글 채움
        if not ko and (ish is None or str(ish).startswith("generated_submodel_list_hack")):
            ko = "목록 항목 - 반복되는 동일 구조의 개별 항목."
            if not en: en = "list item"
        # 현재 언어 집합
        cur = set()
        if d is not None:
            try: cur = set(d.keys())
            except Exception: cur = set()
        target = set()
        if en: target.add("en")
        if ko: target.add("ko")
        # en/ko만, 그 외 제거. 변화 있을 때만 재작성.
        need = (cur - {"en", "ko"}) or ("ko" in target and "ko" not in cur) or ("en" in target and "en" not in cur)
        if need and target:
            nd = {}
            if en: nd["en"] = str(en)[:1023]
            if ko: nd["ko"] = str(ko)[:1023]
            obj.description = m.MultiLanguageTextType(nd)
            n_fix += 1
            if ko: n_ko += 1
    def walk(el):
        for c in _children(el):
            apply(c); walk(c)
    for o in store:
        if isinstance(o, m.AssetAdministrationShell):
            apply(o, fb_en=f"{equip_en} reference model (Type)",
                  fb_ko=f"{equip_ko or equip_en} 참조 모델 - 자산관리쉘(AAS) Type 수준 표준 모델.")
        if isinstance(o, Submodel):
            apply(o); walk(o)
    if verbose:
        print(f"description 정규화(en+ko): {n_fix}개 수정 · 한글 채움 {n_ko}개")
    return n_fix


_CT = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml",
       ".pdf": "application/pdf", ".html": "text/html", ".htm": "text/html", ".csv": "text/csv",
       ".txt": "text/plain"}

def _pkg_path(aas_name, src, role):
    """첨부 파일의 패키지 파트 경로(전부 소문자: OPC 관계 대상과 대소문자까지 일치해야 KOSMO 'non-existing target' 회피)."""
    base, ext = os.path.splitext(os.path.basename(src))
    safe = re.sub(r"[^a-z0-9._-]+", "_", base.lower()).strip("_")
    if not re.search(r"[a-z0-9]", safe):
        safe = role
    return f"/aasx/files/{aas_name.lower()}/{safe}{ext.lower()}"

def _find_child(el, ish):
    for c in _children(el):
        if c.id_short == ish:
            return c
    return None

def attach_files(store, fstore, aas_name, attachments=None, needs_review=None, verbose=True):
    """계획서 옆에 둔 첨부 파일을 공식 템플릿의 File 요소에 연결한다(선제검토 #64·#65).
      attachments = {"marking": 경로|None, "handover": 경로|None}
      - marking  → Nameplate/Markings/[i]/MarkingFile (마킹 항목 전부, 필수 File)
      - handover → HandoverDocumentation/Documents/[0]/DocumentVersions/[0]/DigitalFiles/[0] (필수 File)
    파일을 지어내지 않는다: 파일이 없으면 값 없이 두고 prune/NEEDS_REVIEW 단계에서 보고한다."""
    attachments = attachments or {}
    done = []
    def put(role, el_list):
        src = attachments.get(role)
        if not (src and os.path.exists(src) and el_list):
            return
        ext = os.path.splitext(src)[1].lower()
        ct = _CT.get(ext, "application/octet-stream")
        pkg = _pkg_path(aas_name, src, role)
        with open(src, "rb") as f:
            fstore.add_file(pkg, f, ct)
        for fe in el_list:
            fe.value = pkg; fe.content_type = ct
        done.append(f"{role}: {len(el_list)}개 File → {pkg} ({ct})")
    for smx in [o for o in store if isinstance(o, Submodel)]:
        if smx.id_short in ("Nameplate", "DigitalNameplate"):
            mk = _find_child(smx, "Markings")
            files = []
            for item in (_children(mk) if mk is not None else []):
                f = _find_child(item, "MarkingFile")
                if isinstance(f, m.File):
                    files.append(f)
            put("marking", files)
        elif smx.id_short == "HandoverDocumentation":
            docs = _find_child(smx, "Documents")
            d0 = (_children(docs) or [None])[0] if docs is not None else None
            vers = _find_child(d0, "DocumentVersions") if d0 is not None else None
            v0 = (_children(vers) or [None])[0] if vers is not None else None
            dfs = _find_child(v0, "DigitalFiles") if v0 is not None else None
            f0 = (_children(dfs) or [None])[0] if dfs is not None else None
            put("handover", [f0] if isinstance(f0, m.File) else [])
    if verbose:
        for d in done:
            print(f"첨부 파일 연결: {d}")
    return done

def _card_value(el):
    q = _card_qual(el)
    return (str(q.value).strip() if (q is not None and q.value is not None) else "")

def prune_empty_optional_files(store, needs_review=None, verbose=True):
    """값(파일 경로)이 없는 File을 정리한다(선제검토 #65③).
    - 선택 요소(카디널리티 ZeroToOne/ZeroToMany): 빈 자리로 남기지 않고 제거(공식 cardinality가 허용하는 생략)
    - 필수 요소(One/OneToMany 또는 미표기): 남겨 두고 NEEDS_REVIEW로 보고(계획서 옆에 파일을 두면 자동 연결)
    반환: (제거한 경로 목록, 필수인데 비어 있는 경로 목록)"""
    removed, missing = [], []
    def walk(el, path):
        for i, c in enumerate(list(_children(el))):
            nm = c.id_short if (c.id_short and not str(c.id_short).startswith(_HACK)) else f"[{i}]"
            p = f"{path}/{nm}"
            if isinstance(c, m.File) and not c.value:
                card = _card_value(c)
                lst = (el.submodel_element if isinstance(el, Submodel)
                       else el.statement if isinstance(el, m.Entity) else el.value)
                if card in ("ZeroToOne", "ZeroToMany") and not (isinstance(el, m.SubmodelElementList) and len(lst) <= 1):
                    lst.remove(c); removed.append(p)
                else:
                    missing.append(p)
            else:
                walk(c, p)
    for smx in [o for o in store if isinstance(o, Submodel)]:
        walk(smx, smx.id_short)
    if needs_review is not None:
        for p in missing:
            # 자동 연결 규칙(run.find_plan_attachments)이 있는 자리만 파일 이름을 안내한다.
            if p.endswith("/MarkingFile"):
                hint = "계획서 옆에 인증마크.png를 두면 자동 연결"
            elif p.startswith("HandoverDocumentation/") and "/DigitalFiles" in p:
                hint = "계획서 옆에 운영매뉴얼.pdf를 두면 자동 연결"
            elif "/ProductImages/" in p:
                hint = "계획서 옆에 장비이미지.png를 두면 자동 연결"
            else:
                hint = "자동 연결 대상 아님, 실제 파일이 있으면 별도 검토"
            needs_review.append(f"{p}: 필수 File에 파일 없음({hint})")
    if verbose and (removed or missing):
        print(f"빈 File 정리: 선택 요소 제거 {len(removed)}개 {removed} / 필수인데 파일 없음 {len(missing)}개")
    return removed, missing


_OFFICIAL_CD_CACHE = None
OFFICIAL_CD_NOTES = {}   # CD id -> 공식 원본 결함 보정 내용(가이던스 예외 목록용)
_OFFICIAL_VL_ORDER = {}  # CD id -> 공식 원본 valueList의 value 순서(basyx는 valueList를 set으로 들고 있어 순서가 사라짐)
_OFFICIAL_NO_CD = {}     # 공식 템플릿 요소 semanticId 중 원본에 같은 id의 CD가 없는 것 -> (파일, 요소 idShort, 같은 idShort의 원본 CD id들)

def _official_json_fixups(d, fname):
    """공식 배포 JSON의 원본 결함 중 AAS 메타모델로 표현할 수 없는 두 가지만 최소 처리한다(나머지는 원문 그대로).
    ① 한 다국어 문자열에 같은 언어가 두 번 이상(예: 'en' 2개, 두 번째는 독일어 문장) → 언어당 첫 번째만 유지
       (메타모델은 언어별 1개만 허용, basyx는 마지막 것을 남겨 독일어가 'en'으로 남게 됨)
    ② 서로 다른 CD가 같은 id를 가짐(IDTA 02048: RULCondition·ConditionName CD가 둘 다 .../RULCondition/1/0)
       → id가 유일해야 하므로 앞의 CD만 쓰고 id는 바꾸지 않는다(선제검토 #77, 반도체홀가공기 0922 #97과 같은 처리)
    처리 내용은 OFFICIAL_CD_NOTES에 CD id별로 남긴다."""
    def fix_lang(o, cd_id, path):
        if isinstance(o, list) and o and all(isinstance(x, dict) and "language" in x and "text" in x for x in o):
            seen, keep = set(), []
            for x in o:
                if x["language"] in seen:
                    continue
                seen.add(x["language"]); keep.append(x)
            if len(keep) != len(o) and cd_id:
                OFFICIAL_CD_NOTES.setdefault(cd_id, []).append(
                    f"{fname}: {path}에 같은 언어 태그가 {len(o)}개 → 언어별 첫 번째만 유지")
            o[:] = keep
            return
        if isinstance(o, dict):
            for k, v in o.items():
                fix_lang(v, cd_id, k)
        elif isinstance(o, list):
            for v in o:
                fix_lang(v, cd_id, path)
    cds = d.get("conceptDescriptions") or []
    for c in cds:
        fix_lang(c, c.get("id"), "CD")
    for sm in d.get("submodels") or []:
        fix_lang(sm, None, "SM")
    first, keep = {}, []
    for c in cds:
        cid = c.get("id")
        if cid in first:
            OFFICIAL_CD_NOTES.setdefault(cid, []).append(
                f"{fname}: 원본 CD '{c.get('idShort')}'가 CD '{first[cid]}'와 같은 id → 앞의 CD만 사용(id는 원본 그대로)")
            continue
        first[cid] = c.get("idShort"); keep.append(c)
    if cds:
        d["conceptDescriptions"] = keep
    return d


def _walk_json(els):
    for x in els or []:
        yield x
        yield from _walk_json(x.get("value") if isinstance(x.get("value"), list) else None)
        yield from _walk_json(x.get("statements"))


def _index_official_gaps(d, fname):
    """원본 템플릿 요소의 semanticId 중 원본 CD 목록에 같은 id가 없는 것(원본 오기·부재)을 모은다.
    예: IDTA 02048 RemainingUsefulLifetime 요소 .../PredictiveMaintenance/RemainingUsefulLifetime/1/0 ↔ 원본 CD
    .../PredictiveMaintenanceRemainingUsefulLifetime/1/0(슬래시 빠짐), IDTA 02006 AddressInformation(원본 CD 없음)."""
    cds = d.get("conceptDescriptions") or []
    ids = {c.get("id") for c in cds}
    by_ish = {}
    for c in cds:
        by_ish.setdefault(c.get("idShort"), []).append(c.get("id"))
    for sm in d.get("submodels") or []:
        for x in _walk_json(sm.get("submodelElements")):
            k = ((x.get("semanticId") or {}).get("keys") or [{}])[0].get("value")
            if k and k not in ids:
                _OFFICIAL_NO_CD.setdefault(k, (fname, x.get("idShort"), by_ish.get(x.get("idShort"), [])))


def official_no_cd():
    """{요소 semanticId: (원본 파일, 요소 idShort, 같은 idShort의 원본 CD id들)} — 원본에 그 id의 CD가 없는 공식 semanticId."""
    _load_official_cds()
    return _OFFICIAL_NO_CD


def _load_official_cds():
    """번들 IDTA 공식 배포 템플릿(templates/official/*.json, admin-shell-io/submodel-templates published)의
    ConceptDescription 원본 색인 {CD id: (CD, 파일명)}. 표현할 수 없는 원본 결함만 _official_json_fixups로 보정."""
    global _OFFICIAL_CD_CACHE
    if _OFFICIAL_CD_CACHE is not None:
        return _OFFICIAL_CD_CACHE
    import glob as _glob, logging as _lg, io as _io
    from basyx.aas.adapter.json import read_aas_json_file
    out = {}
    lg = _lg.getLogger("basyx"); old = lg.level; lg.setLevel(_lg.CRITICAL)   # 원본 id 중복 안내는 숨김(_quiet_basyx 참고)
    try:
        for f in sorted(_glob.glob(os.path.join(_res("templates"), "official", "*.json"))):
            try:
                with open(f, encoding="utf-8-sig") as fh:
                    d = _official_json_fixups(json.load(fh), os.path.basename(f))
                _index_official_gaps(d, os.path.basename(f))
                for c in d.get("conceptDescriptions") or []:
                    for eds in c.get("embeddedDataSpecifications") or []:
                        vl = (((eds.get("dataSpecificationContent") or {}).get("valueList") or {})
                              .get("valueReferencePairs"))
                        if vl:
                            _OFFICIAL_VL_ORDER.setdefault(c.get("id"), [p.get("value") for p in vl])
                st = read_aas_json_file(_io.StringIO(json.dumps(d, ensure_ascii=False)), failsafe=True)
            except Exception:
                continue
            for o in st:
                if isinstance(o, ConceptDescription):
                    out.setdefault(o.id, (o, os.path.basename(f)))
    finally:
        lg.setLevel(old)
    _OFFICIAL_CD_CACHE = out
    return out

def _official_copy(cid):
    """공식 원본 CD의 사본(valueList는 원본 JSON 순서로 고정 → 매 실행 같은 출력)."""
    new = copy.deepcopy(_load_official_cds()[cid][0])
    order = _OFFICIAL_VL_ORDER.get(cid)
    if order:
        pos = {v: i for i, v in enumerate(order)}
        for eds in new.embedded_data_specifications:
            c = eds.data_specification_content
            if getattr(c, "value_list", None):
                c.value_list = _OrderedRefs(sorted(c.value_list, key=lambda p: pos.get(p.value, len(pos))))
    return new


def _used_semantic_ids(store):
    used = set()
    def rec(el):
        s = getattr(el, "semantic_id", None)
        if s and s.key:
            used.add(s.key[0].value)
        if isinstance(el, m.SubmodelElementList) and el.semantic_id_list_element and el.semantic_id_list_element.key:
            used.add(el.semantic_id_list_element.key[0].value)
        kids = list(el.value) if isinstance(el, (m.SubmodelElementCollection, m.SubmodelElementList)) else \
            (list(el.statement) if isinstance(el, m.Entity) else [])
        for k in kids:
            rec(k)
    for sm in [o for o in store if isinstance(o, Submodel)]:
        for e in sm.submodel_element:
            rec(e)
    return used


def restore_official_cds(store, verbose=True):
    """공식 IDTA 템플릿에 있는 ConceptDescription(id 일치)은 공식 배포 원본을 그대로 쓴다(선제검토 #68·#69).
    preferredName·definition·dataType(원본이 미지정이면 미지정)·unit·symbol·valueList·idShort 등을
    생성기가 보충하거나 바꾸지 않는다. 원본 CD와 SME 자료형이 달라 검증기가 지적하는 경우는 예외로 기록한다.
    원본 요소 semanticId에 맞는 CD가 원본에 없으면(원본 오기·부재, 선제검토 #77):
      - 그 semanticId로 생성기가 만든 CD는 지운다(원본에 없는 CD를 공식처럼 두지 않음, 요소 semanticId는 그대로)
      - 같은 idShort의 원본 CD가 있으면 원본 id 그대로 넣는다(예: .../PredictiveMaintenanceRemainingUsefulLifetime/1/0,
        0922 검토본 #97 반도체홀가공기와 같은 처리)"""
    off = _load_official_cds()
    n, by_src = 0, {}
    for cd in [o for o in store if isinstance(o, ConceptDescription)]:
        hit = off.get(cd.id)
        if hit is None:
            continue
        store.discard(cd)
        store.add(_official_copy(cd.id))
        n += 1
        by_src[hit[1]] = by_src.get(hit[1], 0) + 1
    removed, added = [], []
    have = {o.id: o for o in store if isinstance(o, ConceptDescription)}
    for sid in sorted(_used_semantic_ids(store)):
        gap = _OFFICIAL_NO_CD.get(sid)
        if gap is None or sid in off:               # 다른 공식 템플릿에 그 id의 CD가 있으면 위에서 원본으로 바뀜
            continue
        if sid in have:
            store.discard(have.pop(sid)); removed.append(gap[1] or sid)
        for a in gap[2]:
            if a in off and a not in have:
                have[a] = _official_copy(a); store.add(have[a]); added.append(a)
                by_src[off[a][1]] = by_src.get(off[a][1], 0) + 1; n += 1
    if verbose:
        print(f"공식 템플릿 CD 원본 복원: {n}개 (" + ", ".join(f"{k.split('_Template')[0]} {v}" for k, v in sorted(by_src.items())) + ")")
        if removed or added:
            print(f"원본에 맞는 CD가 없는 공식 semanticId: 생성 CD 제거 {len(removed)}개 {removed} / 같은 idShort 원본 CD 포함 {len(added)}개")
    return n


class _OrderedRefs(list):
    """AAS.submodel·IEC61360 valueList용 순서 보존 컬렉션(set처럼 add/discard 지원)."""
    def add(self, x):
        if x not in self:
            self.append(x)
    def discard(self, x):
        if x in self:
            self.remove(x)


def generate(mapping, out_dir, thumbnail=None, product_image=None, attachments=None, verbose=True):
    equip = mapping.get("equipment", {})
    aas_name = mapping.get("aas_name") or _camel(equip.get("name_en", "Equipment"))
    equip_en = equip.get("name_en") or aas_name
    # 출력 파일명은 사람이 식별하기 쉽게 한글 장비명 우선(없으면 aas_name). IRI는 aas_name(ASCII) 사용.
    _fn = (equip.get("name_ko") or "").strip() or aas_name
    file_name = re.sub(r'[\\/:*?"<>|]+', '', _fn).replace(' ', '_').strip('_') or aas_name
    g = Gen(aas_name, equip_en)
    store = DictObjectStore()
    sm_refs = []
    # 계획서에서 단위 수집(측정형 CD 단위용)
    unit_map = {}
    def _um(nodes):
        for n in nodes:
            if n.get("children"): _um(n["children"])
            elif n.get("unit"): unit_map[clean_idshort(n["idShort"])] = n["unit"]
    for _smx in mapping["submodels"]: _um(_smx.get("elements", []))

    for sm_map in mapping["submodels"]:
        plan_name = sm_map["idShort"]
        std_key, std_info = resolve_std(plan_name)
        is_std = (std_key is not None) and (sm_map.get("dev", {}).get("template") in ("IDTA", None, "unknown"))
        sm_idshort = std_info["sm_idShort"] if is_std else _camel(plan_name)
        # 서브모델 semanticId: 표준 IDTA 서브모델은 IDTA 템플릿 semanticId(인식·검사제외), 자체제작만 smart-factory IRI
        sm_sid = std_info["submodel_semanticId"] if is_std else f"{NS}/sm/{aas_name}/{sm_idshort}/1/0"
        # 요소
        plan_nodes = sm_map.get("elements", [])
        if is_std and plan_nodes and std_key in OVERLAY_STD:
            # 구조 변경이 허용되지 않는 표준 템플릿: 공식 구조 그대로 + 계획서 예시값만 반영
            els, _cds = load_template_elements(std_info["template_path"])
            if els:
                for e in els: strip_sml_child_ids(e)
                nv = overlay_template(els, plan_nodes, g.needs_review)
                if verbose:
                    print(f"{sm_idshort}: 공식 템플릿 구조에 계획서 예시값 {nv}개 반영")
                elems = els
            else:
                elems = g._dedup([g.build(n) for n in plan_nodes])
        else:
            elems = g._dedup([g.build(n) for n in plan_nodes])
        # 표준인데 계획서에 프로퍼티 없음 → IDTA 템플릿 요소 복사(구조만; CD/semanticId는 이후 KOSMO 정규화)
        if is_std and not elems:
            els, _cds = load_template_elements(std_info["template_path"])
            if els:
                for e in els: strip_sml_child_ids(e)   # AASd-120: SML 원소 id_short 제거
                elems = els
            else:
                g.needs_review.append(f"{plan_name}: 표준 템플릿 요소 로드 실패 → 빈 서브모델")
        sm = m.Submodel(
            id_=f"{NS}/sm/{aas_name}/{sm_idshort}/1/0", id_short=sm_idshort,
            kind=m.ModellingKind.TEMPLATE,
            semantic_id=m.ExternalReference((m.Key(m.KeyTypes.GLOBAL_REFERENCE, sm_sid),)),
            administration=m.AdministrativeInformation(version="1", revision="0"),
            description=g.desc(f"{sm_idshort} of the {equip_en} (Type template)"),
            submodel_element=elems)
        store.add(sm); sm_refs.append(m.ModelReference.from_referable(sm))

    # 썸네일
    fstore = DictSupplementaryFileContainer()
    if thumbnail and os.path.exists(thumbnail):
        with open(thumbnail, "rb") as tf:
            part = fstore.add_file("/aasx/thumbnail.png", tf, "image/png")
        thumb_bytes = open(thumbnail, "rb").read()
    else:
        import io as _io
        part = fstore.add_file("/aasx/thumbnail.png", _io.BytesIO(_PLACEHOLDER_PNG), "image/png")
        thumb_bytes = _PLACEHOLDER_PNG

    aas = m.AssetAdministrationShell(
        id_=f"{NS}/aas/{aas_name}/1/0", id_short=aas_name,
        asset_information=m.AssetInformation(
            asset_kind=m.AssetKind.TYPE,
            global_asset_id=f"{NS}/asset/{aas_name}/1/0",
            asset_type=f"{NS}/asset-type/{aas_name}/1/0",
            default_thumbnail=m.Resource(part, "image/png")),
        administration=m.AdministrativeInformation(version="1", revision="0"),
        submodel=set(sm_refs),
        description=g.desc(f"{equip_en} reference model (Type)"))
    # basyx는 서브모델 참조를 set으로 보관해 저장 순서가 매번 달라진다(APE 트리 순서 뒤섞임).
    # 계획서 순서(#01→#0N)대로 직렬화되도록 순서 있는 컬렉션으로 바꾼다.
    aas.submodel = _OrderedRefs(sm_refs)
    store.add(aas)
    # 최종 안전 패스: hack id_short 정리(SML 원소→None, 그 외→semanticId 이름). make_cds/fill 전에 수행.
    for sm in [o for o in store if isinstance(o, Submodel)]:
        for e in sm.submodel_element:
            sanitize_ids(e, False)
    strip_sample_elements(store, verbose)   # #74: IDTA 샘플 요소(Arbitrary*) 제거
    align_template_valuetypes(store, g.needs_review, verbose)   # #72·#73: 공식 템플릿 자료형 정합
    restore_template_container_sems(store, g.needs_review, verbose)   # #71: 공식 컨테이너 semanticId 복원
    n_ex = fill_examples(store, equip_en)
    if verbose and n_ex:
        print(f"빈 leaf 예시 자동채움(R24): {n_ex}개")
    refine_std_examples(store, aas_name, verbose,
                        equip_ko=(equip.get("name_ko") or None), equip_en=equip_en)   # #75: placeholder 정리
    # 파일 연결(장비 대표 이미지·첨부 파일) 후 빈 선택 File 정리. CD 생성 전에 해서 지운 요소의 CD가 남지 않게 한다.
    _embed_product_image(store, fstore, aas_name, product_image or thumbnail, verbose)
    attach_files(store, fstore, aas_name, attachments, g.needs_review, verbose)        # 선제검토 #64·#65
    prune_empty_optional_files(store, g.needs_review, verbose)                         # 선제검토 #65③
    # KOSMO 정규화(최종): 서브모델/요소 semanticId·CD를 smart-factory.kr 네임스페이스로, dataType 부여
    n_cd = kosmo_normalize(store, aas_name, equip_en, unit_map)
    if verbose:
        print(f"KOSMO 정규화: ConceptDescription {n_cd}개 생성(자체 정의는 smart-factory.kr, 공식 템플릿 CD는 마지막에 배포 원본으로 교체)")

    # description 정규화: 모든 설명을 en+ko(한글 상세)로. 계획서 def_ko를 idShort별로 수집.
    ko_map = {}
    def _kum(nodes):
        for n in nodes:
            k = clean_idshort(n.get("idShort", ""))
            if k and n.get("def_ko"): ko_map.setdefault(k, n["def_ko"])
            if n.get("children"): _kum(n["children"])
    for _smx in mapping["submodels"]: _kum(_smx.get("elements", []))
    equip_ko = equip.get("name_ko") or ""
    localize_descriptions(store, ko_map, equip_ko, equip_en, verbose)

    # CD 내용 실질화: 표준 요소는 공식 IEC61360 정의 이식, 자체 요소는 한글 정의 주입(PE Content 채움).
    enrich_cds(store, equip_en, verbose)

    # 공식 템플릿 qualifier 이식: 매핑 조립형 서브모델(TD/PP/TS)에 카디널리티·AllowedIdShort 등 원문 부여.
    apply_cardinality(store, verbose)

    # 공식 템플릿 CD는 배포 원본 그대로(생성기가 만든 CD를 원본으로 교체, 선제검토 #68·#69). 마지막에 수행.
    restore_official_cds(store, verbose)

    # NEEDS_REVIEW 정확화: 빌드 때 '자체정의로 대체'로 메모됐으나 최종적으로 공식 semanticId(IRDI/IDTA/ECLASS)로
    # 복원된 항목은 제외(허위 경보 제거). 진짜 자체정의(표준 없는 장비특화 그룹)만 남긴다.
    def _is_official_sid(s):
        return bool(s and (re.match(r'^\d{3,4}[-/]', s) or 'admin-shell' in s or 'eclass-cdp.com' in s))
    _off_ids = set()
    def _collect_off(e):
        for c in _children(e):
            sref = getattr(c, 'semantic_id', None)
            s = sref.key[0].value if (sref and sref.key) else ''
            if _is_official_sid(s) and c.id_short:
                _off_ids.add(c.id_short)
            _collect_off(c)
    for _sm in [o for o in store if isinstance(o, Submodel)]:
        _collect_off(_sm)
    g.needs_review = [r for r in g.needs_review
                      if not (r.endswith('자체정의로 대체') and r.split(':', 1)[0].strip() in _off_ids)]

    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, file_name)
    with open(base + ".json", "w", encoding="utf-8") as f: write_aas_json_file(f, store)
    with open(base + ".xml", "wb") as f: write_aas_xml_file(f, store)
    with AASXWriter(base + ".aasx") as w:
        w.write_all_aas_objects("/aasx/data.xml", store, file_store=fstore)
        w.write_thumbnail("/aasx/thumbnail.png", bytearray(thumb_bytes), "image/png")

    nsub = sum(1 for o in store if isinstance(o, Submodel))
    ncd = sum(1 for o in store if isinstance(o, ConceptDescription))
    if verbose:
        print(f"AASX 생성: {base}.aasx ({os.path.getsize(base+'.aasx')//1024}KB)")
        print(f"서브모델 {nsub} · ConceptDescription {ncd}")
        if g.needs_review:
            print("NEEDS_REVIEW:", len(g.needs_review))
            for r in g.needs_review[:10]: print("  -", r)
    # round-trip
    s2 = DictObjectStore()
    with AASXReader(base + ".aasx") as r:
        r.read_into(object_store=s2, file_store=DictSupplementaryFileContainer())
    ak = [o for o in s2 if isinstance(o, m.AssetAdministrationShell)][0].asset_information.asset_kind.name
    if verbose:
        print(f"round-trip OK: 재파싱 {len(s2)}객체 · Submodel {sum(1 for o in s2 if isinstance(o,Submodel))} · assetKind {ak}")
    return base + ".aasx", {"submodels": nsub, "cds": ncd, "needs_review": g.needs_review,
                            "file_name": file_name, "aas_name": aas_name,
                            "submodel_list": [s.id_short for s in store if isinstance(s, Submodel)]}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("사용: python generate_aasx.py <mapping.json> [출력폴더] [썸네일.png]")
    mp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "out")
    thumb = sys.argv[3] if len(sys.argv) > 3 else None
    data = json.load(open(mp, encoding="utf-8"))
    generate(data, out, thumbnail=thumb)
