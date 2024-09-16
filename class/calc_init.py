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

x = 100
y = 50

obj1 = Calc(x, y) # creating object of class calc and here the init class get called

print(obj1.add())
print(obj1.sub())
print(obj1.mul(10,20))