package Stacks_Queue;

import java.util.NoSuchElementException;


/** Class to implement interface StackInt<E> as a linked list. */
public class LinkedStack<E> implements StackIF<E> {
// Insert inner class Node<E> here. (See Listing 2.1)
	
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
	// Data Fields
	/** The reference to the first stack node. */
	private Node<E> topOfStackRef = null;
	private int size = 0;
	
	/** Insert a new item on top of the stack.
	@post The new item is the top item on the stack.
	All other items are one position lower.
	@param obj The item to be inserted
	@return The item that was inserted
	*/
	
	@Override
	public E push(E obj) {
		topOfStackRef = new Node<>(obj, topOfStackRef);
		size++;
		return obj;
	}
	
	/** Remove and return the top item on the stack.
	@pre The stack is not empty.
	@post The top item on the stack has been
	removed and the stack is one item smaller.
	@return The top item on the stack
	@throws NoSuchElementException if the stack is empty
	*/
	@Override
	public E pop() {
		if (isEmpty()) {
			throw new NoSuchElementException();
		}
		else {
			E result = topOfStackRef.data;
			topOfStackRef = topOfStackRef.next;
			size--;
			return result;
		}
	}
	
	/** Return the top item on the stack.
	@pre The stack is not empty.
	@post The stack remains unchanged.
	@return The top item on the stack
	@throws NoSuchElementException if the stack is empty
	*/
	@Override
	public E peek() {
		if (isEmpty()) {
			throw new NoSuchElementException ();
		}
		else {
			return topOfStackRef.data;
		}
	}
	
	/** See whether the stack is empty.
	@return true if the stack is empty
	*/
	@Override
	public boolean isEmpty() {
		return topOfStackRef == null;
	}
	
	//Exercise
	
	public int size() {
		return size;
	}
}