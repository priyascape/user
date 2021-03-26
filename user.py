class Profile:
    def __init__(self, name = "Unknown", age=70): 
        print("hello from init!")
        self.name = name
        self.age = age
        self.favePrimes = []
    def printMe(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        print(f"My fav prime numbers are {self.favePrimes}")
        return self
    def resetMe(self):
        self.name = "blank"
        self.age = 0
        self.printMe()
        return self
    def addPrime(self, num):
        self.favePrimes.append(num)
        return self
    def secondPrime(self):
        return self.favePrimes[1]

priyaProfile = Profile(name="Priya", age=45)
# rajiv = Profile("Locahana", 52)
# unknown = Profile()
# priyaProfile.resetMe()
# print(priyaProfile.name)
# print(rajiv.name)
# print(unknown.name)

priyaProfile.addPrime(173).addPrime(7).addPrime(19)
priyaProfile.printMe()