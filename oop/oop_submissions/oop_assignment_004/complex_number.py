class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        
        if type(real_part) == str and type(imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
        elif type(real_part)==str:
            raise ValueError("Invalid value for real part")
        elif type(imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
     
    def __add__(self,second):
        return ComplexNumber(self.real_part+second.real_part,self.imaginary_part+second.imaginary_part)
        
    def __sub__(self,second):
        return ComplexNumber(self.real_part-second.real_part,self.imaginary_part-second.imaginary_part)
        
    def __mul__(self,second):
        return ComplexNumber(self.real_part*second.real_part-self.imaginary_part*second.imaginary_part,self.real_part*second.imaginary_part+second.real_part*self.imaginary_part)
        
    def __truediv__(self,second):
        k=second.real_part**2+second.imaginary_part**2
        return ComplexNumber((self.real_part*second.real_part+self.imaginary_part*second.imaginary_part)/k,(self.imaginary_part*second.real_part-self.real_part*second.imaginary_part)/k)
        
    def __abs__(self):
        import math
        return round(math.sqrt(self.real_part**2+self.imaginary_part**2),3)  
        
    def __eq__(self,second):
        return (self.real_part==second.real_part and self.imaginary_part==second.imaginary_part)    
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
        
    def __str__(self):
        return "{}{}{}i".format(self.real_part, "+" if self.imaginary_part>=0 else "-",abs(self.imaginary_part))    