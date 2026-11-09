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
| URIOfTheProduct | unique global identification of the product instance using an universal resource identifier (URI)<br><sub>0112/2///61987#ABN590#002</sub> | URI |  | https://www.smart-factory.kr/ids/asset/DieCastingMachine/DC… |
| ManufacturerName | legally valid designation of the natural or judicial person which is directly responsible for the design, production, packaging and labelin…<br><sub>0112/2///61987#ABA565#009</sub> | 다국어 |  | ExampleCompany |
| ManufacturerProductDesignation | short description of the product (short text), third or lowest level of a 3 level manufacturer specific product hierarchy<br><sub>0112/2///61987#ABA567#009</sub> | 다국어 |  | Cold Chamber Die Casting Machine |
| **AddressInformation** | Note: this set of information is defined by SMT drop-in &quot;Address Information&quot;<br><sub>ai:zvei/nameplate/1/0/ContactInformations/AddressInformation</sub> | 묶음 (4) |  |  |
| &emsp;Street | <br><sub>0173-1#02-AAO128#002</sub> | 다국어 |  | Example Street 1 |
| &emsp;Zipcode | <br><sub>0173-1#02-AAO129#002</sub> | 다국어 |  | 12345 |
| &emsp;CityTown | <br><sub>0173-1#02-AAO132#002</sub> | 다국어 |  | Example City |
| &emsp;NationalCode | <br><sub>0173-1#02-AAO134#002</sub> | 다국어 |  | KR |
| ManufacturerProductRoot | top level of a 3 level manufacturer specific product hierarchy<br><sub>0112/2///61360_7#AAS011#001</sub> | 다국어 |  | Casting Equipment |
| ManufacturerProductFamily | second level of a 3 level manufacturer specific product hierarchy<br><sub>0112/2///61987#ABP464#002</sub> | 다국어 |  | High-Pressure Die Casting Machine |
| ManufacturerProductType | characteristic to differentiate between different products of a product family or special variants<br><sub>0112/2///61987#ABA300#008</sub> | 문자열 |  | DC-800 |
| OrderCodeOfManufacturer | unique combination of numbers and letters issued by the manufacturer that is used to identify the device for ordering<br><sub>0112/2///61987#ABA950#008</sub> | 문자열 |  | DC-800-ORD |
| ProductArticleNumberOfManufacturer | unique product identifier of the manufacturer<br><sub>0112/2///61987#ABA581#007</sub> | 문자열 |  | DC-800-ART |
| SerialNumber | unique combination of numbers and letters used to identify the device once it has been manufactured<br><sub>0112/2///61987#ABA951#009</sub> | 문자열 |  | DC-SN-2026-0001 |
| YearOfConstruction | year in which the manufacturing process is completed<br><sub>0112/2///61987#ABP000#002</sub> | 문자열 |  | 2026 |
| DateOfManufacture | date when an item was manufactured<br><sub>0112/2///61987#ABB757#007</sub> | 날짜 |  | 2026-06-17 |
| HardwareVersion | version of the hardware supplied with the device<br><sub>0112/2///61987#ABA926#008</sub> | 문자열 |  | HW-1.0 |
| FirmwareVersion | version of the firmware supplied with the device<br><sub>0112/2///61987#ABA302#006</sub> | 문자열 |  | FW-1.0 |
| SoftwareVersion | version of the software used by the device<br><sub>0112/2///61987#ABA601#008</sub> | 문자열 |  | SW-1.0 |
| CountryOfOrigin | Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes<br><sub>0112/2///61987#ABP462#001</sub> | 문자열 |  | KR |
| UniqueFacilityIdentifier | unique string of characters for the identification of locations or buildings involved in a product’s value chain or used by actors involved…<br><sub>ai:idta/nameplate/3/0/UniqueFacilityIdentifier</sub> | 문자열 |  | TYPE-DC-800 |
| CompanyLogo | a graphic mark used to represent a company, an organisation or a product<br><sub>0112/2///61987#ABP463#001</sub> | 파일 |  | CompanyLogo.png |
| **Markings** | Note: CE marking is declared as mandatory according to EU Blue Guide<br><sub>0112/2///61360_7#AAS006#001</sub> | 목록 (1) |  |  |
| &emsp;**(항목)** | Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission<br><sub>0112/2///61360_7#AAS009#001</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;MarkingName | common name of the marking<br><sub>0112/2///61987#ABA231#009</sub> | 문자열 |  | CE |
| &emsp;&emsp;DesignationOfCertificateOrApproval | Note: Approval identifier, reference to the certificate number, to be entered without spaces<br><sub>0112/2///61987#ABH783#003</sub> | 문자열 |  | Declaration of Conformity |
| &emsp;&emsp;IssueDate | Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day<br><sub>0112/2///61987#ABO097#001</sub> | 날짜 |  | 2026-06-17 |
| &emsp;&emsp;ExpiryDate | Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day<br><sub>0112/2///61987#ABH830#002</sub> | 날짜 |  | 2036-06-16 |
| &emsp;&emsp;MarkingFile | conformity symbol of the marking<br><sub>0112/2///61987#ABO100#002</sub> | 파일 |  | DieCastingMachine_CertificatesDeclarations_EN.pdf |
| &emsp;&emsp;MarkingAdditionalText | where applicable, additional information on the marking in plain text, e.g. the ID-number of the notified body involved in the conformity p…<br><sub>0112/2///61987#ABB146#007</sub> | 문자열 |  | Conformity information for the DC-800 equipment type. |

</details>

<details>
<summary><b>HandoverDocumentation</b> · 납품 시 함께 전달하는 문서 목록 · 항목 121개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Documents** | Information for a document identity<br><sub>0173-1#02-ABI500#003</sub> | 목록 (5) |  |  |
| &emsp;**(항목)** | This SubmodelElementCollection holds the information for a VDI 2770 Document entity<br><sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;**DocumentIds** | Set of document identifiers for the document. One ID in this collection should be used as a preferred ID<br><sub>0173-1#02-ABI501#003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | This SubmodelElementCollection holds the information for a VDI 2770 Document entity<br><sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;&emsp;DocumentDomainId | Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organ…<br><sub>0173-1#02-ABH994#003</sub> | 문자열 |  | EXAMPLE_DIE_CASTING_DOC |
| &emsp;&emsp;&emsp;&emsp;DocumentIdentifier | alphanumeric character sequence uniquely identifying a document<br><sub>0173-1#02-AAO099#004</sub> | 문자열 |  | DC-OM-001 |
| &emsp;&emsp;&emsp;&emsp;DocumentIsPrimary | Flag indicating that a DocumentId within a collection of at least two DocumentId`s is the ‘primary’ identifier for the document. This is th…<br><sub>0173-1#02-ABH995#003</sub> | 참/거짓 |  | true |
| &emsp;&emsp;**DocumentClassifications** | Set of information for describing the classification of the Document according to ClassificationSystems<br><sub>0173-1#02-ABI502#003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | Set of information for describing the classification of the Document according to a ClassificationSystem<br><sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;&emsp;ClassId | Unique ID of the document class within a classficationsystem<br><sub>0173-1#02-ABH996#003</sub> | 문자열 |  | 03-02 |
| &emsp;&emsp;&emsp;&emsp;ClassName | Name of the class in the classification system<br><sub>0173-1#02-ABJ219#002</sub> | 다국어 |  | Operation |
| &emsp;&emsp;&emsp;&emsp;ClassificationSystem | Identification of the classification system<br><sub>0173-1#02-ABH997#003</sub> | 문자열 |  | VDI 2770 Blatt 1:2020 |
| &emsp;&emsp;**DocumentVersions** | Information elements of individual Document Version entities<br><sub>0173-1#02-ABI503#003</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;**(항목)** | Information about a document version entity<br><sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> | 묶음 (9) |  |  |
| &emsp;&emsp;&emsp;&emsp;**Language** | Language style of the document<br><sub>0173-1#02-AAN468#008</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;&emsp;&emsp;(항목) | Language style of the document<br><sub>0173-1#02-AAN468#008</sub> | 문자열 |  | en |
| &emsp;&emsp;&emsp;&emsp;Version | Design that partly deviates from the previous<br><sub>0173-1#02-AAP003#005</sub> | 문자열 |  | 1.0 |
| &emsp;&emsp;&emsp;&emsp;Title | Name of the document<br><sub>0173-1#02-ABG940#003</sub> | 다국어 |  | Die Casting Machine Operating Manual |
| &emsp;&emsp;&emsp;&emsp;Description | Plain text characterizing the content of the document<br><sub>0173-1#02-AAN466#004</sub> | 다국어 |  | Example handover document for the DC-800 die casting machin… |
| &emsp;&emsp;&emsp;&emsp;StatusSetDate | Date when the document status was set<br><sub>0173-1#02-ABI000#003</sub> | 날짜 |  | 2026-06-17 |
| &emsp;&emsp;&emsp;&emsp;StatusValue | Each document version represents a point in time in the document life cycle. This status value refers to the milestones in the document lif…<br><sub>0173-1#02-ABI001#003</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;OrganizationShortName | Short name of the organization<br><sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> | 문자열 |  | ExampleOrg |
| &emsp;&emsp;&emsp;&emsp;OrganizationOfficialName | Official name of the organization of the author of the document<br><sub>0173-1#02-ABI004#003</sub> | 문자열 |  | Example Organization |
| &emsp;&emsp;&emsp;&emsp;**DigitalFiles** | MIME-Type, file name and file contents given by the file SubmodelElement<br><sub>0173-1#02-ABK126#002</sub> | 목록 (1) |  |  |
| &emsp;&emsp;&emsp;&emsp;&emsp;(항목) | MIME-Type, file name and file contents given by the file SubmodelElement<br><sub>0173-1#02-ABK126#002</sub> | 파일 |  | DieCastingMachine_OperatingManual_EN.pdf |
| &emsp;<sub>⋯ 같은 구성의 묶음 4개 더 (항목 96개 생략)</sub> | | | | |

</details>

<details>
<summary><b>TechnicalData</b> · 제조사가 제시하는 기술 사양 · 항목 96개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **GeneralInformation** | General information, for example ordering and manufacturer information<br><sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> | 묶음 (6) |  |  |
| &emsp;ManufacturerName | Legally valid designation of the natural or judicial person which is directly responsible for the design, production, packaging and labelin…<br><sub>0173-1#02-AAO677#004</sub> | 문자열 |  | ExampleCompany |
| &emsp;CompanyLogo | Imagefile for logo of the company provided in common format (.png, .jpg)<br><sub>0173-1#02-ABI776#002</sub> | 파일 |  | CompanyLogo.png |
| &emsp;ManufacturerProductDesignation | Short description of the product (short text)<br><sub>0173-1#02-AAW338#003</sub> | 다국어 |  | ExampleCompany Cold Chamber Die Casting Machine |
| &emsp;ManufacturerArticleNumber | unique product identifier of the manufacturer<br><sub>0173-1#02-AAO676#005</sub> | 문자열 |  | DC-800-ART |
| &emsp;ManufacturerOrderCode | by manufactures issued unique combination of numbers and letters used to identify the device for ordering<br><sub>0173-1#02-AAO227#004</sub> | 문자열 |  | DC-800-ORD |
| &emsp;**ProductImages** | Pictorial representations of the product also related to different applications<br><sub>0173-1#02-ABM220#001</sub> | 목록 (1) |  |  |
| &emsp;&emsp;**(항목)** | Pictorial representation of the product related to an application<br><sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;&emsp;ImageFile | Picture of the product (low resolution) 72 dpi / rgb (GIF or JPG)<br><sub>0173-1#02-ABK291#002</sub> | 파일 |  | CASTINGMACHINE_ProductImage.jpg |
| &emsp;&emsp;&emsp;ImageNote | Notes or explanations about the image provided<br><sub>0173-1#02-ABL423#001</sub> | 다국어 |  | Side view of ExampleCompany cold-chamber die casting machine |
| **ProductClassifications** | Product classifications by association of product classes with common classification systems<br><sub>0173-1#02-ABK162#002</sub> | 목록 (1) |  |  |
| &emsp;**(항목)** | Single product classification item by association with product class in a particular classification system or property dictionary<br><sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;ClassificationSystem | Reference to the scheduled collection of abstract concepts that are used to distinguish and order objects<br><sub>0173-1#02-ABL424#001</sub> | 문자열 |  | ECLASS |
| &emsp;&emsp;ClassificationSystemVersion | Referenced state of the published classification system<br><sub>0173-1#02-AAR710#003</sub> | 문자열 |  | ECLASS 16.0 |
| &emsp;&emsp;ClassificationSystemUrl | Classification system URL<br><sub>ai:IDTA/TechnicalData/ProductClassifications/ProduktClassification/Cl…</sub> | 문자열 |  | https://eclass.eu/eclass-standard/search-content |
| &emsp;&emsp;ProductClassId | Class of the associated product or industrial equipment in the classification system. According to the notation of the system (IRDI)<br><sub>0173-1#02-ABG776#003</sub> | 문자열 |  | 0173-1#01-AKK476#011 |
| &emsp;&emsp;ProductClassCodedName | Unique class code in a classification hierarchy<br><sub>0173-1#02-ABK128#002</sub> | 문자열 |  | 18-07-00-00 |
| &emsp;&emsp;ProductClassName | Name of product class in the used classification system<br><sub>0173-1#02-ABK273#002</sub> | 다국어 |  | Equipment for casting NF metal |
| &emsp;&emsp;ReferenceToTechnicalPropertyArea | Reference to technical property area<br><sub>0173-1#02-ABL358#002</sub> | 참조 |  |  |
| **TechnicalPropertyAreas** | List of all technical property areas<br><sub>0173-1#02-ABK163#002</sub> | 목록 (6) |  |  |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**DieCastingCommonSystem** | Groups common equipment-type characteristics of the die casting machine.<br><sub>sf:DieCastingCommonSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**DieCastingCommonSpecifications** | Common process, configuration, installation and mass specifications.<br><sub>sf:DieCastingCommonSpecifications/1/0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;&emsp;&emsp;CastingProcessType | Type of casting process performed by the equipment.<br><sub>sf:CastingProcessType/1/0</sub> | 문자열 |  | High-pressure die casting (cold chamber) |
| &emsp;&emsp;&emsp;&emsp;DieCastingMachineType | Mechanical configuration of the die casting machine.<br><sub>sf:DieCastingMachineType/1/0</sub> | 문자열 |  | Horizontal cold chamber die casting machine |
| &emsp;&emsp;&emsp;&emsp;CastMetalType | Metal families supported by the equipment type.<br><sub>sf:CastMetalType/1/0</sub> | 문자열 |  | Aluminum and zinc alloys |
| &emsp;&emsp;&emsp;&emsp;SystemConfiguration | Integrated equipment systems included in the reference configuration.<br><sub>sf:SystemConfiguration/1/0</sub> | 문자열 |  | Integrated injection, clamping, hydraulic, cooling and safe… |
| &emsp;&emsp;&emsp;&emsp;InstallationType | Installation arrangement of the equipment.<br><sub>sf:InstallationType/1/0</sub> | 문자열 |  | Floor-mounted stationary equipment |
| &emsp;&emsp;&emsp;&emsp;NetWeight | Net mass of the equipment type.<br><sub>sf:NetWeight/1/0</sub> | 실수 | kg | 42000 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**CastingCapacityAndProductionSystem** | Groups casting capacity and production capability specifications.<br><sub>sf:CastingCapacityAndProductionSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**CastingCapacityAndProductionSpecifications** | Capacity, cycle, shot and alloy-range specifications of the equipment type.<br><sub>sf:CastingCapacityAndProductionSpecifications/1/0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;&emsp;&emsp;ClampingForce | Maximum rated die clamping force.<br><sub>sf:ClampingForce/1/0</sub> | 실수 | kN | 8000 |
| &emsp;&emsp;&emsp;&emsp;MaxShotWeight | Maximum metal mass injected in one shot.<br><sub>sf:MaxShotWeight/1/0</sub> | 실수 | kg | 6.5 |
| &emsp;&emsp;&emsp;&emsp;MaxProjectedArea | Maximum allowable projected casting area.<br><sub>sf:MaxProjectedArea/1/0</sub> | 실수 | cm² | 1600 |
| &emsp;&emsp;&emsp;&emsp;DieCastingCycleTime | Reference duration of one complete casting cycle.<br><sub>sf:DieCastingCycleTime/1/0</sub> | 기간 |  | PT45S |
| &emsp;&emsp;&emsp;&emsp;CastingCyclesPerHour | Reference number of casting cycles per hour.<br><sub>sf:CastingCyclesPerHour/1/0</sub> | 실수 | shots/h | 80 |
| &emsp;&emsp;&emsp;&emsp;ProductionCapacity | Reference daily shot production capacity.<br><sub>sf:ProductionCapacity/1/0</sub> | 실수 | shots/day | 1900 |
| &emsp;&emsp;&emsp;&emsp;CastAlloyRange | Representative alloys supported by the equipment type.<br><sub>sf:CastAlloyRange/1/0</sub> | 문자열 |  | ADC12, A380, Zamak 3/5 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**MoltenMetalAndInjectionSystem** | Groups molten-metal and hydraulic injection specifications.<br><sub>sf:MoltenMetalAndInjectionSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**MoltenMetalAndInjectionSpecifications** | Temperature, pressure, speed, plunger and shot-sleeve specifications.<br><sub>sf:MoltenMetalAndInjectionSpecifications/1/0</sub> | 묶음 (10) |  |  |
| &emsp;&emsp;&emsp;&emsp;MoltenMetalType | Molten-metal material used for the reference configuration.<br><sub>sf:MoltenMetalType/1/0</sub> | 문자열 |  | Aluminum alloy (ADC12) |
| &emsp;&emsp;&emsp;&emsp;MoltenMetalTemperatureRange | Supported molten-metal temperature range.<br><sub>sf:MoltenMetalTemperatureRange/1/0</sub> | 실수 범위 | °C | 640 ~ 700 |
| &emsp;&emsp;&emsp;&emsp;MaxInjectionPressure | Maximum rated injection pressure.<br><sub>sf:MaxInjectionPressure/1/0</sub> | 실수 | bar | 1000 |
| &emsp;&emsp;&emsp;&emsp;InjectionPressureRange | Supported injection-pressure range.<br><sub>sf:InjectionPressureRange/1/0</sub> | 실수 범위 | bar | 300 ~ 1000 |
| &emsp;&emsp;&emsp;&emsp;IntensificationPressure | Reference secondary intensification pressure.<br><sub>sf:IntensificationPressure/1/0</sub> | 실수 | bar | 1050 |
| &emsp;&emsp;&emsp;&emsp;MaxPlungerSpeed | Maximum plunger speed during injection.<br><sub>sf:MaxPlungerSpeed/1/0</sub> | 실수 | m/s | 8 |
| &emsp;&emsp;&emsp;&emsp;PlungerSpeedRange | Supported plunger-speed range.<br><sub>sf:PlungerSpeedRange/1/0</sub> | 실수 범위 | m/s | 0.1 ~ 8 |
| &emsp;&emsp;&emsp;&emsp;PlungerDiameter | Nominal plunger-tip diameter.<br><sub>sf:PlungerDiameter/1/0</sub> | 실수 | mm | 100 |
| &emsp;&emsp;&emsp;&emsp;ShotSleeveLength | Nominal shot-sleeve length.<br><sub>sf:ShotSleeveLength/1/0</sub> | 실수 | mm | 600 |
| &emsp;&emsp;&emsp;&emsp;HydraulicSystemPressure | Rated hydraulic system pressure.<br><sub>sf:HydraulicSystemPressure/1/0</sub> | 실수 | MPa | 16 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**ClampingUnitAndDimensionSystem** | Groups clamping-unit, mechanical envelope and acoustic specifications.<br><sub>sf:ClampingUnitAndDimensionSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**ClampingUnitAndDimensionSpecifications** | Clamping geometry, motion, force, dimensions and sound-power specifications.<br><sub>sf:ClampingUnitAndDimensionSpecifications/1/0</sub> | 묶음 (13) |  |  |
| &emsp;&emsp;&emsp;&emsp;ClampingUnitType | Mechanical type of clamping unit.<br><sub>sf:ClampingUnitType/1/0</sub> | 문자열 |  | Toggle-type clamping unit |
| &emsp;&emsp;&emsp;&emsp;PlatenWidth | Overall width of the machine platen.<br><sub>sf:PlatenWidth/1/0</sub> | 실수 | mm | 1150 |
| &emsp;&emsp;&emsp;&emsp;PlatenHeight | Overall height of the machine platen.<br><sub>sf:PlatenHeight/1/0</sub> | 실수 | mm | 1150 |
| &emsp;&emsp;&emsp;&emsp;TieBarClearanceHorizontal | Clear horizontal distance between tie bars.<br><sub>sf:TieBarClearanceHorizontal/1/0</sub> | 실수 | mm | 820 |
| &emsp;&emsp;&emsp;&emsp;TieBarClearanceVertical | Clear vertical distance between tie bars.<br><sub>sf:TieBarClearanceVertical/1/0</sub> | 실수 | mm | 820 |
| &emsp;&emsp;&emsp;&emsp;DieHeightRange | Supported die-height range.<br><sub>sf:DieHeightRange/1/0</sub> | 실수 범위 | mm | 300 ~ 800 |
| &emsp;&emsp;&emsp;&emsp;DieOpeningStroke | Maximum die-opening stroke.<br><sub>sf:DieOpeningStroke/1/0</sub> | 실수 | mm | 700 |
| &emsp;&emsp;&emsp;&emsp;EjectorForce | Maximum rated ejector force.<br><sub>sf:EjectorForce/1/0</sub> | 실수 | kN | 500 |
| &emsp;&emsp;&emsp;&emsp;EjectorStroke | Maximum ejector stroke.<br><sub>sf:EjectorStroke/1/0</sub> | 실수 | mm | 120 |
| &emsp;&emsp;&emsp;&emsp;DimensionsLength | largest length dimension of an item, including protruding parts<br><sub>0173-1#02-BAB146#011</sub> | 실수 | mm | 8500 |
| &emsp;&emsp;&emsp;&emsp;DimensionsWidth | greatest width expansion of an object, including projecting parts<br><sub>0173-1#02-BAA705#009</sub> | 실수 | mm | 2600 |
| &emsp;&emsp;&emsp;&emsp;DimensionsHeight | largest hight dimension of an item, including projection parts<br><sub>0173-1#02-BAB707#009</sub> | 실수 | mm | 3200 |
| &emsp;&emsp;&emsp;&emsp;SoundPowerLevel | Reference A-weighted sound power level.<br><sub>sf:SoundPowerLevel/1/0</sub> | 실수 | dB(A) | 82 |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**DieCoolingAndSpraySystem** | Groups die cooling, spraying, vacuum and fume-extraction specifications.<br><sub>sf:DieCoolingAndSpraySystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**DieCoolingAndSpraySpecifications** | Cooling, release-agent, vacuum and extraction capabilities.<br><sub>sf:DieCoolingAndSpraySpecifications/1/0</sub> | 묶음 (8) |  |  |
| &emsp;&emsp;&emsp;&emsp;DieCoolingMethod | Method used to cool and regulate the die.<br><sub>sf:DieCoolingMethod/1/0</sub> | 문자열 |  | Closed-loop water cooling with temperature control |
| &emsp;&emsp;&emsp;&emsp;DieCoolingWaterFlowRate | Reference cooling-water volumetric flow rate.<br><sub>sf:DieCoolingWaterFlowRate/1/0</sub> | 실수 | L/min | 60 |
| &emsp;&emsp;&emsp;&emsp;DieTemperatureControlSupported | Indicates whether closed-loop die-temperature control is supported.<br><sub>sf:DieTemperatureControlSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;DieSprayType | Type of automatic die-spray mechanism.<br><sub>sf:DieSprayType/1/0</sub> | 문자열 |  | Automatic reciprocating die spray |
| &emsp;&emsp;&emsp;&emsp;ReleaseAgentSupplyMethod | Method used to supply release agent to the die-spray unit.<br><sub>sf:ReleaseAgentSupplyMethod/1/0</sub> | 문자열 |  | Central pressure-fed supply |
| &emsp;&emsp;&emsp;&emsp;VacuumCastingSupported | Indicates whether vacuum-assisted casting is supported.<br><sub>sf:VacuumCastingSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;FumeExtractionSupported | Indicates whether a fume-extraction connection is supported.<br><sub>sf:FumeExtractionSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;FumeExtractionConnectionSize | Nominal connection size for the fume-extraction duct.<br><sub>sf:FumeExtractionConnectionSize/1/0</sub> | 문자열 |  | Ø250 mm |
| &emsp;**(항목)** | Specific property area referenced by a product classification<br><sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;**ElectricalAndSafetySystem** | Groups electrical ratings and supported equipment safety functions.<br><sub>sf:ElectricalAndSafetySystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;&emsp;&emsp;**ElectricalAndSafetySpecifications** | Power-supply, protection and functional-safety specifications.<br><sub>sf:ElectricalAndSafetySpecifications/1/0</sub> | 묶음 (14) |  |  |
| &emsp;&emsp;&emsp;&emsp;RatedVoltage | Supported line-to-line AC supply-voltage range.<br><sub>sf:RatedVoltage/1/0</sub> | 실수 범위 | V AC | 380 ~ 415 |
| &emsp;&emsp;&emsp;&emsp;PowerSupplyPhase | Number and arrangement of electrical supply phases.<br><sub>sf:PowerSupplyPhase/1/0</sub> | 문자열 |  | 3-phase |
| &emsp;&emsp;&emsp;&emsp;PowerSupplyFrequency | Supported electrical supply frequencies.<br><sub>sf:PowerSupplyFrequency/1/0</sub> | 문자열 | Hz | 50/60 |
| &emsp;&emsp;&emsp;&emsp;RatedPower | Rated active power of the equipment type.<br><sub>sf:RatedPower/1/0</sub> | 실수 | kW | 75 |
| &emsp;&emsp;&emsp;&emsp;MaxRunningCurrent | Maximum current during normal operation.<br><sub>sf:MaxRunningCurrent/1/0</sub> | 실수 | A | 140 |
| &emsp;&emsp;&emsp;&emsp;LeakageBreakerCapacity | Rated current capacity of the earth-leakage circuit breaker.<br><sub>sf:LeakageBreakerCapacity/1/0</sub> | 실수 | A | 200 |
| &emsp;&emsp;&emsp;&emsp;SupportedSafetyFunctions | Safety functions included in the reference configuration.<br><sub>sf:SupportedSafetyFunctions/1/0</sub> | 문자열 |  | Emergency stop, guard interlock, light curtain, two-hand co… |
| &emsp;&emsp;&emsp;&emsp;SafetyGateInterlockSupported | Indicates whether a safety-gate interlock is supported.<br><sub>sf:SafetyGateInterlockSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;TwoHandControlSupported | Indicates whether two-hand control is supported.<br><sub>sf:TwoHandControlSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;EmergencyStopSupported | Indicates whether an emergency-stop function is supported.<br><sub>sf:EmergencyStopSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;OverPressureReliefSupported | Indicates whether hydraulic over-pressure relief is supported.<br><sub>sf:OverPressureReliefSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;LightCurtainSupported | Indicates whether light-curtain protection is supported.<br><sub>sf:LightCurtainSupported/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;&emsp;IPRating | Ingress-protection rating of the equipment enclosure.<br><sub>sf:IPRating/1/0</sub> | 문자열 |  | IP54 |
| &emsp;&emsp;&emsp;&emsp;GroundingRequired | Indicates whether protective grounding is required.<br><sub>sf:GroundingRequired/1/0</sub> | 참/거짓 |  | true |

</details>

<details>
<summary><b>OperationalData</b> · 운전 중 변하는 장비 상태 값 · 항목 52개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **DeviceOperationSystem** | Groups machine-level operating state information.<br><sub>sf:DeviceOperationSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**DeviceOperationMonitoring** | Current machine mode, process identity, shot count and operating timestamps.<br><sub>sf:DeviceOperationMonitoring/1/0</sub> | 묶음 (10) |  |  |
| &emsp;&emsp;DeviceRunState | Current high-level operating state of the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;ActiveProcessId | Identifier of the currently active casting process.<br><sub>sf:ActiveProcessId/1/0</sub> | 문자열 |  | DC-P-001 |
| &emsp;&emsp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;CastingRunState | Current execution state of the casting process.<br><sub>sf:CastingRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;CurrentShotId | Identifier of the current or most recently completed shot.<br><sub>sf:CurrentShotId/1/0</sub> | 문자열 |  | SHOT-2026-0617-1032 |
| &emsp;&emsp;CumulativeShotCount | Cumulative number of casting shots executed.<br><sub>sf:CumulativeShotCount/1/0</sub> | 정수 | shots | 1560000 |
| &emsp;&emsp;CumulativeOperatingHours | Cumulative equipment operating time.<br><sub>sf:CumulativeOperatingHours/1/0</sub> | 실수 | h | 18600 |
| &emsp;&emsp;OperationStartTimestamp | Timestamp at which the current operating period started.<br><sub>sf:OperationStartTimestamp/1/0</sub> | 일시 |  | 2026-06-17T08:00:00+09:00 |
| &emsp;&emsp;LastUpdateTimestamp | Timestamp of the most recent operational-data update.<br><sub>sf:LastUpdateTimestamp/1/0</sub> | 일시 |  | 2026-06-17T08:20:30+09:00 |
| **CastingProcessSystem** | Groups live high-pressure die casting process data.<br><sub>sf:CastingProcessSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**CastingProcessMonitoring** | Current injection, temperature, cycle, throughput and quality measurements.<br><sub>sf:CastingProcessMonitoring/1/0</sub> | 묶음 (13) |  |  |
| &emsp;&emsp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실수 | °C | 675 |
| &emsp;&emsp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실수 | bar | 920 |
| &emsp;&emsp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실수 | bar | 1020 |
| &emsp;&emsp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실수 | m/s | 6.8 |
| &emsp;&emsp;SlowShotSpeedActual | Measured slow-shot plunger speed.<br><sub>sf:SlowShotSpeedActual/1/0</sub> | 실수 | m/s | 0.3 |
| &emsp;&emsp;BiscuitThicknessActual | Measured biscuit thickness after injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실수 | mm | 21 |
| &emsp;&emsp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실수 | °C | 220 |
| &emsp;&emsp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실수 | °C | 45 |
| &emsp;&emsp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;CavityFillTimeActual | Measured time required to fill the die cavity.<br><sub>sf:CavityFillTimeActual/1/0</sub> | 실수 | ms | 45 |
| &emsp;&emsp;CastingThroughputRate | Current number of completed casting shots per hour.<br><sub>sf:CastingThroughputRate/1/0</sub> | 실수 | shots/h | 78 |
| &emsp;&emsp;ShotWeightConsistencyIndex | Normalized consistency index of shot mass.<br><sub>sf:ShotWeightConsistencyIndex/1/0</sub> | 실수 | 1 | 0.97 |
| &emsp;&emsp;CastingRejectRate | Current proportion of rejected castings.<br><sub>sf:CastingRejectRate/1/0</sub> | 실수 | % | 1.8 |
| **ClampingAndHydraulicSystem** | Groups live clamping and hydraulic system data.<br><sub>sf:ClampingAndHydraulicSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**ClampingAndHydraulicMonitoring** | Current force, position, pressure, temperature, pump and spray states.<br><sub>sf:ClampingAndHydraulicMonitoring/1/0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실수 | kN | 7800 |
| &emsp;&emsp;DieOpenPositionActual | Measured die-open position.<br><sub>sf:DieOpenPositionActual/1/0</sub> | 실수 | mm | 0 |
| &emsp;&emsp;EjectorPositionActual | Measured ejector position.<br><sub>sf:EjectorPositionActual/1/0</sub> | 실수 | mm | 0 |
| &emsp;&emsp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실수 | MPa | 15.2 |
| &emsp;&emsp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실수 | °C | 48 |
| &emsp;&emsp;HydraulicPumpRunState | Current hydraulic-pump run state.<br><sub>sf:HydraulicPumpRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;DieSprayStatus | Current operating state of the die-spray unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문자열 |  | Active |
| **ProtectionAndSafetyStateSystem** | Groups protection and machine-safety operating states.<br><sub>sf:ProtectionAndSafetyStateSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**ProtectionAndSafetyStateMonitoring** | Current overload, gate, light-curtain, stop and alarm states.<br><sub>sf:ProtectionAndSafetyStateMonitoring/1/0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;OverPressureAlarmStatus | Current hydraulic over-pressure alarm state.<br><sub>sf:OverPressureAlarmStatus/1/0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;DieOverloadAlarmStatus | Current die-overload alarm state.<br><sub>sf:DieOverloadAlarmStatus/1/0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;LightCurtainStatus | Current light-curtain state.<br><sub>sf:LightCurtainStatus/1/0</sub> | 문자열 |  | Clear |
| &emsp;&emsp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문자열 |  | None |
| **ElectricalAndSafetyConditionSystem** | Groups electrical supply and safety-condition data.<br><sub>sf:ElectricalAndSafetyConditionSystem/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**ElectricalAndSafetyConditionMonitoring** | Current power, supply, emergency-stop, guard and permission states.<br><sub>sf:ElectricalAndSafetyConditionMonitoring/1/0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실수 | W | 58000 |
| &emsp;&emsp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;GuardInterlockStatus | Current guard-interlock state.<br><sub>sf:GuardInterlockStatus/1/0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;SafetyCoverState | Current state of the safety cover.<br><sub>sf:SafetyCoverState/1/0</sub> | 문자열 |  | Closed |
| &emsp;&emsp;OperationPermittedState | Indicates whether machine operation is currently permitted.<br><sub>sf:OperationPermittedState/1/0</sub> | 문자열 |  | Permitted |

</details>

<details>
<summary><b>TimeSeries</b> · 상태 값의 시간별 기록 · 항목 1506개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Metadata** | A set of data describing and providing information about the time series<br><sub>ai:idta/TimeSeries/Metadata/1/1</sub> | 묶음 (3) |  |  |
| &emsp;Name | Meaningful name for labeling<br><sub>ai:idta/TimeSeries/Metadata/Name/1/1</sub> | 다국어 |  | Die casting machine operation time series |
| &emsp;Description | Short description of the time series<br><sub>ai:idta/TimeSeries/Metadata/Description/1/1</sub> | 다국어 |  | Operational signals for the injection, die, hydraulic and s… |
| &emsp;**Record** | A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID. Simil…<br><sub>ai:idta/TimeSeries/Record/1/1</sub> | 묶음 (23) |  |  |
| &emsp;&emsp;Time | Point of Time in seconds. Time points refer to the start time of the time series segment.<br><sub>ai:idta/TimeSeries/RelativePointInTime/1/1</sub> | 정수 | s | 0 |
| &emsp;&emsp;DeviceRunState | Current high-level operating state of the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;CastingRunState | Current execution state of the casting process.<br><sub>sf:CastingRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실수 | °C | 675.00 |
| &emsp;&emsp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실수 | bar | 920.00 |
| &emsp;&emsp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실수 | bar | 1020.00 |
| &emsp;&emsp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실수 | m/s | 6.800 |
| &emsp;&emsp;BiscuitThicknessActual | Measured biscuit thickness after injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실수 | mm | 21.000 |
| &emsp;&emsp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실수 | °C | 220.00 |
| &emsp;&emsp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실수 | °C | 45.00 |
| &emsp;&emsp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실수 | kN | 7800.00 |
| &emsp;&emsp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실수 | MPa | 15.200 |
| &emsp;&emsp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실수 | °C | 48.00 |
| &emsp;&emsp;DieSprayStatus | Current operating state of the die-spray unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문자열 |  | Active |
| &emsp;&emsp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실수 | W | 58000.00 |
| &emsp;&emsp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문자열 |  | None |
| **Segments** | Contains segments of a time series<br><sub>ai:idta/TimeSeries/Segments/1/1</sub> | 묶음 (3) |  |  |
| &emsp;**ExternalSegment** | Reference to a file of data points in sequential order over a period of time<br><sub>ai:idta/TimeSeries/Segments/ExternalSegment/1/1</sub> | 묶음 (12) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다국어 |  | Die casting machine historian file data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다국어 |  | Die casting machine time series data stored in external CSV… |
| &emsp;&emsp;RecordCount | Indicates how many records are present in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정수 |  | 86400 |
| &emsp;&emsp;StartTime | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문자열 |  | 2026-06-17T00:00:00Z |
| &emsp;&emsp;EndTime | <br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문자열 |  | 2026-06-17T23:59:59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문자열 |  | PT24H |
| &emsp;&emsp;SamplingInterval | The time period between two time series records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정수 | s | 1 |
| &emsp;&emsp;SamplingRate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문자열 |  | completed |
| &emsp;&emsp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문자열 |  | 2026-06-18T00:00:05Z |
| &emsp;&emsp;File | Sequence of data points in sequential order over a period of time within a paged data file<br><sub>ai:idta/TimeSeries/File/1/1</sub> | 파일 |  | DC_TS_20260617.csv |
| &emsp;&emsp;Blob | Sequence of data points in sequential order over a period of time within a BLOB<br><sub>ai:idta/TimeSeries/Blob/1/1</sub> | 내장 데이터 |  |  |
| &emsp;**LinkedSegment** | Reference to an endpoint of data points in sequential order over a period of time<br><sub>ai:idta/TimeSeries/Segments/LinkedSegment/1/1</sub> | 묶음 (12) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다국어 |  | Die casting machine historian API data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다국어 |  | Die casting machine time series data queried from external … |
| &emsp;&emsp;RecordCount | Indicates how many records are present in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정수 |  | 86400 |
| &emsp;&emsp;StartTime | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문자열 |  | 2026-06-17T00:00:00Z |
| &emsp;&emsp;EndTime | <br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문자열 |  | 2026-06-17T23:59:59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문자열 |  | PT24H |
| &emsp;&emsp;SamplingInterval | The time period between two time series records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정수 | s | 1 |
| &emsp;&emsp;SamplingRate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문자열 |  | completed |
| &emsp;&emsp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문자열 |  | 2026-06-18T00:00:05Z |
| &emsp;&emsp;Endpoint | Specifies a location of a resource on an API server through which time series can be requested<br><sub>ai:idta/TimeSeries/Endpoint/1/1</sub> | 문자열 |  | https://historian.example.com/api/timeseries |
| &emsp;&emsp;Query | generic query component to read time series data from an API<br><sub>ai:idta/TimeSeries/Query/1/1</sub> | 문자열 |  | assetId=DC-SN-2026-0001&amp;from=2026-06-17T00:00:00Z&amp;to=2026-0… |
| &emsp;**InternalSegment** | Grouped sequence of data points in successive order over a specified period of time<br><sub>ai:idta/TimeSeries/Segments/InternalSegment/1/1</sub> | 묶음 (11) |  |  |
| &emsp;&emsp;Name | Meaningful name for labeling.<br><sub>ai:idta/TimeSeries/Segment/Name/1/1</sub> | 다국어 |  | Recent die casting machine operation data |
| &emsp;&emsp;Description | Short description of the time series segment.<br><sub>ai:idta/TimeSeries/Segment/Description/1/1</sub> | 다국어 |  | Recent die casting machine operation records stored directl… |
| &emsp;&emsp;RecordCount | Indicates how many records are present in a segment.<br><sub>ai:idta/TimeSeries/Segment/RecordCount/1/1</sub> | 정수 |  | 60 |
| &emsp;&emsp;StartTime | Contains the first recorded timestamp of the time series segment and thus represents the beginning of a time series. Time format and scale …<br><sub>ai:idta/TimeSeries/Segment/StartTime/1/1</sub> | 문자열 |  | 2026-06-17T08:15:00Z |
| &emsp;&emsp;EndTime | Contains the last recorded timestamp of the time series segment and thus represents the end of a time series. Time format and scale corresp…<br><sub>ai:idta/TimeSeries/Segment/EndTime/1/1</sub> | 문자열 |  | 2026-06-17T08:15:59Z |
| &emsp;&emsp;Duration | Period covered by the segment, represented according to ISO 8601 by the format P[n]Y[n]M[n]DT[n]H[n]M[n]S<br><sub>ai:idta/TimeSeries/Segment/Duration/1/1</sub> | 문자열 |  | PT1M |
| &emsp;&emsp;SamplingInterval | The time period between two time series records (Length of cycle).<br><sub>ai:idta/TimeSeries/Segment/SamplingInterval/1/1</sub> | 정수 | s | 1 |
| &emsp;&emsp;SamplingRate | Defines the number of samples per second for a regular time series in Hz.<br><sub>ai:idta/TimeSeries/Segment/SamplingRate/1/1</sub> | 정수 | Hz | 1 |
| &emsp;&emsp;State | State of the time series related to its progress<br><sub>ai:idta/TimeSeries/Segment/State/1/1</sub> | 문자열 |  | completed |
| &emsp;&emsp;LastUpdate | Time of the last chance<br><sub>ai:idta/TimeSeries/Segment/LastUpdate/1/1</sub> | 문자열 |  | 2026-06-17T08:16:00Z |
| &emsp;&emsp;**Records** | Group of data points in successive order over a specified period of time<br><sub>ai:idta/TimeSeries/Records/1/1</sub> | 묶음 (60) |  |  |
| &emsp;&emsp;&emsp;**Record__0000__** | A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID. Simil…<br><sub>ai:idta/TimeSeries/Record/1/1</sub> | 묶음 (23) |  |  |
| &emsp;&emsp;&emsp;&emsp;Time | Point of Time in seconds. Time points refer to the start time of the time series segment.<br><sub>ai:idta/TimeSeries/RelativePointInTime/1/1</sub> | 정수 | s | 0 |
| &emsp;&emsp;&emsp;&emsp;DeviceRunState | Current high-level operating state of the equipment.<br><sub>sf:DeviceRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;&emsp;&emsp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;&emsp;&emsp;CastingPhase | Current phase of the die casting cycle.<br><sub>sf:CastingPhase/1/0</sub> | 문자열 |  | Injection |
| &emsp;&emsp;&emsp;&emsp;CastingRunState | Current execution state of the casting process.<br><sub>sf:CastingRunState/1/0</sub> | 문자열 |  | Running |
| &emsp;&emsp;&emsp;&emsp;MoltenMetalTemperatureActual | Measured molten-metal temperature.<br><sub>sf:MoltenMetalTemperatureActual/1/0</sub> | 실수 | °C | 675.00 |
| &emsp;&emsp;&emsp;&emsp;InjectionPressureActual | Measured injection pressure.<br><sub>sf:InjectionPressureActual/1/0</sub> | 실수 | bar | 920.00 |
| &emsp;&emsp;&emsp;&emsp;IntensificationPressureActual | Measured intensification pressure.<br><sub>sf:IntensificationPressureActual/1/0</sub> | 실수 | bar | 1020.00 |
| &emsp;&emsp;&emsp;&emsp;PlungerSpeedActual | Measured fast-shot plunger speed.<br><sub>sf:PlungerSpeedActual/1/0</sub> | 실수 | m/s | 6.800 |
| &emsp;&emsp;&emsp;&emsp;BiscuitThicknessActual | Measured biscuit thickness after injection.<br><sub>sf:BiscuitThicknessActual/1/0</sub> | 실수 | mm | 21.000 |
| &emsp;&emsp;&emsp;&emsp;DieTemperatureActual | Measured die temperature.<br><sub>sf:DieTemperatureActual/1/0</sub> | 실수 | °C | 220.00 |
| &emsp;&emsp;&emsp;&emsp;DieCoolingWaterTempActual | Measured die-cooling water temperature.<br><sub>sf:DieCoolingWaterTempActual/1/0</sub> | 실수 | °C | 45.00 |
| &emsp;&emsp;&emsp;&emsp;CycleTimeActual | Measured duration of one casting cycle.<br><sub>sf:CycleTimeActual/1/0</sub> | 기간 |  | PT44S |
| &emsp;&emsp;&emsp;&emsp;ClampingForceActual | Measured clamping force.<br><sub>sf:ClampingForceActual/1/0</sub> | 실수 | kN | 7800.00 |
| &emsp;&emsp;&emsp;&emsp;HydraulicPressureActual | Measured hydraulic system pressure.<br><sub>sf:HydraulicPressureActual/1/0</sub> | 실수 | MPa | 15.200 |
| &emsp;&emsp;&emsp;&emsp;HydraulicOilTemperatureActual | Measured hydraulic-oil temperature.<br><sub>sf:HydraulicOilTemperatureActual/1/0</sub> | 실수 | °C | 48.00 |
| &emsp;&emsp;&emsp;&emsp;DieSprayStatus | Current operating state of the die-spray unit.<br><sub>sf:DieSprayStatus/1/0</sub> | 문자열 |  | Active |
| &emsp;&emsp;&emsp;&emsp;PowerConsumptionActual | Measured electrical power consumption.<br><sub>sf:PowerConsumptionActual/1/0</sub> | 실수 | W | 58000.00 |
| &emsp;&emsp;&emsp;&emsp;ElectricalSupplyStatus | Current electrical-supply state.<br><sub>sf:ElectricalSupplyStatus/1/0</sub> | 문자열 |  | Normal |
| &emsp;&emsp;&emsp;&emsp;EmergencyStopStatus | Current emergency-stop state.<br><sub>sf:EmergencyStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;SafetyGateInterlockStatus | Current safety-gate interlock state.<br><sub>sf:SafetyGateInterlockStatus/1/0</sub> | 문자열 |  | Locked |
| &emsp;&emsp;&emsp;&emsp;ProtectionStopStatus | Current protective-stop state.<br><sub>sf:ProtectionStopStatus/1/0</sub> | 문자열 |  | Released |
| &emsp;&emsp;&emsp;&emsp;CastingAlarmStatus | Current active casting alarm state.<br><sub>sf:CastingAlarmStatus/1/0</sub> | 문자열 |  | None |
| &emsp;&emsp;&emsp;<sub>⋯ 같은 구성의 묶음 59개 더 (항목 1416개 생략)</sub> | | | | |

</details>

<details>
<summary><b>ProcessParameters</b> · 제품·공정별 설정값 · 항목 41개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **Processes** | Provides all the necessary parameters of processes in a structured form that are required to manufacture a product<br><sub>ai:idta/ProcessParameters/Processes/1/0</sub> | 묶음 (1) |  |  |
| &emsp;**Process__00__** | The processes to be executed are described individually in the SMC Process.<br><sub>ai:idta/ProcessParameters/Process/1/0</sub> | 묶음 (8) |  |  |
| &emsp;&emsp;ProcessId | Describes the ID of the process<br><sub>ai:idta/ProcessParameters/ProcessId/1/0</sub> | 문자열 |  | DC-P-001 |
| &emsp;&emsp;ProcessName | Describes the Name of the Process<br><sub>ai:idta/ProcessParameters/ProcessName/1/0</sub> | 문자열 |  | High-pressure die casting |
| &emsp;&emsp;ProcessDescription | Describes the process.<br><sub>ai:idta/ProcessParameters/ProcessDescription/1/0</sub> | 다국어 |  | Process parameters for high-pressure die casting shot opera… |
| &emsp;&emsp;PlannedProcessTime | Planned processing time for process execution (without set-up time)<br><sub>ai:idta/ProcessParameters/PlannedProcessTime/1/0</sub> | 기간 |  | PT45S |
| &emsp;&emsp;**ProductParameters** | Mandatory product parameters for process execution<br><sub>ai:idta/ProcessParameters/ProductParameters/1/0</sub> | 묶음 (6) |  |  |
| &emsp;&emsp;&emsp;CastAlloyType | Alloy selected for the casting process.<br><sub>sf:CastAlloyType/1/0</sub> | 문자열 |  | Aluminum alloy ADC12 |
| &emsp;&emsp;&emsp;MoltenMetalTargetTemperature | Target molten-metal temperature before injection.<br><sub>sf:MoltenMetalTargetTemperature/1/0</sub> | 실수 | °C | 680 |
| &emsp;&emsp;&emsp;PartNetWeight | Target net mass of one cast part.<br><sub>sf:PartNetWeight/1/0</sub> | 실수 | kg | 3.8 |
| &emsp;&emsp;&emsp;ShotWeight | Target total shot mass including runners and overflows.<br><sub>sf:ShotWeight/1/0</sub> | 실수 | kg | 5.2 |
| &emsp;&emsp;&emsp;CavityCount | Number of cavities in the die.<br><sub>sf:CavityCount/1/0</sub> | 정수 |  | 2 |
| &emsp;&emsp;&emsp;TargetProductionQuantity | Target number of casting shots for the production order.<br><sub>sf:TargetProductionQuantity/1/0</sub> | 정수 | shots | 1900 |
| &emsp;&emsp;**ProcessParameters** | Mandatory process parameters for process execution<br><sub>ai:idta/ProcessParameters/ProcessParameters/1/0</sub> | 묶음 (15) |  |  |
| &emsp;&emsp;&emsp;OperationRecipeId | Identifier of the die casting process recipe.<br><sub>sf:OperationRecipeId/1/0</sub> | 문자열 |  | RECIPE-DC-001 |
| &emsp;&emsp;&emsp;OperationMode | Selected machine operating mode.<br><sub>sf:OperationMode/1/0</sub> | 문자열 |  | Automatic casting |
| &emsp;&emsp;&emsp;ProcessStepSequence | Ordered sequence of process steps in one casting cycle.<br><sub>sf:ProcessStepSequence/1/0</sub> | 문자열 |  | Mold close &gt; Molten metal dosing &gt; Slow shot &gt; Fast shot &gt; … |
| &emsp;&emsp;&emsp;SlowShotSpeedSetpoint | Target plunger speed during the slow-shot phase.<br><sub>sf:SlowShotSpeedSetpoint/1/0</sub> | 실수 | m/s | 0.3 |
| &emsp;&emsp;&emsp;FastShotSpeedSetpoint | Target plunger speed during the fast-shot phase.<br><sub>sf:FastShotSpeedSetpoint/1/0</sub> | 실수 | m/s | 6.5 |
| &emsp;&emsp;&emsp;ShotChangeoverPosition | Plunger position at the slow-to-fast-shot transition.<br><sub>sf:ShotChangeoverPosition/1/0</sub> | 실수 | mm | 350 |
| &emsp;&emsp;&emsp;InjectionPressureSetpoint | Target injection pressure.<br><sub>sf:InjectionPressureSetpoint/1/0</sub> | 실수 | bar | 900 |
| &emsp;&emsp;&emsp;IntensificationPressureSetpoint | Target intensification pressure.<br><sub>sf:IntensificationPressureSetpoint/1/0</sub> | 실수 | bar | 1050 |
| &emsp;&emsp;&emsp;ClampingForceSetpoint | Target die clamping force.<br><sub>sf:ClampingForceSetpoint/1/0</sub> | 실수 | kN | 8000 |
| &emsp;&emsp;&emsp;DieTemperatureSetpoint | Target die temperature.<br><sub>sf:DieTemperatureSetpoint/1/0</sub> | 실수 | °C | 220 |
| &emsp;&emsp;&emsp;HoldTime | Target pressure-holding duration.<br><sub>sf:HoldTime/1/0</sub> | 기간 |  | PT3S |
| &emsp;&emsp;&emsp;InDieCoolingTime | Target cooling duration before die opening.<br><sub>sf:InDieCoolingTime/1/0</sub> | 기간 |  | PT8S |
| &emsp;&emsp;&emsp;DieSprayTime | Target die-spray duration.<br><sub>sf:DieSprayTime/1/0</sub> | 기간 |  | PT2S |
| &emsp;&emsp;&emsp;BiscuitThicknessSetpoint | Target biscuit thickness.<br><sub>sf:BiscuitThicknessSetpoint/1/0</sub> | 실수 | mm | 20 |
| &emsp;&emsp;&emsp;OverPressureAlarmThreshold | Injection-pressure threshold for an over-pressure alarm.<br><sub>sf:OverPressureAlarmThreshold/1/0</sub> | 실수 | bar | 1150 |
| &emsp;&emsp;**ResourceParameters** | Mandatory resource parameters for process execution<br><sub>ai:idta/ProcessParameters/ResourceParameters/1/0</sub> | 묶음 (7) |  |  |
| &emsp;&emsp;&emsp;RequiredMoltenMetalTempSensor | Temperature sensor required to execute the casting process.<br><sub>sf:RequiredMoltenMetalTempSensor/1/0</sub> | 문자열 |  | MetalTempSensor01 |
| &emsp;&emsp;&emsp;RequiredInjectionPressureSensor | Injection-pressure sensor required to execute the casting process.<br><sub>sf:RequiredInjectionPressureSensor/1/0</sub> | 문자열 |  | InjectionPressureSensor01 |
| &emsp;&emsp;&emsp;RequiredPlungerPositionSensor | Plunger-position sensor required to execute the casting process.<br><sub>sf:RequiredPlungerPositionSensor/1/0</sub> | 문자열 |  | PlungerPositionSensor01 |
| &emsp;&emsp;&emsp;RequiredShotCylinder | Shot-cylinder resource required to execute the casting process.<br><sub>sf:RequiredShotCylinder/1/0</sub> | 문자열 |  | ShotCylinder01 |
| &emsp;&emsp;&emsp;RequiredClampingUnit | Clamping-unit resource required to execute the casting process.<br><sub>sf:RequiredClampingUnit/1/0</sub> | 문자열 |  | ToggleClampingUnit01 |
| &emsp;&emsp;&emsp;RequiredDieSprayUnit | Die-spray resource required to execute the casting process.<br><sub>sf:RequiredDieSprayUnit/1/0</sub> | 문자열 |  | DieSprayUnit01 |
| &emsp;&emsp;&emsp;RequiredHydraulicPump | Hydraulic-pump resource required to execute the casting process.<br><sub>sf:RequiredHydraulicPump/1/0</sub> | 문자열 |  | HydraulicPump01 |
| &emsp;&emsp;**ProcessBoM** | Describes the products or semi-finished products to be involved in the process<br><sub>ai:idta/ProcessParameters/ProcessBoM/1/0</sub> | 묶음 (3) |  |  |
| &emsp;&emsp;&emsp;MoltenMetalConsumable | Controlled identifier of the molten-metal consumable.<br><sub>sf:MoltenMetalConsumable/1/0</sub> | 문자열 |  | AL-ADC12-INGOT-001 |
| &emsp;&emsp;&emsp;ReleaseAgentConsumable | Controlled identifier of the release-agent consumable.<br><sub>sf:ReleaseAgentConsumable/1/0</sub> | 문자열 |  | RELEASE-AGENT-001 |
| &emsp;&emsp;&emsp;HydraulicOil | Controlled identifier of the hydraulic oil used by the equipment.<br><sub>sf:HydraulicOil/1/0</sub> | 문자열 |  | HYD-OIL-001 |

</details>

<details>
<summary><b>PredictiveMaintenance</b> · 예지정비 모델과 결과 · 항목 91개</summary>

| 항목 | 설명 · 의미 ID | 형식 | 단위 | 예시값 |
|---|---|---|---|---|
| **RemainingUsefulLifePrediction** | Information about remaining useful life (RUL) prediction in the context of predictive maintenance<br><sub>ai:idta/PredictiveMaintenance/RemainingUsefulLifePrediction/1/0</sub> | 묶음 (7) |  |  |
| &emsp;**RemainingUsefulLifetime** | Remaining useful life time, bades on Lifetime model of OPC Foundation (https://reference.opcfoundation.org/DI/v104/docs/10)<br><sub>ai:idta/PredictiveMaintenance/RemainingUsefulLifetime/1/0</sub> | 개체 (6) |  |  |
| &emsp;&emsp;IndicationType | Type of wear-relevant duration, e.g. time, cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/IndicationType/1/0</sub> | 문자열 |  | OperatingHours |
| &emsp;&emsp;DurationValue | Value of duration in the wear relevant unit, e.g. time, operation cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/DurationValue/1/0</sub> | 실수 |  | 9000 |
| &emsp;&emsp;EngineeringUnit | Wear relevant physical unit, e.g. time, operation cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> | 문자열 |  | h |
| &emsp;&emsp;StartValue | Starting value from which the duration is measured in the wear-relevant unit, e.g. time, cycles, distance, etc.<br><sub>ai:idta/PredictiveMaintenance/StartValue/1/0</sub> | 실수 |  | 9000 |
| &emsp;&emsp;StartDateTime | Start date and time from which the duration is measured<br><sub>ai:idta/PredictiveMaintenance/StartDateTime/1/0</sub> | 일시 |  | 2026-06-26T09:00:00+09:00 |
| &emsp;&emsp;Description | Description of the wear duration information<br><sub>ai:idta/PredictiveMaintenance/Description/1/0</sub> | 문자열 |  | Estimated remaining operating time for the shot sleeve and … |
| &emsp;RemainingUsfulLifeDateTime | mark attributed to an instant by means of a specified timescale, expressed as a date and a time<br><sub>ai:idta/PredictiveMaintenance/RemainingUsfulLifeDateTime/1/0</sub> | 일시 |  | 2027-07-15T09:00:00+09:00 |
| &emsp;ConfidenceInterval | confidence interval, measured in the unit of the predicted value<br><sub>ai:idta/PredictiveMaintenance/ConfidenceInterval/1/0</sub> | 실수 범위 |  | 7800 ~ 10500 |
| &emsp;**ListRULBoundaryConditions** | List of boundary conditions for which remaining useful life has been predicted<br><sub>ai:idta/PredictiveMaintenance/ListRULBoundaryConditions/1/0</sub> | 목록 (7) |  |  |
| &emsp;&emsp;**(항목)** | Boundary condition for which remaining useful life has been predicted<br><sub>ai:idta/PredictiveMaintenance/RULCondition/1/0</sub> | 묶음 (9) |  |  |
| &emsp;&emsp;&emsp;ConditionName | Name of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL prediction is v…<br><sub>ai:idta/PredictiveMaintenance/ConditionName/1/0</sub> | 문자열 |  | HydraulicPumpCurrentActual |
| &emsp;&emsp;&emsp;IsBoundaryConditionUsedInModel | If this boundary condition is used in the model for RUL prediction true, else false<br><sub>ai:idta/PredictiveMaintenance/IsBoundaryConditionUsedInModel/1/0</sub> | 참/거짓 |  | true |
| &emsp;&emsp;&emsp;BoundaryValueRange | Value range of the indicator (process value, KPI, material property, asset property) describing a boundary condition for which RUL predicti…<br><sub>ai:idta/PredictiveMaintenance/BoundaryValueRange/1/0</sub> | 실수 |  | 96 |
| &emsp;&emsp;&emsp;BoundaryEngineeringUnit | Engineering Unit of the boundary condition indicator<br><sub>ai:idta/PredictiveMaintenance/BoundaryEngineeringUnit/1/0</sub> | 문자열 |  | A |
| &emsp;&emsp;&emsp;DriftInfoAIModel | Drift information of AI model<br><sub>ai:idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> | 실수 범위 |  | 0.07 ~ 0.07 |
| &emsp;&emsp;&emsp;MeanValue | Mean value of the distribution of indicator values<br><sub>ai:idta/PredictiveMaintenance/MeanValue/1/0</sub> | 실수 |  | 96 |
| &emsp;&emsp;&emsp;Standarddeviation | Standard deviation of the distribution of indicator values<br><sub>ai:idta/PredictiveMaintenance/Standarddeviation/1/0</sub> | 실수 |  | 10 |
| &emsp;&emsp;&emsp;Skewness | Skewness of the distribution of indicator values<br><sub>ai:idta/PredictiveMaintenance/Skewness/1/0</sub> | 실수 |  | 0.4 |
| &emsp;&emsp;&emsp;BoundaryDescription | Description of the boundary of a RUL prediction condition<br><sub>ai:idta/PredictiveMaintenance/BoundaryDescription/1/0</sub> | 문자열 |  | Hydraulic pump current window used to identify sustained ov… |
| &emsp;&emsp;<sub>⋯ 같은 구성의 묶음 6개 더 (항목 60개 생략)</sub> | | | | |
| &emsp;**PredictionModelInformation** | Information about the model for RUL prediction relevant in the context of predictive maintenance<br><sub>ai:idta/PredictiveMaintenance/PredictionModelInformation/1/0</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;ModelType | Model type as an enumerated value: physical based methods, data-driven methods, hybrid methods<br><sub>ai:idta/PredictiveMaintenance/ModelType/1/0</sub> | 문자열 |  | ModelTypeHybrid |
| &emsp;&emsp;ModelDescription | More detailed description of the model type used for RUL prediction (optional)<br><sub>ai:idta/PredictiveMaintenance/ModelDescription/1/0</sub> | 문자열 |  | Hybrid physics- and data-driven RUL model. Feature importan… |
| &emsp;**ListPreAlerts** | List for defining pre-alerts which should be raised before remaining useful life is exceeded<br><sub>ai:idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> | 목록 (1) |  |  |
| &emsp;&emsp;**(항목)** | Definition of a pre-alert which should be raised before remaining useful life is exceeded<br><sub>ai:idta/PredictiveMaintenance/PreAlerts/1/0</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;&emsp;PreAlertMessage | Message to be displayed when alarm regarding predicted remaining useful life is raised<br><sub>ai:idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> | 문자열 |  | Inspect the shot sleeve, plunger tip and hydraulic pump bef… |
| &emsp;&emsp;&emsp;PreAlertValue | Pre-warning duration in wear relevant unit before remaining useful life is exceeded<br><sub>ai:idta/PredictiveMaintenance/PreAlertValue/1/0</sub> | 실수 |  | 1200 |
| &emsp;**AlertAfterExceedingRemainingUsableLife** | Alert information which should be triggered or displayed after exceeding remaining useful life<br><sub>ai:idta/PredictiveMaintenance/AlertAfterExceedingRemainingUsableLife/…</sub> | 묶음 (2) |  |  |
| &emsp;&emsp;AlertMessage | Message to be displayed when alarm regarding predicted remaining useful life is raised<br><sub>ai:idta/PredictiveMaintenance/AlertMessage/1/0</sub> | 문자열 |  | Maintenance is required after the remaining useful life of … |
| &emsp;&emsp;MaintenanceRequired | Maintenance required<br><sub>ai:idta/PredictiveMaintenance/MaintenanceRequired/1/0</sub> | 참/거짓 |  | false |

</details>
