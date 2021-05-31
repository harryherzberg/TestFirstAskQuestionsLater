#i decided to just do this all in one file since there is no real reason to have 2 files. 


class palendrome:
  def __init__(self):
    print("My Fiz Buzz Program")
    self.printed = []
  def fizzBuzzMe(self):
    i=1
    for i in range (100):
      gen = i
      if gen%3 == 0:
        self.printed.append("fizz")
        print("fizz")
      else:
        self.printed.append(gen)
        print(gen)
      
      



    #tests to see if the third thing it prints is "fizz"
    #should run false since I dont have any logic making it turn shit into fizz or buzz
def testFizz():
    print("testing to see if the third thing it prints is fizz:")
    name = palendrome()
    name.fizzBuzzMe()
    
    assert name.printed[3] == "fizz"
    



testFizz()
