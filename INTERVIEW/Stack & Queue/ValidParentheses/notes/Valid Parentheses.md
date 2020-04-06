# 20. Valid Parentheses

## Topic

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```



## Intuition

第一眼看到括号匹配问题，下意识地反应大概率会用到`stack` 。

为什么？因为`stack` 的特点是`LIFO` 也就是“后进先出”。

为什么“后进先出”就和括号匹配扯上关系了呢？因为括号匹配是从里到外的，一层一层往外的。显然，假设我们碰到左括号就将其压栈，遇到右括号就检查栈顶元素是否与其匹配，并且确保栈不为空，否则就没得给右括号匹配了。



## Explanation

这里需要一个`hashmap`来存储左右括号的对应关系（当然用`if`来判断也行）。

遍历数组（字符型数组 / 字符串），

>注意，这里说的字符串和数组概念其实类似，本质上都是一种线性有序结构，查找易，增删难。

遇到左括号：

压栈

遇到右括号：

1. 判断栈是否为空
2. 判断栈顶元素是否与当前右括号相匹配。

最终返回栈是否为空，看看是否所有都完全匹配。

## Code

**Java**

```java
class Solution {
    public boolean isValid(String s) {
        // Initialization of hashmap
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
        
        // Match the parentheses
        Stack<Character> stack = new Stack<>();
        // For loop char array 
        for (char ch : s.toCharArray()) {
            if (!map.containsKey(ch)) {
                // Nothing to be matched
                if (stack.isEmpty()) {
                    return false;
                }
                // Not the valid parentheses
                if (map.get(stack.pop()) != ch) {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }
        
        // All should be mathched and nothing left
        return stack.isEmpty();
    }
}

```

**Python**

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Note that an empty string is also considered valid.
        if not s: 
            return True
        hashmap, stack = {'(' : ')', '{' : '}', '[' : ']'}, []
        for ch in s:
            if ch not in hashmap:
                if not stack:
                    return False
                if hashmap[stack.pop()] != ch:
                    return False
            else:
                stack.append(ch)
        return not stack
        
```



