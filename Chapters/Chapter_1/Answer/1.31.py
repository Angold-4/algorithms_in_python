# Angold4 20200509 C1.1.31
def main():
    Need = float(input("Please Enter the money that you need to pay: "))
    Paid = float(input("Please Enter The Money that you've already paid: "))
    Banknotes = [1000, 500, 100, 50, 20, 10, 5]
    Coin = [1, 0.5, 0.1]
    Extra = Paid - Need
    BAnswer = []
    CAnswer = []
    if Need == Paid:
        print("Just Right:-)")
    if Need > Paid:
        print("Please Enter the right number!")
    else:
        for i in range(7):
            E = Extra // Banknotes[i]
            Extra -= E*Banknotes[i]
            BAnswer.append(E)
        for j in range(3):
            E = Extra // Coin[j]
            Extra -= E*Coin[j]
            CAnswer.append(E)
        print("Money to be recovered:")
        for p in range(7):
            if BAnswer[p] != 0:
                print("%d piece of HK$: %d." % (BAnswer[p], Banknotes[p]))
        for q in range(3):
            if CAnswer[q] != 0:
                print("%d piece of HK$: %s (Coin)." % (CAnswer[q], Coin[q]))


if __name__ == "__main__":
    main()
