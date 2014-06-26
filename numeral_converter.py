def getNumerals(n):
	ones = [1,"IV","IX","V","I"]
	tens = [10, "XL", "XC", "L", "X"]
	hundreds = [100, "CD", "CM", "D", "C"]
	numerals = [hundreds, tens, ones]
	
	roman = "M" * (n/1000)
	n = n%1000
	for i in numerals:
		count = n/i[0]
		if count == 4: 
			roman += i[1]
		elif count == 9:
			roman += i[2]
		else:
			if count >= 5:
				roman += i[3]
				count -= 5
			roman += i[4] * count
		n = n%i[0]
	return roman