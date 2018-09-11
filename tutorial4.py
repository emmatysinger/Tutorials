dinnercost = 15     # cost of dining out
bankaccount = 150   # dollars
while bankaccount > 0:
    print("Yumm.. I would love to eat out tonight!")
    bankaccount = bankaccount - dinnercost
    print("Uh oh.. I only have ${0} left!".format(bankaccount))
    
for i in range(5):
    print(i)
    
for i in ['a', 'b', 'c', 'd']:
    print(i)
    
for i in [1, 2, 3]:
    for j in [4, 5]:
        print(i, j)
        
b = -4
while b <= 0:
    b += 1
    print(b)
    
for i in [1, 2, 3]:
    for j in range(i):
        print(i, j)
        
while 1 == 99:
    print("hi")
