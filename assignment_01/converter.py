def convert(fah):
	return (5.0/9.0)*(fah - 32)

def main():
	fah = int(input("What temperature would you like to convert to Cel?"))
	cel = convert(fah)
	count = 0
	while (count < 5):
		print (str(fah) + " degrees farenheight is " + str(cel) + " degrees celsius.")
		count += 1

main()