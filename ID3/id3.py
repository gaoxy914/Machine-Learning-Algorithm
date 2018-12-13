# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:39:19 2018

@author: gaoxy
"""

import math

"""
attr: split attibute
label: inner and target attribute
children: value->Node
"""
class Node:
    def __init__(self, attr, label, children):
        self.attr = attr
        self.label = label
        self.children = children
    
def get_lables(data, target_attr):
    labels = {}
    for row in data:
        label = row[target_attr]
        if label in labels:
            labels[label] = labels[label] + 1
        else:
            labels[l] = 1
    return labels

def entropy(data, target_attr):
    labels = get_lables(data, target_attr)
    entropy = 0.0
    for freq in labels.values():
        entropy = entropy + (-freq / len(data)) * math.log(freq / len(data))
    return entropy

def gain(data, split_attr, target_attr):
    split_attr_values = {}
    for row in data:
        value = row[split_attr]
        if value in split_attr_values:
            split_attr_values[value] = split_attr_values[value] + 1
        else:
            split_attr_values[value] = 1
    sub_data_entropy = 0.0
    n = sum(split_attr_values.values())
    for value in split_attr_values.keys():
        sub_data = [row for row in data if row[split_attr] == value]
        sub_data_entropy = sub_data_entropy + (split_attr_values[value] / n) * entropy(sub_data, target_attr)
    return (entropy(data, target_attr) - sub_entropy)
    
def id3(data, remaining_attrs, target_attr):
    label = get_labels(data, target_attr)
    if len(label) == 1:
        
    if len(label) == 0:
        
    
