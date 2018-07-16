tenderTypes = {
	'hundred dollar bill':100.00,
	'fifty dollar bill':50.00,
	'twenty dollar bill':20.00,
	'ten dollar bill':10.00,
	'five dollar bill':5.00,
	'one dollar bill':1.00,
	'quarter':.25,
	'dime':.10,
	'nickel':.05,
	'penny':.01
}

def howManyCoins():
	total = float(input("How much change is to be dispensed?"))
	piecesOfTender = 0
	tenderUsed = {}
	for i in tenderTypes:
		tenderUsed[i] = 0
		while tenderTypes[i] <= total:
			total -= tenderTypes[i]
			piecesOfTender += 1
			tenderUsed[i] += 1
	print()
	print("The total number of bills and coins needed is: ", str(piecesOfTender))
	print()
	print("Here's the breakdown: ")
	print()
	for j in tenderUsed:
		if tenderUsed[j] != 0:
			print(j + " x" + str(tenderUsed[j]))


howManyCoins()