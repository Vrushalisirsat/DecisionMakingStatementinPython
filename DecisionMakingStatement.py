'''
#Decision Making :-
# 1) if-else statement :-
#Example-1 :- WAP to read age of a person and check the person can vote or note.

# __main__
a = int(input("Enter Your age :"))
#start of if statement

if a>=18:
    print("You can vote")
else:
    print("you cannot vote")

#end of if
#end of __main__



#Example-2 :- WAP to read 2 numbers and find greatest of them.

# __main__

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))

if a>b:
    print("Greatest is ",a)
else:
    print("Greatest is ",b)

# end of __main__



#Example-3:- WAP to read 3 angles and check it forms an isosceles or not.

# __main__

a=int(input("Enter 1st angle :"))
b=int(input("Enter 2nd angle :"))
c=int(input("Enter 3rd angle :"))

if (a+b+c == 180) and (a==b or b==c or c==a):
    print("It is a isosceles Triangle")
else:
    print("It is not a isosceles Triangle")

# end of __if__
#end of __main__



#Example-4 :- WAP to read 3 angles and check it is right angle triangle or not.

# __main__

a=int(input("Enter 1st angle :"))
b=int(input("Enter 2nd angle :"))
c=int(input("Enter 3rd angle :"))

if (a+b+c == 180) and (a==90 or b==90 or c==90):
    print("It is a right angle Triangle")
else:
    print("It is not a right angle Triangle")

# end of __if__



# if-elif-else statements :

#Example-4 :- WAP to read a number and check it is a positive number or negative number.

# __main__

n=int(input("Enter your number :"))

if(n==0):
    print("It is zero")
elif n>0:
    print("positive number")
else:
    print("Negative number")

#end of if
#end of __main__



#Example-4 :- WAP to read a 3 different number and find the greatest of them.

# __main__

a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))

if a>b and a>c:
    print("Greatest Number is ",a)
elif b>c:
    print("Greatest Number is ",b)
else:
    print("Greatest Number is ",c)

#end of if
# end of __main__



# Example-4 :- WAP to read percentage marks obtained by a student and print appropriate division,as per the following criteria.

p = int(input("Enter Your Percentage :"))

if p>=75:
    print("Distinction")
elif p>=60:
    print("1st Division")
elif p>=50:
    print("2nd division")
elif p>=40:
    print("3rd division")
else:
    print("Failed")




# Conditional Expression (Like Ternary Operator) :
# Example-4 :- WAP to read two differnt number and find greatest of them.

a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))

g=a if a>b else b
print("Greatest Number is ",g)



#Q.WAP to read a number or check it is even or odd.

n=int(input("Enter a 1st number :"))
print("Even Number") if n%2==0 else print("Odd Number")


# match_case statement :
#Q1. WAP to read a digit and print that digit in words.

n=int(input("Enter a number :"))

match n:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _:
        print("Invalid digit")


# end of match_case
# end of __main__

#Q2 WAP to read a number from 1 to 10 and check number is even or odd.

# __main__
n=int(input("Enter a number in the range 1 to 10 :"))

match n:
     case 2 | 4 | 6 | 8 | 10:
        print("Even Number")
     case 1 | 3 | 5 | 7 | 9:
         print("Odd number")
     case _:
         print("Invalid number...")

#end of match
#end of __main__



#Q.3WAP to read input as per following criteria and print appropriate message.
# ENG -> You selected English , MAR -> you selected Marathi , HIN -> you selected Hindi

#__main__
l=input("Select a language - ENG,MAR,HIN :").upper()

match l:
    case "ENG":
        print("You selected English")
    case "MAR":
        print("You selected Marathi")
    case "HIN":
        print("You selected Hindi")
    case _:
        print("Invalid Input..")

#end of match-case
#end of __main__



# Example-4 :- WAP to read percentage marks obtained by a student and print appropriate division,as per the following criteria.

#__main__
p=int(input("Enter your percentage :"))

if p>=0 and p<=100:
    match p:
        case p if p>=75:
            print("Distinction")
        case p if p>=60:
            print("1st Division")
        case p if p>=50:
            print("2nd Division")
        case p if p>=40:
            print("3rd Division")
        case p if p<40:
            print("Failed..")
    #end of match
else:
    print("Invalid percentage")
#end of if
#end of __main__

# Loops / Iterative Statements
# 1) while loop :-

#Q1. WAP to print all number from 1 to 5.

# __main__

i=1

while i<=5:
    print(i ,end=" ")
    i=i+1
else:
    print("\nelse block is executed")
    print("i =",i)

#end of while loop
# end of __main__



#Q2. WAP to read a number and find the factorial of a number.

# __main__

n=int(input("Enter a number :"))

i=1
fact=1

while i<=n:
    fact=fact*i
    i=i+1
print("Factorial of",n,"=",fact)
#end of while
#end of __main__




# Q.3 WAP to print first N fibonacci numbers.Read the value of N from user.

n=int(input("Enter the number that you want to find fibonacci number :"))

a=0
b=1
i=1

while i<=n:
    print(a , end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
#end of loop
#end of __main__





# 2) for in loop

# q.1 WAP to retrive and display all values in an array by using loop.

#__main__

arr = array("i", [10,20,30,40,50])

for x in arr:
    print("X = ",x)
#end of for loop
#end of __main__




# range() function :-  used to generate number in the specified range.
# bydefault value :- increment=1, start_value=0 ,start_value is includes and  end_value is excludes.
#syntax :=> 1) range(end_value)   or   2) range(start_value,end_value,increment)

# Q.1 WAP to print all number from 1 to 5.

#__main__

for n in range(1,6,1):
    print(n , end=" ")

# end of for in loop.
#end of __main__

print("\n*****************************************")

# Q.2 WAP to print all number from 0 to 4.

# __main__
for n in range(0,5,1):        # or for n in range(0,5)
    print(n)
# end of for in loop.
#end of __main__



# Q.3 WAP to print all number from 5 to 1.

# __main__

for n in range(5,0,-1):
    print(n, end=" ")
# end of for in loop.
#end of __main__


# Q.4 WAP to print all even number from 1 to 10.

# __main__

for x in range(2,11,2):
     print(x, end=" ")

# end of for in loop.
#end of __main__



# Q.4 WAP to read a number and find its factorial.

# __main__

n=int(input("Enter a number :"))

fact=1

for i in range(1,n+1):
     fact=fact*i
#end of loop

print("Factorial is ",fact)

#end of __main__



# 3) Nested Loop :- loop inside a loop called as Nested Loop.

# Q.1 WAP to print following output.
#             1
#             12
#             123
#             1234
#             12345


# __main__

for i in range(2,7):

     for j in range(1,i):
          print(j , end="")

     # end of inner (i.e : j) for-in loop
     print()

#end of outer (i.e : i) for-in loop
#end of __main__


# Q.2 WAP to print following output.
#             A
#             AB
#             ABC
#             ABCD
#             ABCDE


# __main__

for i in range(66,71):

     for j in range(65,i):
          print(chr(j),end="")
     # end of inner (i.e : j) for-in loop
     print()
#end of outer (i.e : i) for-in loop
#end of __main__




# Q.3 WAP to print following output.
#             ABCDE
#             ABCD
#             ABC
#             AB
#             A


# __main__

for i in range(70,65,-1):

     for j in range(65,i):
          print(chr(j), end ="")
     # end of inner (i.e : j) for-in loop
     print()
#end of outer (i.e : i) for-in loop
#end of __main__



# Q.4 WAP to print following output.
#             12345
#             1234
#             123
#             12
#             1


# __main__

for i in range(6,1-,-1):

     for j in range(1,i):
          print(j, end="")
     # end of inner (i.e : j) for-in loop
     print()

#end of outer (i.e : i) for-in loop
#end of __main__

'''

# Q.5 WAP to print following output.
#             -----1
#             ----121
#             ---12321
#             --1234321
#             -123454321


# __main__

p=2
for q in range(6,1,-1):

     for i in range(1,q):
          print("-",end="")
     #end of loop

     for j in range(1,p):
          print(j,end="")
     #end of loop

     for k in range(p-2,0,-1):
          print(k,end="")
     #end of loop
     print()
     p=p+1

#end of outer loop
#end of __main__




# NOTE :- for Exploring more pattern questions ,refer the pattern folder.
