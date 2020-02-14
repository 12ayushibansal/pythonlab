ls = [(10,20,30),(40,50,60),(70,80,90)]
lst = []
tup = ()
list2 = []
for i in range (len(ls)):
       lst = list(ls[i])
       ls[-1] = 100
       tup = tuple(lst)
       list2.append(tup)
print(list2)
       
       
