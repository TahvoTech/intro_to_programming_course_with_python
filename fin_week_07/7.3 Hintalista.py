# COMP.CS.100 6.13 Pisin järjestetty alimerkkijono
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
this program gives prices for the products in dict.

asks what product.

"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def check_price():
    """
    checks price

    :param: no parameter
    :return: str
    """
    while True:
        name = input("Enter product name: ")
        if name.isspace() or name == "":
            return print("Bye!")
        elif name.strip() not in PRICES:
             print(f"Error: {name.strip()} is unknown.")
        elif name.strip() in PRICES:
             print(f"The price of {name.strip()} is"
                         f" {PRICES[name.strip()]:.2f} e")

def main():

    check_price()

if __name__ == "__main__":
    main()