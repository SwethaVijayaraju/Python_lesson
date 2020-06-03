student = "harry"


def house(student):
    if student == "ron" or student == "harry":
        return "Griffindor"
    elif student == "Draco":
        return "Slytherin"
    elif student == "Penelope":
        return "Ravenclaw"
    elif student == "Cedric":
        return "Hufflepuff"
    else:
        return "unknown"


print(house("Penelope"))
print(house("Draco"))
print(house("ron"))
print(house("harry"))
print(house("Cedric"))
print(house("Ginny"))
