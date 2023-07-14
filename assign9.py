from mycalci import * #userdefined module
import math as m #builtin module
class WrongDataTypeError(Exception):
    def _init_(self, *args):
        super()._init_(*args)

num1=None
num2=None
try:
    num1=int(input("Enter num: "))
    num2=int(input("Enter num: "))

except ValueError:
    try:
        if num1 or num2 ==None:
            raise WrongDataTypeError("It is taking a Wrong datatype")
    except WrongDataTypeError as s:
        print(s.args[0])
        print("******Usertdefined Module-mycalci.py****** ")
        obj = Mycalci.add(num1=4,num2=5)
        obj = Mycalci.sub(num1=4,num2=5)
        obj = Mycalci.mul(num1=4,num2=5)
        obj = Mycalci.div(num1=4,num2=5)
        obj = Mycalci.mod(num1=4,num2=5)
        obj = Mycalci.exp(num1=4,num2=5)
        obj = Mycalci.fdiv(num1=4,num2=5)
        print()
        print("******Inbuilt Module-math.py****** ")
        print(m.ceil(5.1))
        print(m.floor(5.9))
        print(m.sin(2))
        print(m.tan(2))
        print(m.fsum([1,2,3,4]))  
        print(2**4)  
        print(m.pow(2,2)) 
        print(m.factorial(5))
    except Exception:
         print("Exception has been raised Plz check the userinput again!")
    finally:
         print("ByeBye....👋")
