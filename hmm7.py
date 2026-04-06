states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']
start_prob = {
    'Rainy': 0.6,
    'Sunny': 0.4
}
transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}
emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}
obs_sequence = ['walk', 'shop', 'clean']
def forward_algorithm_stepwise(states, observations, start_prob, transition_prob, emission_prob):
    forward = []
    print("\n--- Step 1: Initialization ---")
    f0 = {}
    for state in states:
        f0[state] = start_prob[state] * emission_prob[state][observations[0]]
        print(f"P({state} at t=0) = {start_prob[state]} * {emission_prob[state][observations[0]]} = {f0[state]}")
    forward.append(f0)
    for t in range(1, len(observations)):
        print(f"\n--- Step {t+1}: Recursion for observation '{observations[t]}' ---")
        ft = {}
        for current_state in states:
            total = 0
            print(f"\nComputing P({current_state} at t={t})")
            for previous_state in states:
                value = (
                    forward[t-1][previous_state]
                    * transition_prob[previous_state][current_state]
                )
                print(
                    f"  From {previous_state} -> {current_state}: "
                    f"{forward[t-1][previous_state]} * {transition_prob[previous_state][current_state]} = {value}"
                )
                total += value
            ft[current_state] = total * emission_prob[current_state][observations[t]]
            print(
                f"  Multiply by emission P({observations[t]}|{current_state}) = {emission_prob[current_state][observations[t]]}"
                f" -> {ft[current_state]}"
            )

        forward.append(ft)
    print("\n--- Step 3: Termination ---")
    total_probability = 0
    for state in states:
        total_probability += forward[-1][state]
        print(f"P(final in {state}) = {forward[-1][state]}")

    print("\nFinal probability of observation sequence:", total_probability)
    return total_probability         
result = forward_algorithm_stepwise(
    states,
    obs_sequence,
    start_prob,
    transition_prob,
    emission_prob
)
