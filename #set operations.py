#set operations
s1=set(input("enter element of first set: "))
s2=set(input("enter elemnts of second set: "))
print(s1)
print(s2)

print("union is:",s1.union(s2))
print("intersection is: ",s1.intersection(s2))
print("difference is: ",s1-s2)
print("symmetric difference is:",s1^s2)

def subset(s1,s2):
    if s1.issubset(s2):
        print("s1 is subset of s2")
    elif s2.issubset(s1):
        print("s2 is a subset of s1")
    else:
        print("no subset")

subset(s1,s2)

def superset(s1,s2):
    if s1.issuperset(s2):
        print("s1 is superset of s2")
    elif s2.issuperset(s1):
        print("s2 is superset of s1")
    else:
        print("none")

superset(s1,s2)

element=input("enter an element:")
if element in s1:
    print("element found!")
else:
    print("element not found!")

list1=[]
length=int(input("enter length of list: "))
for i in range(length):
    element=int(input("enter element: "))
    list1.append(element)
print(set(list1))

def power_set(s3):
    result = [[]]   

    for elem in s:
        new_subsets = []
        
        for subset in result:
            new_subsets.append(subset + [elem])
        
        result = result + new_subsets

    for subset in result:
        print(set(subset))
s3=int(input("enter set elements: "))
print(power_set(s3))