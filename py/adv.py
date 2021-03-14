#classes and object
#classes
#
#
class Employee:
 def __init__(self,first,last,pay):
     super(). __init__(first,last,pay) #child call parent class
    self.first =first
    self.last = last
    self.pay  = pay
    self.email = first + '.' +'@company.com'
    self.pay_raise = pay*1.04
    print(self,first,pay)
