class Node {

    public int value;
    public Node next;

    public Node(int n, Node next) {
        this.value = n;
        this.next = next;

    }

    public String toString(){
        return String.valueOf(this.value) + "->" + ((this.next != null) ? this.next : "x");
    }
}

public class jtest {

    public static void main(String []args){
        Node n = new Node(1, new Node(2, new Node(3, null)));
        System.out.println(n);
    }
    
}