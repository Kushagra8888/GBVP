/**
 * Created by kushasharma on 10/20/2015.
 */
public class Edge {
    Vertex vertex1;
    Vertex vertex2;

    public void Vertex(Vertex vertex1, Vertex vertex2){
        this.vertex1 = vertex1;
        this.vertex2 = vertex2;
    }

    public Vertex getVertex1(){
        return this.vertex1;
    }

    public Vertex getVertex2(){
        return this.vertex2;
    }
}
