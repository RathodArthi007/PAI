Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
================== RESTART: C:/Users/AIML LAB2/Downloads/6.py ==================
INFO:pgmpy: Datatype (N=numerical, C=Categorical Unordered, O=Categorical Ordered) inferred from data: 
 {'Income_Stability': 'C', 'Credit_History': 'C', 'Employment_Type': 'C', 'Default_Risk': 'C'}
+------------------------+-----+
| Income_Stability(High) | 0.5 |
+------------------------+-----+
| Income_Stability(Low)  | 0.5 |
+------------------------+-----+
+--------------------+-----+----------------------------+
| Credit_History     | ... | Credit_History(Good)       |
+--------------------+-----+----------------------------+
| Employment_Type    | ... | Employment_Type(Permanent) |
+--------------------+-----+----------------------------+
| Income_Stability   | ... | Income_Stability(Low)      |
+--------------------+-----+----------------------------+
| Default_Risk(High) | ... | 0.0                        |
+--------------------+-----+----------------------------+
| Default_Risk(Low)  | ... | 1.0                        |
+--------------------+-----+----------------------------+
+----------------------+-----+
| Credit_History(Bad)  | 0.5 |
+----------------------+-----+
| Credit_History(Good) | 0.5 |
+----------------------+-----+
+----------------------------+-----+
| Employment_Type(Contract)  | 0.5 |
+----------------------------+-----+
| Employment_Type(Permanent) | 0.5 |
+----------------------------+-----+

Predicted Default Risk Probability:
+--------------------+---------------------+
| Default_Risk       |   phi(Default_Risk) |
+====================+=====================+
| Default_Risk(High) |              1.0000 |
+--------------------+---------------------+
| Default_Risk(Low)  |              0.0000 |
+--------------------+---------------------+
