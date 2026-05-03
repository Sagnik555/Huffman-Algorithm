Code for finding the most optimal codewords given their probabilities using huffman algorithm.

No libraries were used.

In each iteration, the smallest probability was removed, then the 2nd smallest probability was removed and indexed were noted in that manner and at the 2nd end smallest probability code was added first, then smallest probability code was added. Similarly, by always appending the merged probability to the end of the list, I ensured the recursive call always knows exactly where the "new" node is. The complexity is O(N^2); it can be improved by using a Min-Priority Queue (heap).
