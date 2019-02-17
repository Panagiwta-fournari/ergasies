#ergasia2
arithmos = []
t = int(input("dwse enan arithmo:"))
i = 1
while (i<=t):
    r = 0
    if (t%i==0):
        k = 1
        while (k<=i):
            if (i%k==0):
                r = r + 1
            k = k + 1
        if (r==2):
            arithmos.append(i)
    i = i + 1

result = ""
for i in range (0,len(arithmos)):
    f = t
    x = 0
    while (f%arithmos[i]==0):
        x = x + 1
        f = f/arithmos[i]

    if (x>1):
        result = result + "(" + str(arithmos[i]) + "**" + str(x) + ")"
    else:
        result = result + "(" + str(arithmos[i]) + ")"

print (result)
