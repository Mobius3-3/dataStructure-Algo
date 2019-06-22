- my solution
    - use bfs recursion to traverse the path in every hierarchy of folders
    - termination condition is: if the path is file, return a list including path or an empty list

- time complexity
    - o(n) (n is amount of all files and directories under the input path)

- space complexity
    - o(n) (n is the amount of all files whose name containing input suffix)