#  Sort an array (ascending order) 
ls = [3, 14, 5, 2, 10]
sortLs =[]

for i in range(len(ls)):
    smallet = ls[0]
    for j in ls:
        if(j < smallet):
            smallet = j

    sortLs.append(smallet)
    ls.remove(smallet)

print(sortLs)