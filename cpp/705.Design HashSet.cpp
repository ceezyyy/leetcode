/*
Source: LeetCode 705. Design HashSet
Author: ceezyyy
Date: 03-28-2019
Reference: @Grandyang http://www.cnblogs.com/grandyang/p/9966807.html
*/


/*
Easy

Share
Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1); // returns true
hashSet.contains(3); // returns false (not found)
hashSet.add(2);
hashSet.contains(2); // returns true
hashSet.remove(2);
hashSet.contains(2); // returns false (already removed)

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

*/


#include<iostream>
#include<vector>
using namespace std;

/*
Solution One:
*/

class MyHashSet {
public:
	/** Initialize your data structure here. */
	MyHashSet() {
		/*
		All values will be in the range of [0, 1000000]
		*/
		data.resize(1000000, 0);
		/*
		void resize( size_type size, TYPE val );
		*/
	}

	void add(int key) {
		data[key] = 1;
	}

	void remove(int key) {
		data[key] = 0;
	}

	/** Returns true if this set contains the specified element */
	bool contains(int key) {
		return data[key] == 1;
	}
private:
	/*
	All values will be in the range of [0, 1000000]
	*/
	vector<int> data;
};


/*
Submission Detail:

Runtime: 184 ms, faster than 20.61% of C++ online submissions for Design HashSet.
Memory Usage: 158.8 MB, less than 13.09% of C++ online submissions for Design HashSet.

*/


/*
Solution Two:
*/

class MyHashSet {
public:
	/** Initialize your data structure here. */
	MyHashSet() {
		/*
		All values will be in the range of [0, 1000000]
		*/
		data.resize(1000, vector<int>());
		/*
		void resize( size_type size, TYPE val );
		*/
	}

	void add(int key) {
		int hashKey = key % 1000;
		data[hashKey].resize(1000, 0);
		data[hashKey][key / 1000] = 1;
	}

	void remove(int key) {
		int hashKey = key % 1000;
		if (!data[hashKey].empty()) {
			data[hashKey][key / 1000] = 0;
		}
	}

	/** Returns true if this set contains the specified element */
	bool contains(int key) {
		int hashKey = key % 1000;
		return(!data[hashKey].empty() && data[hashKey][key / 1000] == 1);

	}
private:
	vector<vector<int>> data;
};


/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */


 /*
 Submission Detail:

 Runtime: 136 ms, faster than 41.80% of C++ online submissions for Design HashSet.
 Memory Usage: 92.3 MB, less than 21.43% of C++ online submissions for Design HashSet.

 */



