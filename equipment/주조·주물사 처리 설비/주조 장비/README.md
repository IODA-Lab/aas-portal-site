# 주조 장비

장비군: 주조·주물사 처리 설비 · 담당자: <a href="https://github.com/IODA-Lab/aas-portal-site/issues/new?template=equipment-question.yml&amp;title=%5B%EB%AC%B8%EC%9D%98%5D+%EC%A3%BC%EC%A1%B0+%EC%9E%A5%EB%B9%84&amp;equipment=%EC%A3%BC%EC%A1%B0+%EC%9E%A5%EB%B9%84">김익제</a> <sub>(이름을 누르면 문의 양식이 열립니다)</sub>

## 자료

| 구분 | 파일 |
|---|---|
| 개발계획서 | [주조장비_개발계획서.hwp](%EA%B0%9C%EB%B0%9C%EA%B3%84%ED%9A%8D%EC%84%9C/%EC%A3%BC%EC%A1%B0%EC%9E%A5%EB%B9%84_%EA%B0%9C%EB%B0%9C%EA%B3%84%ED%9A%8D%EC%84%9C.hwp) |
| 가이던스 | [주조장비_가이던스.docx](%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4/%EC%A3%BC%EC%A1%B0%EC%9E%A5%EB%B9%84_%EA%B0%80%EC%9D%B4%EB%8D%98%EC%8A%A4.docx) |
| AASX | [DieCastingMachine_v0.0.1_260930.aasx](AASX/DieCastingMachine_v0.0.1_260930.aasx) |

## 서브모델

| 서브모델 | 용도 | 항목 수 |
|---|---|--:|
| Nameplate | 장비를 식별하는 명판 정보 | 30 |
| HandoverDocumentation | 납품 시 함께 전달하는 문서 목록 | 121 |
| TechnicalData | 제조사가 제시하는 기술 사양 | 96 |
| OperationalData | 운전 중 변하는 장비 상태 값 | 52 |
| TimeSeries | 상태 값의 시간별 기록 | 1506 |
| ProcessParameters | 제품·공정별 설정값 | 41 |
| PredictiveMaintenance | 예지정비 모델과 결과 | 91 |

## 프로퍼티

서브모델 이름을 누르면 표가 펼쳐집니다. **표의 예시값은 참조모델 설명을 위한 값이며 실제 장비의 측정값이 아닙니다.** 의미 ID의 `sf:`는 `https://www.smart-factory.kr/ids/cd/`, `ai:`는 `https://admin-shell.io/`를 줄인 것입니다.

<details>
<summary><b>Nameplate</b> · 장비를 식별하는 명판 정보 · 항목 30개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| URIOf<wbr>The<wbr>Product | unique global identification of the product instance using an universal resource identifier (URI)<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABN590#<wbr>002</sub> | URI |  | https:<wbr>/<wbr>/<wbr>www.<wbr>smart-<wbr>factory.<wbr>kr/<wbr>ids/<wbr>asset/<wbr>DieCastingMachine/<wbr>DC… |
| Manufacturer<wbr>Name | legally valid designation of the natural or judicial person which is directly responsible for the design, production, packaging and labelin…<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA565#<wbr>009</sub> | 다국어 |  | ExampleCompany |
| Manufacturer<wbr>Product<wbr>Designation | short description of the product (short text), third or lowest level of a 3 level manufacturer specific product hierarchy<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA567#<wbr>009</sub> | 다국어 |  | Cold Chamber Die Casting Machine |
| **Address<wbr>Information** | Note: this set of information is defined by SMT drop-in &quot;Address Information&quot;<br><sub>ai:<wbr>zvei/<wbr>nameplate/<wbr>1/<wbr>0/<wbr>ContactInformations/<wbr>AddressInformation</sub> | 묶음 (4) |  |  |
| &emsp;Street | <br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO128#<wbr>002</sub> | 다국어 |  | Example Street 1 |
| &emsp;Zipcode | <br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO129#<wbr>002</sub> | 다국어 |  | 12345 |
| &emsp;City<wbr>Town | <br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO132#<wbr>002</sub> | 다국어 |  | Example City |
| &emsp;National<wbr>Code | <br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO134#<wbr>002</sub> | 다국어 |  | KR |
| Manufacturer<wbr>Product<wbr>Root | top level of a 3 level manufacturer specific product hierarchy<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61360_<wbr>7#<wbr>AAS011#<wbr>001</sub> | 다국어 |  | Casting Equipment |
| Manufacturer<wbr>Product<wbr>Family | second level of a 3 level manufacturer specific product hierarchy<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABP464#<wbr>002</sub> | 다국어 |  | High-<wbr>Pressure Die Casting Machine |
| Manufacturer<wbr>Product<wbr>Type | characteristic to differentiate between different products of a product family or special variants<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA300#<wbr>008</sub> | 문자열 |  | DC-<wbr>800 |
| Order<wbr>Code<wbr>Of<wbr>Manufacturer | unique combination of numbers and letters issued by the manufacturer that is used to identify the device for ordering<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA950#<wbr>008</sub> | 문자열 |  | DC-<wbr>800-<wbr>ORD |
| Product<wbr>Article<wbr>Number<wbr>Of<wbr>Manufacturer | unique product identifier of the manufacturer<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA581#<wbr>007</sub> | 문자열 |  | DC-<wbr>800-<wbr>ART |
| Serial<wbr>Number | unique combination of numbers and letters used to identify the device once it has been manufactured<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA951#<wbr>009</sub> | 문자열 |  | DC-<wbr>SN-<wbr>2026-<wbr>0001 |
| Year<wbr>Of<wbr>Construction | year in which the manufacturing process is completed<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABP000#<wbr>002</sub> | 문자열 |  | 2026 |
| Date<wbr>Of<wbr>Manufacture | date when an item was manufactured<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABB757#<wbr>007</sub> | 날짜 |  | 2026-<wbr>06-<wbr>17 |
| Hardware<wbr>Version | version of the hardware supplied with the device<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA926#<wbr>008</sub> | 문자열 |  | HW-<wbr>1.<wbr>0 |
| Firmware<wbr>Version | version of the firmware supplied with the device<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA302#<wbr>006</sub> | 문자열 |  | FW-<wbr>1.<wbr>0 |
| Software<wbr>Version | version of the software used by the device<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA601#<wbr>008</sub> | 문자열 |  | SW-<wbr>1.<wbr>0 |
| Country<wbr>Of<wbr>Origin | Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABP462#<wbr>001</sub> | 문자열 |  | KR |
| Unique<wbr>Facility<wbr>Identifier | unique string of characters for the identification of locations or buildings involved in a product’s value chain or used by actors involved…<br><sub>ai:<wbr>idta/<wbr>nameplate/<wbr>3/<wbr>0/<wbr>UniqueFacilityIdentifier</sub> | 문자열 |  | TYPE-<wbr>DC-<wbr>800 |
| Company<wbr>Logo | a graphic mark used to represent a company, an organisation or a product<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABP463#<wbr>001</sub> | 파일 |  | CompanyLogo.<wbr>png |
| **Markings** | Note: CE marking is declared as mandatory according to EU Blue Guide<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61360_<wbr>7#<wbr>AAS006#<wbr>001</sub> | 목록 (1) |  |  |
| &emsp;**(항목)** | Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61360_<wbr>7#<wbr>AAS009#<wbr>001</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;Marking<wbr>Name | common name of the marking<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABA231#<wbr>009</sub> | 문자열 |  | CE |
| &emsp;&emsp;Designation<wbr>Of<wbr>Certificate<wbr>Or<wbr>Approval | Note: Approval identifier, reference to the certificate number, to be entered without spaces<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABH783#<wbr>003</sub> | 문자열 |  | Declaration of Conformity |
| &emsp;&emsp;Issue<wbr>Date | Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABO097#<wbr>001</sub> | 날짜 |  | 2026-<wbr>06-<wbr>17 |
| &emsp;&emsp;Expiry<wbr>Date | Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABH830#<wbr>002</sub> | 날짜 |  | 2036-<wbr>06-<wbr>16 |
| &emsp;&emsp;Marking<wbr>File | conformity symbol of the marking<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABO100#<wbr>002</sub> | 파일 |  | DieCastingMachine_<wbr>CertificatesDeclarations_<wbr>EN.<wbr>pdf |
| &emsp;&emsp;Marking<wbr>Additional<wbr>Text | where applicable, additional information on the marking in plain text, e.g. the ID-number of the notified body involved in the conformity p…<br><sub>0112/<wbr>2/<wbr>/<wbr>/<wbr>61987#<wbr>ABB146#<wbr>007</sub> | 문자열 |  | Conformity information for the DC-<wbr>800 equipment type. |

</details>

<details>
<summary><b>HandoverDocumentation</b> · 납품 시 함께 전달하는 문서 목록 · 항목 121개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Documents** | Information for a document identity<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI500#<wbr>003</sub> | 목록 (5) |  |  |
| &emsp;**(항목)** | This SubmodelElementCollection holds the information for a VDI 2770 Document entity<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI500#<wbr>003/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHF579#<wbr>003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;**Document<wbr>Ids** | Set of document identifiers for the document. One ID in this collection should be used as a preferred ID<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI501#<wbr>003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | This SubmodelElementCollection holds the information for a VDI 2770 Document entity<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI501#<wbr>003/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHF580#<wbr>003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;&emsp;Document<wbr>Domain<wbr>Id | Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organ…<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABH994#<wbr>003</sub> | 문자열 |  | EXAMPLE_<wbr>DIE_<wbr>CASTING_<wbr>DOC |
| &emsp;&emsp;&emsp;&emsp;Document<wbr>Identifier | alphanumeric character sequence uniquely identifying a document<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO099#<wbr>004</sub> | 문자열 |  | DC-<wbr>OM-<wbr>001 |
| &emsp;&emsp;&emsp;&emsp;Document<wbr>Is<wbr>Primary | Flag indicating that a DocumentId within a collection of at least two DocumentId`s is the ‘primary’ identifier for the document. This is th…<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABH995#<wbr>003</sub> | 참/거짓 |  | true |
| &emsp;&emsp;**Document<wbr>Classifications** | Set of information for describing the classification of the Document according to ClassificationSystems<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI502#<wbr>003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | Set of information for describing the classification of the Document according to a ClassificationSystem<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI502#<wbr>003/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHF581#<wbr>003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;&emsp;Class<wbr>Id | Unique ID of the document class within a classficationsystem<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABH996#<wbr>003</sub> | 문자열 |  | 03-<wbr>02 |
| &emsp;&emsp;&emsp;&emsp;Class<wbr>Name | Name of the class in the classification system<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABJ219#<wbr>002</sub> | 다국어 |  | Operation |
| &emsp;&emsp;&emsp;&emsp;Classification<wbr>System | Identification of the classification system<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABH997#<wbr>003</sub> | 문자열 |  | VDI 2770 Blatt 1:<wbr>2020 |
| &emsp;&emsp;**Document<wbr>Versions** | Information elements of individual Document Version entities<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI503#<wbr>003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | Information about a document version entity<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI503#<wbr>003/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHF582#<wbr>003</sub> | 묶음 (9) |  |  |
| &emsp;&emsp;&emsp;&emsp;**Language** | Language style of the document<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAN468#<wbr>008</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;&emsp;&emsp;(항목) | Language style of the document<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAN468#<wbr>008</sub> | 문자열 |  | en |
| &emsp;&emsp;&emsp;&emsp;Version | Design that partly deviates from the previous<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAP003#<wbr>005</sub> | 문자열 |  | 1.<wbr>0 |
| &emsp;&emsp;&emsp;&emsp;Title | Name of the document<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABG940#<wbr>003</sub> | 다국어 |  | Die Casting Machine Operating Manual |
| &emsp;&emsp;&emsp;&emsp;Description | Plain text characterizing the content of the document<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAN466#<wbr>004</sub> | 다국어 |  | Example handover document for the DC-<wbr>800 die casting machin… |
| &emsp;&emsp;&emsp;&emsp;Status<wbr>Set<wbr>Date | Date when the document status was set<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI000#<wbr>003</sub> | 날짜 |  | 2026-<wbr>06-<wbr>17 |
| &emsp;&emsp;&emsp;&emsp;Status<wbr>Value | Each document version represents a point in time in the document life cycle. This status value refers to the milestones in the document lif…<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI001#<wbr>003</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;Organization<wbr>Short<wbr>Name | Short name of the organization<br><sub>https:<wbr>/<wbr>/<wbr>api.<wbr>eclass-<wbr>cdp.<wbr>com/<wbr>0173-<wbr>1-<wbr>02-<wbr>ABI002-<wbr>003</sub> | 문자열 |  | ExampleOrg |
| &emsp;&emsp;&emsp;&emsp;Organization<wbr>Official<wbr>Name | Official name of the organization of the author of the document<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI004#<wbr>003</sub> | 문자열 |  | Example Organization |
| &emsp;&emsp;&emsp;&emsp;**Digital<wbr>Files** | MIME-Type, file name and file contents given by the file SubmodelElement<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK126#<wbr>002</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;&emsp;&emsp;(항목) | MIME-Type, file name and file contents given by the file SubmodelElement<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK126#<wbr>002</sub> | 파일 |  | DieCastingMachine_<wbr>OperatingManual_<wbr>EN.<wbr>pdf |
| &emsp;<sub>⋯ 같은 구성의 묶음 4개 더 (항목 96개 생략)</sub> | | | | |

</details>

<details>
<summary><b>TechnicalData</b> · 제조사가 제시하는 기술 사양 · 항목 96개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **General<wbr>Information** | General information, for example ordering and manufacturer information<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK161#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX838#<wbr>002</sub> | 묶음 (6) |  |  |
| &emsp;Manufacturer<wbr>Name | Legally valid designation of the natural or judicial person which is directly responsible for the design, production, packaging and labelin…<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO677#<wbr>004</sub> | 문자열 |  | ExampleCompany |
| &emsp;Company<wbr>Logo | Imagefile for logo of the company provided in common format (.png, .jpg)<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABI776#<wbr>002</sub> | 파일 |  | CompanyLogo.<wbr>png |
| &emsp;Manufacturer<wbr>Product<wbr>Designation | Short description of the product (short text)<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAW338#<wbr>003</sub> | 다국어 |  | ExampleCompany Cold Chamber Die Casting Machine |
| &emsp;Manufacturer<wbr>Article<wbr>Number | unique product identifier of the manufacturer<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO676#<wbr>005</sub> | 문자열 |  | DC-<wbr>800-<wbr>ART |
| &emsp;Manufacturer<wbr>Order<wbr>Code | by manufactures issued unique combination of numbers and letters used to identify the device for ordering<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAO227#<wbr>004</sub> | 문자열 |  | DC-<wbr>800-<wbr>ORD |
| &emsp;**Product<wbr>Images** | Pictorial representations of the product also related to different applications<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABM220#<wbr>001</sub> | 목록 (1) |  |  |
| &emsp;&emsp;**(항목)** | Pictorial representation of the product related to an application<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABM220#<wbr>001/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHY911#<wbr>001</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;&emsp;Image<wbr>File | Picture of the product (low resolution) 72 dpi / rgb (GIF or JPG)<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK291#<wbr>002</sub> | 파일 |  | CASTINGMACHINE_<wbr>ProductImage.<wbr>jpg |
| &emsp;&emsp;&emsp;Image<wbr>Note | Notes or explanations about the image provided<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL423#<wbr>001</sub> | 다국어 |  | Side view of ExampleCompany cold-<wbr>chamber die casting machine |
| **Product<wbr>Classifications** | Product classifications by association of product classes with common classification systems<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK162#<wbr>002</sub> | 목록 (1) |  |  |
| &emsp;**(항목)** | Single product classification item by association with product class in a particular classification system or property dictionary<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK162#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX839#<wbr>002</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;Classification<wbr>System | Reference to the scheduled collection of abstract concepts that are used to distinguish and order objects<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL424#<wbr>001</sub> | 문자열 |  | ECLASS |
| &emsp;&emsp;Classification<wbr>System<wbr>Version | Referenced state of the published classification system<br><sub>0173-<wbr>1#<wbr>02-<wbr>AAR710#<wbr>003</sub> | 문자열 |  | ECLASS 16.<wbr>0 |
| &emsp;&emsp;Classification<wbr>System<wbr>Url | Classification system URL<br><sub>ai:<wbr>IDTA/<wbr>TechnicalData/<wbr>ProductClassifications/<wbr>ProduktClassification/<wbr>Cl…</sub> | 문자열 |  | https:<wbr>/<wbr>/<wbr>eclass.<wbr>eu/<wbr>eclass-<wbr>standard/<wbr>search-<wbr>content |
| &emsp;&emsp;Product<wbr>Class<wbr>Id | Class of the associated product or industrial equipment in the classification system. According to the notation of the system (IRDI)<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABG776#<wbr>003</sub> | 문자열 |  | 0173-<wbr>1#<wbr>01-<wbr>AKK476#<wbr>011 |
| &emsp;&emsp;Product<wbr>Class<wbr>Coded<wbr>Name | Unique class code in a classification hierarchy<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK128#<wbr>002</sub> | 문자열 |  | 18-<wbr>07-<wbr>00-<wbr>00 |
| &emsp;&emsp;Product<wbr>Class<wbr>Name | Name of product class in the used classification system<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK273#<wbr>002</sub> | 다국어 |  | Equipment for casting NF metal |
| &emsp;&emsp;Reference<wbr>To<wbr>Technical<wbr>Property<wbr>Area | Reference to technical property area<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002</sub> | 참조 |  |  |
| **Technical<wbr>Property<wbr>Areas** | List of all technical property areas<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABK163#<wbr>002</sub> | 목록 (6) |  |  |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Die<wbr>Casting<wbr>Common<wbr>System** | Groups common equipment-type characteristics of the die casting machine.<br><sub>sf:<wbr>DieCastingCommonSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Die<wbr>Casting<wbr>Common<wbr>Specifications** | Common process, configuration, installation and mass specifications.<br><sub>sf:<wbr>DieCastingCommonSpecifications/<wbr>1/<wbr>0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;&emsp;&emsp;Casting<wbr>Process<wbr>Type | Type of casting process performed by the equipment.<br><sub>sf:<wbr>CastingProcessType/<wbr>1/<wbr>0</sub> | 문자열 |  | High-<wbr>pressure die casting (cold chamber) |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Casting<wbr>Machine<wbr>Type | Mechanical configuration of the die casting machine.<br><sub>sf:<wbr>DieCastingMachineType/<wbr>1/<wbr>0</sub> | 문자열 |  | Horizontal cold chamber die casting machine |
| &emsp;&emsp;&emsp;&emsp;Cast<wbr>Metal<wbr>Type | Metal families supported by the equipment type.<br><sub>sf:<wbr>CastMetalType/<wbr>1/<wbr>0</sub> | 문자열 |  | Aluminum and zinc alloys |
| &emsp;&emsp;&emsp;&emsp;System<wbr>Configuration | Integrated equipment systems included in the reference configuration.<br><sub>sf:<wbr>SystemConfiguration/<wbr>1/<wbr>0</sub> | 문자열 |  | Integrated injection, clamping, hydraulic, cooling and safe… |
| &emsp;&emsp;&emsp;&emsp;Installation<wbr>Type | Installation arrangement of the equipment.<br><sub>sf:<wbr>InstallationType/<wbr>1/<wbr>0</sub> | 문자열 |  | Floor-<wbr>mounted stationary equipment |
| &emsp;&emsp;&emsp;&emsp;Net<wbr>Weight | Net mass of the equipment type.<br><sub>sf:<wbr>NetWeight/<wbr>1/<wbr>0</sub> | 실수 | kg | 42000 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Casting<wbr>Capacity<wbr>And<wbr>Production<wbr>System** | Groups casting capacity and production capability specifications.<br><sub>sf:<wbr>CastingCapacityAndProductionSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Casting<wbr>Capacity<wbr>And<wbr>Production<wbr>Specifications** | Capacity, cycle, shot and alloy-range specifications of the equipment type.<br><sub>sf:<wbr>CastingCapacityAndProductionSpecifications/<wbr>1/<wbr>0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;&emsp;&emsp;Clamping<wbr>Force | Maximum rated die clamping force.<br><sub>sf:<wbr>ClampingForce/<wbr>1/<wbr>0</sub> | 실수 | kN | 8000 |
| &emsp;&emsp;&emsp;&emsp;Max<wbr>Shot<wbr>Weight | Maximum metal mass injected in one shot.<br><sub>sf:<wbr>MaxShotWeight/<wbr>1/<wbr>0</sub> | 실수 | kg | 6.<wbr>5 |
| &emsp;&emsp;&emsp;&emsp;Max<wbr>Projected<wbr>Area | Maximum allowable projected casting area.<br><sub>sf:<wbr>MaxProjectedArea/<wbr>1/<wbr>0</sub> | 실수 | cm² | 1600 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Casting<wbr>Cycle<wbr>Time | Reference duration of one complete casting cycle.<br><sub>sf:<wbr>DieCastingCycleTime/<wbr>1/<wbr>0</sub> | 기간 |  | PT45S |
| &emsp;&emsp;&emsp;&emsp;Casting<wbr>Cycles<wbr>Per<wbr>Hour | Reference number of casting cycles per hour.<br><sub>sf:<wbr>CastingCyclesPerHour/<wbr>1/<wbr>0</sub> | 실수 | shots/h | 80 |
| &emsp;&emsp;&emsp;&emsp;Production<wbr>Capacity | Reference daily shot production capacity.<br><sub>sf:<wbr>ProductionCapacity/<wbr>1/<wbr>0</sub> | 실수 | shots/day | 1900 |
| &emsp;&emsp;&emsp;&emsp;Cast<wbr>Alloy<wbr>Range | Representative alloys supported by the equipment type.<br><sub>sf:<wbr>CastAlloyRange/<wbr>1/<wbr>0</sub> | 문자열 |  | ADC12, A380, Zamak 3/<wbr>5 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Molten<wbr>Metal<wbr>And<wbr>Injection<wbr>System** | Groups molten-metal and hydraulic injection specifications.<br><sub>sf:<wbr>MoltenMetalAndInjectionSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Molten<wbr>Metal<wbr>And<wbr>Injection<wbr>Specifications** | Temperature, pressure, speed, plunger and shot-sleeve specifications.<br><sub>sf:<wbr>MoltenMetalAndInjectionSpecifications/<wbr>1/<wbr>0</sub> | 묶음 (10) |  |  |
| &emsp;&emsp;&emsp;&emsp;Molten<wbr>Metal<wbr>Type | Molten-metal material used for the reference configuration.<br><sub>sf:<wbr>MoltenMetalType/<wbr>1/<wbr>0</sub> | 문자열 |  | Aluminum alloy (ADC12) |
| &emsp;&emsp;&emsp;&emsp;Molten<wbr>Metal<wbr>Temperature<wbr>Range | Supported molten-metal temperature range.<br><sub>sf:<wbr>MoltenMetalTemperatureRange/<wbr>1/<wbr>0</sub> | 실수 범위 | °C | 640 ~ 700 |
| &emsp;&emsp;&emsp;&emsp;Max<wbr>Injection<wbr>Pressure | Maximum rated injection pressure.<br><sub>sf:<wbr>MaxInjectionPressure/<wbr>1/<wbr>0</sub> | 실수 | bar | 1000 |
| &emsp;&emsp;&emsp;&emsp;Injection<wbr>Pressure<wbr>Range | Supported injection-pressure range.<br><sub>sf:<wbr>InjectionPressureRange/<wbr>1/<wbr>0</sub> | 실수 범위 | bar | 300 ~ 1000 |
| &emsp;&emsp;&emsp;&emsp;Intensification<wbr>Pressure | Reference secondary intensification pressure.<br><sub>sf:<wbr>IntensificationPressure/<wbr>1/<wbr>0</sub> | 실수 | bar | 1050 |
| &emsp;&emsp;&emsp;&emsp;Max<wbr>Plunger<wbr>Speed | Maximum plunger speed during injection.<br><sub>sf:<wbr>MaxPlungerSpeed/<wbr>1/<wbr>0</sub> | 실수 | m/s | 8 |
| &emsp;&emsp;&emsp;&emsp;Plunger<wbr>Speed<wbr>Range | Supported plunger-speed range.<br><sub>sf:<wbr>PlungerSpeedRange/<wbr>1/<wbr>0</sub> | 실수 범위 | m/s | 0.<wbr>1 ~ 8 |
| &emsp;&emsp;&emsp;&emsp;Plunger<wbr>Diameter | Nominal plunger-tip diameter.<br><sub>sf:<wbr>PlungerDiameter/<wbr>1/<wbr>0</sub> | 실수 | mm | 100 |
| &emsp;&emsp;&emsp;&emsp;Shot<wbr>Sleeve<wbr>Length | Nominal shot-sleeve length.<br><sub>sf:<wbr>ShotSleeveLength/<wbr>1/<wbr>0</sub> | 실수 | mm | 600 |
| &emsp;&emsp;&emsp;&emsp;Hydraulic<wbr>System<wbr>Pressure | Rated hydraulic system pressure.<br><sub>sf:<wbr>HydraulicSystemPressure/<wbr>1/<wbr>0</sub> | 실수 | MPa | 16 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Clamping<wbr>Unit<wbr>And<wbr>Dimension<wbr>System** | Groups clamping-unit, mechanical envelope and acoustic specifications.<br><sub>sf:<wbr>ClampingUnitAndDimensionSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Clamping<wbr>Unit<wbr>And<wbr>Dimension<wbr>Specifications** | Clamping geometry, motion, force, dimensions and sound-power specifications.<br><sub>sf:<wbr>ClampingUnitAndDimensionSpecifications/<wbr>1/<wbr>0</sub> | 묶음 (13) |  |  |
| &emsp;&emsp;&emsp;&emsp;Clamping<wbr>Unit<wbr>Type | Mechanical type of clamping unit.<br><sub>sf:<wbr>ClampingUnitType/<wbr>1/<wbr>0</sub> | 문자열 |  | Toggle-<wbr>type clamping unit |
| &emsp;&emsp;&emsp;&emsp;Platen<wbr>Width | Overall width of the machine platen.<br><sub>sf:<wbr>PlatenWidth/<wbr>1/<wbr>0</sub> | 실수 | mm | 1150 |
| &emsp;&emsp;&emsp;&emsp;Platen<wbr>Height | Overall height of the machine platen.<br><sub>sf:<wbr>PlatenHeight/<wbr>1/<wbr>0</sub> | 실수 | mm | 1150 |
| &emsp;&emsp;&emsp;&emsp;Tie<wbr>Bar<wbr>Clearance<wbr>Horizontal | Clear horizontal distance between tie bars.<br><sub>sf:<wbr>TieBarClearanceHorizontal/<wbr>1/<wbr>0</sub> | 실수 | mm | 820 |
| &emsp;&emsp;&emsp;&emsp;Tie<wbr>Bar<wbr>Clearance<wbr>Vertical | Clear vertical distance between tie bars.<br><sub>sf:<wbr>TieBarClearanceVertical/<wbr>1/<wbr>0</sub> | 실수 | mm | 820 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Height<wbr>Range | Supported die-height range.<br><sub>sf:<wbr>DieHeightRange/<wbr>1/<wbr>0</sub> | 실수 범위 | mm | 300 ~ 800 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Opening<wbr>Stroke | Maximum die-opening stroke.<br><sub>sf:<wbr>DieOpeningStroke/<wbr>1/<wbr>0</sub> | 실수 | mm | 700 |
| &emsp;&emsp;&emsp;&emsp;Ejector<wbr>Force | Maximum rated ejector force.<br><sub>sf:<wbr>EjectorForce/<wbr>1/<wbr>0</sub> | 실수 | kN | 500 |
| &emsp;&emsp;&emsp;&emsp;Ejector<wbr>Stroke | Maximum ejector stroke.<br><sub>sf:<wbr>EjectorStroke/<wbr>1/<wbr>0</sub> | 실수 | mm | 120 |
| &emsp;&emsp;&emsp;&emsp;Dimensions<wbr>Length | largest length dimension of an item, including protruding parts<br><sub>0173-<wbr>1#<wbr>02-<wbr>BAB146#<wbr>011</sub> | 실수 | mm | 8500 |
| &emsp;&emsp;&emsp;&emsp;Dimensions<wbr>Width | greatest width expansion of an object, including projecting parts<br><sub>0173-<wbr>1#<wbr>02-<wbr>BAA705#<wbr>009</sub> | 실수 | mm | 2600 |
| &emsp;&emsp;&emsp;&emsp;Dimensions<wbr>Height | largest hight dimension of an item, including projection parts<br><sub>0173-<wbr>1#<wbr>02-<wbr>BAB707#<wbr>009</sub> | 실수 | mm | 3200 |
| &emsp;&emsp;&emsp;&emsp;Sound<wbr>Power<wbr>Level | Reference A-weighted sound power level.<br><sub>sf:<wbr>SoundPowerLevel/<wbr>1/<wbr>0</sub> | 실수 | dB(A) | 82 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Die<wbr>Cooling<wbr>And<wbr>Spray<wbr>System** | Groups die cooling, spraying, vacuum and fume-extraction specifications.<br><sub>sf:<wbr>DieCoolingAndSpraySystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Die<wbr>Cooling<wbr>And<wbr>Spray<wbr>Specifications** | Cooling, release-agent, vacuum and extraction capabilities.<br><sub>sf:<wbr>DieCoolingAndSpraySpecifications/<wbr>1/<wbr>0</sub> | 묶음 (8) |  |  |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Cooling<wbr>Method | Method used to cool and regulate the die.<br><sub>sf:<wbr>DieCoolingMethod/<wbr>1/<wbr>0</sub> | 문자열 |  | Closed-<wbr>loop water cooling with temperature control |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Cooling<wbr>Water<wbr>Flow<wbr>Rate | Reference cooling-water volumetric flow rate.<br><sub>sf:<wbr>DieCoolingWaterFlowRate/<wbr>1/<wbr>0</sub> | 실수 | L/min | 60 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Temperature<wbr>Control<wbr>Supported | Indicates whether closed-loop die-temperature control is supported.<br><sub>sf:<wbr>DieTemperatureControlSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Spray<wbr>Type | Type of automatic die-spray mechanism.<br><sub>sf:<wbr>DieSprayType/<wbr>1/<wbr>0</sub> | 문자열 |  | Automatic reciprocating die spray |
| &emsp;&emsp;&emsp;&emsp;Release<wbr>Agent<wbr>Supply<wbr>Method | Method used to supply release agent to the die-spray unit.<br><sub>sf:<wbr>ReleaseAgentSupplyMethod/<wbr>1/<wbr>0</sub> | 문자열 |  | Central pressure-<wbr>fed supply |
| &emsp;&emsp;&emsp;&emsp;Vacuum<wbr>Casting<wbr>Supported | Indicates whether vacuum-assisted casting is supported.<br><sub>sf:<wbr>VacuumCastingSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Fume<wbr>Extraction<wbr>Supported | Indicates whether a fume-extraction connection is supported.<br><sub>sf:<wbr>FumeExtractionSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Fume<wbr>Extraction<wbr>Connection<wbr>Size | Nominal connection size for the fume-extraction duct.<br><sub>sf:<wbr>FumeExtractionConnectionSize/<wbr>1/<wbr>0</sub> | 문자열 |  | Ø250 mm |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-<wbr>1#<wbr>02-<wbr>ABL358#<wbr>002/<wbr>0173-<wbr>1#<wbr>01-<wbr>AHX773#<wbr>002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**Electrical<wbr>And<wbr>Safety<wbr>System** | Groups electrical ratings and supported equipment safety functions.<br><sub>sf:<wbr>ElectricalAndSafetySystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**Electrical<wbr>And<wbr>Safety<wbr>Specifications** | Power-supply, protection and functional-safety specifications.<br><sub>sf:<wbr>ElectricalAndSafetySpecifications/<wbr>1/<wbr>0</sub> | 묶음 (14) |  |  |
| &emsp;&emsp;&emsp;&emsp;Rated<wbr>Voltage | Supported line-to-line AC supply-voltage range.<br><sub>sf:<wbr>RatedVoltage/<wbr>1/<wbr>0</sub> | 실수 범위 | V AC | 380 ~ 415 |
| &emsp;&emsp;&emsp;&emsp;Power<wbr>Supply<wbr>Phase | Number and arrangement of electrical supply phases.<br><sub>sf:<wbr>PowerSupplyPhase/<wbr>1/<wbr>0</sub> | 문자열 |  | 3-<wbr>phase |
| &emsp;&emsp;&emsp;&emsp;Power<wbr>Supply<wbr>Frequency | Supported electrical supply frequencies.<br><sub>sf:<wbr>PowerSupplyFrequency/<wbr>1/<wbr>0</sub> | 문자열 | Hz | 50/<wbr>60 |
| &emsp;&emsp;&emsp;&emsp;Rated<wbr>Power | Rated active power of the equipment type.<br><sub>sf:<wbr>RatedPower/<wbr>1/<wbr>0</sub> | 실수 | kW | 75 |
| &emsp;&emsp;&emsp;&emsp;Max<wbr>Running<wbr>Current | Maximum current during normal operation.<br><sub>sf:<wbr>MaxRunningCurrent/<wbr>1/<wbr>0</sub> | 실수 | A | 140 |
| &emsp;&emsp;&emsp;&emsp;Leakage<wbr>Breaker<wbr>Capacity | Rated current capacity of the earth-leakage circuit breaker.<br><sub>sf:<wbr>LeakageBreakerCapacity/<wbr>1/<wbr>0</sub> | 실수 | A | 200 |
| &emsp;&emsp;&emsp;&emsp;Supported<wbr>Safety<wbr>Functions | Safety functions included in the reference configuration.<br><sub>sf:<wbr>SupportedSafetyFunctions/<wbr>1/<wbr>0</sub> | 문자열 |  | Emergency stop, guard interlock, light curtain, two-<wbr>hand co… |
| &emsp;&emsp;&emsp;&emsp;Safety<wbr>Gate<wbr>Interlock<wbr>Supported | Indicates whether a safety-gate interlock is supported.<br><sub>sf:<wbr>SafetyGateInterlockSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Two<wbr>Hand<wbr>Control<wbr>Supported | Indicates whether two-hand control is supported.<br><sub>sf:<wbr>TwoHandControlSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Emergency<wbr>Stop<wbr>Supported | Indicates whether an emergency-stop function is supported.<br><sub>sf:<wbr>EmergencyStopSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Over<wbr>Pressure<wbr>Relief<wbr>Supported | Indicates whether hydraulic over-pressure relief is supported.<br><sub>sf:<wbr>OverPressureReliefSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;Light<wbr>Curtain<wbr>Supported | Indicates whether light-curtain protection is supported.<br><sub>sf:<wbr>LightCurtainSupported/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;IPRating | Ingress-protection rating of the equipment enclosure.<br><sub>sf:<wbr>IPRating/<wbr>1/<wbr>0</sub> | 문자열 |  | IP54 |
| &emsp;&emsp;&emsp;&emsp;Grounding<wbr>Required | Indicates whether protective grounding is required.<br><sub>sf:<wbr>GroundingRequired/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |

</details>

<details>
<summary><b>OperationalData</b> · 운전 중 변하는 장비 상태 값 · 항목 52개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Device<wbr>Operation<wbr>System** | Groups machine-level operating state information.<br><sub>sf:<wbr>DeviceOperationSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Device<wbr>Operation<wbr>Monitoring** | Current machine mode, process identity, shot count and operating timestamps.<br><sub>sf:<wbr>DeviceOperationMonitoring/<wbr>1/<wbr>0</sub> | 묶음 (10) |  |  |
| &emsp;&emsp;Device<wbr>Run<wbr>State | Current high-level operating state of the equipment.<br><sub>sf:<wbr>DeviceRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;Operation<wbr>Mode | Selected machine operating mode.<br><sub>sf:<wbr>OperationMode/<wbr>1/<wbr>0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;Active<wbr>Process<wbr>Id | Identifier of the currently active casting process.<br><sub>sf:<wbr>ActiveProcessId/<wbr>1/<wbr>0</sub> | 문자열 |  | DC-<wbr>P-<wbr>001 |
| &emsp;&emsp;Casting<wbr>Phase | Current phase of the die casting cycle.<br><sub>sf:<wbr>CastingPhase/<wbr>1/<wbr>0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;Casting<wbr>Run<wbr>State | Current execution state of the casting process.<br><sub>sf:<wbr>CastingRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;Current<wbr>Shot<wbr>Id | Identifier of the current or most recently completed shot.<br><sub>sf:<wbr>CurrentShotId/<wbr>1/<wbr>0</sub> | 문자열 |  | SHOT-<wbr>2026-<wbr>0617-<wbr>1032 |
| &emsp;&emsp;Cumulative<wbr>Shot<wbr>Count | Cumulative number of casting shots executed.<br><sub>sf:<wbr>CumulativeShotCount/<wbr>1/<wbr>0</sub> | 정수 | shots | 1560000 |
| &emsp;&emsp;Cumulative<wbr>Operating<wbr>Hours | Cumulative equipment operating time.<br><sub>sf:<wbr>CumulativeOperatingHours/<wbr>1/<wbr>0</sub> | 실수 | h | 18600 |
| &emsp;&emsp;Operation<wbr>Start<wbr>Timestamp | Timestamp at which the current operating period started.<br><sub>sf:<wbr>OperationStartTimestamp/<wbr>1/<wbr>0</sub> | 일시 |  | 2026-<wbr>06-<wbr>17T08:<wbr>00:<wbr>00+09:<wbr>00 |
| &emsp;&emsp;Last<wbr>Update<wbr>Timestamp | Timestamp of the most recent operational-data update.<br><sub>sf:<wbr>LastUpdateTimestamp/<wbr>1/<wbr>0</sub> | 일시 |  | 2026-<wbr>06-<wbr>17T08:<wbr>20:<wbr>30+09:<wbr>00 |
| **Casting<wbr>Process<wbr>System** | Groups live high-pressure die casting process data.<br><sub>sf:<wbr>CastingProcessSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Casting<wbr>Process<wbr>Monitoring** | Current injection, temperature, cycle, throughput and quality measurements.<br><sub>sf:<wbr>CastingProcessMonitoring/<wbr>1/<wbr>0</sub> | 묶음 (13) |  |  |
| &emsp;&emsp;Molten<wbr>Metal<wbr>Temperature<wbr>Actual | Measured molten-metal temperature.<br><sub>sf:<wbr>MoltenMetalTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 675 |
| &emsp;&emsp;Injection<wbr>Pressure<wbr>Actual | Measured injection pressure.<br><sub>sf:<wbr>InjectionPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 920 |
| &emsp;&emsp;Intensification<wbr>Pressure<wbr>Actual | Measured intensification pressure.<br><sub>sf:<wbr>IntensificationPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 1020 |
| &emsp;&emsp;Plunger<wbr>Speed<wbr>Actual | Measured fast-shot plunger speed.<br><sub>sf:<wbr>PlungerSpeedActual/<wbr>1/<wbr>0</sub> | 실수 | m/s | 6.<wbr>8 |
| &emsp;&emsp;Slow<wbr>Shot<wbr>Speed<wbr>Actual | Measured slow-shot plunger speed.<br><sub>sf:<wbr>SlowShotSpeedActual/<wbr>1/<wbr>0</sub> | 실수 | m/s | 0.<wbr>3 |
| &emsp;&emsp;Biscuit<wbr>Thickness<wbr>Actual | Measured biscuit thickness after injection.<br><sub>sf:<wbr>BiscuitThicknessActual/<wbr>1/<wbr>0</sub> | 실수 | mm | 21 |
| &emsp;&emsp;Die<wbr>Temperature<wbr>Actual | Measured die temperature.<br><sub>sf:<wbr>DieTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 220 |
| &emsp;&emsp;Die<wbr>Cooling<wbr>Water<wbr>Temp<wbr>Actual | Measured die-cooling water temperature.<br><sub>sf:<wbr>DieCoolingWaterTempActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 45 |
| &emsp;&emsp;Cycle<wbr>Time<wbr>Actual | Measured duration of one casting cycle.<br><sub>sf:<wbr>CycleTimeActual/<wbr>1/<wbr>0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;Cavity<wbr>Fill<wbr>Time<wbr>Actual | Measured time required to fill the die cavity.<br><sub>sf:<wbr>CavityFillTimeActual/<wbr>1/<wbr>0</sub> | 실수 | ms | 45 |
| &emsp;&emsp;Casting<wbr>Throughput<wbr>Rate | Current number of completed casting shots per hour.<br><sub>sf:<wbr>CastingThroughputRate/<wbr>1/<wbr>0</sub> | 실수 | shots/h | 78 |
| &emsp;&emsp;Shot<wbr>Weight<wbr>Consistency<wbr>Index | Normalized consistency index of shot mass.<br><sub>sf:<wbr>ShotWeightConsistencyIndex/<wbr>1/<wbr>0</sub> | 실수 | 1 | 0.<wbr>97 |
| &emsp;&emsp;Casting<wbr>Reject<wbr>Rate | Current proportion of rejected castings.<br><sub>sf:<wbr>CastingRejectRate/<wbr>1/<wbr>0</sub> | 실수 | % | 1.<wbr>8 |
| **Clamping<wbr>And<wbr>Hydraulic<wbr>System** | Groups live clamping and hydraulic system data.<br><sub>sf:<wbr>ClampingAndHydraulicSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Clamping<wbr>And<wbr>Hydraulic<wbr>Monitoring** | Current force, position, pressure, temperature, pump and spray states.<br><sub>sf:<wbr>ClampingAndHydraulicMonitoring/<wbr>1/<wbr>0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;Clamping<wbr>Force<wbr>Actual | Measured clamping force.<br><sub>sf:<wbr>ClampingForceActual/<wbr>1/<wbr>0</sub> | 실수 | kN | 7800 |
| &emsp;&emsp;Die<wbr>Open<wbr>Position<wbr>Actual | Measured die-open position.<br><sub>sf:<wbr>DieOpenPositionActual/<wbr>1/<wbr>0</sub> | 실수 | mm | 0 |
| &emsp;&emsp;Ejector<wbr>Position<wbr>Actual | Measured ejector position.<br><sub>sf:<wbr>EjectorPositionActual/<wbr>1/<wbr>0</sub> | 실수 | mm | 0 |
| &emsp;&emsp;Hydraulic<wbr>Pressure<wbr>Actual | Measured hydraulic system pressure.<br><sub>sf:<wbr>HydraulicPressureActual/<wbr>1/<wbr>0</sub> | 실수 | MPa | 15.<wbr>2 |
| &emsp;&emsp;Hydraulic<wbr>Oil<wbr>Temperature<wbr>Actual | Measured hydraulic-oil temperature.<br><sub>sf:<wbr>HydraulicOilTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 48 |
| &emsp;&emsp;Hydraulic<wbr>Pump<wbr>Run<wbr>State | Current hydraulic-pump run state.<br><sub>sf:<wbr>HydraulicPumpRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;Die<wbr>Spray<wbr>Status | Current operating state of the die-spray unit.<br><sub>sf:<wbr>DieSprayStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Active |
| **Protection<wbr>And<wbr>Safety<wbr>State<wbr>System** | Groups protection and machine-safety operating states.<br><sub>sf:<wbr>ProtectionAndSafetyStateSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Protection<wbr>And<wbr>Safety<wbr>State<wbr>Monitoring** | Current overload, gate, light-curtain, stop and alarm states.<br><sub>sf:<wbr>ProtectionAndSafetyStateMonitoring/<wbr>1/<wbr>0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;Over<wbr>Pressure<wbr>Alarm<wbr>Status | Current hydraulic over-pressure alarm state.<br><sub>sf:<wbr>OverPressureAlarmStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;Die<wbr>Overload<wbr>Alarm<wbr>Status | Current die-overload alarm state.<br><sub>sf:<wbr>DieOverloadAlarmStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;Safety<wbr>Gate<wbr>Interlock<wbr>Status | Current safety-gate interlock state.<br><sub>sf:<wbr>SafetyGateInterlockStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;Light<wbr>Curtain<wbr>Status | Current light-curtain state.<br><sub>sf:<wbr>LightCurtainStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Clear |
| &emsp;&emsp;Protection<wbr>Stop<wbr>Status | Current protective-stop state.<br><sub>sf:<wbr>ProtectionStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;Casting<wbr>Alarm<wbr>Status | Current active casting alarm state.<br><sub>sf:<wbr>CastingAlarmStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | None |
| **Electrical<wbr>And<wbr>Safety<wbr>Condition<wbr>System** | Groups electrical supply and safety-condition data.<br><sub>sf:<wbr>ElectricalAndSafetyConditionSystem/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Electrical<wbr>And<wbr>Safety<wbr>Condition<wbr>Monitoring** | Current power, supply, emergency-stop, guard and permission states.<br><sub>sf:<wbr>ElectricalAndSafetyConditionMonitoring/<wbr>1/<wbr>0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;Power<wbr>Consumption<wbr>Actual | Measured electrical power consumption.<br><sub>sf:<wbr>PowerConsumptionActual/<wbr>1/<wbr>0</sub> | 실수 | W | 58000 |
| &emsp;&emsp;Electrical<wbr>Supply<wbr>Status | Current electrical-supply state.<br><sub>sf:<wbr>ElectricalSupplyStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;Emergency<wbr>Stop<wbr>Status | Current emergency-stop state.<br><sub>sf:<wbr>EmergencyStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;Guard<wbr>Interlock<wbr>Status | Current guard-interlock state.<br><sub>sf:<wbr>GuardInterlockStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;Safety<wbr>Cover<wbr>State | Current state of the safety cover.<br><sub>sf:<wbr>SafetyCoverState/<wbr>1/<wbr>0</sub> | 문자열 |  | Closed |
| &emsp;&emsp;Operation<wbr>Permitted<wbr>State | Indicates whether machine operation is currently permitted.<br><sub>sf:<wbr>OperationPermittedState/<wbr>1/<wbr>0</sub> | 문자열 |  | Permitted |

</details>

<details>
<summary><b>TimeSeries</b> · 상태 값의 시간별 기록 · 항목 1506개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Metadata** | A set of data describing and providing information about the time series<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Metadata/<wbr>1/<wbr>1</sub> | 묶음 (3) |  |  |
| &emsp;Name | Meaningful name for labeling<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Metadata/<wbr>Name/<wbr>1/<wbr>1</sub> | 다국어 |  | Die casting machine operation time series |
| &emsp;Description | Short description of the time series<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Metadata/<wbr>Description/<wbr>1/<wbr>1</sub> | 다국어 |  | Operational signals for the injection, die, hydraulic and s… |
| &emsp;**Record** | A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID. Simil…<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Record/<wbr>1/<wbr>1</sub> | 묶음 (23) |  |  |
| &emsp;&emsp;Time | Point of Time in seconds. Time points refer to the start time of the time series segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>RelativePointInTime/<wbr>1/<wbr>1</sub> | 정수 | s | 0 |
| &emsp;&emsp;Device<wbr>Run<wbr>State | Current high-level operating state of the equipment.<br><sub>sf:<wbr>DeviceRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;Operation<wbr>Mode | Selected machine operating mode.<br><sub>sf:<wbr>OperationMode/<wbr>1/<wbr>0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;Casting<wbr>Phase | Current phase of the die casting cycle.<br><sub>sf:<wbr>CastingPhase/<wbr>1/<wbr>0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;Casting<wbr>Run<wbr>State | Current execution state of the casting process.<br><sub>sf:<wbr>CastingRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;Molten<wbr>Metal<wbr>Temperature<wbr>Actual | Measured molten-metal temperature.<br><sub>sf:<wbr>MoltenMetalTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 675.<wbr>00 |
| &emsp;&emsp;Injection<wbr>Pressure<wbr>Actual | Measured injection pressure.<br><sub>sf:<wbr>InjectionPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 920.<wbr>00 |
| &emsp;&emsp;Intensification<wbr>Pressure<wbr>Actual | Measured intensification pressure.<br><sub>sf:<wbr>IntensificationPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 1020.<wbr>00 |
| &emsp;&emsp;Plunger<wbr>Speed<wbr>Actual | Measured fast-shot plunger speed.<br><sub>sf:<wbr>PlungerSpeedActual/<wbr>1/<wbr>0</sub> | 실수 | m/s | 6.<wbr>800 |
| &emsp;&emsp;Biscuit<wbr>Thickness<wbr>Actual | Measured biscuit thickness after injection.<br><sub>sf:<wbr>BiscuitThicknessActual/<wbr>1/<wbr>0</sub> | 실수 | mm | 21.<wbr>000 |
| &emsp;&emsp;Die<wbr>Temperature<wbr>Actual | Measured die temperature.<br><sub>sf:<wbr>DieTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 220.<wbr>00 |
| &emsp;&emsp;Die<wbr>Cooling<wbr>Water<wbr>Temp<wbr>Actual | Measured die-cooling water temperature.<br><sub>sf:<wbr>DieCoolingWaterTempActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 45.<wbr>00 |
| &emsp;&emsp;Cycle<wbr>Time<wbr>Actual | Measured duration of one casting cycle.<br><sub>sf:<wbr>CycleTimeActual/<wbr>1/<wbr>0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;Clamping<wbr>Force<wbr>Actual | Measured clamping force.<br><sub>sf:<wbr>ClampingForceActual/<wbr>1/<wbr>0</sub> | 실수 | kN | 7800.<wbr>00 |
| &emsp;&emsp;Hydraulic<wbr>Pressure<wbr>Actual | Measured hydraulic system pressure.<br><sub>sf:<wbr>HydraulicPressureActual/<wbr>1/<wbr>0</sub> | 실수 | MPa | 15.<wbr>200 |
| &emsp;&emsp;Hydraulic<wbr>Oil<wbr>Temperature<wbr>Actual | Measured hydraulic-oil temperature.<br><sub>sf:<wbr>HydraulicOilTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 48.<wbr>00 |
| &emsp;&emsp;Die<wbr>Spray<wbr>Status | Current operating state of the die-spray unit.<br><sub>sf:<wbr>DieSprayStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Active |
| &emsp;&emsp;Power<wbr>Consumption<wbr>Actual | Measured electrical power consumption.<br><sub>sf:<wbr>PowerConsumptionActual/<wbr>1/<wbr>0</sub> | 실수 | W | 58000.<wbr>00 |
| &emsp;&emsp;Electrical<wbr>Supply<wbr>Status | Current electrical-supply state.<br><sub>sf:<wbr>ElectricalSupplyStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;Emergency<wbr>Stop<wbr>Status | Current emergency-stop state.<br><sub>sf:<wbr>EmergencyStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;Safety<wbr>Gate<wbr>Interlock<wbr>Status | Current safety-gate interlock state.<br><sub>sf:<wbr>SafetyGateInterlockStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;Protection<wbr>Stop<wbr>Status | Current protective-stop state.<br><sub>sf:<wbr>ProtectionStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;Casting<wbr>Alarm<wbr>Status | Current active casting alarm state.<br><sub>sf:<wbr>CastingAlarmStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | None |
| **Segments** | Contains segments of a time series<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segments/<wbr>1/<wbr>1</sub> | 묶음 (3) |  |  |
| &emsp;**External<wbr>Segment** | Reference to a file of data points in sequential order over a period of time<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segments/<wbr>ExternalSegment/<wbr>1/<wbr>1</sub> | 묶음 (12) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Name/<wbr>1/<wbr>1</sub> | 다국어 |  | Die casting machine historian file data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Description/<wbr>1/<wbr>1</sub> | 다국어 |  | Die casting machine time series data stored in external CSV… |
| &emsp;&emsp;Record<wbr>Count | Indicates how many records are present in a segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>RecordCount/<wbr>1/<wbr>1</sub> | 정수 |  | 86400 |
| &emsp;&emsp;Start<wbr>Time | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>StartTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T00:<wbr>00:<wbr>00Z |
| &emsp;&emsp;End<wbr>Time | <br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>EndTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T23:<wbr>59:<wbr>59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Duration/<wbr>1/<wbr>1</sub> | 문자열 |  | PT24H |
| &emsp;&emsp;Sampling<wbr>Interval | The time period between two time series records (Length of cycle).<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingInterval/<wbr>1/<wbr>1</sub> | 정수 | s | 1 |
| &emsp;&emsp;Sampling<wbr>Rate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingRate/<wbr>1/<wbr>1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>State/<wbr>1/<wbr>1</sub> | 문자열 |  | completed |
| &emsp;&emsp;Last<wbr>Update | Time of the last chance<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>LastUpdate/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>18T00:<wbr>00:<wbr>05Z |
| &emsp;&emsp;File | Sequence of data points in sequential order over a period of time within a paged data file<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>File/<wbr>1/<wbr>1</sub> | 파일 |  | DC_<wbr>TS_<wbr>20260617.<wbr>csv |
| &emsp;&emsp;Blob | Sequence of data points in sequential order over a period of time within a BLOB<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Blob/<wbr>1/<wbr>1</sub> | 내장 데이터 |  |  |
| &emsp;**Linked<wbr>Segment** | Reference to an endpoint of data points in sequential order over a period of time<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segments/<wbr>LinkedSegment/<wbr>1/<wbr>1</sub> | 묶음 (12) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Name/<wbr>1/<wbr>1</sub> | 다국어 |  | Die casting machine historian API data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Description/<wbr>1/<wbr>1</sub> | 다국어 |  | Die casting machine time series data queried from external … |
| &emsp;&emsp;Record<wbr>Count | Indicates how many records are present in a segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>RecordCount/<wbr>1/<wbr>1</sub> | 정수 |  | 86400 |
| &emsp;&emsp;Start<wbr>Time | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>StartTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T00:<wbr>00:<wbr>00Z |
| &emsp;&emsp;End<wbr>Time | <br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>EndTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T23:<wbr>59:<wbr>59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Duration/<wbr>1/<wbr>1</sub> | 문자열 |  | PT24H |
| &emsp;&emsp;Sampling<wbr>Interval | The time period between two time series records (Length of cycle).<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingInterval/<wbr>1/<wbr>1</sub> | 정수 | s | 1 |
| &emsp;&emsp;Sampling<wbr>Rate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingRate/<wbr>1/<wbr>1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>State/<wbr>1/<wbr>1</sub> | 문자열 |  | completed |
| &emsp;&emsp;Last<wbr>Update | Time of the last chance<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>LastUpdate/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>18T00:<wbr>00:<wbr>05Z |
| &emsp;&emsp;Endpoint | Specifies a location of a resource on an API server through which time series can be requested<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Endpoint/<wbr>1/<wbr>1</sub> | 문자열 |  | https:<wbr>/<wbr>/<wbr>historian.<wbr>example.<wbr>com/<wbr>api/<wbr>timeseries |
| &emsp;&emsp;Query | generic query component to read time series data from an API<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Query/<wbr>1/<wbr>1</sub> | 문자열 |  | assetId=DC-<wbr>SN-<wbr>2026-<wbr>0001&amp;from=2026-<wbr>06-<wbr>17T00:<wbr>00:<wbr>00Z&amp;to=2026-<wbr>0… |
| &emsp;**Internal<wbr>Segment** | Grouped sequence of data points in successive order over a specified period of time<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segments/<wbr>InternalSegment/<wbr>1/<wbr>1</sub> | 묶음 (11) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Name/<wbr>1/<wbr>1</sub> | 다국어 |  | Recent die casting machine operation data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Description/<wbr>1/<wbr>1</sub> | 다국어 |  | Recent die casting machine operation records stored directl… |
| &emsp;&emsp;Record<wbr>Count | Indicates how many records are present in a segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>RecordCount/<wbr>1/<wbr>1</sub> | 정수 |  | 60 |
| &emsp;&emsp;Start<wbr>Time | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>StartTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T08:<wbr>15:<wbr>00Z |
| &emsp;&emsp;End<wbr>Time | Contains the last recorded timestamp of the time series segment and thus represents the end of a time series. Time format and scale corresp…<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>EndTime/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T08:<wbr>15:<wbr>59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>Duration/<wbr>1/<wbr>1</sub> | 문자열 |  | PT1M |
| &emsp;&emsp;Sampling<wbr>Interval | The time period between two time series records (Length of cycle).<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingInterval/<wbr>1/<wbr>1</sub> | 정수 | s | 1 |
| &emsp;&emsp;Sampling<wbr>Rate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>SamplingRate/<wbr>1/<wbr>1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>State/<wbr>1/<wbr>1</sub> | 문자열 |  | completed |
| &emsp;&emsp;Last<wbr>Update | Time of the last chance<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Segment/<wbr>LastUpdate/<wbr>1/<wbr>1</sub> | 문자열 |  | 2026-<wbr>06-<wbr>17T08:<wbr>16:<wbr>00Z |
| &emsp;&emsp;**Records** | Group of data points in successive order over a specified period of time<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Records/<wbr>1/<wbr>1</sub> | 묶음 (60) |  |  |
| &emsp;&emsp;&emsp;**Record__0000__** | A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID. Simil…<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>Record/<wbr>1/<wbr>1</sub> | 묶음 (23) |  |  |
| &emsp;&emsp;&emsp;&emsp;Time | Point of Time in seconds. Time points refer to the start time of the time series segment.<br><sub>ai:<wbr>idta/<wbr>TimeSeries/<wbr>RelativePointInTime/<wbr>1/<wbr>1</sub> | 정수 | s | 0 |
| &emsp;&emsp;&emsp;&emsp;Device<wbr>Run<wbr>State | Current high-level operating state of the equipment.<br><sub>sf:<wbr>DeviceRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;&emsp;&emsp;Operation<wbr>Mode | Selected machine operating mode.<br><sub>sf:<wbr>OperationMode/<wbr>1/<wbr>0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;&emsp;&emsp;Casting<wbr>Phase | Current phase of the die casting cycle.<br><sub>sf:<wbr>CastingPhase/<wbr>1/<wbr>0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;&emsp;&emsp;Casting<wbr>Run<wbr>State | Current execution state of the casting process.<br><sub>sf:<wbr>CastingRunState/<wbr>1/<wbr>0</sub> | 문자열 |  | Running |
| &emsp;&emsp;&emsp;&emsp;Molten<wbr>Metal<wbr>Temperature<wbr>Actual | Measured molten-metal temperature.<br><sub>sf:<wbr>MoltenMetalTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 675.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Injection<wbr>Pressure<wbr>Actual | Measured injection pressure.<br><sub>sf:<wbr>InjectionPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 920.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Intensification<wbr>Pressure<wbr>Actual | Measured intensification pressure.<br><sub>sf:<wbr>IntensificationPressureActual/<wbr>1/<wbr>0</sub> | 실수 | bar | 1020.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Plunger<wbr>Speed<wbr>Actual | Measured fast-shot plunger speed.<br><sub>sf:<wbr>PlungerSpeedActual/<wbr>1/<wbr>0</sub> | 실수 | m/s | 6.<wbr>800 |
| &emsp;&emsp;&emsp;&emsp;Biscuit<wbr>Thickness<wbr>Actual | Measured biscuit thickness after injection.<br><sub>sf:<wbr>BiscuitThicknessActual/<wbr>1/<wbr>0</sub> | 실수 | mm | 21.<wbr>000 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Temperature<wbr>Actual | Measured die temperature.<br><sub>sf:<wbr>DieTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 220.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Cooling<wbr>Water<wbr>Temp<wbr>Actual | Measured die-cooling water temperature.<br><sub>sf:<wbr>DieCoolingWaterTempActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 45.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Cycle<wbr>Time<wbr>Actual | Measured duration of one casting cycle.<br><sub>sf:<wbr>CycleTimeActual/<wbr>1/<wbr>0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;&emsp;&emsp;Clamping<wbr>Force<wbr>Actual | Measured clamping force.<br><sub>sf:<wbr>ClampingForceActual/<wbr>1/<wbr>0</sub> | 실수 | kN | 7800.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Hydraulic<wbr>Pressure<wbr>Actual | Measured hydraulic system pressure.<br><sub>sf:<wbr>HydraulicPressureActual/<wbr>1/<wbr>0</sub> | 실수 | MPa | 15.<wbr>200 |
| &emsp;&emsp;&emsp;&emsp;Hydraulic<wbr>Oil<wbr>Temperature<wbr>Actual | Measured hydraulic-oil temperature.<br><sub>sf:<wbr>HydraulicOilTemperatureActual/<wbr>1/<wbr>0</sub> | 실수 | °C | 48.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Die<wbr>Spray<wbr>Status | Current operating state of the die-spray unit.<br><sub>sf:<wbr>DieSprayStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Active |
| &emsp;&emsp;&emsp;&emsp;Power<wbr>Consumption<wbr>Actual | Measured electrical power consumption.<br><sub>sf:<wbr>PowerConsumptionActual/<wbr>1/<wbr>0</sub> | 실수 | W | 58000.<wbr>00 |
| &emsp;&emsp;&emsp;&emsp;Electrical<wbr>Supply<wbr>Status | Current electrical-supply state.<br><sub>sf:<wbr>ElectricalSupplyStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;&emsp;&emsp;Emergency<wbr>Stop<wbr>Status | Current emergency-stop state.<br><sub>sf:<wbr>EmergencyStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;Safety<wbr>Gate<wbr>Interlock<wbr>Status | Current safety-gate interlock state.<br><sub>sf:<wbr>SafetyGateInterlockStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;&emsp;&emsp;Protection<wbr>Stop<wbr>Status | Current protective-stop state.<br><sub>sf:<wbr>ProtectionStopStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;Casting<wbr>Alarm<wbr>Status | Current active casting alarm state.<br><sub>sf:<wbr>CastingAlarmStatus/<wbr>1/<wbr>0</sub> | 문자열 |  | None |
| &emsp;&emsp;&emsp;<sub>⋯ 같은 구성의 묶음 59개 더 (항목 1416개 생략)</sub> | | | | |

</details>

<details>
<summary><b>ProcessParameters</b> · 제품·공정별 설정값 · 항목 41개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Processes** | Provides all the necessary parameters of processes in a structured form that are required to manufacture a product<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>Processes/<wbr>1/<wbr>0</sub> | 묶음 (1) |  |  |
| &emsp;**Process__00__** | The processes to be executed are described individually in the SMC Process.<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>Process/<wbr>1/<wbr>0</sub> | 묶음 (8) |  |  |
| &emsp;&emsp;Process<wbr>Id | Describes the ID of the process<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProcessId/<wbr>1/<wbr>0</sub> | 문자열 |  | DC-<wbr>P-<wbr>001 |
| &emsp;&emsp;Process<wbr>Name | Describes the Name of the Process<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProcessName/<wbr>1/<wbr>0</sub> | 문자열 |  | High-<wbr>pressure die casting |
| &emsp;&emsp;Process<wbr>Description | Describes the process.<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProcessDescription/<wbr>1/<wbr>0</sub> | 다국어 |  | Process parameters for high-<wbr>pressure die casting shot opera… |
| &emsp;&emsp;Planned<wbr>Process<wbr>Time | Planned processing time for process execution (without set-up time)<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>PlannedProcessTime/<wbr>1/<wbr>0</sub> | 기간 |  | PT45S |
| &emsp;&emsp;**Product<wbr>Parameters** | Mandatory product parameters for process execution<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProductParameters/<wbr>1/<wbr>0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;&emsp;Cast<wbr>Alloy<wbr>Type | Alloy selected for the casting process.<br><sub>sf:<wbr>CastAlloyType/<wbr>1/<wbr>0</sub> | 문자열 |  | Aluminum alloy ADC12 |
| &emsp;&emsp;&emsp;Molten<wbr>Metal<wbr>Target<wbr>Temperature | Target molten-metal temperature before injection.<br><sub>sf:<wbr>MoltenMetalTargetTemperature/<wbr>1/<wbr>0</sub> | 실수 | °C | 680 |
| &emsp;&emsp;&emsp;Part<wbr>Net<wbr>Weight | Target net mass of one cast part.<br><sub>sf:<wbr>PartNetWeight/<wbr>1/<wbr>0</sub> | 실수 | kg | 3.<wbr>8 |
| &emsp;&emsp;&emsp;Shot<wbr>Weight | Target total shot mass including runners and overflows.<br><sub>sf:<wbr>ShotWeight/<wbr>1/<wbr>0</sub> | 실수 | kg | 5.<wbr>2 |
| &emsp;&emsp;&emsp;Cavity<wbr>Count | Number of cavities in the die.<br><sub>sf:<wbr>CavityCount/<wbr>1/<wbr>0</sub> | 정수 |  | 2 |
| &emsp;&emsp;&emsp;Target<wbr>Production<wbr>Quantity | Target number of casting shots for the production order.<br><sub>sf:<wbr>TargetProductionQuantity/<wbr>1/<wbr>0</sub> | 정수 | shots | 1900 |
| &emsp;&emsp;**Process<wbr>Parameters** | Mandatory process parameters for process execution<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProcessParameters/<wbr>1/<wbr>0</sub> | 묶음 (15) |  |  |
| &emsp;&emsp;&emsp;Operation<wbr>Recipe<wbr>Id | Identifier of the die casting process recipe.<br><sub>sf:<wbr>OperationRecipeId/<wbr>1/<wbr>0</sub> | 문자열 |  | RECIPE-<wbr>DC-<wbr>001 |
| &emsp;&emsp;&emsp;Operation<wbr>Mode | Selected machine operating mode.<br><sub>sf:<wbr>OperationMode/<wbr>1/<wbr>0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;&emsp;Process<wbr>Step<wbr>Sequence | Ordered sequence of process steps in one casting cycle.<br><sub>sf:<wbr>ProcessStepSequence/<wbr>1/<wbr>0</sub> | 문자열 |  | Mold close &gt; Molten metal dosing &gt; Slow shot &gt; Fast shot &gt; … |
| &emsp;&emsp;&emsp;Slow<wbr>Shot<wbr>Speed<wbr>Setpoint | Target plunger speed during the slow-shot phase.<br><sub>sf:<wbr>SlowShotSpeedSetpoint/<wbr>1/<wbr>0</sub> | 실수 | m/s | 0.<wbr>3 |
| &emsp;&emsp;&emsp;Fast<wbr>Shot<wbr>Speed<wbr>Setpoint | Target plunger speed during the fast-shot phase.<br><sub>sf:<wbr>FastShotSpeedSetpoint/<wbr>1/<wbr>0</sub> | 실수 | m/s | 6.<wbr>5 |
| &emsp;&emsp;&emsp;Shot<wbr>Changeover<wbr>Position | Plunger position at the slow-to-fast-shot transition.<br><sub>sf:<wbr>ShotChangeoverPosition/<wbr>1/<wbr>0</sub> | 실수 | mm | 350 |
| &emsp;&emsp;&emsp;Injection<wbr>Pressure<wbr>Setpoint | Target injection pressure.<br><sub>sf:<wbr>InjectionPressureSetpoint/<wbr>1/<wbr>0</sub> | 실수 | bar | 900 |
| &emsp;&emsp;&emsp;Intensification<wbr>Pressure<wbr>Setpoint | Target intensification pressure.<br><sub>sf:<wbr>IntensificationPressureSetpoint/<wbr>1/<wbr>0</sub> | 실수 | bar | 1050 |
| &emsp;&emsp;&emsp;Clamping<wbr>Force<wbr>Setpoint | Target die clamping force.<br><sub>sf:<wbr>ClampingForceSetpoint/<wbr>1/<wbr>0</sub> | 실수 | kN | 8000 |
| &emsp;&emsp;&emsp;Die<wbr>Temperature<wbr>Setpoint | Target die temperature.<br><sub>sf:<wbr>DieTemperatureSetpoint/<wbr>1/<wbr>0</sub> | 실수 | °C | 220 |
| &emsp;&emsp;&emsp;Hold<wbr>Time | Target pressure-holding duration.<br><sub>sf:<wbr>HoldTime/<wbr>1/<wbr>0</sub> | 기간 |  | PT3S |
| &emsp;&emsp;&emsp;In<wbr>Die<wbr>Cooling<wbr>Time | Target cooling duration before die opening.<br><sub>sf:<wbr>InDieCoolingTime/<wbr>1/<wbr>0</sub> | 기간 |  | PT8S |
| &emsp;&emsp;&emsp;Die<wbr>Spray<wbr>Time | Target die-spray duration.<br><sub>sf:<wbr>DieSprayTime/<wbr>1/<wbr>0</sub> | 기간 |  | PT2S |
| &emsp;&emsp;&emsp;Biscuit<wbr>Thickness<wbr>Setpoint | Target biscuit thickness.<br><sub>sf:<wbr>BiscuitThicknessSetpoint/<wbr>1/<wbr>0</sub> | 실수 | mm | 20 |
| &emsp;&emsp;&emsp;Over<wbr>Pressure<wbr>Alarm<wbr>Threshold | Injection-pressure threshold for an over-pressure alarm.<br><sub>sf:<wbr>OverPressureAlarmThreshold/<wbr>1/<wbr>0</sub> | 실수 | bar | 1150 |
| &emsp;&emsp;**Resource<wbr>Parameters** | Mandatory resource parameters for process execution<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ResourceParameters/<wbr>1/<wbr>0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;&emsp;Required<wbr>Molten<wbr>Metal<wbr>Temp<wbr>Sensor | Temperature sensor required to execute the casting process.<br><sub>sf:<wbr>RequiredMoltenMetalTempSensor/<wbr>1/<wbr>0</sub> | 문자열 |  | MetalTempSensor01 |
| &emsp;&emsp;&emsp;Required<wbr>Injection<wbr>Pressure<wbr>Sensor | Injection-pressure sensor required to execute the casting process.<br><sub>sf:<wbr>RequiredInjectionPressureSensor/<wbr>1/<wbr>0</sub> | 문자열 |  | InjectionPressureSensor01 |
| &emsp;&emsp;&emsp;Required<wbr>Plunger<wbr>Position<wbr>Sensor | Plunger-position sensor required to execute the casting process.<br><sub>sf:<wbr>RequiredPlungerPositionSensor/<wbr>1/<wbr>0</sub> | 문자열 |  | PlungerPositionSensor01 |
| &emsp;&emsp;&emsp;Required<wbr>Shot<wbr>Cylinder | Shot-cylinder resource required to execute the casting process.<br><sub>sf:<wbr>RequiredShotCylinder/<wbr>1/<wbr>0</sub> | 문자열 |  | ShotCylinder01 |
| &emsp;&emsp;&emsp;Required<wbr>Clamping<wbr>Unit | Clamping-unit resource required to execute the casting process.<br><sub>sf:<wbr>RequiredClampingUnit/<wbr>1/<wbr>0</sub> | 문자열 |  | ToggleClampingUnit01 |
| &emsp;&emsp;&emsp;Required<wbr>Die<wbr>Spray<wbr>Unit | Die-spray resource required to execute the casting process.<br><sub>sf:<wbr>RequiredDieSprayUnit/<wbr>1/<wbr>0</sub> | 문자열 |  | DieSprayUnit01 |
| &emsp;&emsp;&emsp;Required<wbr>Hydraulic<wbr>Pump | Hydraulic-pump resource required to execute the casting process.<br><sub>sf:<wbr>RequiredHydraulicPump/<wbr>1/<wbr>0</sub> | 문자열 |  | HydraulicPump01 |
| &emsp;&emsp;**Process<wbr>Bo<wbr>M** | Describes the products or semi-finished products to be involved in the process<br><sub>ai:<wbr>idta/<wbr>ProcessParameters/<wbr>ProcessBoM/<wbr>1/<wbr>0</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;Molten<wbr>Metal<wbr>Consumable | Controlled identifier of the molten-metal consumable.<br><sub>sf:<wbr>MoltenMetalConsumable/<wbr>1/<wbr>0</sub> | 문자열 |  | AL-<wbr>ADC12-<wbr>INGOT-<wbr>001 |
| &emsp;&emsp;&emsp;Release<wbr>Agent<wbr>Consumable | Controlled identifier of the release-agent consumable.<br><sub>sf:<wbr>ReleaseAgentConsumable/<wbr>1/<wbr>0</sub> | 문자열 |  | RELEASE-<wbr>AGENT-<wbr>001 |
| &emsp;&emsp;&emsp;Hydraulic<wbr>Oil | Controlled identifier of the hydraulic oil used by the equipment.<br><sub>sf:<wbr>HydraulicOil/<wbr>1/<wbr>0</sub> | 문자열 |  | HYD-<wbr>OIL-<wbr>001 |

</details>

<details>
<summary><b>PredictiveMaintenance</b> · 예지정비 모델과 결과 · 항목 91개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Remaining<wbr>Useful<wbr>Life<wbr>Prediction** | Information about remaining useful life (RUL) prediction in the context of predictive maintenance<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>RemainingUsefulLifePrediction/<wbr>1/<wbr>0</sub> | 묶음 (7) |  |  |
| &emsp;**Remaining<wbr>Useful<wbr>Lifetime** | Remaining useful life time, bades on Lifetime model of OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>RemainingUsefulLifetime/<wbr>1/<wbr>0</sub> | 개체 (6) |  |  |
| &emsp;&emsp;Indication<wbr>Type | Type of wear-relevant duration, e.g. time, cycles, distance, etc.<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>IndicationType/<wbr>1/<wbr>0</sub> | 문자열 |  | OperatingHours |
| &emsp;&emsp;Duration<wbr>Value | Value of duration in the wear relevant unit, e.g. time, operation cycles, distance, etc.<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>DurationValue/<wbr>1/<wbr>0</sub> | 실수 |  | 9000 |
| &emsp;&emsp;Engineering<wbr>Unit | Wear relevant physical unit, e.g. time, operation cycles, distance, etc.<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>EngineeringUnit/<wbr>1/<wbr>0</sub> | 문자열 |  | h |
| &emsp;&emsp;Start<wbr>Value | Starting value from which the duration is measured in the wear-relevant unit, e.g. time, cycles, distance, etc.<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>StartValue/<wbr>1/<wbr>0</sub> | 실수 |  | 9000 |
| &emsp;&emsp;Start<wbr>Date<wbr>Time | Start date and time from which the duration is measured<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>StartDateTime/<wbr>1/<wbr>0</sub> | 일시 |  | 2026-<wbr>06-<wbr>26T09:<wbr>00:<wbr>00+09:<wbr>00 |
| &emsp;&emsp;Description | Description of the wear duration information<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>Description/<wbr>1/<wbr>0</sub> | 문자열 |  | Estimated remaining operating time for the shot sleeve and … |
| &emsp;Remaining<wbr>Usful<wbr>Life<wbr>Date<wbr>Time | mark attributed to an instant by means of a specified timescale, expressed as a date and a time<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>RemainingUsfulLifeDateTime/<wbr>1/<wbr>0</sub> | 일시 |  | 2027-<wbr>07-<wbr>15T09:<wbr>00:<wbr>00+09:<wbr>00 |
| &emsp;Confidence<wbr>Interval | confidence interval, measured in the unit of the predicted value<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ConfidenceInterval/<wbr>1/<wbr>0</sub> | 실수 범위 |  | 7800 ~ 10500 |
| &emsp;**List<wbr>RULBoundary<wbr>Conditions** | List of boundary conditions for which remaining useful life has been predicted<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ListRULBoundaryConditions/<wbr>1/<wbr>0</sub> | 목록 (7) |  |  |
| &emsp;&emsp;**(항목)** | Boundary condition for which remaining useful life has been predicted<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>RULCondition/<wbr>1/<wbr>0</sub> | 묶음 (9) |  |  |
| &emsp;&emsp;&emsp;Condition<wbr>Name | Name of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is v…<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ConditionName/<wbr>1/<wbr>0</sub> | 문자열 |  | HydraulicPumpCurrentActual |
| &emsp;&emsp;&emsp;Is<wbr>Boundary<wbr>Condition<wbr>Used<wbr>In<wbr>Model | If this boundary condition is used in the model for RUL prediction true, else false<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>IsBoundaryConditionUsedInModel/<wbr>1/<wbr>0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;Boundary<wbr>Value<wbr>Range | Value range of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL predicti…<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>BoundaryValueRange/<wbr>1/<wbr>0</sub> | 실수 |  | 96 |
| &emsp;&emsp;&emsp;Boundary<wbr>Engineering<wbr>Unit | Engineering Unit of the boundary condition indicator<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>BoundaryEngineeringUnit/<wbr>1/<wbr>0</sub> | 문자열 |  | A |
| &emsp;&emsp;&emsp;Drift<wbr>Info<wbr>AIModel | Drift information of AI model<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>DriftInfoAIModel/<wbr>1/<wbr>0</sub> | 실수 범위 |  | 0.<wbr>07 ~ 0.<wbr>07 |
| &emsp;&emsp;&emsp;Mean<wbr>Value | Mean value of the distribution of indicator values<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>MeanValue/<wbr>1/<wbr>0</sub> | 실수 |  | 96 |
| &emsp;&emsp;&emsp;Standarddeviation | Standard deviation of the distribution of indicator values<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>Standarddeviation/<wbr>1/<wbr>0</sub> | 실수 |  | 10 |
| &emsp;&emsp;&emsp;Skewness | Skewness of the distribution of indicator values<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>Skewness/<wbr>1/<wbr>0</sub> | 실수 |  | 0.<wbr>4 |
| &emsp;&emsp;&emsp;Boundary<wbr>Description | Description of the boundary of a RUL prediction condition<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>BoundaryDescription/<wbr>1/<wbr>0</sub> | 문자열 |  | Hydraulic pump current window used to identify sustained ov… |
| &emsp;&emsp;<sub>⋯ 같은 구성의 묶음 6개 더 (항목 60개 생략)</sub> | | | | |
| &emsp;**Prediction<wbr>Model<wbr>Information** | Information about the model for RUL prediction relevant in the context of predictive maintenance<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>PredictionModelInformation/<wbr>1/<wbr>0</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;Model<wbr>Type | Model type as an enumerated value: physical based methods, data-driven methods, hybrid methods<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ModelType/<wbr>1/<wbr>0</sub> | 문자열 |  | ModelTypeHybrid |
| &emsp;&emsp;Model<wbr>Description | More detailed description of the model type used for RUL prediction (optional)<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ModelDescription/<wbr>1/<wbr>0</sub> | 문자열 |  | Hybrid physics- and data-<wbr>driven RUL model. Feature importan… |
| &emsp;**List<wbr>Pre<wbr>Alerts** | List for defining pre-alerts which should be raised before remaining useful life is exceeded<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>ListPreAlerts/<wbr>1/<wbr>0</sub> | 목록 (1) |  |  |
| &emsp;&emsp;**(항목)** | Definition of a pre-alert which should be raised before remaining useful life is exceeded<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>PreAlerts/<wbr>1/<wbr>0</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;&emsp;Pre<wbr>Alert<wbr>Message | Message to be displayed when alarm regarding predicted remaining useful life is raised<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>PreAlertMessage/<wbr>1/<wbr>0</sub> | 문자열 |  | Inspect the shot sleeve, plunger tip and hydraulic pump bef… |
| &emsp;&emsp;&emsp;Pre<wbr>Alert<wbr>Value | Pre-warning duration in wear relevant unit before remaining useful life is exceeded<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>PreAlertValue/<wbr>1/<wbr>0</sub> | 실수 |  | 1200 |
| &emsp;**Alert<wbr>After<wbr>Exceeding<wbr>Remaining<wbr>Usable<wbr>Life** | Alert information which should be triggered or displayed after exceeding remaining useful life<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>AlertAfterExceedingRemainingUsableLife/<wbr>…</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;Alert<wbr>Message | Message to be displayed when alarm regarding predicted remaining useful life is raised<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>AlertMessage/<wbr>1/<wbr>0</sub> | 문자열 |  | Maintenance is required after the remaining useful life of … |
| &emsp;&emsp;Maintenance<wbr>Required | Maintenance required<br><sub>ai:<wbr>idta/<wbr>PredictiveMaintenance/<wbr>MaintenanceRequired/<wbr>1/<wbr>0</sub> | 참/거짓 |  | false |

</details>
