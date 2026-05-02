print("________  _____________  __.___________ _________                                   __   ")
print(" /  _____/ /   _____/    |/ _|\__    ___/ \_   ___ \  ____   _______  __ ____________/  |_ ")
print(" /   \  ___ \_____  \|      <    |    |    /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\ ")
print(" \    \_\  \/        \    |  \   |    |    \     \___(  <_> )   |  \   /\  ___/|  | \/|  |  ")
print("  \______  /_______  /____|__ \  |____|     \______  /\____/|___|  /\_/  \___  >__|   |__|  ")
print("         \/        \/        \/                    \/            \/          \/             ")
print("%@@@@@%%%@@@@@@@@@%%@%%@@@@@@@@@@@@@@@@@@@@%%@@%%%%@@@@%%@@%%%@@@@@@@@@%%@@@@@@@@@@@@%@@@%%@@@@@@@@%")

numero = int(input("Digite um número: "))

UltimoDigito = numero % 2
calculo = numero // 2

if calculo > 0:
    PenultimoDigito = calculo % 2
    calculo //= 2
    if calculo > 0:
        AntepenultimoDigito = calculo % 2
        calculo //= 2
        if calculo > 0:
            QuartoDigito = calculo % 2
            calculo //= 2
            if calculo > 0:
                QuintoDigito = calculo % 2
                calculo //= 2
                if calculo > 0:
                    SextoDigito = calculo % 2
                    calculo //= 2
                    if calculo > 0:
                        SetimoDigito = calculo % 2
                        calculo //= 2
                        if calculo > 0:
                            OitavoDigito = calculo % 2
                            print(OitavoDigito, SetimoDigito, SextoDigito, QuintoDigito, QuartoDigito, AntepenultimoDigito, PenultimoDigito, UltimoDigito)
                        else:
                            print(SetimoDigito, SextoDigito, QuintoDigito, QuartoDigito, AntepenultimoDigito, PenultimoDigito, UltimoDigito)
                    else:
                        print(SextoDigito, QuintoDigito, QuartoDigito, AntepenultimoDigito, PenultimoDigito, UltimoDigito)
                else:
                    print(QuintoDigito, QuartoDigito, AntepenultimoDigito, PenultimoDigito, UltimoDigito)
            else:
                print(QuartoDigito, AntepenultimoDigito, PenultimoDigito, UltimoDigito)
        else:
            print(AntepenultimoDigito, PenultimoDigito, UltimoDigito)
    else:
        print(PenultimoDigito, UltimoDigito)
else:
    print(UltimoDigito)
