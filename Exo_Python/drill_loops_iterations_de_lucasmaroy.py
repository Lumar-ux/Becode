# -*- coding: utf-8 -*-
"""drill-loops-iterations de LucasMaroy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dj04v1Mn-EnGwdlqSSTOTQ8Mz9iGByZ5

# Drill loops and iterations

### 1. Display all students in the `students` list in alphabetical order.
"""

students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
print(sorted(students))

"""### 2. Display only the names which begin with the letter "M"."""

name_m=[]
for nom in students:
  if nom.startswith("M"):
      name_m.append(nom)
print(name_m)

"""### 3. Display integers from 0 to 15 not included, using a `for` loop and the `range()` instruction."""

for i in range(1,16):
  print(i)

"""### 4. Create a `for` loop that displays integers from 1 to 10 included, but use the `break` instruction to interrupt it at 5."""

for i in range(1,10):
  if i == 5:
    break
  print(i)

"""### 4. Create a `for` loop that displays integers from 1 to 10 included, but use the `continue` to modify its execution at 5."""

for i in range(1,11):
  if i == 5:
    continue
  print(i)

"""### 6. Follow the instructions :

- **Sort and display the list.**
    - Output expected: `[10, 17, 25, 38, 72]`
- **Add item 12 to the list and display the list.**
    - Output expected: `[17, 38, 10, 25, 72, 12]`
- **Reverse and display the list.**
    - Output expected: `[12, 72, 25, 10, 38, 17]`
- **Display the index of element 17.**
    - Output expected: `5`
- **Remove item 38 and display the list.**
    - Output expected: `[12, 72, 25, 10, 17]`
- **Display the sub-list of the 2nd to 3rd element.**
    - Output expected: `[72, 25]`
- **Display the sub-list from the beginning to the 2nd element.**
    - Output expected: `[12, 72]`
- **Display the sub-list of the 3rd element at the end of the list.**
    - Output expected: `[25, 10, 17]`
- **Display the complete sub-list of the list.**
    - Output expected: `[12, 72, 25, 10, 17]`
- **Display the last element using a negative indication.**
    - Output expected: `[17]`
"""

list_of_numbers = [17, 38, 10, 25, 72]

print(sorted(list_of_numbers))
list_of_numbers.append(12)
print(list_of_numbers)
num_revers = list(reversed(list_of_numbers))
print(num_revers)
print(num_revers.index(17))
num_revers.remove(38)
print(num_revers)
spec = num_revers[1:3]
print(spec)
spec = num_revers[:2]
print(spec)
spec = num_revers[2:]
print(spec)
print(num_revers)
print(num_revers[-1:])
# Code here

"""Note that some list methods do not return anything.

### 7. Write an algorithm that:
1. Asks the user to enter a number.
2. Make sure that your program displays all the numbers down to 0. For example, if the user enters the number 3, then your program will display something like this: `3,2,1,0`
"""

number = int(input("Enter a number: "))
number = number + 1
lt=[]
for i in range(0, number):
    lt.append(i)
num=lt[::-1]
for n in num:
    print(str(n))

"""### 8.The price is right !
- Create a variable that will contain the number to be found.
- Then create a function that will ask the user to find this price (asking for a number).
- If the user enters a number that is too high, output the sentence: "It's less.".
- If he enters a number that is too low, output the sentence: "It's more.".
- If the user finds the right price, output the sentence: "Well done, you won!".
"""

find1=7
def choose(find1):
    n=1
    name1=input("Entrez un nom de joueur : ")
    shooc=int(input("Essaye de trouver le numéro : "))
    while shooc > 100 or shooc < 0:
        shooc=int(input("Essaye de trouver le numéro  : "))
    # for i in range(10):
    while shooc != find1:
        n=n+1
        if n == 11:
            print(f"{name1}, You failed, try again!")
            break
        if n <= 10:
            if shooc > find1:
                print("Le numéro choisi est plus grand")
                shooc=int(input("Essaye de trouver le numéro : "))
            elif shooc < find1:
                print("Le numéro choisi est plus petit")
                shooc=int(input("Essaye de trouver le numéro  : "))
    if shooc == find1:
        print(f"Player {name1}, Vous avez deviné le bon chiffre en {n} tours")
        msg=True
    return(msg)
print(choose(find1))

"""### 9. Display all students with the sentence "NAME is an alumni. "
"""

all_students = [
    ["David", "Justine", "Valentin", "Axel", "Redouane"],
    ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"],
]
for name in all_students[0]:
  print(f"{name} is an alumni.")
for name in all_students[1]:
  print(f"{name} is an alumni.")

"""**10. Display all elements. If the element is part of the first list, display - `"ELEMENT_HERE is a backend language?"` - and if the element is part of the second list, display - `"ELEMENT_HERE is a frontend language?"`**"""

languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
for name in all_students[0]:
  print("ELEMENT_HERE is a backend language?")
for name in all_students[1]:
  print("ELEMENT_HERE is a frontend language?")