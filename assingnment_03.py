
print("FIRST PROGRAM")

string = input("Enter a string: ").lower()

#converting to list for counting words
stringlist = string.split()

def count_in_dict(list):
    count = {}
    
    n = len(list)
    for i in range(n):
        if list[i] in count:
            count[list[i]] += 1
        else:
            count[list[i]] = 1
    return count

#checking for number of words
if len(stringlist) == 1:
    
    #making a list of all the letters
    stringlist = list(stringlist[0])

    print(count_in_dict(stringlist))
else:
    # the list has more than one word
    
    print(count_in_dict(stringlist))



print("SECOND PROGRAM")
day=0
month=0
year=0

# months having 30 days
mon30 = [4, 6, 9, 11]

# months having 31 days
mon31 = [1, 3, 5, 7, 8, 10, 12]

#inputing the date
def input_date():
    global day
    global month
    global year
    day = int(input("Day- "))
    month = int(input("Month- "))
    year = int(input("Year- "))
    
    if year>2025 or year<1800 or month<1 or month>12 or day<1 or day>31:
        print("Conditions not met, Try Again")
        input_date()

    #check for if the date is not in the calender
    if day > 28 and month == 2 and year%4 != 0:
        print("Not a date! Try Again")
        input_date()
    elif day > 29 and month ==2 and year%4 == 0:
        print("Not a date! Try Again")
        input_date()
    elif day > 30 and month in mon30:
        print("Not a date! Try Again")
        input_date()
input_date()


#for non leap year feb
if day == 28 and month == 2 and year%4 != 0:
    day = 1
   
    month = 3
# checking for leap year
elif day == 28 and month == 2 and year%4 == 0:
    day += 1
elif day == 29 and month == 2 and year%4 == 0:
    day = 1
   
    month = 3

elif day == 30 and month in mon30:
    day = 1
    
    month += 1
elif day == 31:
    day = 1
    month += 1
else:
   
    day += 1

# changing the month and year
if month == 13:
    month = 1
    year += 1


print(day,'/',month,'/',year)




print("THIRD PROGRAM")

inputlist = list(map(int, input("Enter a list of numbers: ").split()))

squarelist = [(inputlist[i], inputlist[i]**2) for i in range(len(inputlist))]

print(squarelist)



print("FOURTH PROGRAM")
def input_point():
    point = int(input("Enter Grade Point: "))
    # check if the grade point meets the conditions
    if point>10 or point<4:
        print("Invalid grade point! Try Again")
        point = input_point()
    return point

# get the user to input a grade point
point = input_point()

#defining letter grade performance dictionary
grader = {10: ("A+","Outstanding"),
9:("A","Excellent"),
8:("B+","Very Good"),
7:("B","Good"),
6:("C+","Average"),
5:("C","Below Average"),
4:("D","Poor")}

remark = grader[point]
print("Your Grade is '{}' and {}".format(*remark))

print("FIFTH PROGRAM")

#making a string of the 11 alphabets
alphabet = "ABCDEFGHIJK"

#defining a var for printing the alphabets
col = 11

#for the rows
for i in range(6):
    # print the spaces
    # 1 less than the row number
    print(" "*i, end="")
    
    # print the alphabets/columns
    # 11 for the first row with a decrement of 2
    print(alphabet[:col])
    col -= 2

print("SIXTH PROGRAM")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("a.",students)

#part b. sort acc to the names
print("b.",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("c.",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("d.",students[sid])

print("SEVENTH PROGRAM")
n = int(input("How long should be the sequence? "))
# making a list of fibonacci sequence
if n == 1:
    fib = [1]
else:
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(fib)

sum = 0
for i in range(n):
    
    sum += fib[i]

#print average
print("The average of the series is ", sum/n)

print("EIGHTH PROGRAM")

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

print("part a")
print("a.",(set1|set2)-(set1&set2))
print("part b")
print("b.",(set1|set2|set3)-((set1&set2)|(set1&set3)|(set3&set2)))
print("part c")
print("c.",((set1&set2)|(set1&set3)|(set3&set2))-(set1&set2&set3))
print("part d")
set10 = {1,2,3,4,5,6,7,8,9,10}
print("d.",set10-set1)
print("part e")
print("e.",set10-(set1|set2|set3))
