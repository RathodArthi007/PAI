# Constraint Satisfaction Problem using Backtracking

# User input
variables = input("Enter variables (space separated): ").split()
domain = list(map(int, input("Enter domain values (space separated): ").split()))

# Constraints: variable pairs that must not be equal
constraints = []
n = int(input("Enter number of constraints (Xi != Xj): "))

for _ in range(n):
    x, y = input("Enter constraint (Xi Xj): ").split()
    constraints.append((x, y))

# Create domain dictionary
domains = {var: domain for var in variables}

# Check constraints
def is_valid(var, value, assignment):
    for (x, y) in constraints:
        if var == x and y in assignment and assignment[y] == value:
            return False
        if var == y and x in assignment and assignment[x] == value:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = next(v for v in variables if v not in assignment)

    for value in domains[var]:
        if is_valid(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]

    return None

# Solve CSP
solution = backtrack({})

if solution:
    print("\nSolution Found:")
    for var in solution:
        print(f"{var} = {solution[var]}")
else:
    print("\nNo solution exists")
