package Fundamentos;

import java.util.Scanner;

public class Exercicio12 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite um numero");
		float numero1 = entrada.nextFloat();
		if (numero1 == 1) {
			System.out.println("domingo");
		}
		else if (numero1 == 2) {
			System.out.println("segunda");
		}
		else if (numero1 == 3) {
			System.out.println("terça");
		}
		else if (numero1 == 4) {
			System.out.println("quarta");
		}
		else if (numero1 == 5) {
			System.out.println("quinta");
		}
		else if (numero1 == 6) {
			System.out.println("sexta");
		}
		else if (numero1 == 7) {
			System.out.println("sabado");
		}
		else {
			System.out.println("numero invalido");
		}
	}
}
}
