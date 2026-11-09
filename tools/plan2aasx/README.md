# plan2aasx

장비개발계획서(AAS 참조모델 개발계획서 양식, `.hwp`/`.hwpx`)를 읽어 **표준 AASX 패키지**와 **사전 검증 리포트**를 자동으로 만드는 변환기입니다.
모든 단계가 규칙 기반 코드로 동작하며, 같은 입력이면 같은 결과를 냅니다.

```
계획서(.hwp/.hwpx) → 매핑표(mapping.json) → AAS 참조모델(.aasx/.json/.xml) → 검증 리포트(.md/.json)
```

현재 버전: **1.1** (2026-10-28)

## 주요 기능

- **계획서 파싱:** 계획서의 장비 정보와 서브모델별 프로퍼티 표(idShort, 자료형, 단위, semanticId, 설명)를 읽어 매핑표로 만듭니다.
- **AASX 생성:** Eclipse BaSyx Python SDK로 AAS 3.0 메타모델에 맞는 `.aasx`, `.json`, `.xml`을 함께 씁니다.
- **IDTA 공식 템플릿 우선:** Digital Nameplate, Technical Data, Handover Documentation, Functional Safety, Predictive Maintenance, Time Series, Process Parameters는 IDTA 공식 템플릿의 구조, semanticId, ConceptDescription을 원문 그대로 씁니다.
- **공통 서브모델 자동 채움:** 계획서에 프로퍼티 표가 없는 Nameplate, HandoverDocumentation은 공식 템플릿 요소로 채웁니다.
- **사전 검증:** 생성한 AASX를 다시 읽어 14개 규칙(Critical, Major, Minor)으로 점검하고, Critical이 0이면 게이트 PASS로 판정합니다.
- **실행 기록:** 도구 버전, 입력 파일, 결과 요약을 로그 JSON으로 남깁니다.
- **두 가지 실행 방식:** 창 프로그램(`plan2aasx.exe`, 파이썬 설치 불필요)과 명령줄(`python run.py`)을 모두 지원합니다.

## 요구사항

- Windows 10/11
- 한컴 오피스: `.hwp` 입력을 `.hwpx`로 바꿀 때만 필요합니다. 한컴이 없으면 계획서를 한컴에서 `.hwpx`로 저장해서 넣으면 됩니다.
- 소스로 실행할 때: Python 3.10 이상

```
pip install basyx-python-sdk==2.0.1 lxml
```

> basyx-python-sdk는 버전에 따라 API가 달라서 2.0.1로 고정합니다.

## 사용법

### 1. 실행 파일

1. `plan2aasx.exe`를 더블클릭합니다.
2. 파일 선택 창에서 계획서를 고릅니다.
3. 변환이 끝나면 완료 창에 결과 폴더와 게이트 판정이 나옵니다.

`plan2aasx.exe "계획서.hwp"`처럼 경로를 주면 창이 열리면서 경로가 미리 채워집니다. 변환은 창에서 실행합니다.

### 2. 명령줄 (소스)

```
python run.py <계획서.hwp|.hwpx> [출력폴더]
```

출력 폴더를 생략하면 계획서 옆에 `<계획서 이름>_AAS` 폴더를 만듭니다.

단계별로 따로 돌릴 수도 있습니다.

```
python parse_plan.py <계획서.hwpx> mapping.json     # 계획서 → 매핑표
python generate_aasx.py mapping.json out           # 매핑표 → AASX (out 폴더)
python validate_aasx.py out/<장비명>.aasx           # AASX → 검증 리포트
```

## 출력 파일

| 파일 | 설명 |
|---|---|
| `mapping.json` | 계획서에서 읽어 낸 중간 매핑표입니다. 결과가 이상할 때 프로그램이 계획서를 어떻게 읽었는지 확인하는 용도입니다. |
| `<장비명>.aasx`, `.json`, `.xml` | 생성된 AAS 참조모델 |
| `<장비명>_validation.md`, `.json` | 사전 검증 리포트 (Critical, Major, Minor, 게이트) |
| `<장비명>_<담당자>_log.json` | 실행 로그 (도구 버전, 입력, 결과) |

고칠 내용이 있으면 출력 파일이나 `mapping.json`을 직접 고치지 말고, **계획서를 고친 뒤 다시 변환**합니다.

### 계획서 옆에 두면 함께 넣는 파일

파일 이름으로 찾으며, 계획서 옆 파일이 항상 우선합니다.

| 파일 이름 | 들어가는 곳 | 없을 때 |
|---|---|---|
| `장비이미지.png` (또는 `productimage.*`) | 썸네일, TechnicalData ProductImages | 비워 두고 검토 필요(NEEDS_REVIEW)로 표시 |
| `인증마크.*` (또는 `marking_example.*`) | Nameplate Markings의 MarkingFile | 공통 예시 파일 `templates/defaults/marking_example.png` |
| `운영매뉴얼.*` (또는 `operation_manual_example.*`) | HandoverDocumentation DigitalFiles | 공통 예시 파일 `templates/defaults/operation_manual_example.pdf` |

공통 예시 파일에는 장비 이름이 없고 "예시, 실제 인증이나 매뉴얼 아님"이라고 적혀 있습니다. 실제 파일이 생기면 계획서 옆에 두고 다시 변환하세요.

## 검증 규칙

| 등급 | 규칙 |
|---|---|
| Critical | C1 AASX 다시 읽기(round-trip), C2 `assetKind=Type`, C3 Submodel `kind=Template`, C4 요소 semanticId에 맞는 ConceptDescription 존재 |
| Major | M1 CD 영문 정의, M2 측정형 CD 단위, M3 서브모델 semanticId (표준은 IDTA, 자체는 smart-factory.kr), M4 SML 원소 idShort 없음, M5 같은 부모 아래 idShort 유일, M6 공식 템플릿 CD가 배포 원본과 같음, M7 File 경로의 실제 파일이 패키지에 있음 |
| Minor | m1 공개 IRI에 장비 고유 id 없음, m2 서브모델 6종 이상, m3 필수 File 값 |

> 이 리포트는 **사전 점검**입니다. 최종 제출 전에 KOSMO, IDTA 검증기로 한 번 더 확인하세요.

## 변환 원칙

- 요소, 값, semanticId는 **계획서에 적힌 그대로** 씁니다. 코드가 의미를 바꾸지 않습니다.
- 표준 IDTA 서브모델은 **IDTA 표준 semanticId**를 씁니다. 표준 템플릿이 없는 서브모델(예: Operational Data)만 `https://www.smart-factory.kr/ids/...` IRI로 자체 정의합니다.
- IDTA 공식 원본(`templates/official/*.json`)의 idShort, semanticId, 자료형, qualifier, ConceptDescription을 원문 그대로 씁니다. 형식 검사기를 통과시키려고 공식 값을 바꾸지 않습니다.
- 원본 템플릿 자체의 결함 가운데 메타모델로 표현할 수 없는 두 가지(같은 언어 태그 중복, CD id 중복)만 최소한으로 처리하고 그 내용을 기록합니다.
- 공식 요소의 semanticId에 맞는 CD가 원본에 없으면 CD를 새로 만들지 않고 원본대로 둡니다. 검증 C4는 이를 "원본 예외"로 표시합니다.
- 실제 파일이 없는 선택(0..1, 0..*) File 요소는 빈 자리로 두지 않고 뺍니다.

## 변환이 멈췄을 때

| 메시지 | 할 일 |
|---|---|
| 입력은 .hwp 또는 .hwpx 여야 합니다 | 한글 계획서 파일인지 확인 |
| HWP→HWPX 변환 실패(한컴 오피스 설치 필요) | 한컴 설치를 확인하거나, 계획서를 `.hwpx`로 저장해서 넣기 |
| 한글 계획서(.hwpx)를 열지 못했습니다 | 파일 손상, 또는 이름만 `.hwpx`인 다른 형식 |
| 계획서 양식의 표를 찾지 못했습니다 | 장비개발계획서 양식이 아닌 문서 |

실패해도 실행 로그(`*_log.json`)에 오류 종류와 내용이 남습니다.

## 폴더 구성

```
plan2aasx/
├─ run.py                 # 오케스트레이터 (한컴 변환 → 파싱 → 생성 → 검증)
├─ gui.py                 # 창 프로그램 (tkinter)
├─ parse_plan.py          # 계획서(HWPX) → 매핑표
├─ generate_aasx.py       # 매핑표 → AASX (BaSyx)
├─ validate_aasx.py       # AASX → 검증 리포트
├─ idta_semantics.json    # 표준 서브모델 semanticId
├─ ko_descriptions.json   # 공식 템플릿 요소의 한국어 설명
├─ plan2aasx.spec         # PyInstaller 빌드 설정
└─ templates/
   ├─ *.aasx              # IDTA 서브모델 템플릿
   ├─ official/           # IDTA 공식 템플릿 JSON (admin-shell-io/submodel-templates)
   └─ defaults/           # 공통 예시 첨부 (인증마크, 운영매뉴얼)
```

## 실행 파일 빌드

```
pip install pyinstaller
python -m PyInstaller plan2aasx.spec --noconfirm
```

`dist/plan2aasx.exe`가 만들어집니다. 콘솔 없는 창 프로그램이며, `idta_semantics.json`, `ko_descriptions.json`, `templates/`를 함께 담습니다.

## 출처와 라이선스

- `templates/`의 IDTA 서브모델 템플릿은 [admin-shell-io/submodel-templates](https://github.com/admin-shell-io/submodel-templates)에서 받은 공식 배포본이며, 원 저작권과 라이선스(CC BY 4.0)를 따릅니다.
- AAS 처리는 [Eclipse BaSyx Python SDK](https://github.com/eclipse-basyx/basyx-python-sdk) (MIT)를 사용합니다.
