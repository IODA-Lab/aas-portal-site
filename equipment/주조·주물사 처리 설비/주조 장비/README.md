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

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| URIOfTheProduct | unique global identification of the<br>product instance using an universal<br>resource identifier (URI)<br><sub>0112/2///61987#ABN590#002</sub> | U⁠R⁠I | https://www.smart-<br>factory.kr/ids/<br>asset/<br>DieCastingMachine/<br>DC… |
| ManufacturerName | legally valid designation of the natural<br>or judicial person which is directly<br>responsible for the design, production,<br>packaging and labelin…<br><sub>0112/2///61987#ABA565#009</sub> | 다⁠국⁠어 | ExampleCompany |
| ManufacturerProductDesignation | short description of the product (short<br>text), third or lowest level of a 3<br>level manufacturer specific product<br>hierarchy<br><sub>0112/2///61987#ABA567#009</sub> | 다⁠국⁠어 | Cold Chamber Die<br>Casting Machine |
| **AddressInformation** | Note: this set of information is defined<br>by SMT drop-in &quot;Address Information&quot;<br><sub>ai:zvei/nameplate/1/0/ContactInformations/<br>AddressInformation</sub> | 묶⁠음&nbsp;(4) |  |
| &ensp;&ensp;Street | <br><sub>0173-1#02-AAO128#002</sub> | 다⁠국⁠어 | Example Street 1 |
| &ensp;&ensp;Zipcode | <br><sub>0173-1#02-AAO129#002</sub> | 다⁠국⁠어 | 12345 |
| &ensp;&ensp;CityTown | <br><sub>0173-1#02-AAO132#002</sub> | 다⁠국⁠어 | Example City |
| &ensp;&ensp;NationalCode | <br><sub>0173-1#02-AAO134#002</sub> | 다⁠국⁠어 | KR |
| ManufacturerProductRoot | top level of a 3 level manufacturer<br>specific product hierarchy<br><sub>0112/2///61360_7#AAS011#001</sub> | 다⁠국⁠어 | Casting Equipment |
| ManufacturerProductFamily | second level of a 3 level manufacturer<br>specific product hierarchy<br><sub>0112/2///61987#ABP464#002</sub> | 다⁠국⁠어 | High-Pressure Die<br>Casting Machine |
| ManufacturerProductType | characteristic to differentiate between<br>different products of a product family<br>or special variants<br><sub>0112/2///61987#ABA300#008</sub> | 문⁠자⁠열 | DC-800 |
| OrderCodeOfManufacturer | unique combination of numbers and<br>letters issued by the manufacturer that<br>is used to identify the device for<br>ordering<br><sub>0112/2///61987#ABA950#008</sub> | 문⁠자⁠열 | DC-800-ORD |
| ProductArticleNumberOfManufacturer | unique product identifier of the<br>manufacturer<br><sub>0112/2///61987#ABA581#007</sub> | 문⁠자⁠열 | DC-800-ART |
| SerialNumber | unique combination of numbers and<br>letters used to identify the device once<br>it has been manufactured<br><sub>0112/2///61987#ABA951#009</sub> | 문⁠자⁠열 | DC-SN-2026-0001 |
| YearOfConstruction | year in which the manufacturing process<br>is completed<br><sub>0112/2///61987#ABP000#002</sub> | 문⁠자⁠열 | 2026 |
| DateOfManufacture | date when an item was manufactured<br><sub>0112/2///61987#ABB757#007</sub> | 날⁠짜 | 2026-06-17 |
| HardwareVersion | version of the hardware supplied with<br>the device<br><sub>0112/2///61987#ABA926#008</sub> | 문⁠자⁠열 | HW-1.0 |
| FirmwareVersion | version of the firmware supplied with<br>the device<br><sub>0112/2///61987#ABA302#006</sub> | 문⁠자⁠열 | FW-1.0 |
| SoftwareVersion | version of the software used by the<br>device<br><sub>0112/2///61987#ABA601#008</sub> | 문⁠자⁠열 | SW-1.0 |
| CountryOfOrigin | Note: Country codes defined accord. to<br>DIN EN ISO 3166-1 alpha-2 codes<br><sub>0112/2///61987#ABP462#001</sub> | 문⁠자⁠열 | KR |
| UniqueFacilityIdentifier | unique string of characters for the<br>identification of locations or buildings<br>involved in a product’s value chain or<br>used by actors involved…<br><sub>ai:idta/nameplate/3/0/UniqueFacilityIdentifier</sub> | 문⁠자⁠열 | TYPE-DC-800 |
| CompanyLogo | a graphic mark used to represent a<br>company, an organisation or a product<br><sub>0112/2///61987#ABP463#001</sub> | 파⁠일 | CompanyLogo.png |
| **Markings** | Note: CE marking is declared as<br>mandatory according to EU Blue Guide<br><sub>0112/2///61360_7#AAS006#001</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;**(항목)** | Note: CE marking is declared as<br>mandatory according to the Blue Guide of<br>the EU-Commission<br><sub>0112/2///61360_7#AAS009#001</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;MarkingName | common name of the marking<br><sub>0112/2///61987#ABA231#009</sub> | 문⁠자⁠열 | CE |
| &ensp;&ensp;&ensp;&ensp;DesignationOfCertificateOrApproval | Note: Approval identifier, reference to<br>the certificate number, to be entered<br>without spaces<br><sub>0112/2///61987#ABH783#003</sub> | 문⁠자⁠열 | Declaration of<br>Conformity |
| &ensp;&ensp;&ensp;&ensp;IssueDate | Note: format by lexical representation:<br>CCYY-MM-DD Note: to be specified to the<br>day<br><sub>0112/2///61987#ABO097#001</sub> | 날⁠짜 | 2026-06-17 |
| &ensp;&ensp;&ensp;&ensp;ExpiryDate | Note: format by lexical representation:<br>CCYY-MM-DD Note: to be specified to the<br>day<br><sub>0112/2///61987#ABH830#002</sub> | 날⁠짜 | 2036-06-16 |
| &ensp;&ensp;&ensp;&ensp;MarkingFile | conformity symbol of the marking<br><sub>0112/2///61987#ABO100#002</sub> | 파⁠일 | DieCastingMachine_<br>CertificatesDeclarations_<br>EN.pdf |
| &ensp;&ensp;&ensp;&ensp;MarkingAdditionalText | where applicable, additional information<br>on the marking in plain text, e.g. the<br>ID-number of the notified body involved<br>in the conformity p…<br><sub>0112/2///61987#ABB146#007</sub> | 문⁠자⁠열 | Conformity<br>information for the<br>DC-800 equipment<br>type. |

</details>

<details>
<summary><b>HandoverDocumentation</b> · 납품 시 함께 전달하는 문서 목록 · 항목 121개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **Documents** | Information for a document identity<br><sub>0173-1#02-ABI500#003</sub> | 목⁠록&nbsp;(5) |  |
| &ensp;&ensp;**(항목)** | This SubmodelElementCollection holds the<br>information for a VDI 2770 Document<br>entity<br><sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;&ensp;&ensp;**DocumentIds** | Set of document identifiers for the<br>document. One ID in this collection<br>should be used as a preferred ID<br><sub>0173-1#02-ABI501#003</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**(항목)** | This SubmodelElementCollection holds the<br>information for a VDI 2770 Document<br>entity<br><sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DocumentDomainId | Identification of the domain in which<br>the given DocumentId is unique. The<br>domain ID can e.g., be the name or<br>acronym of the providing organ…<br><sub>0173-1#02-ABH994#003</sub> | 문⁠자⁠열 | EXAMPLE_DIE_CASTING_<br>DOC |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DocumentIdentifier | alphanumeric character sequence uniquely<br>identifying a document<br><sub>0173-1#02-AAO099#004</sub> | 문⁠자⁠열 | DC-OM-001 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DocumentIsPrimary | Flag indicating that a DocumentId within<br>a collection of at least two<br>DocumentId`s is the ‘primary’ identifier<br>for the document. This is th…<br><sub>0173-1#02-ABH995#003</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;**DocumentClassifications** | Set of information for describing the<br>classification of the Document according<br>to ClassificationSystems<br><sub>0173-1#02-ABI502#003</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**(항목)** | Set of information for describing the<br>classification of the Document according<br>to a ClassificationSystem<br><sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClassId | Unique ID of the document class within a<br>classficationsystem<br><sub>0173-1#02-ABH996#003</sub> | 문⁠자⁠열 | 03-02 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClassName | Name of the class in the classification<br>system<br><sub>0173-1#02-ABJ219#002</sub> | 다⁠국⁠어 | Operation |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClassificationSystem | Identification of the classification<br>system<br><sub>0173-1#02-ABH997#003</sub> | 문⁠자⁠열 | VDI 2770 Blatt<br>1:2020 |
| &ensp;&ensp;&ensp;&ensp;**DocumentVersions** | Information elements of individual<br>Document Version entities<br><sub>0173-1#02-ABI503#003</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**(항목)** | Information about a document version<br>entity<br><sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> | 묶⁠음&nbsp;(9) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Language** | Language style of the document<br><sub>0173-1#02-AAN468#008</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;(항목) | Language style of the document<br><sub>0173-1#02-AAN468#008</sub> | 문⁠자⁠열 | en |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Version | Design that partly deviates from the<br>previous<br><sub>0173-1#02-AAP003#005</sub> | 문⁠자⁠열 | 1.0 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Title | Name of the document<br><sub>0173-1#02-ABG940#003</sub> | 다⁠국⁠어 | Die Casting Machine<br>Operating Manual |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Description | Plain text characterizing the content of<br>the document<br><sub>0173-1#02-AAN466#004</sub> | 다⁠국⁠어 | Example handover<br>document for the<br>DC-800 die casting<br>machin… |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;StatusSetDate | Date when the document status was set<br><sub>0173-1#02-ABI000#003</sub> | 날⁠짜 | 2026-06-17 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;StatusValue | Each document version represents a point<br>in time in the document life cycle. This<br>status value refers to the milestones in<br>the document lif…<br><sub>0173-1#02-ABI001#003</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OrganizationShortName | Short name of the organization<br><sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> | 문⁠자⁠열 | ExampleOrg |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OrganizationOfficialName | Official name of the organization of the<br>author of the document<br><sub>0173-1#02-ABI004#003</sub> | 문⁠자⁠열 | Example Organization |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**DigitalFiles** | MIME-Type, file name and file contents<br>given by the file SubmodelElement<br><sub>0173-1#02-ABK126#002</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;(항목) | MIME-Type, file name and file contents<br>given by the file SubmodelElement<br><sub>0173-1#02-ABK126#002</sub> | 파⁠일 | DieCastingMachine_<br>OperatingManual_EN.<br>pdf |
| &ensp;&ensp;<sub>⋯ 같은 구성 4개 더<br>(항목 96개 생략)</sub> | | | |

</details>

<details>
<summary><b>TechnicalData</b> · 제조사가 제시하는 기술 사양 · 항목 96개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **GeneralInformation** | General information, for example<br>ordering and manufacturer information<br><sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;ManufacturerName | Legally valid designation of the natural<br>or judicial person which is directly<br>responsible for the design, production,<br>packaging and labelin…<br><sub>0173-1#02-AAO677#004</sub> | 문⁠자⁠열 | ExampleCompany |
| &ensp;&ensp;CompanyLogo | Imagefile for logo of the company<br>provided in common format (.png, .jpg)<br><sub>0173-1#02-ABI776#002</sub> | 파⁠일 | CompanyLogo.png |
| &ensp;&ensp;ManufacturerProductDesignation | Short description of the product (short<br>text)<br><sub>0173-1#02-AAW338#003</sub> | 다⁠국⁠어 | ExampleCompany Cold<br>Chamber Die Casting<br>Machine |
| &ensp;&ensp;ManufacturerArticleNumber | unique product identifier of the<br>manufacturer<br><sub>0173-1#02-AAO676#005</sub> | 문⁠자⁠열 | DC-800-ART |
| &ensp;&ensp;ManufacturerOrderCode | by manufactures issued unique<br>combination of numbers and letters used<br>to identify the device for ordering<br><sub>0173-1#02-AAO227#004</sub> | 문⁠자⁠열 | DC-800-ORD |
| &ensp;&ensp;**ProductImages** | Pictorial representations of the product<br>also related to different applications<br><sub>0173-1#02-ABM220#001</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**(항목)** | Pictorial representation of the product<br>related to an application<br><sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> | 묶⁠음&nbsp;(2) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ImageFile | Picture of the product (low resolution)<br>72 dpi / rgb (GIF or JPG)<br><sub>0173-1#02-ABK291#002</sub> | 파⁠일 | CASTINGMACHINE_<br>ProductImage.jpg |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ImageNote | Notes or explanations about the image<br>provided<br><sub>0173-1#02-ABL423#001</sub> | 다⁠국⁠어 | Side view of<br>ExampleCompany<br>cold-chamber die<br>casting machine |
| **ProductClassifications** | Product classifications by association<br>of product classes with common<br>classification systems<br><sub>0173-1#02-ABK162#002</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;**(항목)** | Single product classification item by<br>association with product class in a<br>particular classification system or<br>property dictionary<br><sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> | 묶⁠음&nbsp;(7) |  |
| &ensp;&ensp;&ensp;&ensp;ClassificationSystem | Reference to the scheduled collection of<br>abstract concepts that are used to<br>distinguish and order objects<br><sub>0173-1#02-ABL424#001</sub> | 문⁠자⁠열 | ECLASS |
| &ensp;&ensp;&ensp;&ensp;ClassificationSystemVersion | Referenced state of the published<br>classification system<br><sub>0173-1#02-AAR710#003</sub> | 문⁠자⁠열 | ECLASS 16.0 |
| &ensp;&ensp;&ensp;&ensp;ClassificationSystemUrl | Classification system URL<br><sub>ai:IDTA/TechnicalData/ProductClassifications/<br>ProduktClassification/ClassificationSystemUr…</sub> | 문⁠자⁠열 | https://eclass.eu/<br>eclass-standard/<br>search-content |
| &ensp;&ensp;&ensp;&ensp;ProductClassId | Class of the associated product or<br>industrial equipment in the<br>classification system. According to the<br>notation of the system (IRDI)<br><sub>0173-1#02-ABG776#003</sub> | 문⁠자⁠열 | 0173-1#01-AKK476#011 |
| &ensp;&ensp;&ensp;&ensp;ProductClassCodedName | Unique class code in a classification<br>hierarchy<br><sub>0173-1#02-ABK128#002</sub> | 문⁠자⁠열 | 18-07-00-00 |
| &ensp;&ensp;&ensp;&ensp;ProductClassName | Name of product class in the used<br>classification system<br><sub>0173-1#02-ABK273#002</sub> | 다⁠국⁠어 | Equipment for<br>casting NF metal |
| &ensp;&ensp;&ensp;&ensp;ReferenceToTechnicalPropertyArea | Reference to technical property area<br><sub>0173-1#02-ABL358#002</sub> | 참⁠조 |  |
| **TechnicalPropertyAreas** | List of all technical property areas<br><sub>0173-1#02-ABK163#002</sub> | 목⁠록&nbsp;(6) |  |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**DieCastingCommonSystem** | Groups common equipment-type<br>characteristics of the die casting<br>machine.<br><sub>sf:DieCastingCommonSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**DieCastingCommonSpecifications** | Common process, configuration,<br>installation and mass specifications.<br><sub>sf:DieCastingCommonSpecifications/1/0</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastingProcessType | Type of casting process performed by the<br>equipment.<br><sub>sf:CastingProcessType/1/0</sub> | 문⁠자⁠열 | High-pressure die<br>casting (cold<br>chamber) |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieCastingMachineType | Mechanical configuration of the die<br>casting machine.<br><sub>sf:DieCastingMachineType/1/0</sub> | 문⁠자⁠열 | Horizontal cold<br>chamber die casting<br>machine |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastMetalType | Metal families supported by the<br>equipment type.<br><sub>sf:CastMetalType/1/0</sub> | 문⁠자⁠열 | Aluminum and zinc<br>alloys |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SystemConfiguration | Integrated equipment systems included in<br>the reference configuration.<br><sub>sf:SystemConfiguration/1/0</sub> | 문⁠자⁠열 | Integrated<br>injection, clamping,<br>hydraulic, cooling<br>and safe… |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;InstallationType | Installation arrangement of the<br>equipment.<br><sub>sf:InstallationType/1/0</sub> | 문⁠자⁠열 | Floor-mounted<br>stationary equipment |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;NetWeight | Net mass of the equipment type.<br><sub>sf:NetWeight/1/0</sub> | 실⁠수 | 42000 kg |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**CastingCapacityAndProductionSystem** | Groups casting capacity and production<br>capability specifications.<br><sub>sf:CastingCapacityAndProductionSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**CastingCapacityAndProductionSpecifications** | Capacity, cycle, shot and alloy-range<br>specifications of the equipment type.<br><sub>sf:CastingCapacityAndProductionSpecifications/1/0</sub> | 묶⁠음&nbsp;(7) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClampingForce | Maximum rated die clamping force.<br><sub>sf:ClampingForce/1/0</sub> | 실⁠수 | 8000 kN |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MaxShotWeight | Maximum metal mass injected in one shot.<br><sub>sf:MaxShotWeight/1/0</sub> | 실⁠수 | 6.5 kg |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MaxProjectedArea | Maximum allowable projected casting<br>area.<br><sub>sf:MaxProjectedArea/1/0</sub> | 실⁠수 | 1600 cm² |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieCastingCycleTime | Reference duration of one complete<br>casting cycle.<br><sub>sf:DieCastingCycleTime/1/0</sub> | 기⁠간 | PT45S |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastingCyclesPerHour | Reference number of casting cycles per<br>hour.<br><sub>sf:CastingCyclesPerHour/1/0</sub> | 실⁠수 | 80 shots/h |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ProductionCapacity | Reference daily shot production<br>capacity.<br><sub>sf:ProductionCapacity/1/0</sub> | 실⁠수 | 1900 shots/day |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastAlloyRange | Representative alloys supported by the<br>equipment type.<br><sub>sf:CastAlloyRange/1/0</sub> | 문⁠자⁠열 | ADC12, A380, Zamak<br>3/5 |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**MoltenMetalAndInjectionSystem** | Groups molten-metal and hydraulic<br>injection specifications.<br><sub>sf:MoltenMetalAndInjectionSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**MoltenMetalAndInjectionSpecifications** | Temperature, pressure, speed, plunger<br>and shot-sleeve specifications.<br><sub>sf:MoltenMetalAndInjectionSpecifications/1/0</sub> | 묶⁠음&nbsp;(10) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MoltenMetalType | Molten-metal material used for the<br>reference configuration.<br><sub>sf:MoltenMetalType/1/0</sub> | 문⁠자⁠열 | Aluminum alloy<br>(ADC12) |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MoltenMetalTemperatureRange | Supported molten-metal temperature<br>range.<br><sub>sf:MoltenMetalTemperatureRange/1/0</sub> | 실⁠수&nbsp;범⁠위 | 640 ~ 700 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MaxInjectionPressure | Maximum rated injection pressure.<br><sub>sf:MaxInjectionPressure/1/0</sub> | 실⁠수 | 1000 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;InjectionPressureRange | Supported injection-pressure range.<br><sub>sf:InjectionPressureRange/1/0</sub> | 실⁠수&nbsp;범⁠위 | 300 ~ 1000 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;IntensificationPressure | Reference secondary intensification<br>pressure.<br><sub>sf:IntensificationPressure/1/0</sub> | 실⁠수 | 1050 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MaxPlungerSpeed | Maximum plunger speed during injection.<br><sub>sf:MaxPlungerSpeed/1/0</sub> | 실⁠수 | 8 m/s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PlungerSpeedRange | Supported plunger-speed range.<br><sub>sf:PlungerSpeedRange/1/0</sub> | 실⁠수&nbsp;범⁠위 | 0.1 ~ 8 m/s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PlungerDiameter | Nominal plunger-tip diameter.<br><sub>sf:PlungerDiameter/1/0</sub> | 실⁠수 | 100 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ShotSleeveLength | Nominal shot-sleeve length.<br><sub>sf:ShotSleeveLength/1/0</sub> | 실⁠수 | 600 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;HydraulicSystemPressure | Rated hydraulic system pressure.<br><sub>sf:HydraulicSystemPressure/1/0</sub> | 실⁠수 | 16 MPa |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**ClampingUnitAndDimensionSystem** | Groups clamping-unit, mechanical<br>envelope and acoustic specifications.<br><sub>sf:ClampingUnitAndDimensionSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**ClampingUnitAndDimensionSpecifications** | Clamping geometry, motion, force,<br>dimensions and sound-power<br>specifications.<br><sub>sf:ClampingUnitAndDimensionSpecifications/1/0</sub> | 묶⁠음&nbsp;(13) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClampingUnitType | Mechanical type of clamping unit.<br><sub>sf:ClampingUnitType/1/0</sub> | 문⁠자⁠열 | Toggle-type clamping<br>unit |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PlatenWidth | Overall width of the machine platen.<br><sub>sf:PlatenWidth/1/0</sub> | 실⁠수 | 1150 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PlatenHeight | Overall height of the machine platen.<br><sub>sf:PlatenHeight/1/0</sub> | 실⁠수 | 1150 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;TieBarClearanceHorizontal | Clear horizontal distance between tie<br>bars.<br><sub>sf:TieBarClearanceHorizontal/1/0</sub> | 실⁠수 | 820 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;TieBarClearanceVertical | Clear vertical distance between tie<br>bars.<br><sub>sf:TieBarClearanceVertical/1/0</sub> | 실⁠수 | 820 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieHeightRange | Supported die-height range.<br><sub>sf:DieHeightRange/1/0</sub> | 실⁠수&nbsp;범⁠위 | 300 ~ 800 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieOpeningStroke | Maximum die-opening stroke.<br><sub>sf:DieOpeningStroke/1/0</sub> | 실⁠수 | 700 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;EjectorForce | Maximum rated ejector force.<br><sub>sf:EjectorForce/1/0</sub> | 실⁠수 | 500 kN |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;EjectorStroke | Maximum ejector stroke.<br><sub>sf:EjectorStroke/1/0</sub> | 실⁠수 | 120 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DimensionsLength | largest length dimension of an item,<br>including protruding parts<br><sub>0173-1#02-BAB146#011</sub> | 실⁠수 | 8500 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DimensionsWidth | greatest width expansion of an object,<br>including projecting parts<br><sub>0173-1#02-BAA705#009</sub> | 실⁠수 | 2600 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DimensionsHeight | largest hight dimension of an item,<br>including projection parts<br><sub>0173-1#02-BAB707#009</sub> | 실⁠수 | 3200 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SoundPowerLevel | Reference A-weighted sound power level.<br><sub>sf:SoundPowerLevel/1/0</sub> | 실⁠수 | 82 dB(A) |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**DieCoolingAndSpraySystem** | Groups die cooling, spraying, vacuum and<br>fume-extraction specifications.<br><sub>sf:DieCoolingAndSpraySystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**DieCoolingAndSpraySpecifications** | Cooling, release-agent, vacuum and<br>extraction capabilities.<br><sub>sf:DieCoolingAndSpraySpecifications/1/0</sub> | 묶⁠음&nbsp;(8) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieCoolingMethod | Method used to cool and regulate the<br>die.<br><sub>sf:DieCoolingMethod/1/0</sub> | 문⁠자⁠열 | Closed-loop water<br>cooling with<br>temperature control |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieCoolingWaterFlowRate | Reference cooling-water volumetric flow<br>rate.<br><sub>sf:DieCoolingWaterFlowRate/1/0</sub> | 실⁠수 | 60 L/min |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieTemperatureControlSupported | Indicates whether closed-loop<br>die-temperature control is supported.<br><sub>sf:DieTemperatureControlSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieSprayType | Type of automatic die-spray mechanism.<br><sub>sf:DieSprayType/1/0</sub> | 문⁠자⁠열 | Automatic<br>reciprocating die<br>spray |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ReleaseAgentSupplyMethod | Method used to supply release agent to<br>the die-spray unit.<br><sub>sf:ReleaseAgentSupplyMethod/1/0</sub> | 문⁠자⁠열 | Central pressure-fed<br>supply |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;VacuumCastingSupported | Indicates whether vacuum-assisted<br>casting is supported.<br><sub>sf:VacuumCastingSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;FumeExtractionSupported | Indicates whether a fume-extraction<br>connection is supported.<br><sub>sf:FumeExtractionSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;FumeExtractionConnectionSize | Nominal connection size for the<br>fume-extraction duct.<br><sub>sf:FumeExtractionConnectionSize/1/0</sub> | 문⁠자⁠열 | Ø250 mm |
| &ensp;&ensp;**(항목)** | Specific property area referenced by a<br>product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**ElectricalAndSafetySystem** | Groups electrical ratings and supported<br>equipment safety functions.<br><sub>sf:ElectricalAndSafetySystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**ElectricalAndSafetySpecifications** | Power-supply, protection and<br>functional-safety specifications.<br><sub>sf:ElectricalAndSafetySpecifications/1/0</sub> | 묶⁠음&nbsp;(14) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RatedVoltage | Supported line-to-line AC supply-voltage<br>range.<br><sub>sf:RatedVoltage/1/0</sub> | 실⁠수&nbsp;범⁠위 | 380 ~ 415 V AC |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PowerSupplyPhase | Number and arrangement of electrical<br>supply phases.<br><sub>sf:PowerSupplyPhase/1/0</sub> | 문⁠자⁠열 | 3-phase |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PowerSupplyFrequency | Supported electrical supply frequencies.<br><sub>sf:PowerSupplyFrequency/1/0</sub> | 문⁠자⁠열 | 50/60 Hz |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RatedPower | Rated active power of the equipment<br>type.<br><sub>sf:RatedPower/1/0</sub> | 실⁠수 | 75 kW |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MaxRunningCurrent | Maximum current during normal operation.<br><sub>sf:MaxRunningCurrent/1/0</sub> | 실⁠수 | 140 A |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;LeakageBreakerCapacity | Rated current capacity of the<br>earth-leakage circuit breaker.<br><sub>sf:LeakageBreakerCapacity/1/0</sub> | 실⁠수 | 200 A |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SupportedSafetyFunctions | Safety functions included in the<br>reference configuration.<br><sub>sf:SupportedSafetyFunctions/1/0</sub> | 문⁠자⁠열 | Emergency stop,<br>guard interlock,<br>light curtain,<br>two-hand co… |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SafetyGateInterlockSupported | Indicates whether a safety-gate<br>interlock is supported.<br><sub>sf:SafetyGateInterlockSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;TwoHandControlSupported | Indicates whether two-hand control is<br>supported.<br><sub>sf:TwoHandControlSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;EmergencyStopSupported | Indicates whether an emergency-stop<br>function is supported.<br><sub>sf:EmergencyStopSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OverPressureReliefSupported | Indicates whether hydraulic<br>over-pressure relief is supported.<br><sub>sf:OverPressureReliefSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;LightCurtainSupported | Indicates whether light-curtain<br>protection is supported.<br><sub>sf:LightCurtainSupported/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;IPRating | Ingress-protection rating of the<br>equipment enclosure.<br><sub>sf:IPRating/1/0</sub> | 문⁠자⁠열 | IP54 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;GroundingRequired | Indicates whether protective grounding<br>is required.<br><sub>sf:GroundingRequired/1/0</sub> | 참⁠/⁠거⁠짓 | true |

</details>

<details>
<summary><b>OperationalData</b> · 운전 중 변하는 장비 상태 값 · 항목 52개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **DeviceOperationSystem** | Groups machine-level operating state<br>information.<br><sub>sf:DeviceOperationSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**DeviceOperationMonitoring** | Current machine mode, process identity,<br>shot count and operating timestamps.<br><sub>sf:DeviceOperationMonitoring/1/0</sub> | 묶⁠음&nbsp;(10) |  |
| &ensp;&ensp;&ensp;&ensp;DeviceRunState | Current high-level operating state of<br>the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문⁠자⁠열 | Automatic casting |
| &ensp;&ensp;&ensp;&ensp;ActiveProcessId | Identifier of the currently active<br>casting process.<br><sub>sf:ActiveProcessId/1/0</sub> | 문⁠자⁠열 | DC-P-001 |
| &ensp;&ensp;&ensp;&ensp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문⁠자⁠열 | Injection |
| &ensp;&ensp;&ensp;&ensp;CastingRunState | Current execution state of the casting<br>process.<br><sub>sf:CastingRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;CurrentShotId | Identifier of the current or most<br>recently completed shot.<br><sub>sf:CurrentShotId/1/0</sub> | 문⁠자⁠열 | SHOT-2026-0617-1032 |
| &ensp;&ensp;&ensp;&ensp;CumulativeShotCount | Cumulative number of casting shots<br>executed.<br><sub>sf:CumulativeShotCount/1/0</sub> | 정⁠수 | 1560000 shots |
| &ensp;&ensp;&ensp;&ensp;CumulativeOperatingHours | Cumulative equipment operating time.<br><sub>sf:CumulativeOperatingHours/1/0</sub> | 실⁠수 | 18600 h |
| &ensp;&ensp;&ensp;&ensp;OperationStartTimestamp | Timestamp at which the current operating<br>period started.<br><sub>sf:OperationStartTimestamp/1/0</sub> | 일⁠시 | 2026-06-17T08:00:<br>00+09:00 |
| &ensp;&ensp;&ensp;&ensp;LastUpdateTimestamp | Timestamp of the most recent<br>operational-data update.<br><sub>sf:LastUpdateTimestamp/1/0</sub> | 일⁠시 | 2026-06-17T08:20:<br>30+09:00 |
| **CastingProcessSystem** | Groups live high-pressure die casting<br>process data.<br><sub>sf:CastingProcessSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**CastingProcessMonitoring** | Current injection, temperature, cycle,<br>throughput and quality measurements.<br><sub>sf:CastingProcessMonitoring/1/0</sub> | 묶⁠음&nbsp;(13) |  |
| &ensp;&ensp;&ensp;&ensp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실⁠수 | 675 °C |
| &ensp;&ensp;&ensp;&ensp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실⁠수 | 920 bar |
| &ensp;&ensp;&ensp;&ensp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실⁠수 | 1020 bar |
| &ensp;&ensp;&ensp;&ensp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실⁠수 | 6.8 m/s |
| &ensp;&ensp;&ensp;&ensp;SlowShotSpeedActual | Measured slow-shot plunger speed.<br><sub>sf:SlowShotSpeedActual/1/0</sub> | 실⁠수 | 0.3 m/s |
| &ensp;&ensp;&ensp;&ensp;BiscuitThicknessActual | Measured biscuit thickness after<br>injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실⁠수 | 21 mm |
| &ensp;&ensp;&ensp;&ensp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실⁠수 | 220 °C |
| &ensp;&ensp;&ensp;&ensp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실⁠수 | 45 °C |
| &ensp;&ensp;&ensp;&ensp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기⁠간 | PT44S |
| &ensp;&ensp;&ensp;&ensp;CavityFillTimeActual | Measured time required to fill the die<br>cavity.<br><sub>sf:CavityFillTimeActual/1/0</sub> | 실⁠수 | 45 ms |
| &ensp;&ensp;&ensp;&ensp;CastingThroughputRate | Current number of completed casting<br>shots per hour.<br><sub>sf:CastingThroughputRate/1/0</sub> | 실⁠수 | 78 shots/h |
| &ensp;&ensp;&ensp;&ensp;ShotWeightConsistencyIndex | Normalized consistency index of shot<br>mass.<br><sub>sf:ShotWeightConsistencyIndex/1/0</sub> | 실⁠수 | 0.97 1 |
| &ensp;&ensp;&ensp;&ensp;CastingRejectRate | Current proportion of rejected castings.<br><sub>sf:CastingRejectRate/1/0</sub> | 실⁠수 | 1.8 % |
| **ClampingAndHydraulicSystem** | Groups live clamping and hydraulic<br>system data.<br><sub>sf:ClampingAndHydraulicSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**ClampingAndHydraulicMonitoring** | Current force, position, pressure,<br>temperature, pump and spray states.<br><sub>sf:ClampingAndHydraulicMonitoring/1/0</sub> | 묶⁠음&nbsp;(7) |  |
| &ensp;&ensp;&ensp;&ensp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실⁠수 | 7800 kN |
| &ensp;&ensp;&ensp;&ensp;DieOpenPositionActual | Measured die-open position.<br><sub>sf:DieOpenPositionActual/1/0</sub> | 실⁠수 | 0 mm |
| &ensp;&ensp;&ensp;&ensp;EjectorPositionActual | Measured ejector position.<br><sub>sf:EjectorPositionActual/1/0</sub> | 실⁠수 | 0 mm |
| &ensp;&ensp;&ensp;&ensp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실⁠수 | 15.2 MPa |
| &ensp;&ensp;&ensp;&ensp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실⁠수 | 48 °C |
| &ensp;&ensp;&ensp;&ensp;HydraulicPumpRunState | Current hydraulic-pump run state.<br><sub>sf:HydraulicPumpRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;DieSprayStatus | Current operating state of the die-spray<br>unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문⁠자⁠열 | Active |
| **ProtectionAndSafetyStateSystem** | Groups protection and machine-safety<br>operating states.<br><sub>sf:ProtectionAndSafetyStateSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**ProtectionAndSafetyStateMonitoring** | Current overload, gate, light-curtain,<br>stop and alarm states.<br><sub>sf:ProtectionAndSafetyStateMonitoring/1/0</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;OverPressureAlarmStatus | Current hydraulic over-pressure alarm<br>state.<br><sub>sf:OverPressureAlarmStatus/1/0</sub> | 문⁠자⁠열 | Normal |
| &ensp;&ensp;&ensp;&ensp;DieOverloadAlarmStatus | Current die-overload alarm state.<br><sub>sf:DieOverloadAlarmStatus/1/0</sub> | 문⁠자⁠열 | Normal |
| &ensp;&ensp;&ensp;&ensp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문⁠자⁠열 | Locked |
| &ensp;&ensp;&ensp;&ensp;LightCurtainStatus | Current light-curtain state.<br><sub>sf:LightCurtainStatus/1/0</sub> | 문⁠자⁠열 | Clear |
| &ensp;&ensp;&ensp;&ensp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문⁠자⁠열 | None |
| **ElectricalAndSafetyConditionSystem** | Groups electrical supply and<br>safety-condition data.<br><sub>sf:ElectricalAndSafetyConditionSystem/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**ElectricalAndSafetyConditionMonitoring** | Current power, supply, emergency-stop,<br>guard and permission states.<br><sub>sf:ElectricalAndSafetyConditionMonitoring/1/0</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실⁠수 | 58000 W |
| &ensp;&ensp;&ensp;&ensp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문⁠자⁠열 | Normal |
| &ensp;&ensp;&ensp;&ensp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;GuardInterlockStatus | Current guard-interlock state.<br><sub>sf:GuardInterlockStatus/1/0</sub> | 문⁠자⁠열 | Locked |
| &ensp;&ensp;&ensp;&ensp;SafetyCoverState | Current state of the safety cover.<br><sub>sf:SafetyCoverState/1/0</sub> | 문⁠자⁠열 | Closed |
| &ensp;&ensp;&ensp;&ensp;OperationPermittedState | Indicates whether machine operation is<br>currently permitted.<br><sub>sf:OperationPermittedState/1/0</sub> | 문⁠자⁠열 | Permitted |

</details>

<details>
<summary><b>TimeSeries</b> · 상태 값의 시간별 기록 · 항목 1506개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **Metadata** | A set of data describing and providing<br>information about the time series<br><sub>ai:idta/TimeSeries/Metadata/1/1</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;Name | Meaningful name for labeling<br><sub>ai:idta/TimeSeries/Metadata/Name/1/1</sub> | 다⁠국⁠어 | Die casting machine<br>operation time<br>series |
| &ensp;&ensp;Description | Short description of the time series<br><sub>ai:idta/TimeSeries/Metadata/Description/1/1</sub> | 다⁠국⁠어 | Operational signals<br>for the injection,<br>die, hydraulic and<br>s… |
| &ensp;&ensp;**Record** | A time series record is unique by its ID<br>within the time series and contains the<br>timestamps and variable values<br>referenced to the ID. Simil…<br><sub>ai:idta/TimeSeries/Record/1/1</sub> | 묶⁠음&nbsp;(23) |  |
| &ensp;&ensp;&ensp;&ensp;Time | Point of Time in seconds. Time points<br>refer to the start time of the time<br>series segment.<br><sub>ai:idta/TimeSeries/RelativePointInTime/1/1</sub> | 정⁠수 | 0 s |
| &ensp;&ensp;&ensp;&ensp;DeviceRunState | Current high-level operating state of<br>the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문⁠자⁠열 | Automatic casting |
| &ensp;&ensp;&ensp;&ensp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문⁠자⁠열 | Injection |
| &ensp;&ensp;&ensp;&ensp;CastingRunState | Current execution state of the casting<br>process.<br><sub>sf:CastingRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실⁠수 | 675.00 °C |
| &ensp;&ensp;&ensp;&ensp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실⁠수 | 920.00 bar |
| &ensp;&ensp;&ensp;&ensp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실⁠수 | 1020.00 bar |
| &ensp;&ensp;&ensp;&ensp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실⁠수 | 6.800 m/s |
| &ensp;&ensp;&ensp;&ensp;BiscuitThicknessActual | Measured biscuit thickness after<br>injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실⁠수 | 21.000 mm |
| &ensp;&ensp;&ensp;&ensp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실⁠수 | 220.00 °C |
| &ensp;&ensp;&ensp;&ensp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실⁠수 | 45.00 °C |
| &ensp;&ensp;&ensp;&ensp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기⁠간 | PT44S |
| &ensp;&ensp;&ensp;&ensp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실⁠수 | 7800.00 kN |
| &ensp;&ensp;&ensp;&ensp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실⁠수 | 15.200 MPa |
| &ensp;&ensp;&ensp;&ensp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실⁠수 | 48.00 °C |
| &ensp;&ensp;&ensp;&ensp;DieSprayStatus | Current operating state of the die-spray<br>unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문⁠자⁠열 | Active |
| &ensp;&ensp;&ensp;&ensp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실⁠수 | 58000.00 W |
| &ensp;&ensp;&ensp;&ensp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문⁠자⁠열 | Normal |
| &ensp;&ensp;&ensp;&ensp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문⁠자⁠열 | Locked |
| &ensp;&ensp;&ensp;&ensp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문⁠자⁠열 | None |
| **Segments** | Contains segments of a time series<br><sub>ai:idta/TimeSeries/Segments/1/1</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;**ExternalSegment** | Reference to a file of data points in<br>sequential order over a period of time<br><sub>ai:idta/TimeSeries/Segments/ExternalSegment/1/1</sub> | 묶⁠음&nbsp;(12) |  |
| &ensp;&ensp;&ensp;&ensp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다⁠국⁠어 | Die casting machine<br>historian file data |
| &ensp;&ensp;&ensp;&ensp;Description | Short description of the time series<br>segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다⁠국⁠어 | Die casting machine<br>time series data<br>stored in external<br>CSV… |
| &ensp;&ensp;&ensp;&ensp;RecordCount | Indicates how many records are present<br>in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정⁠수 | 86400 |
| &ensp;&ensp;&ensp;&ensp;StartTime | Contains the first recorded timestamp of<br>the time series segment and thus<br>represents the beginning of a time<br>series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T00:00:00Z |
| &ensp;&ensp;&ensp;&ensp;EndTime | <br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T23:59:59Z |
| &ensp;&ensp;&ensp;&ensp;Duration | Period covered by the segment,<br>represented according to ISO 8601 by the<br>format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문⁠자⁠열 | PT24H |
| &ensp;&ensp;&ensp;&ensp;SamplingInterval | The time period between two time series<br>records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정⁠수 | 1 s |
| &ensp;&ensp;&ensp;&ensp;SamplingRate | Defines the number of samples per second<br>for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정⁠수 | 1 Hz |
| &ensp;&ensp;&ensp;&ensp;State | State of the time series related to its<br>progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문⁠자⁠열 | completed |
| &ensp;&ensp;&ensp;&ensp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문⁠자⁠열 | 2026-06-18T00:00:05Z |
| &ensp;&ensp;&ensp;&ensp;File | Sequence of data points in sequential<br>order over a period of time within a<br>paged data file<br><sub>ai:idta/TimeSeries/File/1/1</sub> | 파⁠일 | DC_TS_20260617.csv |
| &ensp;&ensp;&ensp;&ensp;Blob | Sequence of data points in sequential<br>order over a period of time within a<br>BLOB<br><sub>ai:idta/TimeSeries/Blob/1/1</sub> | 내⁠장⁠ ⁠데⁠이⁠터 |  |
| &ensp;&ensp;**LinkedSegment** | Reference to an endpoint of data points<br>in sequential order over a period of<br>time<br><sub>ai:idta/TimeSeries/Segments/LinkedSegment/1/1</sub> | 묶⁠음&nbsp;(12) |  |
| &ensp;&ensp;&ensp;&ensp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다⁠국⁠어 | Die casting machine<br>historian API data |
| &ensp;&ensp;&ensp;&ensp;Description | Short description of the time series<br>segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다⁠국⁠어 | Die casting machine<br>time series data<br>queried from<br>external … |
| &ensp;&ensp;&ensp;&ensp;RecordCount | Indicates how many records are present<br>in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정⁠수 | 86400 |
| &ensp;&ensp;&ensp;&ensp;StartTime | Contains the first recorded timestamp of<br>the time series segment and thus<br>represents the beginning of a time<br>series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T00:00:00Z |
| &ensp;&ensp;&ensp;&ensp;EndTime | <br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T23:59:59Z |
| &ensp;&ensp;&ensp;&ensp;Duration | Period covered by the segment,<br>represented according to ISO 8601 by the<br>format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문⁠자⁠열 | PT24H |
| &ensp;&ensp;&ensp;&ensp;SamplingInterval | The time period between two time series<br>records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정⁠수 | 1 s |
| &ensp;&ensp;&ensp;&ensp;SamplingRate | Defines the number of samples per second<br>for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정⁠수 | 1 Hz |
| &ensp;&ensp;&ensp;&ensp;State | State of the time series related to its<br>progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문⁠자⁠열 | completed |
| &ensp;&ensp;&ensp;&ensp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문⁠자⁠열 | 2026-06-18T00:00:05Z |
| &ensp;&ensp;&ensp;&ensp;Endpoint | Specifies a location of a resource on an<br>API server through which time series can<br>be requested<br><sub>ai:idta/TimeSeries/Endpoint/1/1</sub> | 문⁠자⁠열 | https://historian.<br>example.com/api/<br>timeseries |
| &ensp;&ensp;&ensp;&ensp;Query | generic query component to read time<br>series data from an API<br><sub>ai:idta/TimeSeries/Query/1/1</sub> | 문⁠자⁠열 | assetId=DC-SN-2026-<br>0001&amp;from=2026-06-<br>17T00:00:<br>00Z&amp;to=2026-0… |
| &ensp;&ensp;**InternalSegment** | Grouped sequence of data points in<br>successive order over a specified period<br>of time<br><sub>ai:idta/TimeSeries/Segments/InternalSegment/1/1</sub> | 묶⁠음&nbsp;(11) |  |
| &ensp;&ensp;&ensp;&ensp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다⁠국⁠어 | Recent die casting<br>machine operation<br>data |
| &ensp;&ensp;&ensp;&ensp;Description | Short description of the time series<br>segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다⁠국⁠어 | Recent die casting<br>machine operation<br>records stored<br>directl… |
| &ensp;&ensp;&ensp;&ensp;RecordCount | Indicates how many records are present<br>in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정⁠수 | 60 |
| &ensp;&ensp;&ensp;&ensp;StartTime | Contains the first recorded timestamp of<br>the time series segment and thus<br>represents the beginning of a time<br>series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T08:15:00Z |
| &ensp;&ensp;&ensp;&ensp;EndTime | Contains the last recorded timestamp of<br>the time series segment and thus<br>represents the end of a time series.<br>Time format and scale corresp…<br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문⁠자⁠열 | 2026-06-17T08:15:59Z |
| &ensp;&ensp;&ensp;&ensp;Duration | Period covered by the segment,<br>represented according to ISO 8601 by the<br>format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문⁠자⁠열 | PT1M |
| &ensp;&ensp;&ensp;&ensp;SamplingInterval | The time period between two time series<br>records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정⁠수 | 1 s |
| &ensp;&ensp;&ensp;&ensp;SamplingRate | Defines the number of samples per second<br>for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정⁠수 | 1 Hz |
| &ensp;&ensp;&ensp;&ensp;State | State of the time series related to its<br>progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문⁠자⁠열 | completed |
| &ensp;&ensp;&ensp;&ensp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문⁠자⁠열 | 2026-06-17T08:16:00Z |
| &ensp;&ensp;&ensp;&ensp;**Records** | Group of data points in successive order<br>over a specified period of time<br><sub>ai:idta/TimeSeries/Records/1/1</sub> | 묶⁠음&nbsp;(60) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;**Record__0000__** | A time series record is unique by its ID<br>within the time series and contains the<br>timestamps and variable values<br>referenced to the ID. Simil…<br><sub>ai:idta/TimeSeries/Record/1/1</sub> | 묶⁠음&nbsp;(23) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Time | Point of Time in seconds. Time points<br>refer to the start time of the time<br>series segment.<br><sub>ai:idta/TimeSeries/RelativePointInTime/1/1</sub> | 정⁠수 | 0 s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DeviceRunState | Current high-level operating state of<br>the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문⁠자⁠열 | Automatic casting |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문⁠자⁠열 | Injection |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastingRunState | Current execution state of the casting<br>process.<br><sub>sf:CastingRunState/1/0</sub> | 문⁠자⁠열 | Running |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실⁠수 | 675.00 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실⁠수 | 920.00 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실⁠수 | 1020.00 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실⁠수 | 6.800 m/s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;BiscuitThicknessActual | Measured biscuit thickness after<br>injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실⁠수 | 21.000 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실⁠수 | 220.00 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실⁠수 | 45.00 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기⁠간 | PT44S |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실⁠수 | 7800.00 kN |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실⁠수 | 15.200 MPa |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실⁠수 | 48.00 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieSprayStatus | Current operating state of the die-spray<br>unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문⁠자⁠열 | Active |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실⁠수 | 58000.00 W |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문⁠자⁠열 | Normal |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문⁠자⁠열 | Locked |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문⁠자⁠열 | Released |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문⁠자⁠열 | None |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;<sub>⋯ 같은 구성 59개 더<br>(항목 1416개 생략)</sub> | | | |

</details>

<details>
<summary><b>ProcessParameters</b> · 제품·공정별 설정값 · 항목 41개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **Processes** | Provides all the necessary parameters of<br>processes in a structured form that are<br>required to manufacture a product<br><sub>ai:idta/ProcessParameters/Processes/1/0</sub> | 묶⁠음&nbsp;(1) |  |
| &ensp;&ensp;**Process__00__** | The processes to be executed are<br>described individually in the SMC<br>Process.<br><sub>ai:idta/ProcessParameters/Process/1/0</sub> | 묶⁠음&nbsp;(8) |  |
| &ensp;&ensp;&ensp;&ensp;ProcessId | Describes the ID of the process<br><sub>ai:idta/ProcessParameters/ProcessId/1/0</sub> | 문⁠자⁠열 | DC-P-001 |
| &ensp;&ensp;&ensp;&ensp;ProcessName | Describes the Name of the Process<br><sub>ai:idta/ProcessParameters/ProcessName/1/0</sub> | 문⁠자⁠열 | High-pressure die<br>casting |
| &ensp;&ensp;&ensp;&ensp;ProcessDescription | Describes the process.<br><sub>ai:idta/ProcessParameters/ProcessDescription/1/0</sub> | 다⁠국⁠어 | Process parameters<br>for high-pressure<br>die casting shot<br>opera… |
| &ensp;&ensp;&ensp;&ensp;PlannedProcessTime | Planned processing time for process<br>execution (without set-up time)<br><sub>ai:idta/ProcessParameters/PlannedProcessTime/1/0</sub> | 기⁠간 | PT45S |
| &ensp;&ensp;&ensp;&ensp;**ProductParameters** | Mandatory product parameters for process<br>execution<br><sub>ai:idta/ProcessParameters/ProductParameters/1/0</sub> | 묶⁠음&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CastAlloyType | Alloy selected for the casting process.<br><sub>sf:CastAlloyType/1/0</sub> | 문⁠자⁠열 | Aluminum alloy ADC12 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MoltenMetalTargetTemperature | Target molten-metal temperature before<br>injection.<br><sub>sf:MoltenMetalTargetTemperature/1/0</sub> | 실⁠수 | 680 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PartNetWeight | Target net mass of one cast part.<br><sub>sf:PartNetWeight/1/0</sub> | 실⁠수 | 3.8 kg |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ShotWeight | Target total shot mass including runners<br>and overflows.<br><sub>sf:ShotWeight/1/0</sub> | 실⁠수 | 5.2 kg |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;CavityCount | Number of cavities in the die.<br><sub>sf:CavityCount/1/0</sub> | 정⁠수 | 2 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;TargetProductionQuantity | Target number of casting shots for the<br>production order.<br><sub>sf:TargetProductionQuantity/1/0</sub> | 정⁠수 | 1900 shots |
| &ensp;&ensp;&ensp;&ensp;**ProcessParameters** | Mandatory process parameters for process<br>execution<br><sub>ai:idta/ProcessParameters/ProcessParameters/1/0</sub> | 묶⁠음&nbsp;(15) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OperationRecipeId | Identifier of the die casting process<br>recipe.<br><sub>sf:OperationRecipeId/1/0</sub> | 문⁠자⁠열 | RECIPE-DC-001 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문⁠자⁠열 | Automatic casting |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ProcessStepSequence | Ordered sequence of process steps in one<br>casting cycle.<br><sub>sf:ProcessStepSequence/1/0</sub> | 문⁠자⁠열 | Mold close &gt; Molten<br>metal dosing &gt; Slow<br>shot &gt; Fast shot &gt; … |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;SlowShotSpeedSetpoint | Target plunger speed during the<br>slow-shot phase.<br><sub>sf:SlowShotSpeedSetpoint/1/0</sub> | 실⁠수 | 0.3 m/s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;FastShotSpeedSetpoint | Target plunger speed during the<br>fast-shot phase.<br><sub>sf:FastShotSpeedSetpoint/1/0</sub> | 실⁠수 | 6.5 m/s |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ShotChangeoverPosition | Plunger position at the<br>slow-to-fast-shot transition.<br><sub>sf:ShotChangeoverPosition/1/0</sub> | 실⁠수 | 350 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;InjectionPressureSetpoint | Target injection pressure.<br><sub>sf:InjectionPressureSetpoint/1/0</sub> | 실⁠수 | 900 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;IntensificationPressureSetpoint | Target intensification pressure.<br><sub>sf:IntensificationPressureSetpoint/1/0</sub> | 실⁠수 | 1050 bar |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ClampingForceSetpoint | Target die clamping force.<br><sub>sf:ClampingForceSetpoint/1/0</sub> | 실⁠수 | 8000 kN |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieTemperatureSetpoint | Target die temperature.<br><sub>sf:DieTemperatureSetpoint/1/0</sub> | 실⁠수 | 220 °C |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;HoldTime | Target pressure-holding duration.<br><sub>sf:HoldTime/1/0</sub> | 기⁠간 | PT3S |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;InDieCoolingTime | Target cooling duration before die<br>opening.<br><sub>sf:InDieCoolingTime/1/0</sub> | 기⁠간 | PT8S |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DieSprayTime | Target die-spray duration.<br><sub>sf:DieSprayTime/1/0</sub> | 기⁠간 | PT2S |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;BiscuitThicknessSetpoint | Target biscuit thickness.<br><sub>sf:BiscuitThicknessSetpoint/1/0</sub> | 실⁠수 | 20 mm |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;OverPressureAlarmThreshold | Injection-pressure threshold for an<br>over-pressure alarm.<br><sub>sf:OverPressureAlarmThreshold/1/0</sub> | 실⁠수 | 1150 bar |
| &ensp;&ensp;&ensp;&ensp;**ResourceParameters** | Mandatory resource parameters for<br>process execution<br><sub>ai:idta/ProcessParameters/ResourceParameters/1/0</sub> | 묶⁠음&nbsp;(7) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredMoltenMetalTempSensor | Temperature sensor required to execute<br>the casting process.<br><sub>sf:RequiredMoltenMetalTempSensor/1/0</sub> | 문⁠자⁠열 | MetalTempSensor01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredInjectionPressureSensor | Injection-pressure sensor required to<br>execute the casting process.<br><sub>sf:RequiredInjectionPressureSensor/1/0</sub> | 문⁠자⁠열 | InjectionPressureSensor01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredPlungerPositionSensor | Plunger-position sensor required to<br>execute the casting process.<br><sub>sf:RequiredPlungerPositionSensor/1/0</sub> | 문⁠자⁠열 | PlungerPositionSensor01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredShotCylinder | Shot-cylinder resource required to<br>execute the casting process.<br><sub>sf:RequiredShotCylinder/1/0</sub> | 문⁠자⁠열 | ShotCylinder01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredClampingUnit | Clamping-unit resource required to<br>execute the casting process.<br><sub>sf:RequiredClampingUnit/1/0</sub> | 문⁠자⁠열 | ToggleClampingUnit01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredDieSprayUnit | Die-spray resource required to execute<br>the casting process.<br><sub>sf:RequiredDieSprayUnit/1/0</sub> | 문⁠자⁠열 | DieSprayUnit01 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;RequiredHydraulicPump | Hydraulic-pump resource required to<br>execute the casting process.<br><sub>sf:RequiredHydraulicPump/1/0</sub> | 문⁠자⁠열 | HydraulicPump01 |
| &ensp;&ensp;&ensp;&ensp;**ProcessBoM** | Describes the products or semi-finished<br>products to be involved in the process<br><sub>ai:idta/ProcessParameters/ProcessBoM/1/0</sub> | 묶⁠음&nbsp;(3) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MoltenMetalConsumable | Controlled identifier of the<br>molten-metal consumable.<br><sub>sf:MoltenMetalConsumable/1/0</sub> | 문⁠자⁠열 | AL-ADC12-INGOT-001 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ReleaseAgentConsumable | Controlled identifier of the<br>release-agent consumable.<br><sub>sf:ReleaseAgentConsumable/1/0</sub> | 문⁠자⁠열 | RELEASE-AGENT-001 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;HydraulicOil | Controlled identifier of the hydraulic<br>oil used by the equipment.<br><sub>sf:HydraulicOil/1/0</sub> | 문⁠자⁠열 | HYD-OIL-001 |

</details>

<details>
<summary><b>PredictiveMaintenance</b> · 예지정비 모델과 결과 · 항목 91개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 예시값 |
|---|---|---|---|
| **RemainingUsefulLifePrediction** | Information about remaining useful life<br>(RUL) prediction in the context of<br>predictive maintenance<br><sub>ai:idta/PredictiveMaintenance/<br>RemainingUsefulLifePrediction/1/0</sub> | 묶⁠음&nbsp;(7) |  |
| &ensp;&ensp;**RemainingUsefulLifetime** | Remaining useful life time, bades on<br>Lifetime model of OPC Foundation<br>(https://reference.opcfoundation.org/DI/<br>v104/docs/10)<br><sub>ai:idta/PredictiveMaintenance/<br>RemainingUsefulLifetime/1/0</sub> | 개⁠체&nbsp;(6) |  |
| &ensp;&ensp;&ensp;&ensp;IndicationType | Type of wear-relevant duration, e.g.<br>time, cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/IndicationType/1/0</sub> | 문⁠자⁠열 | OperatingHours |
| &ensp;&ensp;&ensp;&ensp;DurationValue | Value of duration in the wear relevant<br>unit, e.g. time, operation cycles,<br>distance, etc.<br><sub>ai:idta/PredictiveMaintenance/DurationValue/1/0</sub> | 실⁠수 | 9000 |
| &ensp;&ensp;&ensp;&ensp;EngineeringUnit | Wear relevant physical unit, e.g. time,<br>operation cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> | 문⁠자⁠열 | h |
| &ensp;&ensp;&ensp;&ensp;StartValue | Starting value from which the duration<br>is measured in the wear-relevant unit,<br>e.g. time, cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/StartValue/1/0</sub> | 실⁠수 | 9000 |
| &ensp;&ensp;&ensp;&ensp;StartDateTime | Start date and time from which the<br>duration is measured<br><sub>ai:idta/PredictiveMaintenance/StartDateTime/1/0</sub> | 일⁠시 | 2026-06-26T09:00:<br>00+09:00 |
| &ensp;&ensp;&ensp;&ensp;Description | Description of the wear duration<br>information<br><sub>ai:idta/PredictiveMaintenance/Description/1/0</sub> | 문⁠자⁠열 | Estimated remaining<br>operating time for<br>the shot sleeve and<br>… |
| &ensp;&ensp;RemainingUsfulLifeDateTime | mark attributed to an instant by means<br>of a specified timescale, expressed as a<br>date and a time<br><sub>ai:idta/PredictiveMaintenance/<br>RemainingUsfulLifeDateTime/1/0</sub> | 일⁠시 | 2027-07-15T09:00:<br>00+09:00 |
| &ensp;&ensp;ConfidenceInterval | confidence interval, measured in the<br>unit of the predicted value<br><sub>ai:idta/PredictiveMaintenance/ConfidenceInterval/<br>1/0</sub> | 실⁠수&nbsp;범⁠위 | 7800 ~ 10500 |
| &ensp;&ensp;**ListRULBoundaryConditions** | List of boundary conditions for which<br>remaining useful life has been predicted<br><sub>ai:idta/PredictiveMaintenance/<br>ListRULBoundaryConditions/1/0</sub> | 목⁠록&nbsp;(7) |  |
| &ensp;&ensp;&ensp;&ensp;**(항목)** | Boundary condition for which remaining<br>useful life has been predicted<br><sub>ai:idta/PredictiveMaintenance/RULCondition/1/0</sub> | 묶⁠음&nbsp;(9) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;ConditionName | Name of the indicator (process value,<br>KPI, material property, asset property)<br>describing a boundary condition for<br>which RUL prediction is v…<br><sub>ai:idta/PredictiveMaintenance/ConditionName/1/0</sub> | 문⁠자⁠열 | HydraulicPumpCurrentActual |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;IsBoundaryConditionUsedInModel | If this boundary condition is used in<br>the model for RUL prediction true, else<br>false<br><sub>ai:idta/PredictiveMaintenance/<br>IsBoundaryConditionUsedInModel/1/0</sub> | 참⁠/⁠거⁠짓 | true |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;BoundaryValueRange | Value range of the indicator (process<br>value, KPI, material property, asset<br>property) describing a boundary<br>condition for which RUL predicti…<br><sub>ai:idta/PredictiveMaintenance/BoundaryValueRange/<br>1/0</sub> | 실⁠수 | 96 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;BoundaryEngineeringUnit | Engineering Unit of the boundary<br>condition indicator<br><sub>ai:idta/PredictiveMaintenance/<br>BoundaryEngineeringUnit/1/0</sub> | 문⁠자⁠열 | A |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DriftInfoAIModel | Drift information of AI model<br><sub>ai:idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> | 실⁠수&nbsp;범⁠위 | 0.07 ~ 0.07 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;MeanValue | Mean value of the distribution of<br>indicator values<br><sub>ai:idta/PredictiveMaintenance/MeanValue/1/0</sub> | 실⁠수 | 96 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Standarddeviation | Standard deviation of the distribution<br>of indicator values<br><sub>ai:idta/PredictiveMaintenance/Standarddeviation/1/<br>0</sub> | 실⁠수 | 10 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Skewness | Skewness of the distribution of<br>indicator values<br><sub>ai:idta/PredictiveMaintenance/Skewness/1/0</sub> | 실⁠수 | 0.4 |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;BoundaryDescription | Description of the boundary of a RUL<br>prediction condition<br><sub>ai:idta/PredictiveMaintenance/BoundaryDescription/<br>1/0</sub> | 문⁠자⁠열 | Hydraulic pump<br>current window used<br>to identify<br>sustained ov… |
| &ensp;&ensp;&ensp;&ensp;<sub>⋯ 같은 구성 6개 더<br>(항목 60개 생략)</sub> | | | |
| &ensp;&ensp;**PredictionModelInformation** | Information about the model for RUL<br>prediction relevant in the context of<br>predictive maintenance<br><sub>ai:idta/PredictiveMaintenance/<br>PredictionModelInformation/1/0</sub> | 묶⁠음&nbsp;(2) |  |
| &ensp;&ensp;&ensp;&ensp;ModelType | Model type as an enumerated value:<br>physical based methods, data-driven<br>methods, hybrid methods<br><sub>ai:idta/PredictiveMaintenance/ModelType/1/0</sub> | 문⁠자⁠열 | ModelTypeHybrid |
| &ensp;&ensp;&ensp;&ensp;ModelDescription | More detailed description of the model<br>type used for RUL prediction (optional)<br><sub>ai:idta/PredictiveMaintenance/ModelDescription/1/0</sub> | 문⁠자⁠열 | Hybrid physics- and<br>data-driven RUL<br>model. Feature<br>importan… |
| &ensp;&ensp;**ListPreAlerts** | List for defining pre-alerts which<br>should be raised before remaining useful<br>life is exceeded<br><sub>ai:idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> | 목⁠록&nbsp;(1) |  |
| &ensp;&ensp;&ensp;&ensp;**(항목)** | Definition of a pre-alert which should<br>be raised before remaining useful life<br>is exceeded<br><sub>ai:idta/PredictiveMaintenance/PreAlerts/1/0</sub> | 묶⁠음&nbsp;(2) |  |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PreAlertMessage | Message to be displayed when alarm<br>regarding predicted remaining useful<br>life is raised<br><sub>ai:idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> | 문⁠자⁠열 | Inspect the shot<br>sleeve, plunger tip<br>and hydraulic pump<br>bef… |
| &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;PreAlertValue | Pre-warning duration in wear relevant<br>unit before remaining useful life is<br>exceeded<br><sub>ai:idta/PredictiveMaintenance/PreAlertValue/1/0</sub> | 실⁠수 | 1200 |
| &ensp;&ensp;**AlertAfterExceedingRemainingUsableLife** | Alert information which should be<br>triggered or displayed after exceeding<br>remaining useful life<br><sub>ai:idta/PredictiveMaintenance/<br>AlertAfterExceedingRemainingUsableLife/1/0</sub> | 묶⁠음&nbsp;(2) |  |
| &ensp;&ensp;&ensp;&ensp;AlertMessage | Message to be displayed when alarm<br>regarding predicted remaining useful<br>life is raised<br><sub>ai:idta/PredictiveMaintenance/AlertMessage/1/0</sub> | 문⁠자⁠열 | Maintenance is<br>required after the<br>remaining useful<br>life of … |
| &ensp;&ensp;&ensp;&ensp;MaintenanceRequired | Maintenance required<br><sub>ai:idta/PredictiveMaintenance/MaintenanceRequired/<br>1/0</sub> | 참⁠/⁠거⁠짓 | false |

</details>
