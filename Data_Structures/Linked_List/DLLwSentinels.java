package LinkedList;

import java.util.*;

import LinkedList.KWLinkedList;


public class DLLwSentinels<E> extends AbstractList<E> {
	
	private static class Node<E> {
		private E data ;
		private Node <E> next , prev ;
		public Node (E data , Node <E> next , Node <E> prev ){ 
			this. data = data ; 
			this. next = next ; 
			this. prev = prev ; 
			}
		}
	
	private Node<E> start , end ;
	private int size ;
	
	// initialize the list with two dummy nodes pointing at each other
	public DLLwSentinels () {
		size = 0;
		start = new Node<E>(null , null , null );
		end = new Node<E>(null , null , start ); // sets end.prev = start
		start.next = end;
	}
	
	private Node <E> getNode (int i) {
		
		if (i<0 || i>=size) {
			throw new IndexOutOfBoundsException("Index out of range" + i);
		}
		Node<E> node;
		if (i < size/2){
			node = start.next;
			for (int k = 0; k < i; k++)
				node = node.next;
			}
		else {
			node = end.prev;
			for (int k = size-1; k > i; k--)
				node = node.prev;
			}
			return node;
		
	}
	private void addBefore (Node <E> n, E data ) {
		Node<E>insert = new Node<E>(data,n,n.prev);
		n.prev.next = insert;
		n.next.prev = insert;
		size++;
	}
	private void remove (Node<E>n) {
		n.prev.next = n.next;
		n.next.prev = n.prev;
		size--;
	}
	
	public void add( int i, E e) {
		if (i<0 || i>=size) {
			throw new IndexOutOfBoundsException("Index out of range" + i);
		}
		addBefore(getNode(i),e);
	}
	public E remove (int i) {
		if (i<0 || i>=size) {
			throw new IndexOutOfBoundsException("Index out of range" + i);
		}
		
		Node<E>target = getNode(i);
		E element = target.data;
		remove(target);
		return element;
	}
	
	//additions
	public int size() {
		return size;
	}
	
	public E get( int i) {
		Node<E> node = getNode(i);
		return node.data;
	}
	
	
}