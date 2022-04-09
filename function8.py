# def number(list):
#     i=0
#     while i<len(list):
#         if list[i]==list[0]:
#             print("True")
#             break
#         else:
#             print("False")
#         i=i+1
# number([1,1,1,1,1,9,1,])



# def number(list):
#     i=0
#     a=[]
#     while i<len(list):
#         if list[i]==list[0]:
#             a.append(list[i])
#         i=i+1
#     if a==list:
#         return "True"
#     else:
#         return "false"
# print(number([1,1,1,1,1,1,]))
# print(number([1]))
# print(number[1,1,1])


def num(list):
    if len(list)<0:
        result="true"
    result=(list[0] for element in list)
    if result:
        return "true"
    else:
        return "false"
print(num([1,1,1]))
print(num([]))
print(num([1,1,1,1,1]))
print(num([4,8,9,2]))


