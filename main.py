
def tri_personnalise(e):
    return len(e)

def afficher(collection, nb=-1):
    # collection.sort(reverse=True, key=tri_personnalise)
    c = collection
    if not nb == -1:
        c = collection[:nb]
    nb_pizzas = len(c)
    if nb_pizzas == 0 :
        print("AUCUNE PIZZA")
        return

    print(f"---------LISTES DE PIZZAS {nb_pizzas}--------")
    for i in range(nb_pizzas):
        print("Nom de pizza: "+ c[i])
    print()
    print("La premiere pizzas est : "+ c[0])
    print("la derrniere pizzas est : "+ c[-1])


def ajouter_pizzas_utilisateur(colletion):
    p = input("Pizza a ajouter : ")
    if p.lower() in colletion:
        print("ERREUR : cette pizzas existe deja")
    else:
        colletion.append(p)


def pizzas_existe(t, collection):
    for i in collection:
        if i == t:
            return True
    return False


pizzas = ["4 fromages", "vegtarienne", "hawai", "calzone"]

ajouter_pizzas_utilisateur(pizzas)
afficher(pizzas, 2)