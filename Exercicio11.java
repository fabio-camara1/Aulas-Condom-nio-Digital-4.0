package Fundamentos;

import java.util.Scanner;

public class Exercicio11 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite o primeiro numero");
		float numero1 = entrada.nextFloat();
		System.out.println("digite o segundo numero");
		float numero2 = entrada.nextFloat();
		System.out.println("digite o terceiro numero");
		float numero3 = entrada.nextFloat();
		if (numero1 > numero2 && numero1 > numero3) {
			System.out.println("numero 1 é o maior");
		}
		else if (numero2 > numero1 && numero2 > numero3) {
			System.out.println("numero 2 é o maior");
		}
		else {
			System.out.println("numero 3 é o maior");
		}
	}
}
}