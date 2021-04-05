# LeetCode

[![](https://img.shields.io/badge/Algo-Daily-orange?style=flat-square)	](https://github.com/ceezyyy/daily-algo)

Study notes for data structures & algorithms

## Data Structures

### Linked List



### Tree

**Root-to-leaf**

int: a + b (choose a non-empty element between a and b)

boolean: false (if root is null)

void: return 



**Whether the node is empty**

(root) ? null : root



**Ancestor**

(root, parent, grandparent)



**Level order traversal**

queue: store the nodes, and keep *FIFO*

n: the size of each layer




### Stack and Queue





### Hashtable





### String

**StringBuilder**

*append*()

*charAt()*

*deleteCharAt()*

*length()*



### Graph







### Bit Manipulation









## Algorithms

### Two Pointers



### Sorting





### Greedy





### Binary Seach



### Divide and Conquer





### Searching

**Backtracking**

```java
private T result;

void backtracking(currentChoice, path) {
  
  if (reach the goal) {
    result.add(copyOfPath);
    return;
  }
  
  // Making choices w/ constraints
  for (choice : choices) {
    path.add(choice);
    backtracking(nextChoice, path);
    path.removeLast();
  }
  
}
```





### Dynamic Programming



### Math






