import java.util.ArrayList;

public class Section {
    private ArrayList<Card> cards = new ArrayList<>();

    public Section(String row) {
        if(!(row.equals("#") || row.equals(""))){
            String[] arrOfStr = row.split(" ", 0);

            for (String a : arrOfStr)
                addCard(a);
        }
    }

    public void addCard(String a){
        this.cards.add(new Card(a));
    }

    public void print(){
        for (Card card : cards){
            System.out.print(card.toString());
        }
    }

    public String toString(){
        String str = "";
        for (Card card : cards){
            str += card.toString();
        }
        return str;
    }

    public Boolean isSort(){
        for (int i = 0; i<cards.size() ; i++){
            char c = cards.get(0).getColor();
            if (cards.get(i).getNumber() != Main.n - i){
                return false;
            }else {
                if (c != cards.get(i).getColor()){
                    return false;
                }

            }
        }
        return true;
    }

    public ArrayList<Card> getCards() {
        return cards;
    }

    public Card getTopCard(){
        return cards.get(cards.size()-1);
    }

    public Card popTopCard(){
        Card card = cards.get(cards.size()-1);
        cards.remove(cards.get(cards.size()-1));
        return card;
    }

    public void addCardToTop(Card card){
        cards.add(card);
    }
}
