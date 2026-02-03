# poo = Programa Orientado a Objetos
# __init__ = initialize
class Person:
    """
    Define a una persona con nombre, edad, dni, correo y nacionalidad.
    """
    def __init__(self, name: str, age: int, dni: str, adress: str, nacionality: str):
        self.name = name
        if self.set_age(age):
            self.age = age
        else:
            self.age = 0
        if self.checkDni(dni):
            self.dni = dni
        else:
            self.dni = "00000000X"
        self.adress = adress
        self.nacionality = nacionality

    def set_age(self, age: int):
        if 0 <= age <= 150:
            return True
        else:
            return False

    def checkDni(self, dni):
        if len(dni) == 9 and dni[:1].isdigit() and dni[-1:].isalpha:
            letterDni = "TRWAGMYFPDXBNJZSQVHLCKE"
            calulation = int(dni[:-1]) % 23
            if letterDni[calulation] == dni[-1:].upper():
                return True
            else:
                return False

    def __str__(self):
        string = (f"name: {self.name}\n "
                  f"age: {self.age}\n "
                  f"dni: {self.dni}\n "
                  f"adress:{self.adress}\n "
                  f"nacionality: {self.nacionality}")
        return string

    def __eq__(self, other): # eq = equal
        return self.dni == other.dni

    def __gt__(self, other): # gt = greater than
        return self.age > other.age

    def __lt__(self, other): # ls = less than
        return self.age < other.age



class Person2:
    """
    Define a una persona con nombre, edad y dni, incluyendo tambien metodos adicionales.
    """
    def __init__(self, name: str, age: int, dni: str):
        self.set_name(name)
        self.set_age(age)
        self.set_dni(dni)

    def set_name(self, name: str):
        self._name = name

    def set_age(self, age: int):

        if age < 0 or age > 150:
            raise ValueError("ERROR: Introduce una edad valida.")

        self._age = age

    def set_dni(self, dni):

        if len(dni) != 9:
            raise ValueError("ERROR: El DNI debe tener 9 caracteres.")

        elif not dni[:8].isdigit():
            raise ValueError("ERROR: Los primeros 8 caracteres del DNI deben ser numeros.")

        elif not dni[-1:].isalpha():
            raise ValueError("ERROR: El ultimo carcater del DNI debe ser una letra.")

        letter_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        calculation = int(dni[:-1]) % 23

        if letter_dni[calculation] != dni[-1:].upper():
            raise ValueError("ERROR: Introduzca un DNI existente.")

        self._dni = dni

    def __str__(self):
        string = (f"name: {self.name}\n "
                  f"age: {self.age}\n "
                  f"dni: {self.dni}\n "
                  f"adress:{self.adress}\n "
                  f"nacionality: {self.nacionality}")
        return string

    def __eq__(self, other):  # eq = equal
        return self.dni == other.dni

    def __gt__(self, other):  # gt = greater than
        return self.age > other.age

    def __lt__(self, other):  # ls = less than
        return self.age < other.age

# __eq__
# __lt__
# __gt__
# __le__
# __ge__
# __ne__