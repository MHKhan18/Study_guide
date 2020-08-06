
class TrieNode{

    private TrieNode[] links;
    private final int CHARSET = 26;
    private boolean isEnd;

    public TrieNode(){
        links = new TrieNode[CHARSET];
        isEnd = false;
    }

    public boolean containsKey(char ch){
        return links[ch - 'a'] != null;
    }

    public TrieNode get(char ch){
        return links[ch - 'a'];
    }

    public void put(char ch , TrieNode node){
        links[ch - 'a'] = node;
    }

    public void setEnd(){
        isEnd = true;
    }

    public boolean isEnd(){
        return isEnd;
    }

}


public class Trie{

    private TrieNode root ;

    public Trie(){
        root = new TrieNode();
    }

    public void insert(String word){
        TrieNode node = root;
        for (int i=0; i < word.length(); i++){
            char currentChar = word.charAt(i);
            if (!node.containsKey(currentChar)){
                node.put(currentChar , new TrieNode());
            }
            node = node.get(currentChar);
        }
        node.setEnd();
    }

    /*
        search a prefix or whole key in the trie and
        return the node where search ends
    */
    private TrieNode searchPrefix(String word){
        TrieNode node = root;
        for (int i=0; i<word.length(); i++ ){
            char currChar = word.charAt(i);
            if (node.containsKey(currChar)){
                node = node.get(currChar);
            }
            else{
                return null;
            }
        }
        return node;
    }

    public boolean search(String word){
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd();
    }

    public boolean startsWith(String prefix){
        TrieNode node = searchPrefix(prefix);
        return node != null;
    }

    public static void main(String[] args){

        Trie trie1 = new Trie();
        trie1.insert("messi");
        trie1.insert("ronaldo");
        trie1.insert("ron");

        boolean test1 = trie1.search("messi"); //true
        boolean test2 = trie1.search("mess"); // false
        boolean test3 = trie1.search("ron"); // true
        boolean test4 = trie1.search("lemon"); // false
        boolean test5 = trie1.search("roneldo"); // false

        boolean test6 = trie1.startsWith("mess"); // true
        boolean test7 = trie1.startsWith("ron"); // true
        boolean test8 = trie1.startsWith("ronaldo"); // true
        boolean test9 = trie1.startsWith("chris"); //false
        
        System.out.println(test1);
        System.out.println(test2);
        System.out.println(test3);
        System.out.println(test4);
        System.out.println(test5);
        System.out.println(test6);
        System.out.println(test7);
        System.out.println(test8);
        System.out.println(test9);

    } 



}