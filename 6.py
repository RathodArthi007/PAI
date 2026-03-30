from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd
data = pd.DataFrame({
    'Income_Stability': ['High', 'High', 'Low', 'Low', 'High', 'Low', 'High', 'Low'],
    'Credit_History': ['Good', 'Good', 'Bad', 'Good', 'Bad', 'Bad', 'Good', 'Bad'],
    'Employment_Type': ['Permanent', 'Contract', 'Contract', 'Permanent', 'Contract', 'Permanent', 'Permanent', 'Contract'],
    'Default_Risk': ['Low', 'Low', 'High', 'Low', 'High', 'High', 'Low', 'High']
})
data = data.astype('category')

model = DiscreteBayesianNetwork([
    ('Income_Stability', 'Default_Risk'),
    ('Credit_History', 'Default_Risk'),
    ('Employment_Type', 'Default_Risk')
])

model.fit(data)

for cpd in model.get_cpds():
    print(cpd)

inference = VariableElimination(model)


result = inference.query(
    variables=['Default_Risk'],
    evidence={'Income_Stability': 'Low', 'Credit_History': 'Bad'}
)

print("\nPredicted Default Risk Probability:")
print(result)
