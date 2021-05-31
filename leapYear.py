#i decided to just do this all in one file since there is no real reason to have 2 files. 


class palendrome:
  def __init__(self):
    print("My Leap year Program")
    self.printed = []
  def leap(self, year):
      gen = year
      if gen%400 == 0:
        print("is leap year")
        return True
      return False
     
      
      



    #should return True since we are putting a  leapyear
def testFor():

    name = palendrome()
    
    
    assert name.leap(4) == True
    


testFor()
