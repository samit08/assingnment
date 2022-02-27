print("Question.1")
#Definig tower of Hanoi function
def tower_of_hanoi(n , source, destination, auxiliary):
    step_number=1
    if n==1:
        print ("Move disk 1 from",source,"to",destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from",source,"to",destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)
#taking number of disk input from the user
no_of_disk=int(input("Enter number of disk in tower of Hanoi:"))
print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks from Source Tower to Destination Tower "
      "is given below:\n")
#Using the function of tower of hanoi
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")



                                
print("Question.2")

#Recuesive Approach
print("\n[Question.2](Recursive)\nThe Pascle's Triangle using"
      " recursive approach is:\n")

# forming function that will return next row of Pascle triangle
def psum(list1, row):#This funct takes current row element and row no. as  input and returns next row elements
    i1 = 0
    i2 = 1
    l = []
    for i1 in range(row - 1):
        l.append(list1[i1] + list1[i2])
        i1 = i1 + 1
        i2 = i2 + 1
    l.insert(0, 1)
    l.append(1)
    return (l)
#Forming a fun that uses recusion to print pascle's triangle
def pascle_triangle(n,list1,row):
    if n==0:
        return
    else:
        next=psum(list1,row)
        liste=next.copy()
        listp=list(map(str,liste))
        p="  ".join(listp)
        print("{s:^100}".format(s=p))
        pascle_triangle(n-1,next,row+1)

n=int(input("Enter number of rows in Pascle's Triangle:"))
#Alligning the pascle's triangle in triangular form using string formatting and printing it
if n==1:
    print("{a:^100}".format(a="1"))
elif n==2:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1 1"))
else:
    print("{b:^100}".format(b="1"))
    print("{b:^100}".format(b="1  1"))
    pascle_triangle(n-2,[1,1],2)



#Iterative Approach


print("\n[Question.2](Iterative)\nThe Pascle's Triangle using "
      "iterative approach is:\n")
#taking number of rows as input
row=int(input("Enter number of rows:"))
#forming fuction that will return next row of pascle triangle
def psum(list1, row):
    i1 = 0
    i2 = 1
    l = []
    for i1 in range(row - 1):
        l.append(list1[i1] + list1[i2])
        i1 = i1 + 1
        i2 = i2 + 1
    l.insert(0, 1)
    l.append(1)
    return (l)

#forming function that will print all rows using previous function
def ptriangle(rows):
    if rows == 1:
        print("{a:^100}".format(a="1"))
    elif rows == 2:
        print("{b:^100}".format(b="1"))
        print("{b:^100}".format(b="1 1"))
    else:
        f = "{p:^100}".format(p=1)
        print(f)
        f = "{p:^100}".format(p="1  1")
        print(f)
        l1 = [1, 1]
        row = 2
        for i in range(rows - 2):
            v = psum(l1, row)
            v2 = v.copy()
            v2 = list(map(str, v2))
            n = rows
            k = "  ".join(v2)
            f = "{p:^100}".format(p=k)
            print(f)
            row = row + 1
            l1 = v
ptriangle(row)


                                   


print("Question.3")
#Taking input from the user
n1=int(input("\nEnter an Integer:"))
n2=int(input("Enter another Integer:"))
#Making a list of return values
list1=list(divmod(n1,n2))
#a1=Quotient
q=list1[0]
#a2=Remainder
r=list1[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")

#Que3.a
print("\nQue3.a")
c1=callable(divmod(n1,n2))
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
#Que3.b
print("\nQue3.b")
#list of values
listv=[q,r]
zero=False
if zero in listv:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are 'non-zero'")
#Que3.c
print("\nQue3.c")
#new values of list
listr=[q,r]
for i in range (4,7):
    listr.append(i)
print(f"Appended (4,5,6) in the values ({q},{r})")
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
#Que3.d
print("\nQue3.d")
set1={1,2}
set1.clear()
#adding above result in set datatype
for el in listv2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print("\nQue3.e")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Que3.f
print("\nQue3.f")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")


                                    


print("Question.4")
#forming a class named student
class student:
    #using constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defing print function
    def pfun(self):
        print(f"Hello, My name is {self.name} and my "
              f"roll no. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Destructor Called")
#makin samit an object of student
samit=student("samit",21104008)
samit.pfun()
del samit


                    


print("Question.5")
#forming class employees
class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
emp_1=employees("Mehak",40000)
emp_2=employees("Ashok",50000)
emp_3=employees("Viren",60000)
#print employee detail
emp_1.pfun()
emp_2.pfun()
emp_3.pfun()
#Updating salary of Mehak to 70000
print("\nQue.5a")
emp_1.salary=70000
print("Mehak salary Updated to 70000")
emp_1.pfun()
#Deleting Viren's data
print("\nQue.5b")
del emp_3
print("Employee Viren's data has been removed.")



print("Question.6")                                     
gap=" "*10
print(f"\n{gap}WELCOME TO THE FRIENDSHIP GAME")
#definig principle of game i.e. anagram
def anagram(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for e in word1:
        l1.append(e)
    for el in word2:
        l2.append(el)
    #sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#taking player name input
player1=str(input("\nEnter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#using anagram function
result=anagram(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
