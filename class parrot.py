class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu=parrot("Blu", 10)
woody=parrot("Woody", 15)


print("blu is a {}".format(blu.species))
print("woody is also a {}".format(woody.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woody.name, woody.age))