class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 10
        self.health = 10
        self.age = 0
 
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
        else:
            self.health -= 1
 
    def play(self):
        if self.happiness < 10:
            self.happiness += 1
        else:
            self.hunger += 1
 
    def sleep(self):
        if self.health < 10:
            self.health += 1
 
    def display(self):
        print("Name: ", self.name)
        print("Hunger: ", self.hunger)
        print("Happiness: ", self.happiness)
        print("Health: ", self.health)
        print("Age: ", self.age)
 
 
def main():
    pet = Tamagotchi("Pet")
    while True:
        print("What would you like to do with your Tamagotchi?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Display Status")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.sleep()
        elif choice == 4:
            pet.display()
        elif choice == 5:
            break
        pet.age += 1
 
 
if __name__ == "__main__":
    main()