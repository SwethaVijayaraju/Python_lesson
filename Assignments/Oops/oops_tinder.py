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
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class MatchMaker:
    def __init__(self):
        self.reg = {}
        self.action = {}

    def register(self, person):
        if person.name not in self.reg:
            self.reg[person.name] = person  # (value=object)

    def users(self):
        return list(self.reg.keys())

    def swipe(self, user1, user2, action):

        if user1 in self.reg and user2 in self.reg:
            if self.reg[user1].sex != self.reg[user2].sex:
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

    def act(self, user1):
        actions = self.action[user1]
        like = []
        dislike = []
        for action in actions:
            if action[1] == "like":
                like.append(action[0])
            elif action[1] == "dislike":
                dislike.append(action[0])

        return [like, dislike]

    def likes(self, user1):
        return self.act(user1)[0]

    def dislikes(self, user1):
        return self.act(user1)[1]

    def recommend(self, user1):
        recommendations = []
        likes = self.likes(user1)
        dislikes = self.dislikes(user1)
        for user2 in self.users():
            if user2 not in likes and user2 not in dislikes and self.reg[user1].sex != self.reg[user2].sex:
                recommendations.append(user2)
        return recommendations

class Bisexual(MatchMaker):
    def recommend(self, user1):
        recommendations = []
        likes = self.likes(user1)
        dislikes = self.dislikes(user1)
        for user2 in self.users():
            if user2 not in likes and user2 not in dislikes:
                recommendations.append(user2)
        return recommendations





p1 = Person("vishnu", "male")
p2 = Person("swetha", "female")
p3 = Person("maya", "female")
m = MatchMaker()
m.register(p1)
m.register(p2)
m.register(p3)
m.register(Person("megan", "female"))
m.register(Person("karthik", "male"))
print(m.users())
print(m.users())
m.swipe("vishnu", "swetha", "right")
m.swipe("vishnu", "megan", "left")
m.swipe("vishnu", "karthik", "right")
m.swipe("swetha", "karthik", "right")
print(m.likes("vishnu"))
print(m.dislikes("vishnu"))
print(m.recommend("vishnu"))
print(m.recommend("swetha"))

m2=Bisexual()
