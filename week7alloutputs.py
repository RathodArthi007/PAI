Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================= RESTART: C:/Users/AIML LAB2/Downloads/hmm7.py ================

--- Step 1: Initialization ---
P(Rainy at t=0) = 0.6 * 0.1 = 0.06
P(Sunny at t=0) = 0.4 * 0.6 = 0.24

--- Step 2: Recursion for observation 'shop' ---

Computing P(Rainy at t=1)
  From Rainy -> Rainy: 0.06 * 0.7 = 0.041999999999999996
  From Sunny -> Rainy: 0.24 * 0.4 = 0.096
  Multiply by emission P(shop|Rainy) = 0.4 -> 0.055200000000000006

Computing P(Sunny at t=1)
  From Rainy -> Sunny: 0.06 * 0.3 = 0.018
  From Sunny -> Sunny: 0.24 * 0.6 = 0.144
  Multiply by emission P(shop|Sunny) = 0.3 -> 0.04859999999999999

--- Step 3: Recursion for observation 'clean' ---

Computing P(Rainy at t=2)
  From Rainy -> Rainy: 0.055200000000000006 * 0.7 = 0.03864
  From Sunny -> Rainy: 0.04859999999999999 * 0.4 = 0.01944
  Multiply by emission P(clean|Rainy) = 0.5 -> 0.02904

Computing P(Sunny at t=2)
  From Rainy -> Sunny: 0.055200000000000006 * 0.3 = 0.016560000000000002
  From Sunny -> Sunny: 0.04859999999999999 * 0.6 = 0.02915999999999999
  Multiply by emission P(clean|Sunny) = 0.1 -> 0.004572

--- Step 3: Termination ---
P(final in Rainy) = 0.02904
P(final in Sunny) = 0.004572

Final probability of observation sequence: 0.033612
>>> 
============== RESTART: C:/Users/AIML LAB2/Downloads/case hmm7.py ==============

--- Step 1: Initialization ---
A: 0.5 * 0.6 = 0.3
B: 0.3 * 0.3 = 0.09
C: 0.2 * 0.1 = 0.020000000000000004

--- Step 2: Observation = L ---
A -> A: 0.3 * 0.6 = 0.18
B -> A: 0.09 * 0.3 = 0.027
C -> A: 0.020000000000000004 * 0.05 = 0.0010000000000000002
A final: 0.0624
A -> B: 0.3 * 0.3 = 0.09
B -> B: 0.09 * 0.4 = 0.036
C -> B: 0.020000000000000004 * 0.15 = 0.0030000000000000005
B final: 0.05160000000000001
A -> C: 0.3 * 0.1 = 0.03
B -> C: 0.09 * 0.3 = 0.027
C -> C: 0.020000000000000004 * 0.8 = 0.016000000000000004
C final: 0.0146

--- Step 3: Observation = M ---
A -> A: 0.0624 * 0.6 = 0.037439999999999994
B -> A: 0.05160000000000001 * 0.3 = 0.01548
C -> A: 0.0146 * 0.05 = 0.0007300000000000001
A final: 0.005365
A -> B: 0.0624 * 0.3 = 0.018719999999999997
B -> B: 0.05160000000000001 * 0.4 = 0.020640000000000006
C -> B: 0.0146 * 0.15 = 0.00219
B final: 0.012465
A -> C: 0.0624 * 0.1 = 0.00624
B -> C: 0.05160000000000001 * 0.3 = 0.01548
C -> C: 0.0146 * 0.8 = 0.011680000000000001
C final: 0.023379999999999998

--- Step 3: Termination ---
P(A) = 0.005365
P(B) = 0.012465
P(C) = 0.023379999999999998

Final Probability: 0.04121

================= RESTART: C:/Users/AIML LAB2/Downloads/7bnn.py ================
Step 1: {'A': 0.3, 'B': 0.09, 'C': 0.020000000000000004}

Step 2:
A = 0.0208
B = 0.0387
C = 0.05109999999999999

Step 3:
A = 0.0079935
B = 0.011754
C = 0.010914

Final Probability: 0.0306615
