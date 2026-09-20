# ## first approch 

number=int(input("enter a number"))

if number == 0:
    print("this is not a joke zero has no devisors")

# c=number
# i=1

# while i<c:
#     if c%i==0:
#         print(i)

#     i+=1

''' approch no. 2 to solve this is O(Root n )'''

c=number
i=1
result=[]
while i <= (c**(1/2)):

    if c%i == 0 :
        r=c/i
        result.append(i)

        if r!=i:
            result.append(r)

    i+=1

    result.sort()
    

print(result)






