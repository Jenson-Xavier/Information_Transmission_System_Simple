f=[2,1,1]
def Find(x:int)->int:
    if f[x]==x:
        return x
    else:
        return Find(f[x])

res=[]
for i in range(0,len(f)):
    res.append(Find(i))

print(res)