class Human:
    species = "Homo sapiens"
    def get_age(self):
        print("Retrieving age.")
        return self._age
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age,)

guido = Human()
guido.age = 0
guido.age = False
guido.age = 99
guido.age