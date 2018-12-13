# Machine-Learning-Algorithm
Algorithms in Machine Learning Course

**ID3**

Input: Dataset

Output: Decision Tree

Algorithm: Starting from the root node of a tree the nodes are split with the 'best attribute' each time until all nodes contain one class of data.

The 'best attribute' means that the attribute with the highest information gain. The information gain is calculated as follow:

<a href="https://www.codecogs.com/eqnedit.php?latex=Gain(A)&space;=&space;I(p,&space;n)&space;-&space;E(A)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Gain(A)&space;=&space;I(p,&space;n)&space;-&space;E(A)" title="Gain(A) = I(p, n) - E(A)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=I(p,n)=-\frac{p}{p&plus;n}\log_2{\frac{p}{p&plus;n}}-\frac{n}{p&plus;n}\log_2{\frac{n}{p&plus;n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I(p,n)=-\frac{p}{p&plus;n}\log_2{\frac{p}{p&plus;n}}-\frac{n}{p&plus;n}\log_2{\frac{n}{p&plus;n}}" title="I(p,n)=-\frac{p}{p+n}\log_2{\frac{p}{p+n}}-\frac{n}{p+n}\log_2{\frac{n}{p+n}}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=E(A)=\sum_{i=1}^{v}\frac{p_i&plus;n_i}{p&plus;n}I(p_i,n_i)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E(A)=\sum_{i=1}^{v}\frac{p_i&plus;n_i}{p&plus;n}I(p_i,n_i)" title="E(A)=\sum_{i=1}^{v}\frac{p_i+n_i}{p+n}I(p_i,n_i)" /></a>

Note: <a href="https://www.codecogs.com/eqnedit.php?latex=p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p" title="p" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a> are the number of positive and negative data of node. A is the attribute which the node is splite with now. <a href="https://www.codecogs.com/eqnedit.php?latex=p_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_i" title="p_i" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=n_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n_i" title="n_i" /></a> means the number of positive and negative data of the node after splition.
