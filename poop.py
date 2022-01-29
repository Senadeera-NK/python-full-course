#-----python object oriented programming-------------#
class Car: #class name first letter should be capital

  #attributes cars might have
    # make=make
    # model=model
    # color=color
    # year=year

#constructor
#self -->> refers to the object that we are currently working on

  wheels = 4 #class variable-->>means 4 wheels is default added to any car created under this class

  def __init__(self,make,model,color,year):
    #these arguments can receive when creating an object
    self.make=make  #instance variables
    self.model=model  #instance variables
    self.color=color   #instance variables
    self.year=year   #instance variables

#methods that cars might have
  def drive(self): #self-->refers to the object using this method
    print('this '+ self.model+' is driving')

  def stop(self):
    print('this '+self.model+' is stopped')
