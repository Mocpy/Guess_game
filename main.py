from random import choice
def vyber_slova():
    with open('slova.txt') as fd:
        radky = fd.readlines()

    vybrane_slovo = choice(radky)
    vybrane_slovo = vybrane_slovo.strip()
    return vybrane_slovo

def uhodnuti():
    a = 0
    vybrane_slovo = vyber_slova()
    while True:
        odpoved = input("Doplň: " + vybrane_slovo[:-2])
        if odpoved == vybrane_slovo[-2:]:
            print("Správně!")
            a += 1
            return str(a)

def nejlepsi_skore():
    with open('nejlepsi_skore.txt', 'w') as fd:
        fd.write(uhodnuti())

nejlepsi_skore()