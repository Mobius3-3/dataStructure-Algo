- my solution
    - use binary tree to generate huffman encoding tree and every loop requires sort the node not concatenated
    - traverse huffman encoding tree to generate encoded data
    - loop over encoded data and check decode dictionary to generate decoded data

- time complexity
    - o(n^2*log(n)) (sort node for n-1 times) for encoding
    - o(n) for decoding

- space complexity
    - o(n) for generate dictionaries/binary tree
