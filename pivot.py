co = input("Podaj wyrazenie: ")
print(co)

t = []
for i in co:
    t.append(i)
print(t)
def dod(t,i):
    x = t.pop(i)
    t.insert(i+1, x)

def ode(t,i):
    x = t.pop(i)
    t.insert(i+1, x)

def razy(t,i):
    x = t.pop(i)
    t.insert(i+1, x)

def dziel(t,i):
    x = t.pop(i)
    t.insert(i+1, x)

def dodzaw(t,i):
    x = t.pop(i+2)
    t.insert(i+3, x)
    y = t.pop(i)
    t.insert(i+3, y)

def odezaw(t,i):
    x = t.pop(i+2)
    t.insert(i+3, x)
    y = t.pop(i)
    t.insert(i+3, y)

i = 0
while i < len(t):
    
    print(t, i)
    if t[i] == "*":
        razy(t, i)
        i += 2
    elif t[i] == "/":
        dziel(t, i)
        i += 2
    elif t[i] == '+' and t[i + 2] == "*" or t[i + 2] == '/':
        dodzaw(t, i)
        i += 4
    elif t[i] == '-' and t[i + 2] == "*" or t[i + 2] == '/':
        odezaw(t, i)
        i += 4
    elif t[i] == "+":
        dod(t, i)
        i += 2
    elif t[i] == "-":
        ode(t, i)
        i += 2
    else:
        i+=1
    


for i in t:
    print(i, end="")
