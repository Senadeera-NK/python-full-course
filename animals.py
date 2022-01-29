class Animal:
  alive = True
  
  #'self' is important since this is object oriented programming(objects are important)
  def eat(self):
    print('this animal is eating')

  def sleep(self):
    print('this animal is sleeping')



class Rabbit(Animal): #to inherit--->>>childclassname(parentclassname)
  def run(self):
    print('this rabbit is running')

class Fish(Animal): #to inherit--->>>childclassname(parentclassname)
  def swim(self):
    print('this fish is swimming')

class Hawk(Animal): #to inherit--->>>childclassname(parentclassname)
  def fly(self):
    print('this hawk is flying')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.eat()
rabbit.run()