#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:55:13 2017

@author: sergey
"""
import math
import random

def rnd_in(input_val,cnt_exampls):
    file_inp=open("input.txt","w")

    for i in range(cnt_exampls):
        input_val.append([])
        input_val[i].append(1)
        for j in range(3):#Заполнение массива входных значений случайными величинами
            input_val[i].append(random.random())    
        file_inp.write(str(input_val[i])[1:-1]+"\n")      
    file_inp.close()
    return input_val
    
def rnd_out(input_val,cnt_exampls):
    requaried_output=[]
    file_req=open("req.txt","w")        
    for i in range(cnt_exampls):
        requaried_output.append([])
        summ_inp=sum(input_val[i])-1
        for j in range(2):
            if j==0:
                requaried_output[i].append(abs(math.cos(summ_inp)))                
            else:
                requaried_output[i].append(input_val[i][1]/summ_inp)
        file_req.write(str(requaried_output[i])[1:-1]+"\n")
    
    file_req.close()
    return requaried_output     

def rnd_wghts(neurons_coefficients,layers_count,neurons_per_layer):

    for k in range(layers_count):                 #Заполнение массива весовых коэффициентов
        neurons_coefficients.append([])
        for i in range(neurons_per_layer[k]+1):
            neurons_coefficients[k].append([])    
            for j in range(neurons_per_layer[k+1]):
                neurons_coefficients[k][i].append(random.random())
    
    return neurons_coefficients  

def rnd_wghts_2(order,neurons_coefficients,layers_count,neurons_per_layer):
    
    for l in range(1,order):
        neurons_coefficients.append([])
        for k in range(layers_count):                 #Заполнение массива весовых коэффициентов
            neurons_coefficients[l].append([])
            for i in range(neurons_per_layer[k]+1):
                neurons_coefficients[l][k].append([])    
                for j in range(neurons_per_layer[k+1]):
                    neurons_coefficients[l][k][i].append(random.random())
        
    return neurons_coefficients
           
def save_coef(neurons_coefficients,neurons_per_layer):
    layers_count=len(neurons_per_layer)-1
    
    file_weights=open("weights_start.txt","w")
    for k in range(layers_count):                 #Заполнение массива весовых коэффициентов
        file_weights.write("~\n") 
        for i in range(neurons_per_layer[k]+1):
            file_weights.write(str(neurons_coefficients[k][i])[1:-1]+"\n")   
    
    file_weights.close()       
