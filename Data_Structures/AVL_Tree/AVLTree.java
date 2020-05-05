package AVL_Tree;

import Binary_Trees.BinaryTreePrinter;


/** Self-balancing binary search tree using the algorithm defined by Adelson-Velskii and Landis.
*/
public class AVLTree<E extends Comparable<E>> extends BinarySearchTreeWithRotate<E> {
	
	/** Class to represent an AVL Node. It extends the
	BinaryTree.Node by adding the balance field.
	*/
	private static class AVLNode<E> extends Node<E> {
		
		/** Constant to indicate left-heavy */
		public static final int LEFT_HEAVY = -1;
		
		/** Constant to indicate balanced */
		public static final int BALANCED = 0;
		
		/** Constant to indicate right-heavy */
		public static final int RIGHT_HEAVY = 1;
		
		/** balance is right subtree height � left subtree height */
		private int balance;
		
		// Methods
		/** Construct a node with the given item as the data field.
		@param item The data field
		*/
		public AVLNode(E item) {
			super(item);
			balance = BALANCED;
		}
		/** Return a string representation of this object.
		The balance value is appended to the contents.
		@return String representation of this object
		*/
		@Override
		public String toString() {
			return balance + ": " + super.toString();
		}
	}
	
	
	
	// Data Fields
	/** Flag to indicate that height of tree has increased. */
	private boolean increase;
	/** Flag to indicate that height of tree has decreased. */
	private boolean decrease;
	
	//Methods
	
	
	
	/** add starter method.
	@pre the item to insert implements the Comparable interface.
	@param item The item being inserted.
	@return true if the object is inserted; false if the object already exists in the tree
	@throws ClassCastException if item is not Comparable
	*/
	@Override
	public boolean add(E item) {
		increase = false;
		root = add((AVLNode<E>) root, item);
		return addReturn;
	}
	
	/** Starter method delete.
	post: The object is not in the tree.
	@param target The object to be deleted
	@return The object deleted from the tree or null if the object was not in the tree
	@throws ClassCastException if target does not implement Comparable
	*/
	@Override
	public E delete( E target) {
		decrease = false;
		root = (AVLNode<E>)delete((AVLNode<E>)root, target);
		return deleteReturn;
	}
	
	/** Recursive add method. Inserts the given object into the tree.
	@post addReturn is set true if the item is inserted,
	false if the item is already in the tree.
	@param localRoot The local root of the subtree
	@param item The object to be inserted
	@return The new local root of the subtree with the item inserted
	*/
	private AVLNode<E> add(AVLNode<E> localRoot, E item){
		
		//insertion
		if (localRoot == null) {
			addReturn = true;
			increase = true;
			return new AVLNode<E>(item);
			}
		
		// item already in tree
		if (item.compareTo(localRoot.data) == 0) {
			// Item is already in the tree.
			increase = false;
			addReturn = false;
			return localRoot;
			}
		
		else if (item.compareTo(localRoot.data) < 0) {
			// item < data
			localRoot.left = add((AVLNode<E>) localRoot.left, item);
			
			if (increase) {
				decrementBalance(localRoot);
				if (localRoot.balance < AVLNode.LEFT_HEAVY) {
					increase = false;
					return rebalanceLeft(localRoot);
				}
				
			}
			return localRoot; // Rebalance not needed.
		}
		
		// greater than case
		else { 
			// item > data
			localRoot.right = add((AVLNode<E>) localRoot.right, item);
			
			if (increase) {
				incrementBalance(localRoot);
				if (localRoot.balance > AVLNode.RIGHT_HEAVY) {
					increase = false;
					return rebalanceRight(localRoot);
				 } 
			 }
			return localRoot;  // rebalance not needed 
			
		}
		
	}
	
	/** Recursive delete method.
	post: The item is not in the tree;
	deleteReturn is equal to the deleted item
	as it was stored in the tree 
	or null if the item was not found.
	@param localRoot The root of the current subtree
	@param item The item to be deleted
	@return The modified local root that does not contain the item
	*/
	private AVLNode<E> delete(AVLNode<E> localRoot, E item) {
		if (localRoot == null) {
			// item is not in the tree.
			decrease = false;
			deleteReturn = null;
			return localRoot;
		}
		// Search for item to delete.
		int compResult = item.compareTo(localRoot.data);
		if (compResult < 0) {
			// item is smaller than localRoot.data.
			localRoot.left = delete((AVLNode<E>)localRoot.left, item);
			if (decrease) {
				incrementBalance(localRoot);
				if ( localRoot.balance > AVLNode.RIGHT_HEAVY ) {
					return rebalanceRight(localRoot);
				}
				
			}
			return localRoot; // rebalance not needed
		} 
		else if (compResult > 0) {
			// item is larger than localRoot.data.
			localRoot.right = delete((AVLNode<E>)localRoot.right, item);
			if(decrease) {
				decrementBalance(localRoot);
				if ( localRoot.balance < AVLNode.LEFT_HEAVY ) {
					return rebalanceLeft(localRoot);
				}
			}
			return localRoot; // rebalance not needed.
		} 
		else {
			// item is at local root.
			deleteReturn = localRoot.data;
			decrease = true;
			if (localRoot.left == null) {
				// If there is no left child, return right child which can also be null.
				return (AVLNode<E>)localRoot.right;
			} else if (localRoot.right == null) {
				// If there is no right child, return left child.
				return (AVLNode<E>)localRoot.left;
			} else {
				// Node being deleted has 2 children, replace the data
				// with inorder predecessor.
				
				if (localRoot.left.right == null) {
					// The left child has no right child.
					// Replace the data with the data in the left child.
					localRoot.data = localRoot.left.data;
					// Replace the left child with its left child.
					localRoot.left = localRoot.left.left;
					

					incrementBalance(localRoot);
					if ( localRoot.balance > AVLNode.RIGHT_HEAVY ) {
						return rebalanceRight(localRoot);
					}
					return localRoot;
					
				} else {
					// Search for the inorder predecessor (ip) and
					// replace deleted node's data with ip.
					AVLNode<E> node = (AVLNode<E>)localRoot.left ;
					localRoot.data = findLargestChild(node);
					localRoot.left = modifyLeft((AVLNode<E>)localRoot.left);
					if (decrease) {
						incrementBalance(localRoot);
						if ( localRoot.balance > AVLNode.RIGHT_HEAVY ) {
							return rebalanceRight(localRoot);
						}
						
					}
					return localRoot;
				}
				
			}
		}
	}
	
	/** Find the node that is the
	inorder predecessor and replace it
	with its left child (if any).
	post: The inorder predecessor is removed from the tree.
	@param parent The parent of possible inorder
	predecessor (ip)
	@return The data in the ip
	*/
	private E findLargestChild(AVLNode<E> parent) {
	// If the right child has no right child, it is
	// the inorder predecessor.
		
		if ( parent.balance == AVLNode.RIGHT_HEAVY) {
			decrease = true;
		}
		AVLNode<E> c_parent = parent;
		while (c_parent.right.right != null ) {
			c_parent = (AVLNode<E>)c_parent.right;
		}
		E returnValue = c_parent.right.data;
		c_parent.right = c_parent.right.left;
		
		return returnValue;
	}
	
	private AVLNode<E> modifyLeft(AVLNode<E> parent) {
		// If the right child has no right child, it is
		// the inorder predecessor.
		
		decrementBalance(parent);
		if ( parent.balance < AVLNode.LEFT_HEAVY ) {
			parent = rebalanceLeft(parent);
		}
		return parent;
		
	}
	
	
	
	/** Method to rebalance left.
	@pre localRoot is the root of an AVL subtree that is critically left-heavy.
	@post Balance is restored.
	@param localRoot Root of the AVL subtree that needs rebalancing
	@return a new localRoot
	*/
	private AVLNode<E> rebalanceLeft(AVLNode<E> localRoot) {
		
		// Obtain reference to left child.
		AVLNode<E> leftChild = (AVLNode<E>) localRoot.left;
		
		// See whether left-right heavy.
		if (leftChild.balance > AVLNode.BALANCED) {  // left -right case
			// Obtain reference to left-right child.
			AVLNode<E> leftRightChild = (AVLNode<E>) leftChild.right;
			/** Adjust the balances to be their new values after the rotations are performed. */
			if (leftRightChild.balance < AVLNode.BALANCED) {
				leftChild.balance = AVLNode.BALANCED;
				leftRightChild.balance = AVLNode.BALANCED;
				localRoot.balance = AVLNode.RIGHT_HEAVY;
			} 
			else if (leftRightChild.balance > AVLNode.BALANCED) {
				leftChild.balance = AVLNode.LEFT_HEAVY;
				leftRightChild.balance = AVLNode.BALANCED;
				localRoot.balance = AVLNode.BALANCED;
			}
			else {  // [deletion case]
				leftChild.balance = AVLNode.BALANCED;
				leftRightChild.balance = AVLNode.BALANCED;
				localRoot.balance = AVLNode.BALANCED;
			}
			// Perform left rotation.
			localRoot.left = rotateLeft(leftChild);
		}
		else if (leftChild.balance < AVLNode.BALANCED){  //Left-Left case
			/** In this case the leftChild (the new root) and the root (new right child) will both be balanced after the rotation. */
			leftChild.balance = AVLNode.BALANCED;
			localRoot.balance = AVLNode.BALANCED;
		}
		else {  // leftChild.balance == AVLNode.BALANCED [ deletion case ]
			localRoot.balance = AVLNode.LEFT_HEAVY;
			leftChild.balance = AVLNode.RIGHT_HEAVY;
		}
		
		if ( localRoot.balance == AVLNode.BALANCED ) {
			decrease = true;
		}
		else {
			decrease = false;
		}
		// Now rotate the local root right.
		return (AVLNode<E>) rotateRight(localRoot);
	}
	
	
	/** Method to rebalance right.
	@pre localRoot is the root of an AVL subtree that is critically right-heavy.
	@post Balance is restored.
	@param localRoot Root of the AVL subtree that needs rebalancing
	@return a new localRoot
	*/
	private AVLNode<E> rebalanceRight(AVLNode<E> localRoot) {
		
		// Assert: localRoot.balance > 1
		
		// Obtain reference to right child.
		AVLNode<E> rightChild = (AVLNode<E>) localRoot.right;
		
		if ( rightChild.balance < AVLNode.BALANCED ) {  // RL-case
			// Obtain reference to right-left child.
			AVLNode<E> rightLeftChild = (AVLNode<E>) rightChild.left;
			
			if ( rightLeftChild.balance < AVLNode.BALANCED ) { // right-left-left case
				localRoot.balance = AVLNode.BALANCED;
				rightChild.balance = AVLNode.RIGHT_HEAVY;
				rightLeftChild.balance = AVLNode.BALANCED ;
			}
			else if ( rightLeftChild.balance > AVLNode.BALANCED ){  // right-left-right case
				localRoot.balance = AVLNode.LEFT_HEAVY;
				rightChild.balance = AVLNode.BALANCED;
				rightLeftChild.balance = AVLNode.BALANCED;
			}
			else { // [deletion case]
				localRoot.balance = AVLNode.BALANCED;
				rightChild.balance = AVLNode.BALANCED;
				rightLeftChild.balance = AVLNode.BALANCED;
				
			}
			// perform right rotation
			localRoot.right = rotateRight(rightChild);
		}
		
		else if ( rightChild.balance > AVLNode.BALANCED ) { // right-right case
			/** In this case the rightChild (the new root) and the root (new left child) will both be balanced after the rotation. */
			rightChild.balance = AVLNode.BALANCED;
			localRoot.balance = AVLNode.BALANCED;
		}
		else { // [deletion case]
			rightChild.balance = AVLNode.LEFT_HEAVY;
			localRoot.balance = AVLNode.RIGHT_HEAVY;
		}
		
		if ( localRoot.balance == AVLNode.BALANCED ) {
			decrease = true;
		}
		else {
			decrease = false;
		} 
		
		// Now rotate the local root left.
		return (AVLNode<E>) rotateLeft(localRoot);
		
	}
	
	private void decrementBalance(AVLNode<E> node) {
		
		int prev_balance = node.balance;
		// Decrement the balance.
		node.balance--;
		if (node.balance == AVLNode.BALANCED) {
			/** If now balanced, overall height has not increased. */
			increase = false;
			/** balancing an unbalanced tree decreases the height */
			decrease = true;
		}
		else if ( prev_balance == AVLNode.BALANCED && node.balance != AVLNode.BALANCED ) {
			/** if a tree was balanced and a deletion makes it unbalanced, then height did not decrease. */
			decrease = false;
			increase = true;
		 }  
		
	}
	
	private void incrementBalance( AVLNode<E> node ) {
		
		int prev_balance = node.balance;
		//increment the balance
		node.balance++;
		if (node.balance == AVLNode.BALANCED) {
			/** If now balanced, overall height has not increased. */
			increase = false;
			decrease = true;
		}
		else if ( prev_balance == AVLNode.BALANCED && node.balance != AVLNode.BALANCED ) {
			/** if a tree was balanced and a deletion makes it unbalanced, then height did not decrease. */
			decrease = false;
			increase = true;
		} 
	}
	
	public static void main ( String[] args) {
		AVLTree<Integer>bst = new AVLTree<>();
		bst.add(1);
		bst.add(2);
		bst.add(3);
		bst.add(4);
		bst.add(5);
		bst.add(6);
		bst.add(7);
		bst.add(8);
		bst.add(9);
		bst.add(10);
		bst.add(11);
		bst.add(12);
		BinaryTreePrinter.printNode(bst.root);
		System.out.println("--------------------------------------------------------------------------------------");
		bst.delete(5);
		bst.delete(10);
		bst.delete(8);
		bst.delete(12);
		bst.delete(7);
		bst.delete(2);
		bst.delete(4);
		bst.delete(6);
		bst.delete(11);
		bst.delete(3);
		BinaryTreePrinter.printNode(bst.root);
		System.out.println("--------------------------------------------------------------------------------------");
		AVLTree<Integer>bst2 = new AVLTree<>();
		bst2.add(12);
		bst2.add(11);
		bst2.add(10);
		bst2.add(9);
		bst2.add(8);
		bst2.add(7);
		bst2.add(6);
		bst2.add(5);
		bst2.add(4);
		bst2.add(3);
		bst2.add(2);
		bst2.add(1);
		BinaryTreePrinter.printNode(bst2.root);
		System.out.println("--------------------------------------------------------------------------------------");
		bst2.delete(5);
		bst2.delete(7);
		BinaryTreePrinter.printNode(bst2.root);
		System.out.println("--------------------------------------------------------------------------------------");
		bst2.delete(4);
		bst2.delete(9);
		bst2.delete(10);
	    bst2.delete(2);
	    bst2.delete(6);
	    bst2.add(9);
	    bst2.delete(11);
	    bst2.delete(8);
	    bst2.delete(1);
		BinaryTreePrinter.printNode(bst2.root);
		System.out.println("--------------------------------------------------------------------------------------");
		
	}
	
	
	
	
}