# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:55:38 2018

@author: gaoxy
"""

import math
import pickle
import numpy as np

def sigmoid(x):
    #return 1.0 / (1.0 + math.exp(-x))
    return math.tanh(x)
    
# y = sigmoid(x)
def dsigmoid(y):
    #return y * (1.0 - y)
    return 1.0 - y**2

class BPNN:
    def __init__(self, ni, nh, no):
        self.ni = ni + 1
        self.nh = nh
        self.no = no
        # wji means the weight from unit i to unit j
        self.i_h_weights = (np.random.random_sample((self.nh, self.ni))- 0.5) * 0.4
        self.h_o_weights = (np.random.random_sample((self.no, self.nh)) - 0.5) * 4.0
        # initiate input layer, hidden layer and output layer
        #self.inputs is initiated in forward_cal
        self.hidden_ouputs = np.zeros(self.nh)
        self.outputs = np.zeros(self.no)
        # record last changes for momentum
        self.i_h_changes = np.zeros((self.nh, self.ni))
        self.h_o_changes = np.zeros((self.no, self.nh))
    
    def forward_cal(self, inputs):
        if len(inputs) != self.ni - 1:
            raise ValueError('wrong number of inputs')
        self.inputs = inputs + [1.0]        
        for k in range(self.nh):
            # h[k] = sigma_i(input[i] * wki)
            self.hidden_ouputs[k] = sigmoid(sum([i * j for i, j in zip(self.inputs, self.i_h_weights[k])]))        
        for k in range(self.no):
            # o[k] = sigma_i(h[i] * wki)
            self.outputs[k] = sigmoid(sum([i * j for i, j in zip(self.hidden_ouputs, self.h_o_weights[k])]))
        #print('i_h_weights: ', self.i_h_weights)
        #print('h_o_weights: ', self.h_o_weights)
        #print('hidden_outputs: ', self.hidden_ouputs)
        #print('outputs: ', self.outputs)
        return self.outputs
    
    def backpropagation(self, targets, learning_rate, momentum):
        if len(targets) != self.no:
            raise ValueError('wrong number of targets')
        # output_delta[k] = o[k](1-o[k])(t[k]-o[k])
        output_delta = [dsigmoid(o) * (t - o) for o, t in zip(self.outputs, targets)]
        #print('output_delta: ', output_delta)
        error = np.zeros(self.nh)
        for k in range(self.nh):
            # error[k] = sigma_i(wik*output_delta[i])
            error[k] = sum([i * j for i, j in zip(self.h_o_weights[:, k], output_delta)])
        hidden_delta = [dsigmoid(o) * e for o, e in zip(self.hidden_ouputs, error)]
        # update h_o_weights
        for j in range(self.no):
            for i in range(self.nh):
                delta = output_delta[j] * self.hidden_ouputs[i]
                self.h_o_weights[j][i] = self.h_o_weights[j][i] + learning_rate * delta + momentum * self.h_o_changes[j][i]
                self.h_o_changes[j][i] = delta
        # update i_h_weights
        for j in range(self.nh):
            for i in range(self.ni):
                delta = hidden_delta[j] * self.inputs[i]
                self.i_h_weights[j][i] = self.i_h_weights[j][i] + learning_rate * delta + momentum *self.i_h_changes[j][i]
                self.i_h_changes[j][i] = delta
        return sum([0.5 * (t - o)**2 for t, o in zip(targets, self.outputs)])
    
    def train(self, data, targets, iterations = 1000, learning_rate = 0.5, momentum = 0.1):
        for i in range(iterations):
            error = 0.0
            for x, y in zip(data, targets):
                #print('x:', x, ' y: ', y)
                self.forward_cal(x)
                error = error + self.backpropagation(y, learning_rate, momentum)
            if i % 100 == 0:
                print('error %-.10f' % error)
    
    def test(self, data, targets):
        for x, y in zip(data, targets):
            pred = self.forward_cal(x)[0]
            print(y, '->', pred)
    
    def save_weights(self, path):
        weights = {
                "h_o_weights" : self.h_o_weights,
                "i_h_weights" : self.i_h_weights
                }
        with open(path, "wb") as f:
            pickle.dump(weights, f)
            
    def load_weights(self, path):
        with open(path, "rb") as f:
            weights = pickle.load(f)
            self.h_o_weights = weights["h_o_weights"]
            self.i_h_weights = weights["i_h_weights"]
    
def demo():
    # Teach network XOR function
    X = [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]
    Y = [[0], [1], [1], [0]]
    # create a network with two input, two hidden, and one output nodes
    n = BPNN(2, 2, 1)
    # train it with some patterns
    n.train(X, Y)
    # test it
    n.test(X, Y)


if __name__=='__main__':
    demo()
           
        
        
        
        
        