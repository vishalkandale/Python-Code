lucky_number = [4,5,7,3,5]
friends = ["kylo","goblin","spower","Omega","goblin","neyo"]
details = ["goblin",2, False]

print(friends)
print(details)
print(friends[0])
print(details[2])
print(friends[-1])
print(details[::-1])
print(friends[1:])
print(details[:1])


friends.extend(lucky_number)
print(friends)

friends.append("Hector")
print(friends)

print(friends.count("goblin"))

friends.remove("goblin")
print(friends)

print(friends.count("goblin"))

friends2 = friends.copy()
print(friends2)
