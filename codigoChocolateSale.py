import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_csv(r"C:\Users\yukic\OneDrive\Área de Trabalho\conexionista\Chocolate Sales.csv")

df.columns = df.columns.str.strip()

df["Amount"] = df["Amount"].replace('[\$,]', '', regex=True).astype(float)

df["Boxes Shipped"] = pd.to_numeric(df["Boxes Shipped"])

df = df.dropna()

# escolher N itens 
N = 10
sample = df.sample(n=N)

weights = sample["Boxes Shipped"].values
prices = sample["Amount"].values

# definir capacidade (ex: 40% da soma dos pesos)
capacity = 0.4 * np.sum(weights)

print("Número de itens:", len(weights))
print("Capacidade:", capacity)

# ================= FITNESS =================
def calc_fitness(solution, weights, prices, capacity):
    value = np.sum(solution * prices)
    weight = np.sum(solution * weights)
    
    if weight > capacity:
        return 0
    return value

# ================= ALGORITMO GENÉTICO =================
def run_ga(weights, prices, capacity, popsize=100, epochs=200):
    population = np.random.randint(0, 2, (popsize, len(prices)))
    
    best_history = []
    avg_history = []
    
    for epoch in range(epochs):
        fitness = np.array([calc_fitness(ind, weights, prices, capacity) for ind in population])
        
        best_history.append(np.max(fitness))
        avg_history.append(np.mean(fitness))
        
        new_pop = []
        
        for _ in range(popsize // 2):
            # seleção (torneio)
            i, j = np.random.randint(0, popsize, 2)
            p1 = population[i] if fitness[i] > fitness[j] else population[j]
            
            i, j = np.random.randint(0, popsize, 2)
            p2 = population[i] if fitness[i] > fitness[j] else population[j]
            
            # crossover
            point = np.random.randint(len(prices))
            c1 = np.concatenate((p1[:point], p2[point:]))
            c2 = np.concatenate((p2[:point], p1[point:]))
            
            # mutação
            for c in [c1, c2]:
                if np.random.rand() < 0.05:
                    pos = np.random.randint(len(c))
                    c[pos] = 1 - c[pos]
            
            new_pop.extend([c1, c2])
        
        population = np.array(new_pop)
    
    fitness = np.array([calc_fitness(ind, weights, prices, capacity) for ind in population])
    best_idx = np.argmax(fitness)
    
    return population[best_idx], fitness[best_idx], best_history, avg_history

num_runs = 10
results = []
times = []

best_global_value = -1
best_global_solution = None

for run in range(num_runs):
    start = time.time()
    
    sol, val, best_hist, avg_hist = run_ga(weights, prices, capacity)
    
    end = time.time()
    
    results.append(val)
    times.append(end - start)
    
    if val > best_global_value:
        best_global_value = val
        best_global_solution = sol

# ================= RESULTADOS =================
best_weight = np.sum(best_global_solution * weights)

print("\n" + "="*50)
print("RESULTADOS")
print("="*50)

print("Melhor valor encontrado:", best_global_value)
print("Média dos resultados:", np.mean(results))
print("Tempo médio:", np.mean(times))

print("\nMelhor solução:", best_global_solution)
print("Peso total:", best_weight)
print("Capacidade:", capacity)

# ================= GRÁFICO =================
plt.plot(best_hist, label="Best Fitness")
plt.plot(avg_hist, label="Average Fitness")
plt.title("Convergência do Algoritmo Genético")
plt.xlabel("Gerações")
plt.ylabel("Fitness")
plt.legend()
plt.grid()
plt.show()

