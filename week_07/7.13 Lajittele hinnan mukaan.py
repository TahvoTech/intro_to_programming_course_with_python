# COMP.CS.100 7.13 Lajittele hinnan mukaan
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413
"""


example:

beans 0.87
noodles 0.97
bananas 1.05
milk 1.09
bread 2.10
chocolate 2.70
Pepsi 3.15
pizza 4.15
fish 4.56
grasshopper 13.25
sushi 19.90

"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15, "pizza": 4.15,
}

def main():

    def payload(key):
        return PRICES[key]

    for i in sorted(PRICES, key=payload):
        print(f"1. {i:12} {PRICES[i]:>6.2f}")



if __name__ == "__main__":
    main()