# 6. Tinder - create a class called Person which stores name and sex
# p1 = Person("vishnu", "male"); p2 = Person("swetha", "female")

# Create a class called MatchMaker which has the following methods.
# The class is responsible for storing and managing the users.
# register(person)
# - Keep track of the users who are registered. You can use any data type to store these users.
# - A user should not be registered multiple times(only one user with the same name).
# e.g m = MatchMaker(); m.register(p1); m.register(p2); m.register(Person("megan", "female");
# m.register(Person("karthik", "male"))

# users()
# - Returns all the registered users names. Could return a set or list
# m.users() # ["vishnu", "swetha", "megan", "karthik"]

# swipe(user1, user2, action)
# - Keep track of who liked/didn't like whom
# e.g ; m.swipe("vishnu", "swetha", "right") # means vishnu swiped right swetha (vishnu likes swetha)
# m.swipe("vishnu", "megan", "left") # means vishnu swiped left megan (vishnu does not like megan)
# - Note it is not valid if the users are the same sex. e.g m.swipe("vishnu", "karthik", "right") will not do anything

# likes(user)
# - Return the list of people liked(swipe right) by the user
# m.likes("vishnu") # ["swetha"] since vishnu swiped right only swetha

# recommend(user)
# - Return the list of people who the user can like (only registered users and of different sex)
# - Should not return the existing swiped left or right people by the user

class Person:
    def __init__(self, name, sex, age, sexuality):
        self.name = name
        self.sex = sex
        self.age = age
        self.sexuality = sexuality


class Straight:
    def __init__(self):
        self.reg = {}
        self.action = {}

    def register(self, person):
        if person.name not in self.reg:
            self.reg[person.name] = person  # (value=object)

    def users(self):
        return list(self.reg.keys())

    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                person1 = self.reg[user1]
                person2 = self.reg[user2]
                if person1.sexuality == "straight" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and person1.sex != person2.sex \
                        and (person2.sexuality == "straight" or person2.sexuality == "bisexual"):
                    recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")
        return recommendations

    def act(self, user1):
        like = []
        dislike = []
        if user1 in self.action:
            for action in self.action[user1]:
                if action[1] == "like":
                    like.append(action[0])
                elif action[1] == "dislike":
                    dislike.append(action[0])
        return [like, dislike]

    def likes(self, user1):
        return self.act(user1)[0]

    def dislikes(self, user1):
        return self.act(user1)[1]

    def swipe(self, user1, user2, action):
        if user1 in self.reg and user2 in self.reg:
            if user2 in self.recommend(user1):
                if action == "right":
                    if user1 not in self.action:
                        self.action[user1] = [(user2, "like")]
                    else:
                        self.action[user1].append((user2, "like"))
                elif action == "left":
                    if user1 not in self.action:
                        self.action[user1] = [(user2, "dislike")]
                    else:
                        self.action[user1].append((user2, "dislike"))
            else:
                print("Error - Preferences of users do not match")
        elif user1 in self.reg and user2 not in self.reg:
            print("Error -", user2, "isn't a registered tinder user")
        elif user1 not in self.reg and user2 in self.reg:
            print("Error -", user1, "isn't a registered tinder user")
        else:
            print("Error -", user1, "and", user2, "aren't registered tinder users")


class Bisexual(Straight):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                person1 = self.reg[user1]
                person2 = self.reg[user2]
                if person1.sexuality == "bisexual" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and (person2.sexuality == "bisexual"
                             or (person2.sexuality == "straight" and person1.sex != person2.sex)
                             or (person2.sexuality == "gay" and person1.sex == "male")
                             or (person2.sexuality == "lesbian" and person1.sex == "female")):
                    recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations


class Gay(Straight):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                person1 = self.reg[user1]
                person2 = self.reg[user2]
                if person1.sexuality == "gay" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and person2.sex == "male" \
                        and (person2.sexuality == "gay" or person2.sexuality == "bisexual"):
                    recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations



class Lesbian(Straight):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                person1 = self.reg[user1]
                person2 = self.reg[user2]
                if person1.sexuality == "lesbian" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and person2.sex == "female" \
                        and (person2.sexuality == "lesbian" or person2.sexuality == "bisexual"):
                    recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations


p1 = Person("Harry", "male", 29, "straight")
p2 = Person("Ginny", "female", 23, "straight")
p3 = Person("Maya", "female", 26, "lesbian")
p4 = Person("Romilda", "female", 27, "straight")
p5 = Person("Hermoine", "female", 29, "straight")

straight = Straight()
bisexual = Bisexual()
gay = Gay()
lesbian = Lesbian()
straight.register(p1)
straight.register(p2)
straight.register(p4)
straight.register(Person("Megan", "female", 27, "bisexual"))
straight.register(Person("Clark", "male", 27, "bisexual"))
straight.register(Person("John", "male", 30, "gay"))
straight.register(Person("Abraham", "male", 28, "gay"))
straight.register(Person("George", "male", 28, "gay"))
straight.register(Person("Samantha", "female", 25, "lesbian"))
straight.register(p3)

print("registered users =", straight.users())

bisexual.register(p1)
bisexual.register(p2)
bisexual.register(p4)
bisexual.register(Person("Megan", "female", 27, "bisexual"))
bisexual.register(Person("Clark", "male", 27, "bisexual"))
bisexual.register(Person("John", "male", 30, "gay"))
bisexual.register(Person("Abraham", "male", 28, "gay"))
bisexual.register(Person("George", "male", 28, "gay"))
bisexual.register(Person("Samantha", "female", 25, "lesbian"))
bisexual.register(p3)

print("registered users =", bisexual.users())

gay.register(p1)
gay.register(p2)
gay.register(p4)
gay.register(Person("Megan", "female", 27, "bisexual"))
gay.register(Person("Clark", "male", 27, "bisexual"))
gay.register(Person("John", "male", 30, "gay"))
gay.register(Person("Abraham", "male", 28, "gay"))
gay.register(Person("George", "male", 28, "gay"))
gay.register(Person("Samantha", "female", 25, "lesbian"))
gay.register(p3)

print("registered users =", gay.users())

lesbian.register(p1)
lesbian.register(p2)
lesbian.register(p4)
lesbian.register(Person("Megan", "female", 27, "bisexual"))
lesbian.register(Person("Clark", "male", 27, "bisexual"))
lesbian.register(Person("John", "male", 30, "gay"))
lesbian.register(Person("Abraham", "male", 28, "gay"))
lesbian.register(Person("George", "male", 28, "gay"))
lesbian.register(Person("Samantha", "female", 25, "lesbian"))
lesbian.register(p3)

print("registered users =", lesbian.users())

print("recommendations for Harry =", straight.recommend("Harry"))
print("recommendations for Ginny =", straight.recommend("Ginny"))
print("recommendations for Romilda =", straight.recommend("Romilda"))
print("recommendations for Hermoine =", straight.recommend("Hermoine"))

print("recommendations for Megan =", bisexual.recommend("Megan"))
print("recommendations for Clark =", bisexual.recommend("Clark"))

print("recommendations John =", gay.recommend("John"))
print("recommendations Abraham =", gay.recommend("Abraham"))
print("recommendations George =", gay.recommend("George"))

print("recommendations Maya =", lesbian.recommend("Maya"))
print("recommendations Samantha =", lesbian.recommend("Samantha"))

straight.swipe("Harry", "Ginny", "right")
straight.swipe("Harry", "Romilda", "left")
straight.swipe("John", "Abraham", "right")
straight.swipe("John", "George", "left")
straight.swipe("Ginny", "Harry", "right")

print("Harry likes =", straight.likes("Harry"))
print("Harry dislikes =", straight.dislikes("Harry"))
print("John likes =", straight.likes("John"))
print("John dislikes =", straight.dislikes("John"))
print("Ginny likes =", straight.likes("Ginny"))
print("Ginny dislikes =", straight.dislikes("Ginny"))

print("recommendations for Harry =", straight.recommend("Harry"))
print("recommendations John =", straight.recommend("John"))

print("recommendations for Ginny =", straight.recommend("Ginny"))
