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

**BPNN**

Initialize all weights to small random numbers.
Until satisfied, Do
* For each training example. Do
   1. Input the traiining exmaple to the network and compute the network outputs
   2. For each output unit k
   
      <a href="https://www.codecogs.com/eqnedit.php?latex=\delta_k\gets&space;o_k(1-o_k)(t_k-o_k)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\delta_k\gets&space;o_k(1-o_k)(t_k-o_k)" title="\delta_k\gets o_k(1-o_k)(t_k-o_k)" /></a>
   
   3. For each hidden unit h
   
      <a href="https://www.codecogs.com/eqnedit.php?latex=\delta_h\gets&space;o_h(1-o_h)\sum_{k\in&space;outputs}\omega_{h,k}\delta_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\delta_h\gets&space;o_h(1-o_h)\sum_{k\in&space;outputs}\omega_{h,k}\delta_k" title="\delta_h\gets o_h(1-o_h)\sum_{k\in outputs}\omega_{h,k}\delta_k" /></a>
   
   4. Update each network weigh 
   
      <a href="https://www.codecogs.com/eqnedit.php?latex=\omega_{i,j}&space;\gets&space;\omega_{i,j}&space;&plus;&space;\Delta&space;\omega_{i,j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\omega_{i,j}&space;\gets&space;\omega_{i,j}&space;&plus;&space;\Delta&space;\omega_{i,j}" title="\omega_{i,j} \gets \omega_{i,j} + \Delta \omega_{i,j}" /></a>
      
      where <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;\omega_{i,j}&space;=&space;\eta&space;\delta_j&space;x_{i,j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;\omega_{i,j}&space;=&space;\eta&space;\delta_j&space;x_{i,j}" title="\Delta \omega_{i,j} = \eta \delta_j x_{i,j}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\eta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\eta" title="\eta" /></a> means learning rate.

Often include weight <a href="https://www.codecogs.com/eqnedit.php?latex=momentum\&space;\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?momentum\&space;\alpha" title="momentum\ \alpha" /></a>

   <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;\omega_{i,j}(n)&space;=&space;\eta&space;\delta_j&space;x_{i,j}&space;&plus;&space;\alpha&space;\Delta&space;\omega_{i,j}(n-1)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;\omega_{i,j}(n)&space;=&space;\eta&space;\delta_j&space;x_{i,j}&space;&plus;&space;\alpha&space;\Delta&space;\omega_{i,j}(n-1)" title="\Delta \omega_{i,j}(n) = \eta \delta_j x_{i,j} + \alpha \Delta \omega_{i,j}(n-1)" /></a>
