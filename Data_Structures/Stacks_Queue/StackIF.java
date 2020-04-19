package Stacks_Queue;

public interface StackIF<E> {
    boolean isEmpty();
    E peek();        // might throw java.util.EmptyStackException
    E pop();         // might throw java.util.EmptyStackException
    E push(E obj);
}
