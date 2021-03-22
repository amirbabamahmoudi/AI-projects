import java.util.*;

public class State {

    private State parent;
    private ArrayList<State> neighbour = new ArrayList<>();
    private ArrayList<Section> sections = new ArrayList<>();
    private int setNeigh = 0;
    private int gCost;
    private int heuristic;
    private int fCost;

    public State(ArrayList<Section> sections, int cost) {

        this.sections = sections;
        this.gCost = cost;
        setHeuristic();
        this.fCost = gCost + heuristic;
    }

    public void print(){
        for (Section sec : sections){
            if(sec.getCards().size() == 0){
                System.out.println("#");
            }else{
                sec.print();
                System.out.println();
            }

        }
        System.out.println();
    }

    public Boolean isFinish(){
        for (Section sec : sections){
            if (!sec.isSort()){
                return false;
            }
        }
        return true;
    }

    public ArrayList<State> getNeighbour() {
        return neighbour;
    }

    public void setNeighbour() {
        if (setNeigh == 0) {
            setNeigh =1;
            for (int i = 0; i < sections.size(); i++) {
                if (sections.get(i).getCards().size() > 0) {
                    int x = sections.get(i).getTopCard().getNumber();
                    outer:
                    for (int j = 0; j < sections.size(); j++) {
                        int y = 0;
                        if (sections.get(j).getCards().size() > 0) {
                            y = sections.get(j).getTopCard().getNumber();
                        }
                        if (y == 0 || x < y) {
                            ArrayList<Section> newSections = new ArrayList<>();
                            for (Section sec : sections) {
                                Section newSec = new Section(sec.toString());
                                newSections.add(newSec);
                            }

                            Card card = newSections.get(i).popTopCard();
                            newSections.get(j).addCardToTop(card);
                            State s = new State(newSections, this.getGCost() + 1);
                            for (State state : neighbour){
                                if (state.equals(s)){
                                    continue outer;
                                }
                            }
                            neighbour.add(s);
                            s.addNeighbour(this);
                        }
                    }
                }
            }
        }
    }

    private void addNeighbour(State s){
        neighbour.add(s);
    }

    public ArrayList<Section> getSections() {
        return sections;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof State)) return false;
        State state = (State) o;
        for (int i = 0; i<sections.size(); i++){
            if (!sections.get(i).toString().equals(state.sections.get(i).toString())){
                return false;
            }

        }
        return true;
    }

    public void setHeuristic() {

        heuristic = 0;

        for (int i = 0; i < sections.size(); i++) {
            HashSet<Character> colors = new HashSet<>();

            if (sections.get(i).getCards().size() > 1) {
                for (int j = 0; j < sections.get(i).getCards().size(); j++) {
                    colors.add(sections.get(i).getCards().get(j).getColor());
                }

                heuristic += colors.size()-1;

                for (int j = 1; j < sections.get(i).getCards().size(); j++) {
                    if(sections.get(i).getCards().get(j).getNumber() >= sections.get(i).getCards().get(j-1).getNumber()){
                        heuristic += 1;
                    }
                }

            }else if(sections.get(i).getCards().size() == 1){
                if (Main.m > 1){
                    heuristic += 1;
                }
            }


        }

    }

    public int getHeuristic() {
        return heuristic;
    }

    public int getGCost() {
        return gCost;
    }

    public int getFCost() {
        return fCost;
    }

    public State getParent() {
        return parent;
    }

    public void setParent(State parent) {
        this.parent = parent;
    }
}


//4 2 3
//1f 2f 3f
//1g 2g 3g
//#
//#
