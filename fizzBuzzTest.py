#i decided to just do this all in one file since there is no real reason to have 2 files. 


class palendrome:
  def __init__(self):
    print("My Fiz Buzz Program")
    self.printed = []
  def fizzBuzzMe(self):
    for i in range (100):
      self.printed.append(i)
      print(i)



    #tests to see if the third thing it prints is "fizz"
    #should run false since I dont have any logic making it turn shit into fizz or buzz
def testFizz():
    print("testing to see if")
    name = palendrome()
    name.fizzBuzzMe()
    print(name.printed[3])
    assert name.printed[3] == "fizz"




testFizz()
