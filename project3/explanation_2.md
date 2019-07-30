- Analysis
    - utilize binary search to find answer
    - target number should be labelled if it is larger than first number or smaller than the last number. if it's larger than first number and middle number  is smaller than first number, search range is left. if it's smaller than last number and middle number  is larger than last number, search range is right.

- Complexity
    - Time: O(log(n)), the search range decrease to half after one-time comparison 
    - Space: O(n), spaces of length of list are used in each search 