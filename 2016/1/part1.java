public class aoc {
    public static void main(String[] args)
    {
        File file = new File("input.txt");
        Scanner myReader = new Scanner(file);
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            System.out.println(data);
        }
        myReader.close();
    }
}