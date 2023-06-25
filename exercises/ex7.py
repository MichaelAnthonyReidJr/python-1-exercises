def calc_total(arrayOfInts, salesTaxString):
    total = 0.00
    tax = float(salesTaxString.replace('%', ""))/100 
    for eachFloatNumber in arrayOfInts:
        total += eachFloatNumber * tax + eachFloatNumber
    totalAsDollars = "${:,.2f}".format(total) 
    return totalAsDollars


