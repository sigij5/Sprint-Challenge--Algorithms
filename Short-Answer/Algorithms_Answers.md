#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The worst case runtime for this code would be Quadratic O(n^c), depending on how large of an input we use for n.  This would be in the case of increasing the amount of digits in n, and therefore increasing the amount of multiplication operations.


b)  The runtime for this algorithm would be Logarithmic O(n log n) I believe.  The outer loop is executing n times, so it is linear.  We are then performing the inner while loop operation on every element in the outer loop.


c)  This would be Linear O(n).  The function is being called recursively n times before reaching the base case.  n-1 is also O(n).

## Exercise II

find_floor(stories, floor, first_floor, top_floor):
    mid floor = (top_floor + first_floor) // 2
    if the mid floor is f:
        we found f, return it
    else the floor we're looking for is lower(to the left) of mid:
        recursive call of find_floor with top floor set to mid - 1
    else the floor is higher(to the right) of mid:
        recursive call of find_floor with the first floor set to mid + 1
    
    will run until f is found

    Runtime complexity is Logarithmic O(log n) because we are halving the iterations for each pass.




