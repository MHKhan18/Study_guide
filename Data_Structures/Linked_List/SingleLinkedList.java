/*<listing chapter="2" section="5">*/
package Linked_List;

/**
 * SingleLinkedList is a class that provides some of the
 * capabilities required by the List interface using
 * a single linked list data structure.
 * Only the following methods are provided:
 * get, set, add, remove, size, toString
 * @author Koffman and Wolfgang 
 */
public class SingleLinkedList<E> {

    // Nested Class
    /*<listing chapter="2" number="1">*/
    /** A Node is the building block for the SingleLinkedList */
    private static class Node<E> {

        /** The data value. */
        private E data;
        /** The link */
        private Node<E> next = null;

        /**
         * Construct a node with the given data value and link
         * @param data - The data value 
         * @param next - The link
         */
        public Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }

        /**
         * Construct a node with the given data value
         * @param data - The data value 
         */
        public Node(E data) {
            this(data, null);
        }
    }
    /*</listing>*/
    // Data fields
    /** A reference to the head of the list */
    private Node<E> head;
    /** The size of the list */
    private int size;
    
    
    // constructor
    public SingleLinkedList() {
    	head = null;
    	size = 0;
    }
    

    // Helper Methods
    /** Insert an item as the first item of the list.
     *	@param item The item to be inserted
     */
    private void addFirst(E item) {
        head = new Node<E>(item, head);
        size++;
    }

    /**
     * Add a node after a given node
     * @param node The node after which the new item is to be inserted
     * @param item The item to insert
     */
    private void addAfter(Node<E> node, E item) {
        node.next = new Node<E>(item, node.next);
        size++;
    }

    /**
     * Remove the first node from the list
     * @return The removed node's data or null if the list is empty
     */
    private E removeFirst() {
    	E data = null;
	
        if (head != null) {
        	data = head.data;
            head = head.next;
            size--;
	    }

	return data;
    }

    /**
     * Remove the node after a given node
     * @param node The node before the one to be removed
     * @return The data from the removed node, or null
     *          if there is no node to remove
     */
    private E removeAfter(Node<E> node) {
        Node<E> temp = node.next;
        E data = null;
	
        if (temp != null) {
            data = temp.data;
            node.next = temp.next;
            size--;
        }

        return data;
    }

    /**
     * Find the node at a specified index
     * @param index The index of the node sought
     * @return The node at index or null if it does not exist
     */
    private Node<E> getNode(int index) {
        Node<E> node = head;
        for (int i = 0; i < index && node != null; i++) {
            node = node.next;
        }
        return node;
    }

    // Public Methods
    /**
     * Get the data value at index
     * @param  The index of the element to return
     * @return The data at index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public E get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        Node<E> node = getNode(index);
        return node.data;
    }

    /**
     * Set the data value at index
     * @param index The index of the item to change
     * @param newValue The new value
     * @return The data value priviously at index
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public E set(int index, E newValue) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        Node<E> node = getNode(index);
        E result = node.data;
        node.data = newValue;
        return result;
    }

    /**
     * Insert the specified item at the specified position in the list.
     * Shifts the element currently at that position (if any) and any
     * subsequent elements to the right (adds one to their indicies)
     * @param index Index at which the specified item is to be inserted
     * @param item The item to be inserted
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void add(int index, E item) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        if (index == 0) {
            addFirst(item);
        } else {
            Node<E> node = getNode(index-1);
            addAfter(node, item);
        }
    }

    /**
     * Append the specified item to the end of the list
     * @param item The item to be appended
     * @return true (as specified by the Collection interface)
     */
    public boolean add(E item) {
        add(size, item);
        return true;
    }

    /*<exercise chapter="2" section="5" type="programming" number="1">*/
    /**
     * Remove the item at the specified position in the list. Shifts
     * any squsequent items to the left (subtracts one from their
     * indicies). Returns the tiem that was removed.
     * @param index The index of the item to be removed
     * @return The item that was at the specified position
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public E remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        
        if (index == 0) {
            return removeFirst();
        } else {
            Node<E> node = getNode(index - 1);
            return removeAfter(node);
        }
    }
    /*</exercise>*/

    /**
     * Query the size of the list
     * @return The number of objects in the list
     */
    int size() {
        return size;
    }

    /**
     * Obtain a string representation of the list
     * @return A String representation of the list 
     */
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Node<E> p = head;
        if (p != null) {
            while (p.next != null) {
                sb.append(p.data.toString());
                sb.append(" ==> ");
                p = p.next;
            }
            sb.append(p.data.toString());
        }
        sb.append("]");
        return sb.toString();
    }

    /*<exercise chapter="2" section="5" type="programming" number="3">*/
    /**
     * Remove the first occurence of element item.
     * @param item The item to be removed
     * @return true if item is found and removed; otherwise, return false.
     */
    public boolean remove(E item) {
        if (null == head) {
            return false;
        }
        Node<E> current = head;
        if (item.equals(current.data)) {
            removeFirst();
            return true;
        }
        while (current.next != null) {
            if (item.equals(current.next.data)) {
                removeAfter(current);
                return true;
            }
            current = current.next;
        }
        return false;
    }
    /*</exercise>*/

    /*<exercise chapter="2" section="5" type="programming" number="4">*/
    /**
     * Insert a new item before the one at position index,
     * starting at 0 for the list head. The new item is inserted
     * between the one at position index-1 and the one formally
     * at position index.
     * The exercise requirements are to not use any helper methods.
     * Since there already is an add method that uses helper
     * methods, this one is named add2.
     * @param index The index where the new item is to be inserted
     * @param item The item to be inserted
     * @throws IndexOutOfBoundsException if the index is out of range
     */
    public void add2(int index, E item) {
        if (index < 0 || index>=size) {
            throw new IndexOutOfBoundsException(Integer.toString(index));
        }
        if (index == 0) {
            head = new Node<E>(item, head);
            size++;
        } else {
            int i = index;
            Node<E> current = head;
            while (current != null && --i > 0) {
                current = current.next;
            }
            if (i == 0) {
                current.next = new Node<E>(item, current.next);
                size++;
            } else {
                throw new IndexOutOfBoundsException(Integer.toString(index));
            }
        }
    }
    /*</exercise>*/
    
    
    // < My Code >
    
    public int indexOf(E item) {
    	for (int i=0; i<size; i++) {
    		Node<E> node = getNode(i);
    		if (item.equals(node.data)) {
    			return i;
    		}
    	}
    	
    	return -1;
    }
    

    /*<exercise chapter="2" section="5" type="programming" number="2">*/
    public static void exercise_2_5_2() {
        // Create the list of figure 2.16
        Node<String> tom = new Node<String>("Tom", null);
        Node<String> dick = new Node<String>("Dick", null);
        Node<String> harry = new Node<String>("Harry", null);
        Node<String> sam = new Node<String>("Sam", null);
        Node<String> head = tom;
        tom.next = dick;
        dick.next = harry;
        harry.next = sam;
        //Insert "Bill" before "Tom"
        Node<String> bill = new Node<String>("Bill", tom);
        head = bill;
        //Insert Sue before Sam
        Node<String> sue = new Node<String>("Sue", sam);
        harry.next = sue;
        // Remove "Bill"
        head = head.next;
        // Remove "Sam"
        sue.next = sue.next.next;
        
     
    }
    /*</exercise>*/
    public static void main( String[] args) {
    	// test
        SingleLinkedList<String>sll = new SingleLinkedList<>();
        sll.add("lets");
        sll.add("do");
        sll.add("again");
        System.out.println(sll);
        sll.add(2,"it");
        sll.add(sll.size(),"really?");
        System.out.println(sll);
        sll.remove(0);
        sll.remove("it");
        System.out.println(sll);
        sll.set(2, "bruh");
        System.out.println(sll);
        System.out.println(sll.get(1));
        System.out.println(sll.indexOf("bruh"));
        
    }
    
    
    
    
}
/*</listing>*/
