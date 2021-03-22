import java.util.*;
import java.util.concurrent.ForkJoinPool;

public class Graph {


    ArrayList<State> visitedNodes = new ArrayList<>();
    ArrayList<State> frontier = new ArrayList<>();

    int toolid = 0;
    int bast = 0;

    State root;

    // Constructor
    Graph(State root) {

        this.root = root;
    }

    public void AStar(State s) {
        frontier.add(s);

        while (!frontier.isEmpty()){
            State current;
            current = smallest(frontier);
//            current.print();
//            System.out.println("current g :" + current.getGCost() );
//            System.out.println("current h :" + current.getHeuristic());
//            System.out.println("current f :" + current.getFCost());
            visitedNodes.add(current);
            bast ++;
            if (current.isFinish()) {
                System.out.println("depth = " + current.getGCost());
                System.out.println("explored = " + visitedNodes.size());
                System.out.println("frontier = " + toolid);

                ArrayList<State> path = new ArrayList<>();

                System.out.println("path from root to goal");
                while (current != null){
                    path.add(current);
                    current = current.getParent();
                }
                Collections.reverse(path);
                for (State parent: path) {
                    System.out.println("---------------------");
                    parent.print();
                }
                return;
            }
            frontier.remove(current);
            current.setNeighbour();
            for (State state : current.getNeighbour()){
                if (!visitedNodes.contains(state)){
                    state.setParent(current);
                    frontier.add(state);
                    toolid ++;
                }
            }
        }

    }

    public State smallest(ArrayList<State> arr) {
        int i;

        State min = arr.get(0);

        for (i = 1; i < arr.size(); i++)
            if (arr.get(i).getFCost() < min.getFCost())
                min = arr.get(i);

        return min;
    }

    public Boolean contain(State s) {
        for (State state : visitedNodes) {
            if (state.equals(s)) {
                return true;
            }
        }
        return false;
    }
}

//5 3 5
//5g 5r 4y
//2g 4r 3y 3g 2y
//1y 4g 1r
//1g 2r 5y 3r
//#