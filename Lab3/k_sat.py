import random 

def generate_k_sat(k, m, n):
    formula = []

    for i in range(m):
        clause = []
        variables = random.sample(range(1, n+1), k) 
        for variable in variables:
            if random.random() < 0.5: 
                clause.append(variable)
            else:
                clause.append(-variable)
        formula.append(clause)

    return formula

arr = [int(x) for x in input().split()]

k = arr[0]
m = arr[1]
n = arr[2]

formula = generate_k_sat(k, m, n)
print(formula)