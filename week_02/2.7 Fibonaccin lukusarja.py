# COMP.CS.100 2.6.3 Tulosteen leveyden asettaminen
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""
Fibonaccin lukusarjan kaksi ensimmäistä lukua ovat ykkösiä ja sen
jälkeen tulevat luvut saadaan muodostettua laskemalla yhteen aina
kaksi edeltävää lukua. Toteuta ohjelma, joka tulostaa Fibonaccin
lukusarjaa niin pitkälle kuin käyttäjä haluaa:

How many Fibonacci numbers do you want? 7
1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13

"""

def main():

    repetition_counter = 1
    number = int(input("How many Fibonacci numbers do you want? "))
    first_fibo = 1
    second_fibo = 1

    while repetition_counter <= number:
        if repetition_counter == 1:
            fibo = first_fibo
            print(f"{repetition_counter}. {fibo}")
        elif repetition_counter == 2:
            fibo = second_fibo
            print(f"{repetition_counter}. {fibo}")
        else:
            fibo = first_fibo + second_fibo
            print(f"{repetition_counter}. {fibo}")
            first_fibo = second_fibo
            second_fibo = fibo
        repetition_counter += 1

if __name__ == "__main__":
    main()

