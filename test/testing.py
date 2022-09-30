'''import random
print("2")
for i in range(2,101):
    prime = False
    for o in range(i-1,1,-1):
        if i%o != 0:
            prime = True
        if i%o == 0:
            prime = False
            break
    if prime:
        print(i)


for p in range(1,5):
    for k in range(1,5):
        print(k, end = " ")
    print("\n")

for m in range (2,-1,-1):
    for s in range (59,-1,-1):
        print(m,":",s)

count =0
for y in range(25):
    if count<=5:
        print(random.randint(1,50), end= " ")
        count = count +1
    if count == 5:
        print("\n")
        count = 0
        '''

print('{0:2d} {1:2d} {2:.2f} '.format(123,324,1231254.234535))


def song(animal, sound):
    print("OLD MACDONALD HAD A FARM \n \
    EE I EE I O \n \
    AND ON HIS FARM HE HAD SOME ",animal," \n \
    EE I EE I OH \n \
    WITH A ",sound,sound," HERE\n \
    AND A ",sound,sound," THERE \n \
    HERE ",sound," THERE ",sound,"\n \
    ",sound,sound,"OLD MACDONALD HAD A FARM \n \
    EE I EE I O")

song("DOG", "WOOF")