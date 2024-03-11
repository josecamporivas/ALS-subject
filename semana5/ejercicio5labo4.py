"""
El enunciado del guión anterior indicaba:
crea un programa que permita guardar y hacer búsquedas sobre pares de (nombre, e.mail).
El programa presentará un menú principal, con las opciones introducir, borrar y buscar. Al introducir datos,
se pide un nombre y un e.mail, y se guardan. Para borrar, sólo se pide el nombre, se busca y se borra.
Para buscar, sólo se pide el nombre, se busca y se muestra. Para ello, se pedía utilizar un diccionario,
junto con las opciones: insertar, borrar, buscar y listar.

Repite el ejercicio anterior encapsulando cada par en una clase. Existirán dos clases de contactos: amigos y trabajo,
este último guardando también el e.mail de la empresa.
"""


class Contacto:
    def __init__(self, nombre: str, email: str):
        self.__nombre = nombre
        self.__email = email

    @property
    def nombre(self):
        return self.__nombre

    @property
    def email(self):
        return self.__email

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @email.setter
    def email(self, value):
        self.__email = value

    def __str__(self):
        return f"{self.nombre}: {self.email}"


class Amigo(Contacto):
    def __init__(self, nombre: str, email: str):
        super().__init__(nombre, email)


class Trabajo(Contacto):
    def __init__(self, nombre: str, email: str, empresa: str):
        super().__init__(nombre, email)
        self.__empresa_email = empresa

    @property
    def empresa_email(self):
        return self.__empresa_email

    @empresa_email.setter
    def empresa_email(self, value):
        self.__empresa_email = value

    def __str__(self):
        return f"{self.nombre}: {self.email} ({self.empresa_email})"


if __name__ == "__main__":
    lista_contactos = []
    while True:
        print("1. Insertar")
        print("2. Borrar")
        print("3. Buscar")
        print("4. Listar")
        print("5. Salir")
        opcion = int(input("Opción: "))

        match opcion:
            case 1:
                print("1. Amigo")
                print("2. Trabajo")
                tipo = int(input("Tipo: "))
                nombre = input("Nombre: ")
                email = input("Email: ")
                if tipo == 1:
                    contacto = Amigo(nombre, email)
                else:
                    empresa = input("Empresa: ")
                    contacto = Trabajo(nombre, email, empresa)
                lista_contactos.append(contacto)

            case 2:
                nombre = input("Nombre: ")
                for i, contacto in enumerate(lista_contactos):
                    if contacto.nombre == nombre:
                        del lista_contactos[i]
                        break
                else:
                    print("No encontrado")

            case 3:
                nombre = input("Nombre: ")
                for contacto in lista_contactos:
                    if contacto.nombre == nombre:
                        print(contacto)
                        break
                else:
                    print("No encontrado")

            case 4:
                for contacto in lista_contactos:
                    print(contacto)

            case 5:
                break

            case _:
                print("Opción no válida")
                continue
