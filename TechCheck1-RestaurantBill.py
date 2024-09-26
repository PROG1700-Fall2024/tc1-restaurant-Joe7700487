#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    #init variables
    taxRate = 0.15
    tipRate = 0.20
    bill = int
    tax = int
    tip = int
    total = int

    #calculate amounts
    bill = int(input("Enter bill amount: "))
    tax = bill * taxRate
    tip = bill * tipRate
    total = bill + tax + tip

    #print out values
    print("Original bill: ${0:.2f}".format(bill))
    print("Tax: ${0:.2f}".format(tax))
    print("Tip: ${0:.2f}".format(tip))
    print("Total: ${0:.2f}".format(total))
main()