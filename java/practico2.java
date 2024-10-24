import java.util.Scanner;

public class practico2 { // Nombre de la clase en mayúscula
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);
        
        // Solicitar la edad al usuario
        System.out.print("Por favor, ingresa tu edad: ");
        
        // Verificar si la entrada es un número entero
        if (scanner.hasNextInt()) {
            int edad = scanner.nextInt();

            // Verificar que la edad sea positiva
            if (edad >= 0) {
                // Clasificar según la edad ingresada
                if (edad < 13) {
                    System.out.println("Eres un niño.");
                } else if (edad >= 13 && edad <= 17) {
                    System.out.println("Eres un adolescente.");
                } else if (edad >= 18 && edad <= 64) {
                    System.out.println("Eres un adulto.");
                } else {
                    System.out.println("Eres un adulto mayor.");
                }
            } else {
                System.out.println("Por favor, ingresa una edad válida.");
            }
        } else {
            System.out.println("Por favor, ingresa un número válido.");
        }

        // Cerrar el escáner
        scanner.close();
    }
}
