"""
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
PassengerId: Identificador del pasajero
Survived: 0 = No, 1 = Sí
Pclass: Clase del pasajero (1, 2 o 3)
Name: Nombre
Sex: Sexo (male/female)
Age: Edad

Ejercicio: Utilizando titanic.csv y lambdas. Calcula:
- La cantidad de pasajeros que sobrevivieron para cada una de las clases (1, 2 y 3)
"""

import csv

def get_list_survivors(nf: str):
    toret = []
    with open(nf, "rt") as f:
        reader = csv.DictReader(f, ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age'], delimiter=",")
        for row in reader:
            if row['Survived'] == '1':
                del row[None]
                toret.append(row)
    return toret

def get_survivors_by_class(l: list):
    class_1 = len(list(filter(lambda x: x['Pclass'] == '1', l)))
    class_2 = len(list(filter(lambda x: x['Pclass'] == '2', l)))
    class_3 = len(list(filter(lambda x: x['Pclass'] == '3', l)))

    return {"class_1": class_1, "class_2": class_2, "class_3": class_3, "total": len(l)}

list_survivors = get_list_survivors("titanic.csv")
survivors_by_class = get_survivors_by_class(list_survivors)
print(f"Class 1: {survivors_by_class['class_1']} ({survivors_by_class['class_1'] / survivors_by_class['total'] * 100:.2f}%)")
print(f"Class 2: {survivors_by_class['class_2']} ({survivors_by_class['class_2'] / survivors_by_class['total'] * 100:.2f}%)")
print(f"Class 3: {survivors_by_class['class_3']} ({survivors_by_class['class_3'] / survivors_by_class['total'] * 100:.2f}%)")
