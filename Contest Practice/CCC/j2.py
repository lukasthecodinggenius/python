numberofbidders = int(input())
bidders = []
bids = []
for i in range(numberofbidders):
    name = str(input())
    bid = int(input())
    bidders.append(name)
    bids.append(bid)

listItem = 0
largest = bids[0]

for i in bids:
    if i > largest:
        largest = i


placeinlist = -1
for i in bids:
    placeinlist += 1
    if i == largest:
        winner = bidders[placeinlist]
        print(winner)
        exit()





