D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 70
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 2: 0x0000 (Success)
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 70
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released
192.168.1.217 - - [10/Jul/2024 15:50:40] "POST / HTTP/1.1" 200 -
=====================
(0008, 0050) Accession Number                    SH: '*'
(0008, 0090) Referring Physician's Name          PN: 'Dr^SURYA^WIJAYA^SPPD'
(0008, 1030) Study Description                   LO: 'ok'
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0010, 1030) Patient's Weight                    DS: '60.0'
(0020, 000d) Study Instance UID                  UI: 112
(0020, 0010) Study ID                            SH: '1'
(0032, 1060) Requested Procedure Description     LO: '*'
(0038, 0050) Special Needs                       LO: '*'
(0040, 0009) Scheduled Procedure Step ID         SH: '112'
(0040, 0100)  Scheduled Procedure Step Sequence  1 item(s) ----
   (0008, 0060) Modality                            CS: 'MR'
   (0040, 0001) Scheduled Station AE Title          AE: 'MRC26266'
   (0040, 0002) Scheduled Procedure Step Start Date DA: '20240710'
   (0040, 0006) Scheduled Performing Physician's Na PN: '*'
   (0040, 0011) Scheduled Procedure Step Location   SH: '*'
   (0040, 0012) Pre-Medication                      LO: '*'
   ---------
(0040, 1001) Requested Procedure ID              SH: '*'
=====================
=====================
(0008, 0050) Accession Number                    SH: '*'
(0008, 0090) Referring Physician's Name          PN: 'Dr^NICO^LIE^SPOT'
(0008, 1030) Study Description                   LO: 'ok'
(0010, 0010) Patient's Name                      PN: 'ELIZABETH^JESSAMINE^DJA'
(0010, 0020) Patient ID                          LO: '10354267'
(0010, 0030) Patient's Birth Date                DA: '19991025'
(0010, 0040) Patient's Sex                       CS: 'F'
(0010, 1030) Patient's Weight                    DS: '60.0'
(0020, 000d) Study Instance UID                  UI: 113
(0020, 0010) Study ID                            SH: '2'
(0032, 1060) Requested Procedure Description     LO: '*'
(0038, 0050) Special Needs                       LO: '*'
(0040, 0009) Scheduled Procedure Step ID         SH: '113'
(0040, 0100)  Scheduled Procedure Step Sequence  1 item(s) ----
   (0008, 0060) Modality                            CS: 'MR'
   (0040, 0001) Scheduled Station AE Title          AE: 'MRC26266'
   (0040, 0002) Scheduled Procedure Step Start Date DA: '20240710'
   (0040, 0006) Scheduled Performing Physician's Na PN: '*'
   (0040, 0011) Scheduled Procedure Step Location   SH: '*'
   (0040, 0012) Pre-Medication                      LO: '*'
   ---------
(0040, 1001) Requested Procedure ID              SH: '*'
=====================
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Worklist Information Model - FIND
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Worklist Information Model - FIND
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
D: ========================== INCOMING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RQ
D: Message ID                    : 71
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Priority                      : Medium
D: ============================ END DIMSE MESSAGE =============================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
I: Find SCP Request Identifier:
I:
I: # DICOM Dataset
I: (0008,0005) CS (no value available)                     # 0 SpecificCharacterSet
I: (0008,0050) SH (no value available)                     # 0 AccessionNumber
I: (0008,0080) LO (no value available)                     # 0 InstitutionName
I: (0008,0081) ST (no value available)                     # 0 InstitutionAddress
I: (0008,0082) SQ (Sequence with 0 items)                  # 0 InstitutionCodeSequence
I: (0008,0090) PN (no value available)                     # 0 ReferringPhysicianName
I: (0008,1080) LO (no value available)                     # 0 AdmittingDiagnosesDescription
I: (0008,1110) SQ (Sequence with 0 items)                  # 0 ReferencedStudySequence
I: (0008,1120) SQ (Sequence with 0 items)                  # 0 ReferencedPatientSequence
I: (0008,1125) SQ (Sequence with 0 items)                  # 0 ReferencedVisitSequence
I: (0010,0010) PN (no value available)                     # 0 PatientName
I: (0010,0020) LO (no value available)                     # 0 PatientID
I: (0010,0021) LO (no value available)                     # 0 IssuerOfPatientID
I: (0010,0030) DA (no value available)                     # 0 PatientBirthDate
I: (0010,0032) TM (no value available)                     # 0 PatientBirthTime
I: (0010,0040) CS (no value available)                     # 0 PatientSex
I: (0010,0050) SQ (Sequence with 0 items)                  # 0 PatientInsurancePlanCodeSequence
I: (0010,1000) LO (no value available)                     # 0 OtherPatientIDs
I: (0010,1001) PN (no value available)                     # 0 OtherPatientNames
I: (0010,1005) PN (no value available)                     # 0 PatientBirthName
I: (0010,1010) AS (no value available)                     # 0 PatientAge
I: (0010,1020) DS (no value available)                     # 0 PatientSize
I: (0010,1030) DS (no value available)                     # 0 PatientWeight
I: (0010,1040) LO (no value available)                     # 0 PatientAddress
I: (0010,1060) PN (no value available)                     # 0 PatientMotherBirthName
I: (0010,1080) LO (no value available)                     # 0 MilitaryRank
I: (0010,1081) LO (no value available)                     # 0 BranchOfService
I: (0010,1090) LO (no value available)                     # 0 MedicalRecordLocator
I: (0010,2000) LO (no value available)                     # 0 MedicalAlerts
I: (0010,2110) LO (no value available)                     # 0 Allergies
I: (0010,2150) LO (no value available)                     # 0 CountryOfResidence
I: (0010,2152) LO (no value available)                     # 0 RegionOfResidence
I: (0010,2154) SH (no value available)                     # 0 PatientTelephoneNumbers
I: (0010,2160) SH (no value available)                     # 0 EthnicGroup
I: (0010,2180) SH (no value available)                     # 0 Occupation
I: (0010,21A0) CS (no value available)                     # 0 SmokingStatus
I: (0010,21B0) LT (no value available)                     # 0 AdditionalPatientHistory
I: (0010,21C0) US (no value available)                     # 0 PregnancyStatus
I: (0010,21D0) DA (no value available)                     # 0 LastMenstrualDate
I: (0010,21F0) LO (no value available)                     # 0 PatientReligiousPreference
I: (0010,4000) LT (no value available)                     # 0 PatientComments
I: (0020,000D) UI (no value available)                     # 0 StudyInstanceUID
I: (0032,1032) PN (no value available)                     # 0 RequestingPhysician
I: (0032,1033) LO (no value available)                     # 0 RequestingService
I: (0032,1060) LO (no value available)                     # 0 RequestedProcedureDescription
I: (0032,1064) SQ (Sequence with 0 items)                  # 0 RequestedProcedureCodeSequence
I: (0038,0004) SQ (Sequence with 0 items)                  # 0 ReferencedPatientAliasSequence
I: (0038,0008) CS (no value available)                     # 0 VisitStatusID
I: (0038,0010) LO (no value available)                     # 0 AdmissionID
I: (0038,0011) LO (no value available)                     # 0 IssuerOfAdmissionID
I: (0038,0050) LO (no value available)                     # 0 SpecialNeeds
I: (0038,0300) LO (no value available)                     # 0 CurrentPatientLocation
I: (0038,0400) LO (no value available)                     # 0 PatientInstitutionResidence
I: (0038,0500) LO (no value available)                     # 0 PatientState
I: (0038,4000) LT (no value available)                     # 0 VisitComments
I: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
I:   (Sequence item #1)
I:     (0008,0060) CS [MR]                                     # 1 Modality
I:     (0032,1070) LO (no value available)                     # 0 RequestedContrastAgent
I:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
I:     (0040,0002) DA [20240710]                               # 1 ScheduledProcedureStepStartDate
I:     (0040,0003) TM [000000-235959]                          # 1 ScheduledProcedureStepStartTime
I:     (0040,0004) DA (no value available)                     # 0 ScheduledProcedureStepEndDate
I:     (0040,0005) TM (no value available)                     # 0 ScheduledProcedureStepEndTime
I:     (0040,0006) PN (no value available)                     # 0 ScheduledPerformingPhysicianName
I:     (0040,0007) LO (no value available)                     # 0 ScheduledProcedureStepDescription
I: (0040,0008) SQ (Sequence with 0 items)                  # 0 ScheduledProtocolCodeSequence
I:     (0040,0009) SH (no value available)                     # 0 ScheduledProcedureStepID
I:     (0040,0010) SH (no value available)                     # 0 ScheduledStationName
I:     (0040,0011) SH (no value available)                     # 0 ScheduledProcedureStepLocation
I:     (0040,0012) LO (no value available)                     # 0 PreMedication
I:     (0040,0020) CS (no value available)                     # 0 ScheduledProcedureStepStatus
I:     (0040,0400) LT (no value available)                     # 0 CommentsOnTheScheduledProcedureStep
I: (0040,1001) SH (no value available)                     # 0 RequestedProcedureID
I: (0040,1002) LO (no value available)                     # 0 ReasonForTheRequestedProcedure
I: (0040,1003) SH (no value available)                     # 0 RequestedProcedurePriority
I: (0040,1004) LO (no value available)                     # 0 PatientTransportArrangements
I: (0040,1005) LO (no value available)                     # 0 RequestedProcedureLocation
I: (0040,1008) LO (no value available)                     # 0 ConfidentialityCode
I: (0040,1009) SH (no value available)                     # 0 ReportingPriority
I: (0040,1010) PN (no value available)                     # 0 NamesOfIntendedRecipientsOfResults
I: (0040,1400) LT (no value available)                     # 0 RequestedProcedureComments
I: (0040,2004) DA (no value available)                     # 0 IssueDateOfImagingServiceRequest
I: (0040,2005) TM (no value available)                     # 0 IssueTimeOfImagingServiceRequest
I: (0040,2008) PN (no value available)                     # 0 OrderEnteredBy
I: (0040,2009) SH (no value available)                     # 0 OrderEntererLocation
I: (0040,2010) SH (no value available)                     # 0 OrderCallbackPhoneNumber
I: (0040,2016) LO (no value available)                     # 0 PlacerOrderNumberImagingServiceRequest
I: (0040,2017) LO (no value available)                     # 0 FillerOrderNumberImagingServiceRequest
I: (0040,2400) LT (no value available)                     # 0 ImagingServiceRequestComments
I: (0040,3001) LO (no value available)                     # 0 ConfidentialityConstraintOnPatientDataDescription
I:
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received C-FIND request from 192.168.1.122:3590 at 2024-07-10 15:50:51
I: Find SCP Response 1: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [YANTI]                                  # 1 PatientName
D: (0010,0020) LO [10228583]                               # 1 PatientID
D: (0010,0030) DA [19820415]                               # 1 PatientBirthDate
D: (0010,0040) CS [F]                                      # 1 PatientSex
D: (0010,1030) DS [60]                                     # 1 PatientWeight
D: (0020,000D) UI [112]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [1]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [20240710]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [112]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 71
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 2: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [ELIZABETH^JESSAMINE^DJA]                # 1 PatientName
D: (0010,0020) LO [10354267]                               # 1 PatientID
D: (0010,0030) DA [19991025]                               # 1 PatientBirthDate
D: (0010,0040) CS [F]                                      # 1 PatientSex
D: (0010,1030) DS [60]                                     # 1 PatientWeight
D: (0020,000D) UI [113]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [2]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [20240710]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [113]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 71
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 3: 0x0000 (Success)
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 71
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-CREATE request from 192.168.1.122:3599 at 2024-07-10 15:51:27
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
=============================================
<pynetdicom.dimse_primitives.N_CREATE object at 0x000001677266AC90>
=============================================
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0060) Modality                            CS: ''
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 1120)  Referenced Patient Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0018, 1110) Distance Source to Detector         DS: None
(0018, 115e) Image and Fluoroscopy Area Dose Pro DS: None
(0020, 0010) Study ID                            SH: 'MR20240710153646'
(0040, 0241) Performed Station AE Title          AE: 'MRC26266'
(0040, 0242) Performed Station Name              SH: 'MRC26266'
(0040, 0243) Performed Location                  SH: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20240710'
(0040, 0245) Performed Procedure Step Start Time TM: '153722.562000'
(0040, 0250) Performed Procedure Step End Date   DA: ''
(0040, 0251) Performed Procedure Step End Time   TM: ''
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0253) Performed Procedure Step ID         SH: '112'
(0040, 0254) Performed Procedure Step Descriptio LO: ''
(0040, 0255) Performed Procedure Type Descriptio LO: ''
(0040, 0260)  Performed Protocol Code Sequence  0 item(s) ----
(0040, 0270)  Scheduled Step Attributes Sequence  1 item(s) ----
   (0008, 0050) Accession Number                    SH: 'M.07.33'
   (0008, 1110)  Referenced Study Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
      (0008, 1155) Referenced SOP Instance UID         UI: 112
      ---------
   (0020, 000d) Study Instance UID                  UI: 112
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0007) Scheduled Procedure Step Descriptio LO: ''
   (0040, 0008)  Scheduled Protocol Code Sequence  0 item(s) ----
   (0040, 0009) Scheduled Procedure Step ID         SH: '112'
   (0040, 1001) Requested Procedure ID              SH: ''
   (0040, 2016) Placer Order Number / Imaging Servi LO: ''
   (0040, 2017) Filler Order Number / Imaging Servi LO: ''
   ---------
(0040, 0280) Comments on the Performed Procedure ST: ''
(0040, 0300) Total Time of Fluoroscopy           US: None
(0040, 0301) Total Number of Exposures           US: None
(0040, 0302) Entrance Dose                       US: None
(0040, 0303) Exposed Area                        US: None
(0040, 0306) Distance Source to Entrance         DS: None
(0040, 030e)  Exposure Dose Sequence  0 item(s) ----
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0320)  Billing Procedure Step Sequence  0 item(s) ----
(0040, 0321)  Film Consumption Sequence  1 item(s) ----
   (2000, 0030) Medium Type                         CS: ''
   (2010, 0050) Film Size ID                        CS: ''
   (2100, 0170) Number of Films                     IS: None
   ---------
(0040, 0324)  Billing Supplies and Devices Sequence  1 item(s) ----
   (0040, 0293)  Quantity Sequence  1 item(s) ----
      (0040, 0294) Quantity                            DS: None
      (0040, 0295)  Measuring Units Sequence  0 item(s) ----
      ---------
   (0040, 0296)  Billing Item Sequence  0 item(s) ----
   ---------
(0040, 0340)  Performed Series Sequence  1 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: ''
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'unknown'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071005583371800000016
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
(0040, 8302) Entrance Dose in mGy                DS: None
=============================================
E: cannot unpack non-iterable int object
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\association.py", line 3478, in _serve_request
    service_class.SCP(msg, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class_n.py", line 208, in SCP
    self._n_create_scp(req, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class.py", line 732, in _n_create_scp
    usr_status, ds = cast(UserReturnType, user_response)
    ^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable int object
I: Aborting Association
D: Abort Parameters:
D: =========================== OUTGOING A-ABORT PDU ===========================
D: Abort Source: DUL service-user
D: Abort Reason: (no value available)
D: ============================= END A-ABORT PDU ==============================
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-CREATE request from 192.168.1.122:3623 at 2024-07-10 15:52:16
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
=============================================
<pynetdicom.dimse_primitives.N_CREATE object at 0x0000016772668DD0>
=============================================
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0060) Modality                            CS: ''
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 1120)  Referenced Patient Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0018, 1110) Distance Source to Detector         DS: None
(0018, 115e) Image and Fluoroscopy Area Dose Pro DS: None
(0020, 0010) Study ID                            SH: 'MR20240710153646'
(0040, 0241) Performed Station AE Title          AE: 'MRC26266'
(0040, 0242) Performed Station Name              SH: 'MRC26266'
(0040, 0243) Performed Location                  SH: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20240710'
(0040, 0245) Performed Procedure Step Start Time TM: '153722.562000'
(0040, 0250) Performed Procedure Step End Date   DA: ''
(0040, 0251) Performed Procedure Step End Time   TM: ''
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0253) Performed Procedure Step ID         SH: '112'
(0040, 0254) Performed Procedure Step Descriptio LO: ''
(0040, 0255) Performed Procedure Type Descriptio LO: ''
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 0270)  Scheduled Step Attributes Sequence  1 item(s) ----
   (0008, 0050) Accession Number                    SH: 'M.07.33'
   (0008, 1110)  Referenced Study Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
      (0008, 1155) Referenced SOP Instance UID         UI: 112
      ---------
   (0020, 000d) Study Instance UID                  UI: 112
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0007) Scheduled Procedure Step Descriptio LO: ''
   (0040, 0008)  Scheduled Protocol Code Sequence  0 item(s) ----
   (0040, 0009) Scheduled Procedure Step ID         SH: '112'
   (0040, 1001) Requested Procedure ID              SH: ''
   (0040, 2016) Placer Order Number / Imaging Servi LO: ''
   (0040, 2017) Filler Order Number / Imaging Servi LO: ''
   ---------
(0040, 0280) Comments on the Performed Procedure ST: ''
(0040, 0300) Total Time of Fluoroscopy           US: None
(0040, 0301) Total Number of Exposures           US: None
(0040, 0302) Entrance Dose                       US: None
(0040, 0303) Exposed Area                        US: None
(0040, 0306) Distance Source to Entrance         DS: None
(0040, 030e)  Exposure Dose Sequence  0 item(s) ----
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0320)  Billing Procedure Step Sequence  0 item(s) ----
(0040, 0321)  Film Consumption Sequence  1 item(s) ----
   (2000, 0030) Medium Type                         CS: ''
   (2010, 0050) Film Size ID                        CS: ''
   (2100, 0170) Number of Films                     IS: None
   ---------
(0040, 0324)  Billing Supplies and Devices Sequence  1 item(s) ----
   (0040, 0293)  Quantity Sequence  1 item(s) ----
      (0040, 0294) Quantity                            DS: None
      (0040, 0295)  Measuring Units Sequence  0 item(s) ----
      ---------
   (0040, 0296)  Billing Item Sequence  0 item(s) ----
   ---------
(0040, 0340)  Performed Series Sequence  2 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000061
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 1(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 1(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015375130116216873.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
(0040, 8302) Entrance Dose in mGy                DS: None
=============================================
E: cannot unpack non-iterable int object
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\association.py", line 3478, in _serve_request
    service_class.SCP(msg, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class_n.py", line 208, in SCP
    self._n_create_scp(req, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class.py", line 732, in _n_create_scp
    usr_status, ds = cast(UserReturnType, user_response)
    ^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable int object
I: Aborting Association
D: Abort Parameters:
D: =========================== OUTGOING A-ABORT PDU ===========================
D: Abort Source: DUL service-user
D: Abort Reason: (no value available)
D: ============================= END A-ABORT PDU ==============================
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-CREATE request from 192.168.1.122:3649 at 2024-07-10 15:52:51
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
=============================================
<pynetdicom.dimse_primitives.N_CREATE object at 0x0000016772668DD0>
=============================================
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0060) Modality                            CS: ''
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 1120)  Referenced Patient Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0018, 1110) Distance Source to Detector         DS: None
(0018, 115e) Image and Fluoroscopy Area Dose Pro DS: None
(0020, 0010) Study ID                            SH: 'MR20240710153646'
(0040, 0241) Performed Station AE Title          AE: 'MRC26266'
(0040, 0242) Performed Station Name              SH: 'MRC26266'
(0040, 0243) Performed Location                  SH: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20240710'
(0040, 0245) Performed Procedure Step Start Time TM: '153722.562000'
(0040, 0250) Performed Procedure Step End Date   DA: ''
(0040, 0251) Performed Procedure Step End Time   TM: ''
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0253) Performed Procedure Step ID         SH: '112'
(0040, 0254) Performed Procedure Step Descriptio LO: ''
(0040, 0255) Performed Procedure Type Descriptio LO: ''
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 0270)  Scheduled Step Attributes Sequence  1 item(s) ----
   (0008, 0050) Accession Number                    SH: 'M.07.33'
   (0008, 1110)  Referenced Study Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
      (0008, 1155) Referenced SOP Instance UID         UI: 112
      ---------
   (0020, 000d) Study Instance UID                  UI: 112
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0007) Scheduled Procedure Step Descriptio LO: ''
   (0040, 0008)  Scheduled Protocol Code Sequence  0 item(s) ----
   (0040, 0009) Scheduled Procedure Step ID         SH: '112'
   (0040, 1001) Requested Procedure ID              SH: ''
   (0040, 2016) Placer Order Number / Imaging Servi LO: ''
   (0040, 2017) Filler Order Number / Imaging Servi LO: ''
   ---------
(0040, 0280) Comments on the Performed Procedure ST: ''
(0040, 0300) Total Time of Fluoroscopy           US: None
(0040, 0301) Total Number of Exposures           US: None
(0040, 0302) Entrance Dose                       US: None
(0040, 0303) Exposed Area                        US: None
(0040, 0306) Distance Source to Entrance         DS: None
(0040, 030e)  Exposure Dose Sequence  0 item(s) ----
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0320)  Billing Procedure Step Sequence  0 item(s) ----
(0040, 0321)  Film Consumption Sequence  1 item(s) ----
   (2000, 0030) Medium Type                         CS: ''
   (2010, 0050) Film Size ID                        CS: ''
   (2100, 0170) Number of Films                     IS: None
   ---------
(0040, 0324)  Billing Supplies and Devices Sequence  1 item(s) ----
   (0040, 0293)  Quantity Sequence  1 item(s) ----
      (0040, 0294) Quantity                            DS: None
      (0040, 0295)  Measuring Units Sequence  0 item(s) ----
      ---------
   (0040, 0296)  Billing Item Sequence  0 item(s) ----
   ---------
(0040, 0340)  Performed Series Sequence  3 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000061
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 1(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 1(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015375130116216873.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 2(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 2(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015382638154917432.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
(0040, 8302) Entrance Dose in mGy                DS: None
=============================================
E: cannot unpack non-iterable int object
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\association.py", line 3478, in _serve_request
    service_class.SCP(msg, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class_n.py", line 208, in SCP
    self._n_create_scp(req, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class.py", line 732, in _n_create_scp
    usr_status, ds = cast(UserReturnType, user_response)
    ^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable int object
I: Aborting Association
D: Abort Parameters:
D: =========================== OUTGOING A-ABORT PDU ===========================
D: Abort Source: DUL service-user
D: Abort Reason: (no value available)
D: ============================= END A-ABORT PDU ==============================
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-CREATE request from 192.168.1.122:3704 at 2024-07-10 15:55:23
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
=============================================
<pynetdicom.dimse_primitives.N_CREATE object at 0x0000016772668C80>
=============================================
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0060) Modality                            CS: ''
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 1120)  Referenced Patient Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0018, 1110) Distance Source to Detector         DS: None
(0018, 115e) Image and Fluoroscopy Area Dose Pro DS: None
(0020, 0010) Study ID                            SH: 'MR20240710153646'
(0040, 0241) Performed Station AE Title          AE: 'MRC26266'
(0040, 0242) Performed Station Name              SH: 'MRC26266'
(0040, 0243) Performed Location                  SH: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20240710'
(0040, 0245) Performed Procedure Step Start Time TM: '153722.562000'
(0040, 0250) Performed Procedure Step End Date   DA: ''
(0040, 0251) Performed Procedure Step End Time   TM: ''
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0253) Performed Procedure Step ID         SH: '112'
(0040, 0254) Performed Procedure Step Descriptio LO: ''
(0040, 0255) Performed Procedure Type Descriptio LO: ''
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 0270)  Scheduled Step Attributes Sequence  1 item(s) ----
   (0008, 0050) Accession Number                    SH: 'M.07.33'
   (0008, 1110)  Referenced Study Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
      (0008, 1155) Referenced SOP Instance UID         UI: 112
      ---------
   (0020, 000d) Study Instance UID                  UI: 112
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0007) Scheduled Procedure Step Descriptio LO: ''
   (0040, 0008)  Scheduled Protocol Code Sequence  0 item(s) ----
   (0040, 0009) Scheduled Procedure Step ID         SH: '112'
   (0040, 1001) Requested Procedure ID              SH: ''
   (0040, 2016) Placer Order Number / Imaging Servi LO: ''
   (0040, 2017) Filler Order Number / Imaging Servi LO: ''
   ---------
(0040, 0280) Comments on the Performed Procedure ST: ''
(0040, 0300) Total Time of Fluoroscopy           US: None
(0040, 0301) Total Number of Exposures           US: None
(0040, 0302) Entrance Dose                       US: None
(0040, 0303) Exposed Area                        US: None
(0040, 0306) Distance Source to Entrance         DS: None
(0040, 030e)  Exposure Dose Sequence  0 item(s) ----
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0320)  Billing Procedure Step Sequence  0 item(s) ----
(0040, 0321)  Film Consumption Sequence  1 item(s) ----
   (2000, 0030) Medium Type                         CS: ''
   (2010, 0050) Film Size ID                        CS: ''
   (2100, 0170) Number of Films                     IS: None
   ---------
(0040, 0324)  Billing Supplies and Devices Sequence  1 item(s) ----
   (0040, 0293)  Quantity Sequence  1 item(s) ----
      (0040, 0294) Quantity                            DS: None
      (0040, 0295)  Measuring Units Sequence  0 item(s) ----
      ---------
   (0040, 0296)  Billing Item Sequence  0 item(s) ----
   ---------
(0040, 0340)  Performed Series Sequence  4 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000061
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 1(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 1(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015375130116216873.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 2(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 2(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015382638154917432.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst WholeSpine'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst WholeSpine'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015401894633518000.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
(0040, 8302) Entrance Dose in mGy                DS: None
=============================================
E: cannot unpack non-iterable int object
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\association.py", line 3478, in _serve_request
    service_class.SCP(msg, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class_n.py", line 208, in SCP
    self._n_create_scp(req, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class.py", line 732, in _n_create_scp
    usr_status, ds = cast(UserReturnType, user_response)
    ^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable int object
I: Aborting Association
D: Abort Parameters:
D: =========================== OUTGOING A-ABORT PDU ===========================
D: Abort Source: DUL service-user
D: Abort Reason: (no value available)
D: ============================= END A-ABORT PDU ==============================
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-CREATE request from 192.168.1.122:3890 at 2024-07-10 15:57:34
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
=============================================
<pynetdicom.dimse_primitives.N_CREATE object at 0x0000016772668980>
=============================================
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0060) Modality                            CS: ''
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 1120)  Referenced Patient Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0010, 0010) Patient's Name                      PN: 'YANTI'
(0010, 0020) Patient ID                          LO: '10228583'
(0010, 0030) Patient's Birth Date                DA: '19820415'
(0010, 0040) Patient's Sex                       CS: 'F'
(0018, 1110) Distance Source to Detector         DS: None
(0018, 115e) Image and Fluoroscopy Area Dose Pro DS: None
(0020, 0010) Study ID                            SH: 'MR20240710153646'
(0040, 0241) Performed Station AE Title          AE: 'MRC26266'
(0040, 0242) Performed Station Name              SH: 'MRC26266'
(0040, 0243) Performed Location                  SH: ''
(0040, 0244) Performed Procedure Step Start Date DA: '20240710'
(0040, 0245) Performed Procedure Step Start Time TM: '153722.562000'
(0040, 0250) Performed Procedure Step End Date   DA: ''
(0040, 0251) Performed Procedure Step End Time   TM: ''
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0253) Performed Procedure Step ID         SH: '112'
(0040, 0254) Performed Procedure Step Descriptio LO: ''
(0040, 0255) Performed Procedure Type Descriptio LO: ''
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 0270)  Scheduled Step Attributes Sequence  1 item(s) ----
   (0008, 0050) Accession Number                    SH: 'M.07.33'
   (0008, 1110)  Referenced Study Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: Detached Study Management SOP Class
      (0008, 1155) Referenced SOP Instance UID         UI: 112
      ---------
   (0020, 000d) Study Instance UID                  UI: 112
   (0032, 1060) Requested Procedure Description     LO: ''
   (0040, 0007) Scheduled Procedure Step Descriptio LO: ''
   (0040, 0008)  Scheduled Protocol Code Sequence  0 item(s) ----
   (0040, 0009) Scheduled Procedure Step ID         SH: '112'
   (0040, 1001) Requested Procedure ID              SH: ''
   (0040, 2016) Placer Order Number / Imaging Servi LO: ''
   (0040, 2017) Filler Order Number / Imaging Servi LO: ''
   ---------
(0040, 0280) Comments on the Performed Procedure ST: ''
(0040, 0300) Total Time of Fluoroscopy           US: None
(0040, 0301) Total Number of Exposures           US: None
(0040, 0302) Entrance Dose                       US: None
(0040, 0303) Exposed Area                        US: None
(0040, 0306) Distance Source to Entrance         DS: None
(0040, 030e)  Exposure Dose Sequence  0 item(s) ----
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0320)  Billing Procedure Step Sequence  0 item(s) ----
(0040, 0321)  Film Consumption Sequence  1 item(s) ----
   (2000, 0030) Medium Type                         CS: ''
   (2010, 0050) Film Size ID                        CS: ''
   (2100, 0170) Number of Films                     IS: None
   ---------
(0040, 0324)  Billing Supplies and Devices Sequence  1 item(s) ----
   (0040, 0293)  Quantity Sequence  1 item(s) ----
      (0040, 0294) Quantity                            DS: None
      (0040, 0295)  Measuring Units Sequence  0 item(s) ----
      ---------
   (0040, 0296)  Billing Item Sequence  0 item(s) ----
   ---------
(0040, 0340)  Performed Series Sequence  5 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000061
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 1(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 1(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015375130116216873.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 2(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'localizer 2(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015382638154917432.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst WholeSpine'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst WholeSpine'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015401894633518000.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst WholeSpine'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst WholeSpine'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015423024941118625.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
(0040, 8302) Entrance Dose in mGy                DS: None
=============================================
E: cannot unpack non-iterable int object
Traceback (most recent call last):
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\association.py", line 3478, in _serve_request
    service_class.SCP(msg, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class_n.py", line 208, in SCP
    self._n_create_scp(req, context)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python312\Lib\site-packages\pynetdicom\service_class.py", line 732, in _n_create_scp
    usr_status, ds = cast(UserReturnType, user_response)
    ^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable int object
I: Aborting Association
D: Abort Parameters:
D: =========================== OUTGOING A-ABORT PDU ===========================
D: Abort Source: DUL service-user
D: Abort Reason: (no value available)
D: ============================= END A-ABORT PDU ==============================








      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575473819620484
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575477013820487
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575496032920509
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575490710620504
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575490099920497
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575496050020510
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557553518720513
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557556443020524
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557559232620529
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575510120020530
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575516716120537
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575521658320546
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575522495620549
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575523350020550
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575530072420557
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575536542820569
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575535891720568
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575536807520570
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575543444420575
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575549225220586
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575550160220589
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575551223120590
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575556809520595
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575562607020606
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575563310320607
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575566081720612
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575569833020615
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575576038620626
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575576528220627
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575580723420632
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575582879220635
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575589414020645
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575589746520646
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575596423420656
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575596079720655
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557562953920665
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557562954820666
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557569248320673
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575611175020680
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575615927720683
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_MYELO_cor'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015575360742120367.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_MYELO_cor_MIP_COR'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575623555720689
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_MYELO_cor'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015575364743720372.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_rst_tra_320_rs'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  15 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005650243721222
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005676901421228
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101600573553721233
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005730223321238
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005756488421243
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005783158921248
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101600589820321253
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005836490621258
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005863151221263
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005889820921268
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005916480421273
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005943153921278
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005969811921283
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005996482521288
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016010023146521293
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_rst_tra_320_rs'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071016005654234921223.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 83
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071003250751500000004
D: Attribute List                : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-SET request from 192.168.1.122:4510 at 2024-07-10 16:19:49
SOP Instance UID:  1.3.12.2.1107.5.2.30.26266.30000024071003250751500000004
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
(0008, 1032)  Procedure Code Sequence  0 item(s) ---- 
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 030e)  Exposure Dose Sequence  1 item(s) ----

   ---------
(0040, 0340)  Performed Series Sequence  15 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000061
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 1(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  7 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015375646014616878
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015375898050716882
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015380150037216886
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101538042000816890
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015380653944216894
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101538095992316898
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015381158244816902
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer 1(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015375130116216873.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer 2(Whole Spine)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  7 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015383173918917437
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015383425878317441
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015383677929817445
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015383929829217449
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015384181913917453
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015384433864617457
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015384685846117461
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer 2(Whole Spine)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015382638154917432.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst WholeSpine'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015401880623217997
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015401910740618003
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015401940651318008
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015401970698018013
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402097418018
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402029994918023
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402060413118028
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402090018118033
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402120264918038
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015402150285218043
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411579707718048
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411613080318053
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411647072818058
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411680108718063
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411713116218068
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411746798718073
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411779660618078
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411812992118083
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015411846684318088
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst WholeSpine'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015401894633518000.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst WholeSpine'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423011351818624
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423041317018630
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423071391918635
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101542311499018640
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423130960518645
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423160833418650
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423190879918655
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423220921618660
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423250887518665
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015423280844218670
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432710784418675
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432744165218680
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432777400218685
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432810784618690
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432844058518695
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432877668518700
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432910874018705
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432944077718710
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015432977453318715
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst WholeSpine'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015423024941118625.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_COR_rst_384'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  11 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015445978718319251
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015450019351619257
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015450060942719262
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101545012697519267
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015450143866819272
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015450185551719277
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015461476969519282
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015461526979619287
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015461576993519292
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015461627011919297
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015461677058819302
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_COR_rst_384'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015445988887719252.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst_384_ORIG'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  11 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484635279119309
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484676815619315
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484718500119320
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484760148219325
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101548481803819330
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484843474119335
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500135001619340
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500184973119345
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500234985819350
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500284961919355
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500334996219360
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst_384'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015473046650819304.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_sag_rst_384'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  11 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484637997019310
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484679560819316
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484721201319321
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484762848319326
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101548484076919331
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015484845742619336
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500137282819341
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500187244619346
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500237256619351
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500287242619356
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015500337266519361
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_sag_rst_384'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015484648223319311.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't1_tse_sag'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  11 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520812624819919
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520815074719923
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520811584619918
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520816699319924
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520824688519928
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520828229019935
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520828278519936
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520829403819937
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520838617619940
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520839954019945
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015520839962819946
      ---------
   (0018, 1030) Protocol Name                       LO: 't1_tse_sag'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015520818137519925.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'tirm_sag'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  11 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543686583419953
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543731887419958
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543777094919962
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543822371019966
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543867579619970
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543912838919974
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015543958117019978
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101554403384419982
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015544048666819986
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015544093920819990
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015544139221319994
      ---------
   (0018, 1030) Protocol Name                       LO: 'tirm_sag'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015543694115419954.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_MYELO_cor'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  60 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575350837720355
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575352832020358
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575367020620384
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575367030920385
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575366815520383
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575381555520405
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575380933820404
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575384640620410
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575395786120426
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575394751420425
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557546774520437
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557549448020440
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575417563420447
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575423074320450
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575452451920467
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575437147220455
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575440927720458
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575459300220470
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575468108420479
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575482451820490
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575473819620484
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575477013820487
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575496032920509
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575490710620504
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575490099920497
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575496050020510
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557553518720513
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557556443020524
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557559232620529
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575510120020530
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575516716120537
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575521658320546
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575522495620549
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575523350020550
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575530072420557
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575536542820569
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575535891720568
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575536807520570
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575543444420575
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575549225220586
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575550160220589
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575551223120590
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575556809520595
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575562607020606
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575563310320607
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575566081720612
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575569833020615
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575576038620626
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575576528220627
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575580723420632
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575582879220635
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575589414020645
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575589746520646
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575596423420656
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575596079720655
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557562953920665
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557562954820666
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101557569248320673
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575611175020680
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575615927720683
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_MYELO_cor'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015575360742120367.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_MYELO_cor_MIP_COR'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015575623555720689
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_MYELO_cor'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015575364743720372.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_rst_tra_320_rs'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  15 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005650243721222
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005676901421228
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101600573553721233
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005730223321238
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005756488421243
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005783158921248
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101600589820321253
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005836490621258
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005863151221263
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005889820921268
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005916480421273
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005943153921278
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005969811921283
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016005996482521288
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016010023146521293
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_rst_tra_320_rs'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071016005654234921223.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_me2d_tra_p2_ORIG'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  15 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054311266122096
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054320578522119
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054325133822132
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054332505722150
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054342249022177
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054347294522188
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054352999222200
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054361817222220
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054366821922239
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054373086122256
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054380770322273
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054386152722286
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054392631122303
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101605443362322332
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101605444068422334
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_me2d_tra_p2'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071016013136061222081.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_me2d_tra_p2'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  15 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054314898422103
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054324542422130
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054328807522139
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054335444122155
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054345038522178
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054349735422191
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054357488222210
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054365524622235
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054372710422250
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054376563722263
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054383185222276
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054389218022297
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071016054395793222314
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101605447438422338
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101605446560522337
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_me2d_tra_p2'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071016054330141022144.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 84
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071003250751500000004
D: Attribute List                : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released






   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [12] t2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014152145312500093
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014152148437500096
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071014152145312500092PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014152145312500092
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_flair_tra'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171765145812387
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171780455012393
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171795930912398
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171811378112403
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171826446812408
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171841913012413
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171857397212418
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171872849612423
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014171888314812428
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101417193776912433
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191464323912438
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191479799612443
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191495248412448
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191510720512453
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191526190712458
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191541657512463
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191557106712468
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191572569112473
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014191588047912478
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_flair_tra'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014171768187212388.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [13] t2_flair_tra'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101419213125000107
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101419217812500110
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.202407101419213125000106PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.202407101419213125000106
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't1_se_tra_nosat'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212054076912486
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212056681212491
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212059365512497
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212061988512502
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212064189612507
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212066866812512
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212069704012517
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212072094612522
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212074822512527
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212077455812532
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212079997612537
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212082702812542
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212085527812547
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212087902312552
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212090533812557
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212093138312562
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212095791412567
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212098408612572
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101421212378612577
      ---------
   (0018, 1030) Protocol Name                       LO: 't1_se_tra_nosat'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014212058941812496.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [14] t1_se_tra_nosat'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212118750000121
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014212123437500124
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071014212118750000120PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014212118750000120
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_swi3d_tra_p2_fast'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  56 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245845283012659
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245845934912661
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245848549312691
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245855178312711
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245850828412701
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245851384812705
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245850857512703
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245853958912708
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245853965712709
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245855929212713
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245858406112721
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245857376812715
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245857424012717
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245857986012719
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245858774212723
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245859833712725
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245860191712727
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245860584012729
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245861230012731
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245862014312733
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245862204512735
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245862624712737
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245863410012739
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245863654812741
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245864026712743
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245865603712751
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245864828912745
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245865087712747
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245865446312749
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245866233612753
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245866494312755
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245866847512757
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245867820312761
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245867763912759
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245867951412763
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245868295512765
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245869262112767
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245869280412769
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245869407912771
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245869736712773
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245870718512775
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245871003912779
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245870846612777
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245872275812785
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245872152412781
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245872270112784
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245872488612787
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245873598812789
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245873912512793
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245873748412791
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245873965312795
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245875026412798
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245875169412800
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245875328312802
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245877147012804
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014245877874912806
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_swi3d_tra_p2_fast'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.202407101421267484112580.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_fl2d_tra_hemo(tumor,perdarahan)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265113658512814
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265117700612818
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265121936012822
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265126109812826
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265130307812830
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265134820412834
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265138737412838
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265142897912842
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265147152912846
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265151333412850
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265155829012854
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265161194212858
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265163962012862
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265168888312866
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265172381612870
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265177874412874
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265181968212878
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265185377212882
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014265189794312884
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_fl2d_tra_hemo(tumor,perdarahan)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014245881725412807.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_ci3d_tra_iso0.6'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  64 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300361014112952
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300362632012989
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300367940313016
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300368431813018
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300372541513034
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300372550913035
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300387869813119
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300382859113069
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300383646913080
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430047097713235
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430049124513245
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430047342413236
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430048188313244
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300427547613332
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300424188613320
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300422394913306
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300421430713304
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300430218213349
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300440689713409
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300455144213436
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300443936713410
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300451101313429
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300451568513432
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300452224313433
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300457738013438
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300460501013446
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300460804213447
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300464955313448
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300467702913452
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300468660213453
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300472344013462
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300474982313465
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300479081213478
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300484448013497
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300486746113500
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300489116413501
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300489849113502
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300491057413503
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300493323413504
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300495769313505
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300497555513506
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300497678413507
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300567313508
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430052335713509
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430054270513510
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430055553413511
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430056795813512
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101430058914113513
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300510832713514
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300513252013515
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300513377613516
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300515492913517
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300517697713518
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300519962413519
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300520517213520
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300522085113521
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300525327513522
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300526563313523
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300528045213524
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300528670513525
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300531911813526
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300533116013527
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300535215013528
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014300535785213529
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_ci3d_tra_iso0.6'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014300368424713017.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'DWI_b0_500_1000'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  57 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364028575213691
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364041748213756
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364055582113799
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364060287613816
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364074540713869
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364088292013918
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364092205113929
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101436416146213984
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364119215314029
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364123720514056
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364137212414103
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364150706014146
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364155148414161
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364168748414210
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364183231514261
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364187346314280
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.20240710143642648314325
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364213503814374
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364217467714391
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364231762614446
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364244109714495
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364248025214506
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364262241714555
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364274577914604
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364278626514621
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364292181014682
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101436435195214721
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364310008214738
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364322973414785
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364336081414834
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364340857814855
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364354310414910
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364367746614949
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364372536014972
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364386177815014
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364399273215066
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101436443746715079
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364417412715130
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364430057015181
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364434434015198
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364447961915246
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364460925215296
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364465805515311
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364479575915362
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364492763315411
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364497319915426
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364510987315479
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364524575915524
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364528709215541
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364542379015578
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364555916415603
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364560867715612
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364574602015637
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364587132615662
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364590999215671
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101436463153115698
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364614861215721
      ---------
   (0018, 1030) Protocol Name                       LO: 'DWI_b0_500_1000'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014345629569213533.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'DWI_b0_500_1000_ADC'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364054592413798
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364087303013917
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364118224514028
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364149723414145
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364182239514260
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364212496714373
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364243108614490
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364273580214603
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101436434210014720
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364335089714833
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364366757914948
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364398286815065
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364429068615180
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364459929715295
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364491763415408
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364523583615521
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364554925815602
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364586143715661
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071014364613879415720
      ---------
   (0018, 1030) Protocol Name                       LO: 'DWI_b0_500_1000'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071014345629569313534.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 106
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071003250751500000002
D: Attribute List                : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released
D: Request Parameters:
D: ======================= INCOMING A-ASSOCIATE-RQ PDU ========================
D: Their Implementation Class UID:      1.3.12.2.1107.5.2
D: Their Implementation Version Name:   MR_VB19A
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Calling Application Name:    MRC26266
D: Called Application Name:     ADM_SCP
D: Their Max PDU Receive Size:  262144
D: Presentation Context:
D:   Context ID:        1 (Proposed)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Proposed SCP/SCU Role: Default
D:     Proposed Transfer Syntaxes:
D:       =Explicit VR Little Endian
D:       =Implicit VR Little Endian
D:       =Explicit VR Big Endian
D: Requested Extended Negotiation: None
D: Requested Common Extended Negotiation: None
D: Requested Asynchronous Operations Window Negotiation: None
D: Requested User Identity Negotiation: None
D: ========================== END A-ASSOCIATE-RQ PDU ==========================
I: Accepting Association
D: Accept Parameters:
D: ======================= OUTGOING A-ASSOCIATE-AC PDU ========================
D: Our Implementation Class UID:      1.2.826.0.1.3680043.9.3811.2.0.2
D: Our Implementation Version Name:   PYNETDICOM_202
D: Application Context Name:    1.2.840.10008.3.1.1.1
D: Responding Application Name: resp. AE Title
D: Our Max PDU Receive Size:    16382
D: Presentation Contexts:
D:   Context ID:        1 (Accepted)
D:     Abstract Syntax: =Modality Performed Procedure Step SOP Class
D:     Accepted SCP/SCU Role: Default
D:     Accepted Transfer Syntax: =Implicit VR Little Endian
D: Accepted Extended Negotiation: None
D: Accepted Asynchronous Operations Window Negotiation: None
D: User Identity Negotiation Response: None
D: ========================== END A-ASSOCIATE-AC PDU ==========================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
Received N-SET request from 192.168.1.122:2751 at 2024-07-10 17:06:46
SOP Instance UID:  1.3.12.2.1107.5.2.30.26266.30000024071003250751500000003
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
(0008, 1032)  Procedure Code Sequence  0 item(s) ---- 
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0040, 0250) Performed Procedure Step End Date   DA: '20240710'
(0040, 0251) Performed Procedure Step End Time   TM: '165241.984000'
(0040, 0252) Performed Procedure Step Status     CS: 'COMPLETED'
(0040, 0260)  Performed Protocol Code Sequence  1 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
(0040, 030e)  Exposure Dose Sequence  1 item(s) ----

   ---------
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0340)  Performed Series Sequence  3 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071003253693700000029
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  3 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101503419002416256
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015034377821916260
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015034646620316264
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015033728373516251.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_fl2d_tra_hemo(tumor,perdarahan)'
   (0008, 1050) Performing Physician's Name         PN: 'INGE, DR, SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'tRi'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054278305916273
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054282560116277
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054286777916281
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054290985416285
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054295170016289
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054299424316293
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101505433790716297
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407101505437784916301
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054311989616305
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054316166016309
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054321598116313
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054324630416317
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054328827616321
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054333090016325
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054337263516329
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054341471416333
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054346075916337
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054350486616341
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071015054354096316343
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_fl2d_tra_hemo(tumor,perdarahan)'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071015035352178816266.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 107
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071003250751500000003
D: Attribute List                : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Release