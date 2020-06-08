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
                if self.reg[user1].sexuality == "straight" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and self.reg[user1].sex != self.reg[user2].sex \
                        and (self.reg[user2].sexuality == "straight" or self.reg[user2].sexuality == "bisexual"):
                    recommendations.append(user2)

                elif self.reg[user1].sexuality == "bisexual" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and (self.reg[user2].sexuality == "bisexual"
                             or (self.reg[user2].sexuality == "straight" and self.reg[user1].sex != self.reg[user2].sex)
                             or (self.reg[user2].sexuality == "gay" and self.reg[user1].sex == "male")
                             or (self.reg[user2].sexuality == "lesbian" and self.reg[user1].sex == "female")):
                    recommendations.append(user2)

                elif self.reg[user1].sexuality == "gay" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and self.reg[user2].sex == "male" \
                        and (self.reg[user2].sexuality == "gay" or self.reg[user2].sexuality == "bisexual"):
                    recommendations.append(user2)

                elif self.reg[user1].sexuality == "lesbian" \
                        and user2 != user1 and user2 not in likes and user2 not in dislikes \
                        and self.reg[user2].sex == "female" \
                        and (self.reg[user2].sexuality == "lesbian" or self.reg[user2].sexuality == "bisexual"):
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


p1 = Person("Harry", "male", 29, "straight")
p2 = Person("Ginny", "female", 23, "straight")
p3 = Person("Maya", "female", 26, "lesbian")
p4 = Person("Romilda", "female", 27, "straight")
p5 = Person("Hermoine", "female", 29, "straight")

m = MatchMaker()
m.register(p1)
m.register(p2)
m.register(p3)
m.register(p4)
m.register(Person("Megan", "female", 27, "bisexual"))
m.register(Person("Clark", "male", 27, "bisexual"))
m.register(Person("John", "male", 30, "gay"))
m.register(Person("Abraham", "male", 28, "gay"))
m.register(Person("George", "male", 28, "gay"))
m.register(Person("Samantha", "female", 25, "lesbian"))

print("registered users =", m.users())

print("recommendations for Harry =", m.recommend("Harry"))
print("recommendations for Ginny =", m.recommend("Ginny"))
print("recommendations for Romilda =", m.recommend("Romilda"))
print("recommendations for Hermoine =", m.recommend("Hermoine"))
print("recommendations for Megan =", m.recommend("Megan"))
print("recommendations for Clark =", m.recommend("Clark"))
print("recommendations John =", m.recommend("John"))
print("recommendations Abraham =", m.recommend("Abraham"))
print("recommendations George =", m.recommend("George"))
print("recommendations Maya =", m.recommend("Maya"))
print("recommendations Samantha =", m.recommend("Samantha"))

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
