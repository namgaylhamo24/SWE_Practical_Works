## Practical 2: Text File Analyzer
**Excercise Question:**
* Modify the program to count the number of unique words in the text.
Add a function to find the longest word in the text.
Implement a feature to count the occurrences of a specific word (case-insensitive).
Create a function to calculate the percentage of words that are longer than the average word length.

## Practical 3:  Implementing Recursive and Iterative Fibonacci sequence generators
**Excercise Question:**
* Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.
Implement a function that finds the index of the first Fibonacci number that exceeds a given value.
Create a function that determines if a given number is a Fibonacci number.
Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.

**Discussion Questions:**
## What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
* ANSWER 
# Recursion vs. Iteration

| **Aspect**                | **Recursion**                                                                               | **Iteration**                                                   |
|---------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| **Code Readability**      | Often shorter and more readable, especially for naturally recursive problems                 | Generally requires more lines of code for recursive-type problems|
| **Memory Usage**          | Higher, as each call uses stack memory                                                       | Lower, as it doesn’t use extra stack space                       |
| **Execution Speed**       | Can be slower due to overhead of function calls                                              | Usually faster due to simple loop structures                     |
| **Risk of Errors**        | Risk of stack overflow if too many recursive calls                                           | No stack overflow risk                                           |
| **Best Use Cases**        | Ideal for divide-and-conquer problems and tree/graph traversal                               | Ideal for simple, repetitive tasks with a fixed number of steps  |




## How does memoization improve the performance of the recursive function? Are there any drawbacks?
### Memoization in Recursive Functions

Memoization is a method to make recursive functions faster. It saves the results of expensive calculations so that when the same inputs are used later, the stored result can be reused instead of recalculated. This is helpful in problems where the same calculations happen multiple times, like finding Fibonacci numbers or solving other complex problems. It speeds things up a lot!
#### Benefits of Using Memoization
- **Cuts Down on Repeated Calculations**: When a result is computed, it gets stored, so the function can use that stored value instead of calculating it again.
- **Speeds Up Processing Time**: It can significantly improve the time complexity of certain algorithms, turning them from slow exponential time into much quicker polynomial time for larger inputs.
- **Great for Dynamic Programming**: Memoization shines in recursive dynamic programming scenarios, where a lot of the same subproblems appear again and again.

#### Drawbacks of Memoization
- **Can Use More Memory**: Since memoization stores results, it can take up more memory, particularly if the function deals with many unique inputs.
- **Not Always Necessary**: If there aren’t overlapping subproblems, memoization won’t help much and might even slow things down because of the extra overhead.
- **Can Make Code Trickier**: While memoization is helpful, it can also complicate the code, making it harder to read and maintain.

## In what scenarios might you prefer to use a generator function over other implementations?
## ANSWER: 
## Memoization in Recursive Functions
### How Memoization Improves Performance
Memoization is a technique that can drastically enhance the efficiency of recursive functions by storing computed results. This way, if a function is called multiple times with the same inputs, it can return the stored result instead of recalculating it.

## When to Use Generator Functions

### Scenarios for Preferring Generator Functions

1. **Handling Large Data Sets**:  
   If you're dealing with large amounts of data or streams, generator functions are a great option. They produce one item at a time rather than loading everything into memory, which keeps memory usage low.

2. **Lazy Evaluation**:  
   Generators compute values as needed, making them perfect for tasks like reading large files or generating sequences where you only need the next item when you're ready for it.

3. **Infinite Sequences**:  
   Generators shine when it comes to infinite sequences, like Fibonacci or prime numbers. Since they don’t need to store all values, they only maintain the current state, which is much more efficient.

4. **Pipeline Processing**:  
   In scenarios where data goes through several processing steps—filtering, transforming, and aggregating—generators make it easy to chain these operations together without needing extra space for intermediate results.

### Benefits of Generators
- **Memory Efficient**: They produce data only when it's needed, preventing heavy memory usage.
- **Improves Performance**: By yielding results on demand, they help to avoid the overhead of calculating and storing large sets of results at once.
- **Simplified Code**: Using the `yield` statement can make your code more straightforward and easier to read compared to complex iterator logic.

### When Not to Use Generators
- **Random Access Needed**: If you need to access elements by index or wish to use values multiple times, generators won't work since once you consume a value, you can't go back to it.
- **One-Time Use**: Generators can be looped over only once. If you want to access the items again, you'll have to create a new generator.
## How does the space complexity differ between these implementations?
## Answer:
## Understanding Space Complexity in Different Ways
### 1. **Iterative Approach**
   - **Space Complexity**: O(1)
    When you tackle a problem iteratively, you’re mostly reusing the same memory space for each loop iteration. You only need a few variables (like counters), keeping your memory usage super efficient.
   - **Usage**: This approach shines when you want to save on memory and the task can be solved with loops, like when you’re going through arrays or performing basic calculations.

### 2. **Recursive Approach (without Memoization)**
   - **Space Complexity**: O(n)
   - With recursion, each time you call the function, a new frame gets added to the call stack. If you have `n` calls, you’ll use `n` frames, which means a linear amount of memory. This can lead to issues like stack overflow if your inputs are too large.
   - **Usage**: This is great for problems that naturally fit a recursive structure, but be cautious with big inputs since it can get memory-hungry quickly.

### 3. **Recursive Approach (with Memoization)**
   - **Space Complexity**: O(n)
   - Here, memoization helps by storing results of previous computations, which speeds things up. However, it also requires extra memory for these stored results. You’ll still have the memory for the call stack plus whatever’s saved in your memoization table, leading to O(n) complexity.
   - **Usage**: This is perfect for problems where you have overlapping subproblems (like in dynamic programming) and you’re willing to trade some memory usage for better performance.

### 4. **Generator Function**
   - **Space Complexity**: O(1)
   - Generators are pretty neat since they produce values one at a time, rather than holding everything in memory. They only keep track of the current value and their internal state, which makes them memory-efficient.
   - **Usage**: This approach is ideal for working with large datasets or data streams where you want to keep memory usage low and don’t need to store all results at once.
