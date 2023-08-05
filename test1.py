import random

pc_number = random.randit(1, 10)

for i in range(5):
user_number = int(input("Enter your num:"))

if user_number == pc_number:
    print("Bordi!!!")
if user_number < pc_number:
    print(" Boro bala!")
if user_number > pc_number:
    print("Boro paeen!")
