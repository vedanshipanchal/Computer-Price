class computer:
  def __init__(self):
    self.__maxprice = 10000

  def sell(self):
    print("selling price:",self.__maxprice)

  def setmax(self,price):
    self.__maxprice = price

#obj
ob1 = computer()
ob1.sell()

#change max price
ob1.__maxprice = 900
ob1.sell()