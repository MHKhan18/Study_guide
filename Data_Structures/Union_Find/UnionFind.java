


// Collected from William Fiset's repo

// Implementation of UnionFind / Disjoint Set witn Path Compression for Integers

public class UnionFind{

    private int size; // no. of elements in this union find
    private int[] sizes; // size of each component
    private int[] id; // id[i] points to the parent of i, id[i]==i -> root node
    // a hash map could be defined to map generic objects to integers in range [0 , size)
    private int numComponents; // no. of components 


    public UnionFind(int size){

        if (size <= 0) throw new IllegalArgumentException("Size <= 0 is not allowed.");

        this.size = numComponents = size;
        sizes = new int[size];
        id = new int[size];

        for (int i=0 ; i < size ; i++){
            id[i] = i; // self root
            sizes[i] = 1; // each node is a component
        }
    }


    // finds which compnent/set contains 'p'
    // takes amortized constant time 
    public int find(int p){

        // find the root of the component containing p
        int root = p;
        while (root != id[root]){
            root = id[root];
        }

        // path compression
        while (p != root){
            int next = id[p];
            id[p] = root;
            p = next;
        }

        return root;
    }

    // returns whether or not the elements 'p' and 'q' are in the same component
    public boolean connected(int p , int q){
        return find(p) == find(q);
    }

    // returns the size of the component 'p' belongs to
    public int compnentSize(int p){
        return sizes[find(p)];
    }

    // returns the number of elements in this UnionFind
    public int size(){
        return size;
    }

    // returns the number of components remaining
    public int compnents(){
        return numComponents;
    }

    // unify the components containing elements 'p' and 'q'
    public void unify(int p , int q){

        // nothing to do if already in same component
        if (connected(p,q)) return ;

        int root1 = find(p);
        int root2 = find(q);

        if (sizes[root1] < sizes[root2]){
            sizes[root2] += sizes[root1];
            id[root1] = root2; // component containing p is merged into component conatining q
        }
        else{
            sizes[root1] += sizes[root2];
            id[root2] = root1; // component containing q is merged into commponent containing p
        }

        numComponents--;
    }

    public static void main(String[] args){

        UnionFind testObj = new UnionFind(10);
        testObj.unify(0,1);
        testObj.unify(2,3);
        testObj.unify(4,5);
        testObj.unify(6,7);
        testObj.unify(8,9);
        testObj.unify(9,6);
        testObj.unify(7,5);
        testObj.unify(0,2);
        testObj.unify(3,4);
        testObj.unify(6,1);
        testObj.unify(8,9);
        
        // root of all nodes is 8
        System.out.println(testObj.find(7));
        System.out.println(testObj.find(2));
        System.out.println(testObj.compnents()); // 1
    
    }

}