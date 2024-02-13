my_num = int(input("Enter a number: "))

if my_num % 2 ==0:
   print("The number is even number")
else:
   print(f"{my_num} is an odd number")

voter = int(input("Enter your age: "))
if voter >= 18:
    print("The voter is eligible")
else:
    print(f"{voter} is not eligible/young")