public class BinaryIndexTree{

    final int N; // size of tree
    private long[] tree; // the array containing BIT tree ranges

    private static int lsb(int i){
        return i & -i; 
    }

    public BinaryIndexTree(int sz){
        N = sz + 1; // make 1 based
        tree = new long[N];
    }

    // Construct a BIT with an initial set of values.
    // The 'values' array MUST BE ONE BASED i.e. values[0] does not get used
    public BinaryIndexTree(long[] values){
        if (values == null){
            throw new IllegalArgumentException("Input array can not be null.");
        }

        N = values.length;
        values[0] = 0L; // confirm assumption
        tree = values.clone();

        for(int i=1; i<N; i++){
            int parent = i + lsb(i);
            if (parent < N){
                tree[parent] += tree[i];
            }
        }
    }

    // Computes the prefix sum from [1 , i]
    private long prefixSum(int i){
        long sum = 0L;
        while(i > 0){
            sum += tree[i];
            i -= lsb(i);
        }
        return sum;
    }
    
    // Returns the sum of the interval [left, right]
    // left > 0 && right < N
    public long sum(int left , int right){
        if (right < left){
            throw new IllegalArgumentException("Make sure right >= left");
        }
        return prefixSum(right) - prefixSum(left-1);
    }

    // Get the value at index i
    public long get(int i){
        return sum(i , i);
    }

    // Add 'v' to index 'i'
    // 0 < i < N
    public void add(int i, long v){
        while(i < N){
            tree[i] += v;
            i += lsb(i);
        }
    }
    
    // Set index i to be equal to v
    public void set(int i , long v){
        add(i , v-get(i));
    }

    @Override
    public String toString(){
        return java.util.Arrays.toString(tree);
    }

    public static void main(String[] args) {
        
        long[] values = {0 , 1 , 2 , 2 , 4};

        BinaryIndexTree bt = new BinaryIndexTree(values);
        System.out.println(bt.sum(1 , 4)); //9

        bt.add(3 , 1);
        System.out.println(bt.sum(1 , 4)); //10

        bt.set(4 , 0);
        System.out.println(bt.sum(1 , 4)); //6

        System.out.println(bt.get(2)); //2
    }

}