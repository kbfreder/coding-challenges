#### Recursion

Functional that calls itself

#### Pros & Cons

- Cons: requires a lot of overhead (multiple function calls)
  - Iterative solutions / dynamic programming usually more efficient (because it doesn't involve any additional function calls)
- Pros: for some problems, recursion is more simple & elegant

Can be used for

- "divide & conquer" type problems (e.g. binary search)



**Tail-recursive** = when the value returned by the recursive call is itself immediately returned

> Ref & example: https://stackoverflow.com/questions/33923/what-is-tail-recursion
>
> In **traditional recursion**, the typical model is that you perform your recursive calls first, and then you take the return value of the recursive call and calculate the result. In this manner, you don't get the result of your calculation until you have returned from every recursive call.
>
> In **tail recursion**, you perform your calculations first, and then you execute the recursive call, passing the results of your current step to the next recursive step. This results in the last statement being in the form of `(return (recursive-function params))`. **Basically, the return value of any given recursive step is the same as the return value of the next recursive call**.





Example problems:

- Fibonacci sequence
- Tower of Hanoi
- Knapsack problem
- Binary Search
- Merge Sort





Refs:

https://www.datacamp.com/community/tutorials/understanding-recursive-functions-python

http://ranger.uta.edu/~kosmopo/cse2320/lectures/05-Recursion_DynamicProgramming.pdf