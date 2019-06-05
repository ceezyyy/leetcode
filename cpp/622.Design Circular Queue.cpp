/**
 * Source: LeetCode 622. Design Circular Queue 
 * Author: ceezyyy
 * Date: 06-05-2019
 * Reference: @Grandyang https://www.cnblogs.com/grandyang/p/9899034.html
 */


/*
Medium

Share
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called ��Ring Buffer��.
One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
Your implementation should support following operations:
MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.

Example:
MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1); // return true
circularQueue.enQueue(2); // return true
circularQueue.enQueue(3); // return true
circularQueue.enQueue(4); // return false, the queue is full
circularQueue.Rear(); // return 3
circularQueue.isFull(); // return true
circularQueue.deQueue(); // return true
circularQueue.enQueue(4); // return true
circularQueue.Rear(); // return 4

Note:
All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.

*/


#include<vector>
using namespace std;

// SolutionOne
class MyCircularQueue {
public:
	/** Initialize your data structure here. Set the size of the queue to be k. */
	MyCircularQueue(int k) {
		size = k;
	}

	/** Insert an element into the circular queue. Return true if the operation is successful. */
	bool enQueue(int value) {
		if (isFull()) {
			return false;
		}
		else {
			data.push_back(value);
			return true;
		}
	}

	/** Delete an element from the circular queue. Return true if the operation is successful. */
	bool deQueue() {
		if (isEmpty()) {
			return false;
		}
		else {
			data.erase(data.begin());
			return true;
		}

	}

	/** Get the front item from the queue. */
	int Front() {
		if (isEmpty()) {
			return -1;
		}
		return data.front();
	}

	/** Get the last item from the queue. */
	int Rear() {
		if (isEmpty()) {
			return -1;
		}
		// if the queue is not empty, return the last element of the queue
		return data.back();
	}

	/** Checks whether the circular queue is empty or not. */
	bool isEmpty() {
		return data.empty();
	}

	/** Checks whether the circular queue is full or not. */
	bool isFull() {
		return data.size() >= size;

	}
private:
	vector<int> data;
	int size;
};


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */


/**
 * Submission Detail:
 * Runtime: 36 ms, faster than 86.12% of C++ online submissions for Design Circular Queue.
 * Memory Usage: 16.5 MB, less than 74.54% of C++ online submissions for Design Circular Queue.
 */