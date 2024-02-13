# Native approach
def palidrome(x):
    return x == x

x = "church"
ans = palidrome(x)

if ans:
    print("Yes")
else:
    print("No")


a = int(input("Enter a number to check whether it's palindrome or not:"))
y = a
if (a == y):
     print(f"Yes {a} is a palindrome number.")
else:
     print(f"No {a} is not a palindrome number")

# in-built function
def palindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
       return True
    return False
s = "malayalam"
ans = palindrome(s)
if ans:
    print("Yes")
else:
    print("No")

t = "odo"
y = ""
for w in t:
    y = y + w
if ( t == y ):
    print("Yes")
else:
    print("No")




