import time
import random
import pandas as pd

# Générer un tableau de 20000 valeurs aléatoires
tableau = [random.randint(0, 100000) for _ in range(20000)]

# Implémentation des algorithmes de tri
def tri_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tri_selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def tri_fusion(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = tri_fusion(arr[:mid])
    right = tri_fusion(arr[mid:])
    return fusionner(left, right)

def fusionner(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Fonction pour mesurer le temps d'exécution
def mesurer_temps(algorithme, tableau):
    tableau_copie = tableau.copy()
    debut = time.time()
    if algorithme == tri_fusion:
        tableau_copie = algorithme(tableau_copie)  # tri_fusion retourne un nouveau tableau
    else:
        algorithme(tableau_copie)  # Ces algorithmes modifient directement le tableau
    fin = time.time()
    return fin - debut

# Comparer les temps d'exécution sans le tri rapide
algorithmes = {
    "Tri par insertion": tri_insertion,
    "Tri par sélection": tri_selection,
    "Tri par fusion": tri_fusion
}

resultats = {}
for nom, algo in algorithmes.items():
    temps = mesurer_temps(algo, tableau)
    resultats[nom] = temps

# Afficher les résultats sous forme de tableau
resultats_df = pd.DataFrame(resultats.items(), columns=["Algorithme", "Temps (secondes)"])
print(resultats_df)
