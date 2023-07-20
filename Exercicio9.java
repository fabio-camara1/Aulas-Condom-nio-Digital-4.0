package Fundamentos;
import java.util.Scanner;

public class Exercicio9 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite um numero:");
		int resp = entrada.nextInt();
		if (resp >= 0) {
			System.out.println("numero é positivo");
		}
		else {
			System.out.println("numero negativo");
		}
	}
}
}
