def main():
	print("This script converts figures from a variety of units to meters. DONT TYPE ANY SPACES")
	sourceUnit = input("What unit is the input in? (accepts inches, feet, miles, kilometers, lightyears)")
	sourceValue = input("What value would you like to convert to meters?")
	newValue = convert(sourceUnit, sourceValue)
	print(str(sourceValue) + " " + str(sourceUnit) + " is equal to " + str(newValue) + " meters.")

#dictionary of conversion factors
conversionFactors = {
	"inches" : 0.0254,
	"feet" : 0.3048,
	"miles" : 1609.34,
	"kilometers" : 1000.00,
	"lightyears" : 9.461 * (10**15),
}

def convert(unit, value):
	if (conversionFactors[unit]):
		return float(value) * float(conversionFactors[unit])
	else:
		print ("Invalid Unit")

main()