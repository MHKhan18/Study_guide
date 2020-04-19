package Stacks_Queue;

import java.util.Queue;
import java.util.LinkedList;
import java.util.EmptyStackException;

public class StackImpl<E> implements StackIF<E> {
    private Queue<E> q1;   // queue that will hold the data
    private Queue<E> q2;   // temporary queue used when popping to convert FIFO policy into LIFO

    public StackImpl() {
        q1 = new LinkedList<E>(); // use LinkedList<> as queue implementation
        q2 = new LinkedList<E>();
    }

    public boolean isEmpty() {
        return (q1.isEmpty());
    }

    // helper method to avoid duplication of code in
    // peek() and pop()
    //
    // When the flag topToBeAddedBack is true, this
    // helper method emulates peek
    // When the flag topToBeAddedBack is false, this
    // helper method emulates pop
    private E peekPop(boolean topToBeAddedBack) {
        if (q1.isEmpty()) {
            throw new EmptyStackException();
        } else {
            E result = null;
            while (!q1.isEmpty()) {
                result = q1.poll();

                // did we just get the last item?  If not, add it to q2
                if (!q1.isEmpty()) {
                    q2.offer(result);
                }
            }

            // at this point, the variable result holds the value that
            // was added last, i.e., the top of the logical stack
            // represented by the two queues

            if (topToBeAddedBack) {
                q2.offer(result);
            }

            // now let's swap the role of q1 and q2
            Queue<E> aux = q1;
            q1 = q2;
            q2 = aux;

            return result;
        }
    }

    public E peek() {
        return peekPop(true);
    }

    public E pop() {
        return peekPop(false);
    }

    public E push(E data) {
        q1.offer(data);
        return data;
    }


}
