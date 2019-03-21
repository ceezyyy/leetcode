/*
Source: LeetCode 412. Fizz Buzz 
Author: ceezyyy
Date: 03-21-2019
*/


/*
Easy

Share
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output ¡°Fizz¡± instead of the number and for the multiples of five output ¡°Buzz¡±. 
For numbers which are multiples of both three and five output ¡°FizzBuzz¡±.

Example:
n = 15,
Return:
[
¡°1¡±,
¡°2¡±,
¡°Fizz¡±,
¡°4¡±,
¡°Buzz¡±,
¡°Fizz¡±,
¡°7¡±,
¡°8¡±,
¡°Fizz¡±,
¡°Buzz¡±,
¡°11¡±,
¡°Fizz¡±,
¡°13¡±,
¡°14¡±,
¡°FizzBuzz¡±
]

*/


#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
	vector<string> fizzBuzz(int n) {
		vector<string> res;
		for (int i = 1; i <= n; i++) {
			if (i % 3 == 0 && i % 5 == 0) {
				res.push_back("FizzBuzz");
			}
			else if (i % 3 == 0) {
				res.push_back("Fizz");
			}
			else if (i % 5 == 0) {
				res.push_back("Buzz");
			}
			else {
				res.push_back(to_string(i));
			}
		}
		return res;
	}
};


/*
Submission Detail:

Runtime: 8 ms, faster than 100.00% of C++ online submissions for Fizz Buzz.
Memory Usage: 10.4 MB, less than 54.97% of C++ online submissions for Fizz Buzz.

*/


/*
Study Notes:

std::to_string

string to_string (int val);
string to_string (long val);
string to_string (long long val);
string to_string (unsigned val);
string to_string (unsigned long val);
string to_string (unsigned long long val);
string to_string (float val);
string to_string (double val);
string to_string (long double val);

Convert numerical value to string
Returns a string with the representation of val.

*/
