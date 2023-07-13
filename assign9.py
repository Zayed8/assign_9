from mycalci import * #userdefined module
import math as m #builtin module
class Myerror(Exception):
    pass
class stringpassedError(Myerror):
    def __init__(self):
        super().__init__("Input passed is String! Plz enter a Integer type-->")
class Operations(stringpassedError):
    if Mycalci and m == "":
            raise stringpassedError
    try:
        print("Usertdefined Module-mycalci.py-> ")
        obj = Mycalci.add(num1=4,num2=5)
        obj = Mycalci.sub(num1=4,num2=5)
        obj = Mycalci.mul(num1=4,num2=5)
        obj = Mycalci.div(num1=4,num2=5)
        obj = Mycalci.mod(num1=4,num2=5)
        obj = Mycalci.exp(num1=4,num2=5)
        obj = Mycalci.fdiv(num1=4,num2=5)
        print("Inbuilt Module-math.py-> ")
        print(m.ceil(5.1))
        print(m.floor(5.9))
        print(m.sin(2))
        print(m.tan(2))
        print(m.fsum([1,2,3,4]))  
        print(2**4)  
        print(m.pow(2,2)) 
        print(m.factorial(5))
    except stringpassedError:
        print("String value Entered....!")
    except Exception:
         print("Exception has been raised Plz check the userinput again!")
    finally:
         print("ByeBye....👋")