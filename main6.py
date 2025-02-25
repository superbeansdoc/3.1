inrange = int(input("how many moives to you want to rank"))
moive = []
for i in range (inrange):
    cow = input("whats your number 1 fav movie")
    moive.append(cow)
print(moive)
for i in range (inrange - 1,-1,-1):
    print(moive[i])
