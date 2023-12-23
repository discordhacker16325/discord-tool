import sys
import colorama

colorama.init()

def main():
    # Wyświetl menu
    print(colorama.Fore.BLUE + "** LightStore **" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "Wybierz opcję:" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "1. Boostuj serwery Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "2. Dołączaj do serwerów Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "3. Pobieraj identyfikatory użytkowników Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "4. Wysyłaj spam i oznaczaj użytkowników Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "5. Zmieniaj biografie użytkowników Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "6. Dodawaj reakcje emoji do wiadomości Discord" + colorama.Fore.RESET)
    print(colorama.Fore.BLUE + "7. Wylogowuj się z serwerów Discord" + colorama.Fore.RESET)

    # Odczytaj wybór użytkownika
    wybor = input(colorama.Fore.BLUE + "Wybór: " + colorama.Fore.RESET)

    # Wykonaj wybraną opcję
    if wybor == "1":
        print(colorama.Fore.BLUE + "Boostujesz serwery Discord..." + colorama.Fore.RESET)
    elif wybor == "2":
        print(colorama.Fore.BLUE + "Dołączasz do serwerów Discord..." + colorama.Fore.RESET)
    elif wybor == "3":
        print(colorama.Fore.BLUE + "Pobierasz identyfikatory użytkowników Discord..." + colorama.Fore.RESET)
    elif wybor == "4":
        print(colorama.Fore.BLUE + "Wysyłasz spam i oznaczasz użytkowników Discord..." + colorama.Fore.RESET)
    elif wybor == "5":
        print(colorama.Fore.BLUE + "Zmieniasz biografie użytkowników Discord..." + colorama.Fore.RESET)
    elif wybor == "6":
        print(colorama.Fore.BLUE + "Dodajesz reakcje emoji do wiadomości Discord..." + colorama.Fore.RESET)
    elif wybor == "7":
        print(colorama.Fore.BLUE + "Wylogowujesz się z serwerów Discord..." + colorama.Fore.RESET)
    else:
        print(colorama.Fore.BLUE + "Nieprawidłowy wybór." + colorama.Fore.RESET)

if __name__ == "__main__":
    main()