# Machine-Learning-Algorithm
Algorithms in Machine Learning Course

**ID3**
Input: Dataset
Output: Decision Tree
Algorithm: Starting from the root node of a tree the nodes are split with the 'best attribute' each time until all nodes contain one class of data.
The 'best attribute' means that the attribute with the highest information gain. The information gain is calculated as follow:
$$Gain(A) = I(p, n) - E(A)$$
$$I(p, n) = -$\frac{p}{p + n}$$
