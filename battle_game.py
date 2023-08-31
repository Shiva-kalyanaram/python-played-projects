#Creating a team and check whether they ready for battle using class and all() function in python

#all() function is built in function which returns True if all iterable elements in function are True, or it returns Fale. 

#Syntax: all(iterables)

#Code:

class character:
  def __init__(self, name, ready, health):
    self.name = name
    self.ready = ready
    self.health = health

shiva = character('shiva', True, 90)
kathir = character('kathir',False,80)
Raja = character('Raja',True, 95)

Family_team = [shiva,kathir,Raja]

if all(character.ready and character.health >=70 for character in Family_team): # this is here I used all() function 
  print('Your Family_team is ready for battle')
else:
  print('Your Family_team is not ready!!!!')
