1. Create a class called Spell which takes a spell name. The generic spell has an execute method which prints something generic. name method returns the name of the spell
You can create specific sub spells and define what they would do when executed. 
So basically create a parent class called Spell and two sub classes called Accio and Confundo (override their execute methods). 

spell = Spell("spell name")
spell.name() # returns "spell name"
spell.execute() # prints "Executing: spell name"

spell1 = Accio()
spell1.name()  # returns "accio"
spell1.execute() # prints "Summons an object to the caster"

spell2 = Confundo()
spell2.name() # returns "confundo"
spell2.execute() # prints "Causes the victim to become confused and befuddled"
