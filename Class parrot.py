class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.age = age
        self.name = name
blue = parrot("blue",10)
woo = parrot("woo",15)
print("blue is a {}".format(blue.species))
print("woo is a {}".format(woo.species))
print(" {} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(woo.name,woo.age))