class Human:
    species = "Homo sapiens"
    def get_age(self):
        print("Retrieving age.")
        return self._age
    def set_age(self,age):
        print(f"Setting age {age}")
        self._age = age

    age = property(get_age,set_age)