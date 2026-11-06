                            #   LIST 
list = ["apple","mango","banana","kivi","watermelon","orange","grapes","mango"]
list.append("apple")
list.insert(5,"litchi")
list.pop()
list.remove("mango")
print(list.sort())
print(list)

 # Q(1) WAP to ask the user to enter names of thier 3 favorite fruites and store them in a list.
fruite1 = input("enter your 1st fruite:")
fruite2 = input("enter your 2nd fruite:")
fruite3 = input("enter your 3rd fruite:")
fruites = [fruite1,fruite2,fruite3]
print(fruites)



# Q(2) WAP to check if a list contains a palindrome of elements.
list1 = [1,2,3,2,1]
copy_list = list1.copy()
copy_list.reverse()
if (copy_list == list1):
    print("this is palindrome")
else:
    print("this is not palindrme")



                            # TUPLE
tup = (1,2,3,4,5,6,7,8,9,10,10)
print(tup.count(10))
print(tup.index(9))
print(tup)

# Q(3) WAP to count the number of student with the "A" grade in the following tuple.
#         ["A","C","F","A","B","E","A","B","A"]

grades = ("A","C","F","A","B","E","A","B","A")
print(grades.count("A"))


# store the above values in a list and sort them from "A" to "F"


grades = ["A","C","F","A","B","E","A","B","A"]
grades.sort()
print(grades)