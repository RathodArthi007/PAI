import pandas as pd

data = pd.DataFrame({
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

print(data)

P_Rain = data['Rain'].value_counts(normalize=True)
print(P_Rain)

P_Traffic_given_Rain = pd.crosstab(
    data['TrafficJam'], data['Rain'], normalize='columns'
)
print(P_Traffic_given_Rain)

P_Late_given_Traffic = pd.crosstab(
    data['ArriveLate'], data['TrafficJam'], normalize='columns'
)
print(P_Late_given_Traffic)

def infer_arrive_late(rain_value):
    result = {}
    for arrive in ['Yes', 'No']:
        prob = 0
        for traffic in ['Yes', 'No']:
            p1 = P_Late_given_Traffic.loc[arrive, traffic]
            p2 = P_Traffic_given_Rain.loc[traffic, rain_value]
            prob += p1 * p2
        result[arrive] = prob
    return result

print(infer_arrive_late('Yes'))
print(infer_arrive_late('No'))
