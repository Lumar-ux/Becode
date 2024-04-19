# def diviseurs(n):
#     liste_diviseurs = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             liste_diviseurs.append(i)
#     return liste_diviseurs

# # Demander à l'utilisateur d'entrer un nombre
# nombre = int(input("Entrez un nombre : "))

# # Afficher les diviseurs du nombre donné
# print(f"Les diviseurs de {nombre} sont :", diviseurs(nombre))



import re
def order(sentence):
    sen_split = sentence.split()
    print(sen_split)
    for i, name in enumerate(sentence):
        print(name)
        sort_nb=sorted(filter(lambda x: x==re.findall("[0-9]", name[i]))
        
        
    return(sort_nb)
print(order("is2 Thi1s T4est 3a"))
