# States (A = Interested, B = Neutral, C = Disengaged)
states = ['A', 'B', 'C']
obs = ['H', 'L', 'M']  # H=HighClick, L=LowClick, M=Medium/Long
start = {'A': 0.5, 'B': 0.3, 'C': 0.2}
transition = {
    'A': {'A': 0.6, 'B': 0.3, 'C': 0.1},
    'B': {'A': 0.3, 'B': 0.4, 'C': 0.3},
    'C': {'A': 0.05, 'B': 0.15, 'C': 0.8}
}
emission = {
    'A': {'H': 0.6, 'L': 0.1, 'M': 0.3},
    'B': {'H': 0.3, 'L': 0.3, 'M': 0.4},
    'C': {'H': 0.1, 'L': 0.7, 'M': 0.2}
}
def forward_hmm():
    f = []
    f0 = {}
    for s in states:
        f0[s] = start[s] * emission[s][obs[0]]
    f.append(f0)
    print("Step 1:", f0)
    for t in range(1, len(obs)):
        ft = {}
        print(f"\nStep {t+1}:")
        for curr in states:
            total = 0
            for prev in states:
                total += f[t-1][prev] * transition[prev][curr]
            ft[curr] = total * emission[curr][obs[t]]
            print(curr, "=", ft[curr])
        f.append(ft)
    result = sum(f[-1].values())
    print("\nFinal Probability:", result)
forward_hmm()
