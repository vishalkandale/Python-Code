i = 1
while i <= 10:
    print(i)
    i += 1

print("Done excution")


for i in range(5):
    print(i)

for i in range(1,5):
    if i < 4:
        print(i, end=",")
    else:
        print(i)


friends = ["kylo","goblin","spower","Omega","goblin","neyo"]
for index in range(len(friends)):

    print(friends[index],end=" ")
    
def power(base_number,power_number):
    return pow(base_number,power_number)

print("\r")
print(power(2,3))

def basepower(base_number,power_number):
    result = 1
    for index in range(power_number):
        result =  result * base_number
    return result

print(basepower(2,4))  