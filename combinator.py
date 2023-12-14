import random
def makeCouples(people):
	destList=[x for x in people]
	couples=[]
	for p in people:
		listWithoutSelf=[x for x in destList if x[0]!=p[0]]
		dest=random.choice(listWithoutSelf)
		destList=[x for x in destList if x[0]!=dest[0] ]
		couples.insert(0,[p,dest])
	return couples

