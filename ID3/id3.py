# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 08:39:19 2018

@author: gaoxy
"""
import pandas as pd
import numpy as np
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
    
def get_labels(data, target_attr):
    labels = {}
    for row in data:
        label = row[target_attr]
        if label in labels:
            labels[label] = labels[label] + 1
        else:
            labels[label] = 1
    return labels

def entropy(data, target_attr):
    labels = get_labels(data, target_attr)
    entropy = 0.0
    for freq in labels.values():
        entropy = entropy + (-freq / len(data)) * math.log(freq / len(data), 2)
    return entropy

def gain(data, split_attr, target_attr):
    split_attr_values = {}
    sub_dataset = {}
    for row in data:
        value = row[split_attr]
        if value in split_attr_values:
            split_attr_values[value] = split_attr_values[value] + 1
        else:
            split_attr_values[value] = 1
    sub_data_entropy = 0.0
    n = sum(split_attr_values.values())
    for value in split_attr_values.keys():
        #print(value)
        sub_data = [row for row in data if row[split_attr] == value]
        sub_dataset[value] = sub_data
        sub_data_entropy = sub_data_entropy + (split_attr_values[value] / n) * entropy(sub_data, target_attr)
    return (entropy(data, target_attr) - sub_data_entropy), sub_dataset

def most_common_label(labels):
    mcl = max(labels, key = lambda k : labels[k])
    return mcl

def id3(data, remaining_attrs, target_attr):
    labels = get_labels(data, next(iter(target_attr.values())))
    if len(labels.keys()) == 1:
        node = Node(remaining_attrs, next(iter(labels.keys())), {})
        #print(node.label)
        return node
    if len(remaining_attrs) == 0:
        node = Node(remaining_attrs, most_common_label(labels), {})
        return node
    max_info_gain = 0
    max_info_gain_attr = None
    max_info_gain_sub_dataset = None
    for attr in remaining_attrs.keys():
        info_gain, sub_dataset = gain(data, remaining_attrs[attr], next(iter(target_attr.values())))
        if info_gain > max_info_gain:
            max_info_gain = info_gain
            max_info_gain_attr = attr
            max_info_gain_sub_dataset = sub_dataset
    del remaining_attrs[max_info_gain_attr]
    #print(max_info_gain_attr)
    #print()
    node = Node(max_info_gain_attr, 'inner', {})
    #print(max_info_gain_sub_dataset.keys())
    #print()
    for key in max_info_gain_sub_dataset.keys():
        #print(key)
        #print(len(max_info_gain_sub_dataset))
        node.children[key] = id3(max_info_gain_sub_dataset[key], remaining_attrs, target_attr)
    #print()
    return node

def load_data(filepath):
    data = pd.read_csv(filepath)
    header = np.array(data.columns[:-1])
    attributes = {}
    for index in range(len(header)):
        attributes[header[index]] = index
    target_attr = {data.columns[-1] : len(data.columns) - 1}
    data = np.array(data)
    return data, attributes, target_attr

def traverse(node):
    if node.label == 'inner':
        print(node.attr)
        print(len(node.children))
        for key in node.children.keys():
            print(key)
            traverse(node.children[key])
    else:
        print(' = ' + node.label)
        
           
if __name__ == '__main__':
    data, attributes, target_attr = load_data('tennis.csv')
    #print(attributes)
    #print(target_attr)
    root = id3(data, attributes, target_attr)
    traverse(root)
    
