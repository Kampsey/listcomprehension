#given three coordinates x,y,z whose sum should not equal a value n
x=2
y=3
z=2
n=3
lists = [[i,j,k] for i in range(x) for j in range(y) for k in range(z)]
final_list=[]
for p in range(len(lists)):
    total= sum(lists[p])
    if total < n:
        final_list.append(lists[p])
    else:
        pass
    p=p+1
print(final_list)