#Defining the function
def percent(a,b,c,d,e):
  percent=(a+b+c+d+e)/5
  print(f"You have scored {percent}% in your exams ! ")

#Taking marks input from the user
m1 = int(input("Enter the marks scored in first subject out of 100 : "))
m2 = int(input("Enter the marks scored in second subject out of 100 : "))
m3 = int(input("Enter the marks scored in third subject out of 100 : "))
m4 = int(input("Enter the marks scored in fourth subject out of 100 : "))
m5 = int(input("Enter the marks scored in fifth subject out of 100 : "))
percent(m1,m2,m3,m4,m5)
