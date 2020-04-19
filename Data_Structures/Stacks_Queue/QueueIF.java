package Stacks_Queue;

public interface QueueIF<E> {
    boolean isEmpty();
    E peek();        // returns null on empty queue
    E poll();         // returns null on empty queue
    boolean offer(E obj);
}
