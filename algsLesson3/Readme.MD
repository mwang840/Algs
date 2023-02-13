<h1>Algorithmic explaination</h1>

<p>The solution listed in the answer file takes in a list of integers, creates variable to hold the sum of the values. First we have a check to see if all of the values in the list are negative, they we print out the text EMPTY and return none (negative numbers except -999 are ignored). We loop over the list given adding up the total amount of grades that are zero or greater than the sum and we return the sum on two conditions. Once we loop over all the numbers that are greater than zero on the list or if we encounter a -999 in the list we then return the sum of all grades.</p>

<h1>Algorithmic Runtime</h1>

<p>The time complexity it takes for this algorithm to run will be in O(n) time as it has to walk over the list of integers and check whether each integer is not negative or -999 to find the total sum of the grades in the list.</p>