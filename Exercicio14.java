package Fundamentos;

import java.util.Scanner;

public class Exercicio14 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite uma letra");
		char letra = entrada.next().charAt(0);
		if (letra == 'f') {
			System.out.println("femenino");
		}
		else if (letra == 'm') {
			System.out.println("masculino");
		}
	}
	
}
}
