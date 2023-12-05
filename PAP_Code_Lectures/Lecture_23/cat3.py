class Cat:

    species = "Felis catus"

    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Cat("Tom", 13)
# print(tom.name)

gerry = Cat("Gerry", 17)
# print(gerry.name)


print(f"specie della classe: {Cat.species}")
tom.species = "gattaccio"
print(f"specie di Tom dopo la modifica: {tom.species}")
print(f"specie di Gerry dopo la modifica: {gerry.species}")
Cat.species = "gattino"
print(f"specie di Tom dopo la modifica della classe: {tom.species}")
print(f"specie di Gerry dopo la modifica della classe: {gerry.species}")
