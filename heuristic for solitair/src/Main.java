import java.util.ArrayList;
import java.util.Scanner;
import java.lang.*;

public class Main {
    static int k, m, n;
    public static void main(String[] args) {
        long startTime = System.nanoTime();

        Scanner input = new Scanner(System.in);

        k = input.nextInt();
        m = input.nextInt();
        n = input.nextInt();
        input.nextLine();

        String row;

        ArrayList<Section> secRoot = new ArrayList<>();

        for(int i=0; i<k; i++){
            row  = input.nextLine();
            secRoot.add(new Section(row));
        }
        State root = new State(secRoot, 0);
        root.setParent(null);

        Graph graph = new Graph(root);


        graph.AStar(root);
        long endTime   = System.nanoTime();
        long totalTime = (endTime - startTime) / 1000000;
        System.out.print("total search time is : ");
        System.out.println(totalTime);
    }

}
