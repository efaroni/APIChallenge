public class APIChallenge
{
	public static void main(String[] args) {
		System.out.println("Testing strings");
		System.out.println("About to reverse abcd to get " + reverse("abcd"));
		System.out.println("About to reverse to get " + reverse(""));
		System.out.println("About to reverse  to get " + reverse(" "));

	}
	public static String reverse(String str) {
		String reversed = "";
		for (int i = str.length() - 1; i >= 0; i -= 1) {
			reversed += str.charAt(i);
		}
		return reversed;
	}
}