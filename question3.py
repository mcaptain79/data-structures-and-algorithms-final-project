#in this line we get our values
#you should get inputs with space between
towers = list(map(int,input("Please enter height of towers: ").split()))
#at first we make an empty list for saving singnal powers
signalPowers = []
while(len(towers) != 0):
    counter = 1
    #here we stimulated stack by poping the last elemnt
    Last_tower = towers.pop(len(towers)-1)
    for i in range(len(towers)-1,-1,-1):
        if towers[i] <= Last_tower:
            counter += 1
        else:
            break
    signalPowers.append(counter)
#we print our list from last element to the first
for i in range(len(signalPowers)-1,-1,-1):
    print(signalPowers[i],end = ' ')
        
        