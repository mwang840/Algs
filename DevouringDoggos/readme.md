The algorithm that I've implemented for this assignment satisfies the o (n * m) time complexity.

First this problem is similar to the knapsack problem (I've used the internet and classmates and office hours as a way to get me through this assignment)

The problem then calls two helper functions to find the capacity of the item and finding total_items of the list.

First I made a 2-d table with the rows representing the capacity and the columns representing the items value

Then I looped over the total items and the capacity and the logic follows

If the weight calcualted from the current weight minus the objects item weight is less than zero or it exceeds the total capacity,

add the max of those two at that table[row][col] and the rows previous cell table[row - 1][col]

Otherwise set that position to the **max** of add the value with the previous rows value and the calculated weight, the current position with the current weight and the previous position with the current weight

Once finished, we can find the possible choices of the total items that hit the criteria and satisfy the max capacity

The nested for loops in the algorithm one running over the total items (n) amd another loop running over the capacity (W)

This satisfied pseudo-polynomial time algorithm and fits the time complexity O(nW)
