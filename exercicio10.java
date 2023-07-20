package Fundamentos;
import java.util.Scanner;

public class exercicio10 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite um numero:");
		int resp = entrada.nextInt();
		System.out.println(resp < 0 ? "numero negativo": "numero positivo");
	}
}
}
