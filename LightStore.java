public class LightStore {

    public static void main(String[] args) {
        System.out.println("** LightStore **");
        System.out.println("Wybierz opcję:");
        System.out.println("1. Boostuj serwery Discord");
        System.out.println("2. Dołączaj do serwerów Discord");
        System.out.println("3. Pobieraj identyfikatory użytkowników Discord");
        System.out.println("4. Wysyłaj spam i oznaczaj użytkowników Discord");
        System.out.println("5. Zmieniaj biografie użytkowników Discord");
        System.out.println("6. Dodawaj reakcje emoji do wiadomości Discord");
        System.out.println("7. Wylogowuj się z serwerów Discord");

        // Odczytaj wybór użytkownika
        String wybor = System.console().readLine("Wybór: ");

        // Wykonaj wybraną opcję
        switch (wybor) {
            case "1":
                System.out.println("Boostujesz serwery Discord...");
                break;
            case "2":
                System.out.println("Dołączasz do serwerów Discord...");
                break;
            case "3":
                System.out.println("Pobierasz identyfikatory użytkowników Discord...");
                break;
            case "4":
                System.out.println("Wysyłasz spam i oznaczasz użytkowników Discord...");
                break;
            case "5":
                System.out.println("Zmieniasz biografie użytkowników Discord...");
                break;
            case "6":
                System.out.println("Dodajesz reakcje emoji do wiadomości Discord...");
                break;
            case "7":
                System.out.println("Wylogowuj się z serwerów Discord...");
                break;
            default:
                System.out.println("Nieprawidłowy wybór.");
        }
    }
}