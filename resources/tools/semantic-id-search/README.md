# 시맨틱ID 검색 효율성 개선 도구

Windows PC에서 ECLASS 속성 후보를 검색하고 정의·단위·적용 조건을 비교하여 IRDI를 선정하는 도구입니다. 단일 검색, 엑셀 일괄 검색, 한국어 참고 번역, 확정 이력 관리를 지원합니다.

**버전 1.0 · Windows 64비트 · 시험 배포 · 2026-10-30 업데이트**

## 자료 목록

| 자료 | 링크 |
|---|---|
| 발표자료 · 편집 가능한 PPT 원본 | [시맨틱ID 검색 효율성 개선도구.pptx](시맨틱ID_검색_효율성_개선도구.pptx) |
| 도움말 | [도움말.html](도움말.html) — 다운로드하여 브라우저에서 열기 |
| 엑셀 입력 예제 | [검색항목_예제.xlsx](검색항목_예제.xlsx) |
| 실행 파일·모델·사전 | 아래 다운로드 표 또는 [버전 1.0 배포 페이지](https://github.com/IODA-Lab/aas-portal-site/releases/tag/semantic-finder-v1.0) |
| 개발용 소스 | [소스 ZIP](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/SemanticFinder-1.0-source.zip) |

## 실행에 필요한 파일

아래 **필수 5개 파일**을 같은 폴더에 저장합니다. 모델 분할 파일의 이름을 바꾸지 마세요.

| 구분 | 다운로드 | 내용 |
|---|---|---|
| 필수 | [실행 패키지](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/SemanticFinder-1.0-windows.zip) | EXE, llama.cpp 실행 도구, 도움말, 예제, 라이선스 |
| 필수 | [AI 모델 · 1/2](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/SemanticFinder-1.0-model.part1) | Qwen3 4B Q4_K_M 분할 파일 |
| 필수 | [AI 모델 · 2/2](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/SemanticFinder-1.0-model.part2) | 위 파일과 함께 필요 |
| 필수 | [설치 실행 파일](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/Install-SemanticFinder.cmd) | 더블클릭하여 설치 스크립트 실행 |
| 필수 | [설치 스크립트](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/Install-SemanticFinder.ps1) | 파일 검증, 압축 해제, 모델 결합 |
| 사전 | [ECLASS 16.0 사전 묶음](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/ECLASS-16.0-dictionaries.zip) | ADVANCED XML · ASSET XML · BASIC CSV |
| 확인용 | [파일 해시 목록](https://github.com/IODA-Lab/aas-portal-site/releases/download/semantic-finder-v1.0/SHA256SUMS.txt) | SHA-256 검증값 |

GitHub가 자동으로 표시하는 **Source code (zip)**은 이 포털 저장소의 문서 묶음이며 실행 패키지가 아닙니다.

## 처음 실행하는 순서

1. 필수 5개 파일을 같은 폴더에 내려받고 `Install-SemanticFinder.cmd`를 실행합니다.
2. 스크립트가 파일을 검증하고 `SemanticFinder-1.0` 폴더를 만듭니다. 기존 폴더는 덮어쓰지 않습니다.
3. 사전 ZIP을 원하는 위치에 압축 해제합니다. 기존에 보유한 지원 형식의 ECLASS 사전을 사용해도 됩니다.
4. `SemanticFinder-1.0/SemanticFinder.exe`를 실행합니다. 별도 Python 설치나 API 키가 필요하지 않습니다.
5. **가져올 자료 종류 → 전체 통합 → 사전 폴더 연결**에서 세 종류의 사전 폴더가 함께 들어 있는 `dictionaries` 폴더를 선택합니다.
6. 현재 검색 사전에 **ADVANCED·ASSET·BASIC CSV**가 표시되는지 확인한 뒤 검색합니다. 처음 사전을 읽을 때는 시간이 걸릴 수 있습니다.

폴더 이름·경로는 자유롭게 지정할 수 있습니다. 특정 드라이브나 `sources`라는 이름은 필요하지 않습니다.

```text
원하는 저장 위치/
├─ SemanticFinder-1.0/
│  ├─ SemanticFinder.exe
│  └─ models/qwen-ko/        # 모델과 llama.cpp 실행 도구
└─ dictionaries/
   ├─ 1730160000enUSadvancedXML01/
   ├─ 1730160000enUSassetXML01/
   └─ 1730160000enUSbasicCSV01/
```

최초 다운로드 이후 검색과 참고 번역은 PC 내부에서 처리합니다. EXE만 다른 위치로 옮기지 말고 설치된 폴더 전체를 함께 보관하세요. 앱과 사전의 다운로드 파일 및 압축 해제 결과를 함께 보관할 경우 **약 12GB 이상의 여유 공간**을 권장합니다.

## 주요 기능

- 한국어·영문 항목명 및 IRDI 단일 검색
- 장비·단위·데이터형·설명 등 적용 조건 비교
- 엑셀 목록의 일괄 검색 및 후보 비교·검토 근거·입력 정보 출력
- 사전 원문과 한국어 참고 번역 확인
- 사용자 검토 후 IRDI 확정, 이력 조회·내보내기·선택 기록 삭제

AI는 검색어 해석과 참고 번역을 보조하며 IRDI를 생성하지 않습니다. 후보는 연결한 ECLASS 사전에서 조회합니다. 모델과 실행 도구는 `models/qwen-ko`에 함께 제공됩니다.

## 개발 진행 중인 시험 기능

최신 EXE에는 개발계획서 비교·검증, 확정 결과 엑셀 내보내기, 확정 IRDI의 AASX 복사본 반영 기능이 포함되어 있습니다. 이 기능들은 개발·검증을 계속하는 시험 기능입니다. 문서 추출 결과와 실제 변경 범위를 확인한 뒤 사용하세요.

- 계획서의 한국어 항목명·기존 semanticID를 추출하고 독립 검색 후보와 비교
- 단위가 불필요한 항목과 누락된 항목을 구분하며 빈 셀을 임의 값으로 채우지 않고 검토 상태 기록
- AASX 대상 항목 선택으로 기존 ID와 대상 파일 정보를 불러오고, 원본을 보존하는 새 파일에 확정 ID 반영
- 저장 전후 첨부파일과 속성값·단위·데이터형 등 변경 범위 검사

## 기존 사용자 업데이트

새 실행 패키지를 별도 폴더에 압축 해제하고 기존 `models` 폴더를 함께 준비합니다. 기존 사용자 데이터 폴더와 확정 이력은 보관하세요. AI 모델·사전 파일의 SHA-256이 기존 배포와 같으면 다시 다운로드할 필요가 없습니다. 처음 설치하는 사용자는 아래 필수 5개 파일을 모두 받으세요.

## 시험 배포 범위와 검토 사항

- 순위는 정답 확률이 아닙니다. 후보의 정의·단위·실제 사용 목적을 검토한 뒤 최종 선정합니다.
- 한국어 표현에 따라 적합한 후보의 순위가 낮아질 수 있습니다. 검색어를 짧게 바꾸거나 영문 항목명으로 함께 확인하세요.
- 한국어 정의는 참고 번역이며 공식 ECLASS 번역을 대체하지 않습니다.
- 다른 개정번호의 IRDI는 별도 식별자입니다. 계획서와 사전 버전이 다른 경우 원문을 대조합니다.
- Windows 64비트 시험 실행 파일이며 코드 서명은 포함하지 않습니다.

## 사전과 저장 데이터

제공 사전은 ECLASS 16.0의 ADVANCED XML·ASSET XML·BASIC CSV 자료입니다. 사전은 도구 소스와 별도의 ECLASS 저작물이며, 이 저장소에 게시되었다는 이유로 별도의 자유 이용 라이선스가 부여되는 것은 아닙니다. 제공된 원문 안내와 적용되는 ECLASS 이용 조건을 따르세요.

사전 묶음에는 사전 파일 및 해당 배포 자료의 안내 문서만 포함합니다. 개인별 라이선스 증명서, 개발계획서, 기존 사전 DB, 검색·번역 캐시, 확정 이력은 포함하지 않습니다. 각 사용자의 검색 처리 결과와 확정 이력은 해당 PC에 생성됩니다.

Qwen·llama.cpp의 출처 및 라이선스는 `models/qwen-ko`, 기타 구성요소의 라이선스는 `licenses`에 있습니다.

[← 공통 양식·도구](../../tool.md)
