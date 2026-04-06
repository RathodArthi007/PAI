
states = ['A', 'B', 'C']   # A=Interested, B=Neutral, C=Disengaged

obs_sequence = ['H', 'L', 'M']  # H=HighClick, L=LongSession, M=LowClick
start_prob = {'A': 0.5, 'B': 0.3, 'C': 0.2}
transition_prob = {
    'A': {'A': 0.6, 'B': 0.3, 'C': 0.1},
    'B': {'A': 0.3, 'B': 0.4, 'C': 0.3},
    'C': {'A': 0.05, 'B': 0.15, 'C': 0.8}
}
emission_prob = {
    'A': {'H': 0.6, 'L': 0.3, 'M': 0.1},
    'B': {'H': 0.3, 'L': 0.4, 'M': 0.3},
    'C': {'H': 0.1, 'L': 0.2, 'M': 0.7}
}
def forward_hmm():
    forward = []
    print("\n--- Step 1: Initialization ---")
    f0 = {}
    for s in states:
        f0[s] = start_prob[s] * emission_prob[s][obs_sequence[0]]
        print(f"{s}: {start_prob[s]} * {emission_prob[s][obs_sequence[0]]} = {f0[s]}")
    forward.append(f0)
    for t in range(1, len(obs_sequence)):
        print(f"\n--- Step {t+1}: Observation = {obs_sequence[t]} ---")
        ft = {}
        for curr in states:
            total = 0
            for prev in states:
                val = forward[t-1][prev] * transition_prob[prev][curr]
                total += val
                print(f"{prev} -> {curr}: {forward[t-1][prev]} * {transition_prob[prev][curr]} = {val}")

            ft[curr] = total * emission_prob[curr][obs_sequence[t]]
            print(f"{curr} final: {ft[curr]}")
        forward.append(ft)
    print("\n--- Step 3: Termination ---")
    result = 0
    for s in states:
        print(f"P({s}) = {forward[-1][s]}")
        result += forward[-1][s]
    print("\nFinal Probability:", result)
forward_hmm()


