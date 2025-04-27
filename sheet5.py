#1-Generate the following lists using the range function:
##[0, 1, 2, 3, 4, 5]
#[4, 6, 8, 10]
#[10, 9, 8, 7, 6]
#[10, 5, 0, -5, -10]

list(range(6))#@# عشان نعمل تسلسل رقمي  range بنستخدم 
list(range(4, 11, 2))
list(range(10, 5, -1))
list(range(10, -11, -5))


##-2What is the output of the following code, and explain the rule of the zip function?
#x_coor = [1, 2, 3, 4, 5]
#y_coor = [2, 4, 6, 8, 10]
#z_coor = [0, -1, -2, -3, -4]
#points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]

#output is 
[(1, 'a'), (2, 'b'), (3, 'c')] #@#  عشان اجمع قائمتين مع بعض    zip بنستخدم ال  



###-3 What is the output of the following code? Use map function to get the same output

Output=[2, 3, 4]

def pil(num):
    return num+1
A380    = list(map(pil, [1, 2, 3]))  #@# عشان اطبق دالة مباشرة على عناصر القائمة map أستخدمت ال 

print(A380)



####4-Modify the code in question 3 to use a lambda function.

A380 = list(map(lambda x: x + 1, [1, 2, 3])) #@#  بتسختدم عشان اعرف دالة بطريقة مختصرة
print(A380)





#####5-What is the output of the following code?

#def modlist(lst):
#    for i in range(len(lst)):
#        lst[i] = 10 * lst[i]

#def modvar(num):
#    num += 10

#lst = [1, 2, 3]
#modlist(lst)
#print(lst)

#x = 0
#modvar(x)
#print(x)

[10, 20, 30]
0






#######6-Using shorthand if-else and list comprehension, generate a list indicating whether the corresponding number in the other list is even.
#x = [1, 2, 10, 13, 1]
# output = [False, True, True, False, False]

x = [1, 2, 10, 13, 1]

print([True if num % 2 == 0 else False for num in x])  #@#استخدمت باقي القسمة عشان اقول ان العدد زوجي






#######-7 Explain the rule of each line in the following class, then modify the class to be Point3d, and add subtract method.


class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y})"

    def add(self, p):
        self.x += p.x
        self.y += p.y
        self.z += p.z

    def subtract(self, p):
        self.x -= p.x
        self.y -= p.y
        self.z -= p.z

    def distance(self, p):
        delta_x = self.x - p.x
        delta_y = self.y - p.y
        delta_z = self.y - p.z

        dist = (delta_x ** 2 + delta_y ** 2 + delta_z ** 2) ** 0.5
        return dist































