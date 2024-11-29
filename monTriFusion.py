def fusionner_tableaux(tableauGauche, tableauDroite):
    tableauTrie = []  # Tableau vide pour stocker les éléments triés
    indiceTableauGauche = 0
    indiceTableauDroite = 0

    # Tant que les deux tableaux contiennent encore des éléments
    while indiceTableauGauche < len(tableauGauche) and indiceTableauDroite < len(tableauDroite):
        if tableauGauche[indiceTableauGauche] <= tableauDroite[indiceTableauDroite]:
            tableauTrie.append(tableauGauche[indiceTableauGauche])
            indiceTableauGauche += 1
        else:
            tableauTrie.append(tableauDroite[indiceTableauDroite])
            indiceTableauDroite += 1

    # Ajouter les éléments restants de tableauGauche (s'il y en a)
    tableauTrie.extend(tableauGauche[indiceTableauGauche:])

    # Ajouter les éléments restants de tableauDroite (s'il y en a)
    tableauTrie.extend(tableauDroite[indiceTableauDroite:])

    return tableauTrie

def tri_fusion(tableau):
    # Cas de base (arrêt de la recursivité): un tableau de longueur <= 1 est déjà trié
    if len(tableau) <= 1:
        return tableau

    # Diviser le tableau en deux parties
    milieu = len(tableau) // 2
    tableauGauche = tableau[:milieu]
    tableauDroite = tableau[milieu:]

    # Appels récursifs pour trier chaque partie
    tableauGauche = tri_fusion(tableauGauche)
    tableauDroite = tri_fusion(tableauDroite)

    # Fusionner les deux parties triées
    return fusionner_tableaux(tableauGauche, tableauDroite)

# Exemple d'utilisation
if __name__ == "__main__":
    tableau = [38, 27, 43, 3, 9, 82, 10]
    print("Tableau non trié :", tableau)
    resultat = tri_fusion(tableau)
    print("Tableau trié :", resultat)
