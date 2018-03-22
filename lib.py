# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:59:38 2017

@author: dsuse
"""
import math

def sigmoid(net):
    return(1/(1+math.exp(-net)))

def sigmoid_derivative(sigm,a):
    return a*sigm*(1-sigm)
    
def layer_out(matr1,matr2):                #Расчёт элементов слоя
    
    matr1_size=len(matr1)
    coloumn_size_2=len(matr2[0])
        
    mult=[]
    mult.append(1.0)
    summ=0
    
    for i in range(coloumn_size_2):
        for j in range(matr1_size):
            summ=summ+matr1[j]*matr2[j][i]
        mult.append(sigmoid(summ))
        summ=0
    return mult         

def l_normalization(data,flag):
    x_min=min(data)
    x_max=max(data)
    
    if flag==0:
        data=[(x-x_min)/(x_max-x_min) for x in data]
    elif flag==-1:
        data=[(2*(x-x_min)/(x_max-x_min))-1 for x in data]
    
    return data
    
def l_denormalization(data,flag):
    y_min=min(data)
    y_max=max(data)
    
    if flag==0:
        data=[y_min+y*(y_max-y_min) for y in data]
    elif flag==-1:
        data=[y_min+((y+1)*(y_max-y_min)/2) for y in data]        
    
    return data    

def n_normalization(data,a,flag):
    x_min=min(data)
    x_max=max(data)
    x_cent=(x_min+x_max)/2
    
    if flag==0:
        data=[1/(math.exp(-a(x-x_cent))+1) for x in data]
    elif flag==-1:
        data=[(math.exp(a(x-x_cent))-1)/(math.exp(a(x-x_cent))+1) for x in data]
        
    return data

def n_denormalization(data,a,flag):
    y_min=min(data)
    y_max=max(data)
    y_cent=(y_min+y_max)/2
    
    if flag==0:
        data=[y_cent-((1/a)*math.log((1/y)-1)) for y in data]
    elif flag==-1:
        data=[y_cent-((1/a)*math.log((1-y)/(1+y))) for y in data]
    
    return data

def new_weights(neurons_coefficients,input_val,layers_elements,discrepancies,neurons_per_layer,layers_count,train_speed):
    for k in range(layers_count):
        for i in range(neurons_per_layer[k]+1):
            for j in range(neurons_per_layer[k+1]):
                if i==0:
                    neurons_coefficients[k][i][j]+=train_speed*discrepancies[k][j]
                elif k==0:
                    neurons_coefficients[k][i][j]+=train_speed*discrepancies[k][j]*input_val[i]
                else :
                    neurons_coefficients[k][i][j]+=train_speed*discrepancies[k][j]*layers_elements[k-1][i-1]
                       
    return neurons_coefficients                

def discr_calc(neurons_coefficients,layers_count,delta,hidden_layers_count,neurons_per_layer,layers_elements,alfa):
    
    output=layers_elements[layers_count-1]
    discrepancies=[]
    
    for i in range(layers_count):
        discrepancies.append([])
    
    for i in range(len(output)):                                        #Расхождения для выходного слоя
        sigm=sigmoid_derivative(output[i],alfa)
        discrepancies[layers_count-1].append((delta[i])*sigm)
    
    temp=0
    summ=0
    
    for i in range(hidden_layers_count-1,-1,-1):
        for j in range(neurons_per_layer[i+1]):
            for k in range(neurons_per_layer[i+2]):
                temp=neurons_coefficients[i+1][j+1][k]*discrepancies[i+1][k]
                summ+=temp
            discrepancies[i].append(summ*sigmoid_derivative(layers_elements[i][j],alfa))
            summ=0    
            
    return discrepancies

def neural_calc(input_val,neurons_coefficients):
    output=input_val                              #Выход каждого слоя  
    layers_count=len(neurons_coefficients)
    layers_elements=[]                            #Массив элементов каждого слоя
    
    for i in range(layers_count):
        output=layer_out(output,neurons_coefficients[i])
        layers_elements.append(output[1:])

    return layers_elements
      
def com_err(deltas,epoch):
    summ=0
    K=len(deltas[0])
    N=len(deltas)
    for i in range(N):
        for j in range(K):
            summ+=deltas[i][j]**2
    err=((1/(N*K))*summ)**(1/2)
    
    f_err=open("erros.txt","a")
    f_err.write("Общая ошибка эпохи " + str(epoch)+" равна: "+str(err))
    f_err.close()
    
    return err

def elem_err(deltas,epoch):
    K=len(deltas[0])
    N=len(deltas)
    summ=0
    el_err=[]
    for i in range(K):
        for j in range(N):
            summ+=(deltas[j][i])**2
        el_err.append(math.sqrt((1/N)*summ))
        summ=0
    
    f_err=open("erros.txt","a")
    
    for i in range(K):
        f_err.write("Ошибка элемента "+str(i+1)+"равна: "+ str(el_err[i])+"\n")
    
    f_err.close()
    return(el_err)    
    
def scan_weights(neural_coef):

    weights=open("weights.txt","r")
    
    i=-1
    for line in weights:
        if line == "~\n":
            neural_coef.append([])
            i+=1
        else:
            string=line.split(",")
            neural_coef[i].append([float(x) for x in string ])
    
    weights.close()
    
    return neural_coef    
   
def scan_inp(input_val):        
            
    file_inp=open("input.txt","r")
    
    for line in file_inp:
        string=line.split(",")
        input_val.append([float(x) for x in string ])
    
    file_inp.close()
    
    return input_val

def scan_rout(requaried_output):           
            
    file_inp=open("req.txt","r")
    
    for line in file_inp:
        string=line.split(",")
        requaried_output.append([float(x) for x in string ])
    
    file_inp.close()
    
    return requaried_output       

def save_coef(neurons_coefficients,neurons_per_layer):
    layers_count=len(neurons_per_layer)-1
    
    file_weights=open("weights.txt","w")
    for k in range(layers_count):                 #Заполнение массива весовых коэффициентов
        file_weights.write("~\n") 
        for i in range(neurons_per_layer[k]+1):
            file_weights.write(str(neurons_coefficients[k][i])[1:-1]+"\n")   
    
    file_weights.close()                     