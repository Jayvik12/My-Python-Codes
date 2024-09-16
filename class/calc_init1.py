class Calc:

    def __init__ (self, a, b): #this is a dynamic function
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    @staticmethod #Python decorator to define following function as static function
    def mul(a, b):
        return a * b

# x = 100
# y = 50

# obj1 = Calc(x, y) # creating object of class calc and here the init class get called

# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul(10,20))

class Newcalc(Calc): # To inherit the proprties of exixting class to new class


    def __init__(self, a,b):
        self.a = a
        self.b = b

    def div(self):

        div = self.a/self.b
        return div

new_class_obj1 = Newcalc(22,11)

tempvar = new_class_obj1.div()
print(tempvar)

tempvar = new_class_obj1.add() # Inherited properties from the Calc function
print(tempvar)