#This function calculates the product of two numbers
def prod(a,b):
  prod=a*b
  return prod
def withoutPrintProd(a,b):
  prod=a*b
  print(prod)
  return prod
int1 = int(input("Enter the first integer : "))
int2 = int(input("Enter the second integer : "))

print("The product is : ")

#The first function would need an additional print command
print(prod(int1,int2))

#The second function simply needs to be called
withoutPrintProd(int1,int2)
