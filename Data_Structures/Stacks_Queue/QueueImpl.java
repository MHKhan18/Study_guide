package Stacks_Queue;

import java.util.Queue;
import java.util.AbstractQueue;

public class QueueImpl<E> implements QueueIF<E> {
    private StackIF<E> s1;  // stack that will hold the data
    private StackIF<E> s2;  // temporary stack used to convert LIFO policy into FIFO

    public QueueImpl() {
        s1 = new LinkedStack<E>(); // use our LinkedStack<> as stack implementation
        s2 = new LinkedStack<E>();
    }

    public boolean offer(E item) {
        s1.push(item);
        return true;
    }

    public boolean isEmpty() {
        return (s1.isEmpty());
    }

    // helper method to avoid duplication of code in
    // peek() and poll()
    //
    // When the flag topToBeAddedBack is true, this
    // helper method emulates peek
    // When the flag topToBeAddedBack is false, this
    // helper method emulates poll
    private E peekPoll(boolean topToBeAddedBack) {
        E result = null;   // default return value on empty Queue

        while (!s1.isEmpty()) {
            result = s1.pop();

            // did we just get the last item?  If not, add it to q2
            if (!s1.isEmpty()) {
                s2.push(result);
            }
        }

        // If this queue wasn't initially empty, then at this point
        // the variable result holds the value that was added first,
        // i.e., the front of the logical queue represented by the two
        // stacks

        if (topToBeAddedBack) {
            s2.push(result);
        }

        // now let's dump everything back into s1
        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }

        return result;
    }

    public E peek() {
        return peekPoll(true);
    }

    public E poll() {
        return peekPoll(false);
    }


}
