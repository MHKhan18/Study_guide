public class SegmentTree{

    final int N; // size of input array
    private long[] values; // input array
    private long[] tree; // the array containing segment tree value

    private static int getMid(int s , int e){
        return (s + (e-s)/2) ;
    }

    public SegmentTree(long[] input){

        if (input == null){
            throw new IllegalArgumentException("Input array can not be null.");
        }
        N = input.length;
        values = input;

        int height = (int) Math.ceil((Math.log(N)/Math.log(2)));
        int max_size = 2 * (int) Math.pow(2 , height) - 1;
        tree = new long[max_size];

        build(0 , 0 , N-1); // root of seg tree represents the entire input array
    }

    private void build(int node, int start, int end){

        if (start == end){
            tree[node] = values[start];
        }

        else{
            int mid = getMid(start , end);
            // build left subtree
            build(2*node + 1 , start , mid);
            // build right subtree
            build(2*node + 2 , mid+1 , end);
            // internal nodes contain the sum
            tree[node] = tree[2*node + 1] + tree[2*node + 2];
        }
    }

    public long getRange(int queryS , int queryE){

        if (queryS < 0 || queryE >= N || queryS > queryE){
            throw new IllegalArgumentException("Make sure start <= right");
        }

        return query(0 , 0 , N-1 , queryS , queryE);
    }

    private long query(int node , int start , int end , int queryS , int queryE){

        if(queryE < start || end < queryS){ // no overlap
            return 0;
        }

        if(queryS <= start && queryE >= end){ // query range com[letely overlaps tree range
            return tree[node];
        }

        // partial overlap
        int mid = getMid(start , end);
        long left = query(2*node + 1 , start , mid , queryS , queryE);
        long right = query(2*node + 2 , mid+1 , end, queryS , queryE);

        return (left + right);
    }


    public void setValue(int index , long newVal){
        if(index < 0 || index >= N){
            throw new IllegalArgumentException("Make sure index is within range");
        }

        update(0 , 0 , N-1 , index , newVal);
    }

    private void update(int node , int start , int end , int idx , long val){

        if (start == end){
            values[idx] = val;
            tree[node] = val;
        }

        else{

            int mid = getMid(start , end);

            if (start <= idx && idx <= mid){ // idx is on the left
                update(2*node + 1 , start , mid , idx , val);
            }
            else{ // idx on the right
                update(2*node + 2 , mid+1 , end , idx , val);
            }

            tree[node] = tree[2*node + 1] + tree[2*node + 2];
        }
    }

    @Override
    public String toString(){
        return java.util.Arrays.toString(tree);
    }

    public static void main(String[] args){

        long[] input = {1 , 3, 5, 7, 9, 11 , 54};
        SegmentTree st = new SegmentTree(input);

        System.out.println(st);

        long valU = st.getRange(2 , 5);
        System.out.println(valU);

        st.setValue(3 , 78);
        System.out.println(st);

        long valV = st.getRange(2 , 5);
        System.out.println(valV);

    }

}