def flames(p1Name, p2Name):
    P1_Name=p1Name
    P2_Name=p2Name
    l=[]
    m=[]
    s=[]
    for i in P1_Name.lower():
        if i !=' ':
            l.append(i)
    for i in P2_Name.lower():
        if i != ' ':
            m.append(i)
    for i in l:
        for j in l:
            if j in m:
                l.remove(j)
                m.remove(j)
    s=l+m
    Flames={'F':'Friends','L':'Love','A':'Attraction','M':'Marriage','E':'Enemy','S':'Siblings'}
    s1='FLAMES'
    l=[]
    for i in s1:
        l.append(i)
    m=len(s1)
    n=len(s)
    for i in range(6):
        if n>m:
            pos=n-m-1
            if pos<len(l):
                l=l[pos+1:]+l[:pos]
            elif pos>=len(l):
                pos-=len(l)
                while(pos>len(l)):
                    pos-=(len(l))
                l = l[pos+1:]+l[:pos]
        if n<=m:
            pos=n-1
            l = l[pos+1:]+l[:pos]
        m-=1
    res = Flames[''.join(l)]
    return res