=======================DATA MASUK======================
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
(0040, 0340)  Performed Series Sequence  2 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071902525984300000039
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  3 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362051400206569
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362320258906573
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362589032006577
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913361673036306564.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
=======================================================
E: Exception in the handler bound to 'evt.EVT_N_SET'
E: 'Dataset' object has no attribute 'PerformedProcedureStepEndDate'
Traceback (most recent call last):
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pynetdicom\service_class.py", line 1249, in _n_set_scp
    user_response = evt.trigger(
                    ^^^^^^^^^^^^
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pynetdicom\events.py", line 387, in trigger
    return handlers[0](evt)
           ^^^^^^^^^^^^^^^^
  File "c:\py\dicom3\dicom\dicom-app\handlers.py", line 375, in handle_set
    worklist_data[index]["PerformedProcedureStepEndDate"] = mod_list.PerformedProcedureStepEndDate  # noqa: E501
                                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pydicom\dataset.py", line 908, in __getattr__
    return object.__getattribute__(self, name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Dataset' object has no attribute 'PerformedProcedureStepEndDate'. Did you mean: 'PerformedProcedureStepStatus'?
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 80
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071902445654600000002
D: Attribute List                : None
D: Status                        : 0x0110
D: ============================ END DIMSE MESSAGE =============================
I: Association Released







FULL
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
Received N-SET request from 192.168.1.122:1326 at 2024-07-19 13:54:05
SOP Instance UID:  1.3.12.2.1107.5.2.30.26266.30000024071902445654600000002
=======================DATA MASUK======================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0040, 0252) Performed Procedure Step Status     CS: 'IN PROGRESS'
(0040, 0260)  Performed Protocol Code Sequence  2 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
   (0008, 0100) Code Value                          SH: 'PP_007'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: '1.3.12.2.1107.5.2.30.26266.2024071913395448437500164PP_007'
   ---------
(0040, 030e)  Exposure Dose Sequence  1 item(s) ----

   ---------
(0040, 0340)  Performed Series Sequence  4 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071902525984300000039
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  3 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362051400206569
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362320258906573
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362589032006577
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913361673036306564.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395059963906846
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395081057206852
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191339512052506857
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395123119106862
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395143727706867
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395164793306872
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395185822606877
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191339526887806882
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395227977506887
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395249018206892
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395270047406897
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395291090406902
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395312150206907
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395333218606912
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395354240806917
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395375360606922
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395396370006927
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395417404006932
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395438477106937
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_tra'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913395066538606847.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [5] t2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395448437500165
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395450000000168
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071913395448437500164PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913395448437500164
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
=======================================================
E: Exception in the handler bound to 'evt.EVT_N_SET'
E: 'Dataset' object has no attribute 'PerformedProcedureStepEndDate'
Traceback (most recent call last):
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pynetdicom\service_class.py", line 1249, in _n_set_scp
    user_response = evt.trigger(
                    ^^^^^^^^^^^^
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pynetdicom\events.py", line 387, in trigger
    return handlers[0](evt)
           ^^^^^^^^^^^^^^^^
  File "c:\py\dicom3\dicom\dicom-app\handlers.py", line 375, in handle_set
    worklist_data[index]["PerformedProcedureStepEndDate"] = mod_list.PerformedProcedureStepEndDate  # noqa: E501
                                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\py\dicom3\dicom\.venv\Lib\site-packages\pydicom\dataset.py", line 908, in __getattr__
    return object.__getattribute__(self, name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'Dataset' object has no attribute 'PerformedProcedureStepEndDate'. Did you mean: 'PerformedProcedureStepStatus'?
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 81
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071902445654600000002
D: Attribute List                : None
D: Status                        : 0x0110
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
Received N-SET request from 192.168.1.122:1351 at 2024-07-19 13:54:46
SOP Instance UID:  1.3.12.2.1107.5.2.30.26266.30000024071902445654600000001
=======================DATA MASUK======================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
(0008, 1032)  Procedure Code Sequence  0 item(s) ----
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0040, 0250) Performed Procedure Step End Date   DA: '20240719'
(0040, 0251) Performed Procedure Step End Time   TM: '123935.500000'
(0040, 0252) Performed Procedure Step Status     CS: 'COMPLETED'
(0040, 0260)  Performed Protocol Code Sequence  3 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
   (0008, 0100) Code Value                          SH: 'PP_007'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: '1.3.12.2.1107.5.2.30.26266.2024071912335040625000133PP_007'
   ---------
   (0008, 0100) Code Value                          SH: 'PP_007'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: '1.3.12.2.1107.5.2.30.26266.2024071912382989062500147PP_007'
   ---------
(0040, 030e)  Exposure Dose Sequence  1 item(s) ----

   ---------
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0340)  Performed Series Sequence  5 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  3 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912294612386005566
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912294881143105570
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912295149983305574
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071912294232265805561.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334653694705843
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334674640005849
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334695805205854
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334716847205859
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334737414505864
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334758445705869
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334779512105874
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.20240719123348546805879
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334821594605884
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334842654905889
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334863748105894
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334884800705899
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191233495820105904
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334926889405909
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334947934305914
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334968960305919
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912334990031005924
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912335011082405929
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912335032191205934
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_tra'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071912334660300805844.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [2] t2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912335040625000134
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912335043750000137
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071912335040625000133PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071912335040625000133
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191238261011705942
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382622086605948
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382643121405953
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382664252505958
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382684836905963
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191238275870205968
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382726920305973
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382747995605978
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382769014105983
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382790091705988
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382811110805993
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382832200005998
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382853256206003
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382874281506008
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382895349406013
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382916383806018
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382937475606023
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382958488406028
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382979635606033
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_tra'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.202407191238268145805943.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [3] t2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  1 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071912382989062500148
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071912382989062500147PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071912382989062500147
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
=======================================================
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 82
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071902445654600000001
D: Attribute List                : Present
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
Received N-SET request from 192.168.1.122:1352 at 2024-07-19 13:54:47
SOP Instance UID:  1.3.12.2.1107.5.2.30.26266.30000024071902445654600000002
=======================DATA MASUK======================
D: pydicom.read_dataset() TransferSyntax="Little Endian Implicit"
(0008, 1032)  Procedure Code Sequence  0 item(s) ---- 
(0008, 2229)  Anatomic Structure, Space or Region Sequence  0 item(s) ----
(0040, 0250) Performed Procedure Step End Date   DA: '20240719'
(0040, 0251) Performed Procedure Step End Time   TM: '134036.375000'
(0040, 0252) Performed Procedure Step Status     CS: 'COMPLETED'
(0040, 0260)  Performed Protocol Code Sequence  2 item(s) ----
   (0008, 0100) Code Value                          SH: 'PP-20'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: 'Phoenix Document'
   ---------
   (0008, 0100) Code Value                          SH: 'PP_007'
   (0008, 0102) Coding Scheme Designator            SH: '99SMS_CTMR'
   (0008, 0103) Coding Scheme Version               SH: '1.0'
   (0008, 0104) Code Meaning                        LO: '1.3.12.2.1107.5.2.30.26266.2024071913395448437500164PP_007'
   ---------
(0040, 030e)  Exposure Dose Sequence  1 item(s) ----

   ---------
(0040, 0310) Comments on Radiation Dose          ST: ''
(0040, 0340)  Performed Series Sequence  4 item(s) ----
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PhoenixZIPReport'
   (0008, 1050) Performing Physician's Name         PN: ''
   (0008, 1070) Operators' Name                     PN: ''
   (0008, 1140)  Referenced Image Sequence  0 item(s) ----
   (0018, 1030) Protocol Name                       LO: 'Phoenix Document'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.30000024071902525984300000039
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'localizer'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  3 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362051400206569
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362320258906573
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913362589032006577
      ---------
   (0018, 1030) Protocol Name                       LO: 'localizer'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913361673036306564.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 't2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  19 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395059963906846
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395081057206852
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191339512052506857
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395123119106862
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395143727706867
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395164793306872
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395185822606877
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.202407191339526887806882
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395227977506887
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395249018206892
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395270047406897
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395291090406902
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395312150206907
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395333218606912
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395354240806917
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395375360606922
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395396370006927
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395417404006932
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395438477106937
      ---------
   (0018, 1030) Protocol Name                       LO: 't2_tse_tra'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913395066538606847.0.0.0
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
   (0008, 0054) Retrieve AE Title                   AE: ''
   (0008, 103e) Series Description                  LO: 'PosDisp: [5] t2_tse_tra'
   (0008, 1050) Performing Physician's Name         PN: 'ENDY,DR,SP.RAD'
   (0008, 1070) Operators' Name                     PN: 'LD'
   (0008, 1140)  Referenced Image Sequence  2 item(s) ----
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395448437500165
      ---------
      (0008, 1150) Referenced SOP Class UID            UI: MR Image Storage
      (0008, 1155) Referenced SOP Instance UID         UI: 1.3.12.2.1107.5.2.30.26266.2024071913395450000000168
      ---------
   (0018, 1030) Protocol Name                       LO: '1.3.12.2.1107.5.2.30.26266.2024071913395448437500164PP_007'
   (0020, 000e) Series Instance UID                 UI: 1.3.12.2.1107.5.2.30.26266.2024071913395448437500164
   (0040, 0220)  Referenced Non-Image Composite SOP Instance Sequence  0 item(s) ----
   ---------
=======================================================
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : N-SET RSP
D: Message ID Being Responded To : 83
D: Affected SOP Class UID        : Modality Performed Procedure Step SOP Class
D: Affected SOP Instance UID     : 1.3.12.2.1107.5.2.30.26266.30000024071902445654600000002
D: Attribute List                : Present
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
D: Message ID                    : 84
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
I:     (0040,0002) DA [20240719]                               # 1 ScheduledProcedureStepStartDate
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
Received C-FIND request from 192.168.1.122:1831 at 2024-07-19 13:57:26
I: Find SCP Response 1: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [Reinert^Yosua^Rumagit]                  # 1 PatientName
D: (0010,0020) LO [1]                                      # 1 PatientID
D: (0010,0030) DA [19921124]                               # 1 PatientBirthDate
D: (0010,0040) CS [M]                                      # 1 PatientSex
D: (0010,1030) DS [87]                                     # 1 PatientWeight
D: (0020,000D) UI [116]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [6]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [19921124]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [116]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 84
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 2: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [Reinert^Yosua^Rumagit]                  # 1 PatientName
D: (0010,0020) LO [2]                                      # 1 PatientID
D: (0010,0030) DA [19921124]                               # 1 PatientBirthDate
D: (0010,0040) CS [M]                                      # 1 PatientSex
D: (0010,1030) DS [87]                                     # 1 PatientWeight
D: (0020,000D) UI [112]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [2]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [19921124]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [112]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 84
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 3: 0x0000 (Success)
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 84
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
D: Message ID                    : 85
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
I:     (0040,0002) DA [20240719]                               # 1 ScheduledProcedureStepStartDate
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
Received C-FIND request from 192.168.1.122:1906 at 2024-07-19 13:57:35
I: Find SCP Response 1: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [Reinert^Yosua^Rumagit]                  # 1 PatientName
D: (0010,0020) LO [1]                                      # 1 PatientID
D: (0010,0030) DA [19921124]                               # 1 PatientBirthDate
D: (0010,0040) CS [M]                                      # 1 PatientSex
D: (0010,1030) DS [87]                                     # 1 PatientWeight
D: (0020,000D) UI [116]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [6]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [19921124]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [116]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 85
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 2: 0xFF00 (Pending)
D: Find SCP Response Identifier:
D:
D: # DICOM Dataset
D: (0010,0010) PN [Reinert^Yosua^Rumagit]                  # 1 PatientName
D: (0010,0020) LO [2]                                      # 1 PatientID
D: (0010,0030) DA [19921124]                               # 1 PatientBirthDate
D: (0010,0040) CS [M]                                      # 1 PatientSex
D: (0010,1030) DS [87]                                     # 1 PatientWeight
D: (0020,000D) UI [112]                                    # 1 StudyInstanceUID
D: (0020,0010) SH [2]                                      # 1 StudyID
D: (0040,0100) SQ (Sequence with 1 item)                   # 1 ScheduledProcedureStepSequence
D:   (Sequence item #1)
D:     (0040,0001) AE [MRC26266]                               # 1 ScheduledStationAETitle
D:     (0040,0002) DA [19921124]                               # 1 ScheduledProcedureStepStartDate
D:     (0040,0009) SH [112]                                    # 1 ScheduledProcedureStepID
D:
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 85
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : Present
D: Status                        : 0xFF00
D: ============================ END DIMSE MESSAGE =============================
I: Find SCP Response 3: 0x0000 (Success)
D: ========================== OUTGOING DIMSE MESSAGE ==========================
D: Message Type                  : C-FIND RSP
D: Message ID Being Responded To : 85
D: Affected SOP Class UID        : Modality Worklist Information Model - FIND
D: Identifier                    : None
D: Status                        : 0x0000
D: ============================ END DIMSE MESSAGE =============================
I: Association Released
