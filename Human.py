class Human():

    name = "John"
    leftArm = 1
    rightArm = "right arm"Л
    leftLeg = 3
    rightLeg = 4
    body = 5
    head = 6

    def walk(self):
        print(self.name + " walks")

    def eat(self):
        print(self.name + " eats with " + self.rightArm)


if __name__ == "__main__":
     human = Human()
     human.eat()
     newName = "Jackson"
     print(human.name + " Changed name to " + newName)
     human.name = newName
     print("Name changed")
     human.eat()