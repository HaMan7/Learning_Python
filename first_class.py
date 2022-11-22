#my_number = 10
#to_string = str(my_number)
#print(type(to_string))

###Basic Calculation
#x= 15
#ans= 4*(x**2) + 2*(x) + 1
#print(ans)

# a= 4
# b= 2
# c= 1
# equation = (-b + (b**2 - 4*(a*c))**0.5)/ (2*a)
# print(equation)

# b="This is a great school"
# print(b[8:15:1])

# user_name = input("Name: ")
# user_yob =  int(input("Your year of Birth please: "))

# current_year = 2022
# age = current_year-user_yob
# print (f"Hello {user_name}! \n You are {age} years old.")

# first_name = input("Please Provide your First Name: ")
# last_name = input("Please Provide your Last Name: ")

# user_name = last_name[:3] + first_name[-3:]
# print(f"Hello {first_name}. \nThank you for Signing UP \nThis is your Username: {user_name}")

##### List

# my_list = [1,2,34,55, "Hauwa", "Rita", "9jaFinder"]

# print(my_list)

###Functions ,Questions: Given the ages of students in a class, calculate the following;
#1. Mean
#2. Median
#3. Range
#4. Variance 
#5. Standard Deviation 
# import statistics
# ages = input("Kindly input all ages of students, please seperate by comma. \n")
# list_of_ages = ages.split(",")
# refined_ages = list(map(int,list_of_ages))
# stddev =  round(statistics.stdev(refined_ages), 2)
# print(f"The Mean is : {statistics.mean(refined_ages)}")
# print(f"The Median is : {statistics.median(refined_ages)}")
# print(f"The Mode is : {statistics.mode(refined_ages)}")
# print(f"The Standard Deviation is : {stddev}")
# print(f"The Variance is : {statistics.variance(refined_ages)}")

#dictionary in python
# a= [1,2,3,4,5]
# b= [1,2,3]
# b[0] = 4
# print(a)
# print(b)

# print(len(a))#length of the array 
# print(min(a))
# print(list(zip(a,b)))#zip puts them together 

#if conditions and condition statement 
# if 1> 10:
#     print("10")
# elif 1<10:
#      if 10 % 2 ==0:
#         print("Its an Even Number")
# else:
#     print(50)

# import random
# an_array = [1,2,3,4,5,6,1]
# q = ""
# for i in range(6):
#     q+=str(random.choice(an_array))
# print(q)

# a = 1
# while a <= 10:
#     print("Hello")
# a+=1

##looks like an error 
