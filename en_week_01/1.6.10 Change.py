# COMP.CS.100
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

def main():

    purchase_price = int(input("Purchase price: "))
    paid_amount = int(input("Paid amount of money: "))
    change = (paid_amount - purchase_price)

    if change > 0:
        print("Offer change:")
    else:
        print("No change")
    if change//10 > 0:
        print(f"{change//10} ten-euro notes")
        change = change%10
    if change//5 > 0:
        print(f"{change//5} five-euro notes")
        change = change%5
    if change//2 > 0:
        print(f"{change//2} two-euro coins")
        change = change%2
    if change//1 > 0:
        print(f"{change//1} one-euro coins")


if __name__ == "__main__":
    main()

'''
Change

Learning Goals

Learning about using arithmetic operators in Python and making calculations with integers.

Create a program that asks how much purchases cost and the amount of paid money and then prints the amount of change. To simplify the program, only 1, 2, 5 and 10 euros are offered as change. It is assumed that the paid amount is always euros, i.e. no cents are paid besides euros. It is further assumed that the paid amount is always at least 1 euro.

Examples of how the program works:

Purchase price: 12
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
1 two-euro coins
1 one-euro coins

Purchase price: 11
Paid amount of money: 50
Offer change:
3 ten-euro notes
1 five-euro notes
2 two-euro coins

Purchase price: 9
Paid amount of money: 20
Offer change:
1 ten-euro notes
1 one-euro coins

Purchase price: 12
Paid amount of money: 12
No change

Purchase price: 23
Paid amount of money: 15
No change

Programming tips:

    Find out how the operators // and % work in Python.

'''