from game.image import change
from game.image import close
from game.image import openn
from game.sound import load as load_sd
from game.sound import pause 
from game.sound import play
from game.level import load as load_lvl
from game.level import over
from game.level import start

while True:
    print("1. change image")
    print("2. close image")
    print("3. open image")
    print("4. load sound")
    print("5. pause sound")
    print("6. play sound")
    print("7. load level")
    print("8. over level")
    print("9. start level")
    print("0. exit")
    choice = input("masukkan pilihan : ")
    if choice == "1":
        print("\n", change.inichange(), "berhasil\n")
    elif choice == "2":
        print(close.iniclose())
    elif choice == "3":
        print(openn.iniopen())
    elif choice == "4":
        print(load_sd.iniload())
    elif choice == "5":
        print(pause.inipasue())
    elif choice == "6":
        print(play.iniplay())
    elif choice == "7":
        print(load_lvl.iniload())
    elif choice == "8":
        print(over.iniover())
    elif choice == "9":
        print(start.inistart())
    elif choice == "0":
        break
    else:
        print("pilihan tidak ada")