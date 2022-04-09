# def function(n,n1):
#     if n<n1:
#         print(n1-n,"  water is oveflow")
#     elif n1==n:
#         print("no more water needed")
#     else:
#         print(n-n1,"liter water to be filled")
# n=int(input("Enter the max of water to be filled:-"))
# n1=int(input("Enter the water filled:-"))
# function(n,n1)

# l=int(input("enter start number"))
# r=int(input("enter teh number")) 
# c=0
# i=0
# while i<=r:
#     if r%10==2 or l%10==3 or i%10==9:
#         i=r+1
# print(c)

# def my (n,m):
#     c=0
#     for i in range(n,m+1):
#         x=i%10
#         if x==2 or x==3 or x==9:
#             c=c+1
#     print(c)
# my(n=int(input("enter the number:")),m=int(input("enter the number")))

def my ():
    a=int(input("enter no"))
    b=int(input("enter no"))
    c=0
    i=a
    while i<=b:
        k=i%10
        if k==2 or k==3 or k==9:
            c=c+1
        i=i+1
    print(c)
my()