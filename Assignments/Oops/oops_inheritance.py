# 1. Create a class called Spell which takes a spell name.
# The generic spell has an execute method which prints something generic. name method returns the name of the spell
# You can create specific sub spells and define what they would do when executed.
# So basically create a parent class called Spell and two sub classes called Accio and Confundo
# (override their execute methods).

# spell = Spell("spell name")
# spell.name() # returns "spell name"
# spell.execute() # prints "Executing: spell name"

# spell1 = Accio()
# spell1.name()  # returns "accio"
# spell1.execute() # prints "Summons an object to the caster"

# spell2 = Confundo()
# spell2.name() # returns "confundo"
# spell2.execute() # prints "Causes the victim to become confused and befuddled"

class Spell:
    def __init__(self, spell_name):
        self.spell_name = spell_name

    def name(self):
        return self.spell_name

    def execute(self):
        print("Executing: " + self.spell_name)


class Accio(Spell):

    def execute(self):
        print("Summons an object to the caster")


class Confundo(Spell):

    def execute(self):
        print("Causes the victim to become confused and befuddled")


spell = Spell("spell name")
spell.name()
spell.execute()
spell1 = Accio("accio")
print(spell1.name())
spell1.execute()
spell2 = Confundo("confundo")
print(spell2.name())
spell2.execute()



