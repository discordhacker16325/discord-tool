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

