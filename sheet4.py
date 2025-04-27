# 1-Write a function that generate a random password, you can use random package with random.choice function
#Your function should take the length of the password and the characters needed in the password as arguments.

import random    # @ #استخدمتها عشان اعمل قيم عشوائية لكلمة السر
 
def Make_password(length, chars):
    return "".join(random.choice(chars) for _ in range(length)) # @ #استخدمت join عشان تجمع الحروف 

passwd = Make_password(25, "pilot_A380")
print(passwd)


##2-Use comperehension to generate a string of characters that contains, all characters (upper and lower), digits.

s = "".join( chr(ord('a') + i) for i in range(26) ) # @ #استخدمت ord عشان ادي قمية بي رقمية للحرف

# @ # استخدمت ال range عشان اعمل حلقة مرجعية لحرف اللغة الانجليزية

s += "".join( chr(ord('0') + i) for i in range(10) )

s += s.upper()



###3-Create a list whose elements are strings, the names of people in your family. Now use a set comprehension
#(and, better yet, a nested set comprehension) to find which letters are used in your family members’ names.


names = ["mohamed", "pilot", "A380"]

s = set ( c for name in names for c in name ) 
# @ #عملت حلقتين تكرار تمر على كل اسم وحرف داخل الاسم مره
# @ # اسختدمت set لان من خصائصها انها لا تحتوي على عناصر مكرر داخلها



####4- Write a function that finds the average of a list of numbers passed as arguments.

def average(*numbers):  #@# * خليتها تاخد عدد لا نهائي من المدخلات عن طريق *
    if len(numbers) == 0: #@# عشان اتجنب القسمة على صفر لو مفيش اي ارقام
        return 0
    x = 0
    for i in numbers:
        x += i
    return x / len(numbers)  #@# بحسب المتوسط بعد جمع الأرقام وقسمته على عددهم

list1 = [15, 29, 13, 32, 55]
print(average(*list1))




#####5-Write a function that substitutes variables into a mathematical equation written as a string.

def value(expression, **variables): #@# ببدل المتغيرات جوه التعبير الرياضي الي عاوزو
    for variable, value in variables.items(): #@# استخدمت الحلقة التكرارية عشان تعدي على كل متغير
        expression = expression.replace(variable, str(value))
    return expression

m_expression = "2 * x + y" #@# x , y ببدل قيمة ال 
result = value(m_expression, x=3, y=4) # استدعاء الدالة الصحيحة
print(result)















