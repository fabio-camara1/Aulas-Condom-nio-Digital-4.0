package Fundamentos;
import java.util.Scanner; // le a entrada 

public class Exercicio8 {
public static void main(String[] args) {
	try (Scanner entrada = new Scanner(System.in)) {
		System.out.println("digite um numero");
		double resp = entrada.nextDouble();
		System.out.println(resp);
	}
			
}
}
