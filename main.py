from random import choice
def vyber_slova():
    with open('slova.txt') as fd:
        radky = fd.readlines()

    vybrane_slovo = choice(radky)
    vybrane_slovo = vybrane_slovo.strip()
    return vybrane_slovo

def uhodnuti():
    a = 0
    while True:
        vybrane_slovo = vyber_slova()
        odpoved = input("Doplň: " + vybrane_slovo[:-2])
        if odpoved == vybrane_slovo[-2:]:
            print("Správně!")
            a += 1
        else:
            return a

def nejlepsi_skore():
    z_uhodnuti = uhodnuti()
    with open('nejlepsi_skore.txt', 'r') as fd:
        precteno = fd.readline()
    print('Tve nejlepší skore je: ', precteno)
    print('Teď jsi získal: ', z_uhodnuti)
    if int(precteno) < z_uhodnuti:
        with open('nejlepsi_skore.txt', 'w') as fd:
            fd.write(str(z_uhodnuti))


nejlepsi_skore()