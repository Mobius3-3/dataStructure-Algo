- my solution
    - use a hashmap(dictionary) to store data, use key to get data value
    - use a deque to store key of hashmap, use FIFO/LILO rules to manage the capacity of cache

- time complexity
    - o(1) for get/set operation

- space complexity
    - o(n) (n is capacity) for create hashmap and queue