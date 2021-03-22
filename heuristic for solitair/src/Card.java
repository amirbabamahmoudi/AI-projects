public class Card {

    private int number;
    private char color;

    public Card(String str) {
        this.color = str.charAt(1);
        String s=Character.toString(color);
        String [] st = str.split(s);
        this.number = Integer.parseInt(st[0]);  ;

    }

    public int getNumber() {
        return number;
    }

    public char getColor() {
        return color;
    }

    @Override
    public String toString() {
        return "" + number + color + " ";
    }
}
