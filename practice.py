class A:
    namee = 12 
    def __init__(self):
        A.namee = 123
        self.name = ''
        self.age = ''
    @classmethod
    def get(cls):
        cls.namee = 'hi its me '
        cls.name = 'hi bitch '
""" A.get()
A.namee= "new" """
a = A()
b = A()
#A.name = 'us,am'


a.name = 'usman'
b.namee ='kadri'
A.name = 'dgfsdjgf'

print(A.__dict__,a.__dict__,A.name)
