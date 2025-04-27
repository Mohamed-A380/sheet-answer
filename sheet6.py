#1- Write a program that create a new file, then write Hello from file to the file.

file = open("sheet6.txt", "w")  #@#بسخدمها عشان افتح الملف والحرف عشان وضع الكتب
file.write("Hello from file")  #@# عشان اكتب الي عاوزه في الملف
file.close() #@# إقفل الملف


##2-Write a program that append your name to the previous file.

file = open("Sheet6.txt", "a") #@#استخدمتها عشان اضيف الملف السابق واكمل عليه
file.write("pilot\n")  
file.close()



###3-Write a program that write a list of numbers from 1 to 100 to the same file.

file = open("sheet6.txt", "a")
for x in range(1, 101):
    file.write(f"{x}\n") 
file.close()   

#@#لما يشتغل الملف هيكون فيه قائمة للارقام من 0الى 100 على كل سطر على لوحدو




####4-Read the lines from 50 to 60 and print it on the screen.


with open("sheet6.txt", "r") as file:
    lines = file.readlines()  #@# أستخدمتها عشان اقراء الملف واحطو في قائمة
if len(lines) >= 60:
    selected_lines = lines[49:60]
    print("Lines 50 to 60:")
    for line in selected_lines:
        print(line.strip())  
else:
    print("The file has less than 60 lines. Try adding more content.")






##### JSON


import json
users = [
    {"username": "pilot", "pass": "A380"},
    {"username": "copilot", "pass": "b474"},
    {"username": "lila", "pass": "m5458"},
    {"username": "saed", "pass": "pop606"}
        ]
file = open('users.json', 'w')
json.dump(users, file)
file.close()
file = open('users.json', 'r')
users = json.load(file)
file.close()
print(f"First user: {users[0]['username']} , pass: {users[0]['pass']}")
users.append({"username": "pilot", "pass": "lol909"})
file = open('users.json', 'w')
json.dump(users, file)
file.close()
print("User added")
u = input("Username: ")
p = input("Password: ")
file = open('users.json', 'r')
users = json.load(file)
file.close()
x = False
for user in users:
    if user['username'] == u and user['pass'] == p:
        x = True
        break
print("Success" if x else "Failed")



###Math Module


import math   #استخدمتها عشان استخدم مكتبة الرياضية 

radius= 4.5

Area= math.pi*radius*radius

print(f"The area of the circle is: {Area:4f}") #@# استخدمتها للتنظيم عشان يكون الناتج عشري بمقدار اربع خانات



















