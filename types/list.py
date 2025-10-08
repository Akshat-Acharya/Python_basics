l1=["Indore","Bhopal","Dewas","Ujjain","Dhar"]
print(l1)
for i in range (len(l1)) :
    print(l1[i],end="\t")
print()
for i in l1 :
    print(i,end="\t")
print(l1[:3])
print(l1[1:3])
print(l1[0:5:2])
print(l1[-1:-6:-1])
l1[3]="Mahakal Nagri"
l1.append("Rau")
l1.insert(2,"Ratlam")
print(l1[::-1])
l1.pop()
print(l1[::-1])
l1.pop(2)
print(l1[::-1])
