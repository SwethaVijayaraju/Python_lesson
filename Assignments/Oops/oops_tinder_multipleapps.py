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


class MatchMaker:
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
                if user2 != user1 and user2 not in likes and user2 not in dislikes and self.reg[user1].sex != self.reg[
                    user2].sex:
                    if self.reg[user2].sexuality == "straight" or self.reg[user2].sexuality == "bisexual":
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


class Bisexual(MatchMaker):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                if user2 != user1 and user2 not in likes and user2 not in dislikes:
                    if self.reg[user2].sexuality == "bisexual":
                        recommendations.append(user2)
                    elif self.reg[user2].sexuality == "straight" and self.reg[user1].sex != self.reg[user2].sex:
                        recommendations.append(user2)
                    elif self.reg[user2].sexuality == "gay" and self.reg[user1].sex == "male":
                        recommendations.append(user2)
                    elif self.reg[user2].sexuality == "lesbian" and self.reg[user1].sex == "female":
                        recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations


class Gay(MatchMaker):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                if user2 != user1 and user2 not in likes and user2 not in dislikes and self.reg[user2].sex == "male":
                    if self.reg[user2].sexuality == "gay" or self.reg[user2].sexuality == "bisexual":
                        recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations


class Lesbian(MatchMaker):
    def recommend(self, user1):
        recommendations = []
        if user1 in self.reg:
            likes = self.likes(user1)
            dislikes = self.dislikes(user1)
            for user2 in self.users():
                if user2 != user1 and user2 not in likes and user2 not in dislikes and self.reg[user2].sex == "female":
                    if self.reg[user2].sexuality == "lesbian" or self.reg[user2].sexuality == "bisexual":
                        recommendations.append(user2)
        else:
            print("Hi", user1, "! You are just 1 step away from registering!")

        return recommendations


p1 = Person("Harry", "male", 29, "straight")
p2 = Person("Ginny", "female", 23, "straight")
p3 = Person("Maya", "female", 26, "lesbian")
p4 = Person("Romilda", "female", 27, "straight")
p5 = Person("Hermoine", "female", 29, "straight")

m = MatchMaker()
s1 = Bisexual()
s2 = Gay()
s3 = Lesbian()
m.register(p1)
m.register(p2)
m.register(p4)
m.register(Person("Megan", "female", 27, "bisexual"))
m.register(Person("Clark", "male", 27, "bisexual"))
m.register(Person("John", "male", 30, "gay"))
m.register(Person("Abraham", "male", 28, "gay"))
m.register(Person("George", "male", 28, "gay"))
m.register(Person("Samantha", "female", 25, "lesbian"))
m.register(p3)

print("registered users =", m.users())

s1.register(p1)
s1.register(p2)
s1.register(p4)
s1.register(Person("Megan", "female", 27, "bisexual"))
s1.register(Person("Clark", "male", 27, "bisexual"))
s1.register(Person("John", "male", 30, "gay"))
s1.register(Person("Abraham", "male", 28, "gay"))
s1.register(Person("George", "male", 28, "gay"))
s1.register(Person("Samantha", "female", 25, "lesbian"))
s1.register(p3)

print("registered users =", s1.users())

s2.register(p1)
s2.register(p2)
s2.register(p4)
s2.register(Person("Megan", "female", 27, "bisexual"))
s2.register(Person("Clark", "male", 27, "bisexual"))
s2.register(Person("John", "male", 30, "gay"))
s2.register(Person("Abraham", "male", 28, "gay"))
s2.register(Person("George", "male", 28, "gay"))
s2.register(Person("Samantha", "female", 25, "lesbian"))
s2.register(p3)

print("registered users =", s2.users())

s3.register(p1)
s3.register(p2)
s3.register(p4)
s3.register(Person("Megan", "female", 27, "bisexual"))
s3.register(Person("Clark", "male", 27, "bisexual"))
s3.register(Person("John", "male", 30, "gay"))
s3.register(Person("Abraham", "male", 28, "gay"))
s3.register(Person("George", "male", 28, "gay"))
s3.register(Person("Samantha", "female", 25, "lesbian"))
s3.register(p3)

print("registered users =", s3.users())

print("recommendations for Harry =", m.recommend("Harry"))
print("recommendations for Ginny =", m.recommend("Ginny"))
print("recommendations for Romilda =", m.recommend("Romilda"))
print("recommendations for Hermoine =", m.recommend("Hermoine"))

print("recommendations for Megan =", s1.recommend("Megan"))
print("recommendations for Clark =", s1.recommend("Clark"))

print("recommendations John =", s2.recommend("John"))
print("recommendations Abraham =", s2.recommend("Abraham"))
print("recommendations George =", s2.recommend("George"))

print("recommendations Maya =", s3.recommend("Maya"))
print("recommendations Samantha =", s3.recommend("Samantha"))

m.swipe("Harry", "Ginny", "right")
m.swipe("Harry", "Romilda", "left")
m.swipe("John", "Abraham", "right")
m.swipe("John", "George", "left")
m.swipe("Ginny", "Harry", "right")

print("Harry likes =", m.likes("Harry"))
print("Harry dislikes =", m.dislikes("Harry"))
print("John likes =", m.likes("John"))
print("John dislikes =", m.dislikes("John"))
print("Ginny likes =", m.likes("Ginny"))
print("Ginny dislikes =", m.dislikes("Ginny"))

print("recommendations for Harry =", m.recommend("Harry"))
print("recommendations John =", m.recommend("John"))

print("recommendations for Ginny =", m.recommend("Ginny"))
