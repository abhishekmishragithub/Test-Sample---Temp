# Logic

1) Initialize two variables largest and second_largest to min as:
   largest = second_largest = min (or temp value)
2) Start looking into the array,
   a) If the current element in array say arr[i] is greater
      than largest. Then update largest and second_largest as,
      second_largest = largest
      largest = arr[i]
   b) If the current element is in between largest and second_largest,
      then update second_largest to store the value of current variable as
      second_largest = arr[i]
3) Return the second_largest.
