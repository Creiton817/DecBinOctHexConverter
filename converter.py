print("________  _____________  __.___________ _________                                   __   ")
print(" /  _____/ /   _____/    |/ _|\__    ___/ \_   ___ \  ____   _______  __ ____________/  |_ ")
print(" /   \  ___ \_____  \|      <    |    |    /    \  \/ /  _ \ /    \  \/ // __ \_  __ \   __\ ")
print(" \    \_\  \/        \    |  \   |    |    \     \___(  <_> )   |  \   /\  ___/|  | \/|  |  ")
print("  \______  /_______  /____|__ \  |____|     \______  /\____/|___|  /\_/  \___  >__|   |__|  ")
print("         \/        \/        \/                    \/            \/          \/             ")
print("%@@@@@%%%@@@@@@@@@%%@%%@@@@@@@@@@@@@@@@@@@@%%@@%%%%@@@@%%@@%%%@@@@@@@@@%%@@@@@@@@@@@@%@@@%%@@@@@@@@%")
try:
    while True:
         numero = input("Digite um número: ")
         numero = int(numero)
         calculo = numero // 2
         UltimoDigito = numero % 2
         if calculo > 1:
             calculo = numero // 2
             PenultimoDigito = numero % 2
             if calculo > 1:
                 calculo = numero // 2
                 AntepenultimoDigito = numero % 2
                 if calculo > 1:
                     calculo = numero // 2
                     QuartoDigito = numero % 2
                     if calculo > 1:
                         calculo = numero // 2
                         QuintoDigito = numero % 2
                         if calculo > 1:
                             calculo = numero // 2
                             SextoDigito = numero % 2
                             if calculo > 1:
                                 calculo = numero // 2
                                 SetimoDigito = numero % 2
                                 if calculo > 1:
                                     calculo = numero // 2
                                     OitavoDigito = numero % 2
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
except ValueError:
    print("Digite um número válido.")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
