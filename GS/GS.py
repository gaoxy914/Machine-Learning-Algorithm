# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:16:09 2018

@author: gaoxy
"""

import pandas as pd
import numpy as np

def load_data(filepath):
    data = pd.read_csv(filepath)
    header = np.array(data.columns[:-1])
    attributes = {}
    for index in range(len(header)):
        attributes[header[index]] = index
    target_attr = {data.columns[-1] : len(data.columns) - 1}
    data = np.array(data)
    #print('data: ', data)
    #print('attributes: ', attributes)
    #print('target_attr: ', target_attr)
    return data.tolist(), attributes, target_attr

def data_partioning(data, target_attr, positive_attr, negative_attr):
    positive_example = []
    negative_example = []
    index = next(iter(target_attr.values()))
    for row in data:
        if row[index] == positive_attr:
            positive_example.append(row[:index])
        else:
            negative_example.append(row[:index])
    #print('positive: ', positive_example)
    #print('negative: ', negative_example)
    return positive_example, negative_example

def count(attribute_index, positive_example, negative_example):
    p_count = {}
    n_count = {}
    for row in positive_example:
        value = row[attribute_index]
        n_count[value] = 0
        if value in p_count:
            p_count[value] = p_count[value] + 1
        else:
            p_count[value] = 1
    for row in negative_example:
        value = row[attribute_index]
        if value in n_count:
            n_count[value] = n_count[value] + 1
        else:
            n_count[value] = 1
    maximum = 0
    ne_number = 0
    value = None
    for key in p_count.keys():
        if p_count[key] > maximum:
            value = key
            maximum = p_count[key]
            ne_number = n_count[key]
        elif p_count[key] == maximum:
            if n_count[key] < ne_number:
                value = key
                ne_number = n_count[key]
    return value, maximum, ne_number
    
    
def GS(attribute, target_attr, positive_example, negative_example):
    formula = []
    while len(positive_example) != 0:
        pe = positive_example
        ne = negative_example
        cpx = {}
        record = []
        while len(ne) != 0:
            max_overlap_attribute = None
            max_overlap_value = None
            max_overlap_p_count = 0
            max_overlap_n_count = 0
            for attr in attribute.keys():
                if attr not in record:
                    value, p_count, n_count = count(attribute[attr], pe, ne)
                    if p_count > max_overlap_p_count:
                        max_overlap_attribute = attr
                        max_overlap_value = value
                        max_overlap_p_count = p_count
                        max_overlap_n_count = n_count
                    elif p_count == max_overlap_p_count:
                        if n_count < max_overlap_n_count:
                            max_overlap_attribute = attr
                            max_overlap_value = value
                            max_overlap_p_count = p_count
                            max_overlap_n_count = n_count
            record.append(max_overlap_attribute)
            cpx[max_overlap_attribute] = max_overlap_value
            index = attribute[max_overlap_attribute]
            pe = [row for row in pe if row[index] == max_overlap_value]
            ne = [row for row in ne if row[index] == max_overlap_value]
            #print('cpx: ', cpx)
            #print('pe: ', pe)
            #print('ne: ', ne)
        for row in pe:
            positive_example.remove(row)
        #print('positive_example: ', positive_example)
        formula.append(cpx)
        #print('formula: ', formula)
    return formula
    
            
    
if __name__ == '__main__':
    data, attribute, target_attr = load_data('case.csv')
    positive_attr = 'Pneumonia'
    negative_attr = 'Pulmonary tuberculosis'
    positive_example, negative_example = data_partioning(data, target_attr, positive_attr, negative_attr)
    formula = GS(attribute, target_attr, positive_example, negative_example)
    print('formula: ', formula)
    
    