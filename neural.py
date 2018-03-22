3# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 20:07:32 2017

@author: dsuse
"""
import lib
import generate

input_neurons_count = int(input("Введите число входных нейронов: "))
hidden_layers_count = int(input("Введите число скрытых слоёв: "))

neurons_per_layer =[]                        #Количество нейронов в каждом слое
input_val=[]                                 #Массив входных значений 
requaried_output=[]                             
train_speed=1                            #Начальная скорость обучения
alfa=1.0                                   #Параметр сигмойдно-логистической ф-ции
cnt_exampls=50

neurons_per_layer.append(input_neurons_count)

input_val=generate.rnd_in(input_val,cnt_exampls)

requaried_output=generate.rnd_out(input_val,cnt_exampls)      
        
for i in range(hidden_layers_count):
    neuron=int(input("Введите число нейронов для слоя "+str(i+1)+" : "))
    neurons_per_layer.append(neuron)    
    
output_neurons=int(input("Введите число выходных нейронов: "))
neurons_per_layer.append(output_neurons) 
   
layers_count=hidden_layers_count+1            #Количество слоёв не считая входной слой

neurons_coefficients=[]                       #Трёхмерный массив для весовых коэффициентов каждого слоя

neurons_coefficients=generate.rnd_wghts(neurons_coefficients,layers_count,neurons_per_layer)
generate.save_coef(neurons_coefficients,neurons_per_layer)
lib.save_coef(neurons_coefficients,neurons_per_layer)

deltas=[]
discrepancies=[]                            #Массив расхождений
epoch=1
fin=1
while True:
    
    for i in range(cnt_exampls):
    #----------------------------------------------------------------------------------------------------
    #Расчёт сети
        layers_elements=lib.neural_calc(input_val[i],neurons_coefficients)
    
        deltas.append([requaried_output[i][x]-layers_elements[layers_count-1][x] for x in range(output_neurons)])
    #----------------------------------------------------------------------------------------------------
    #Вычисление расхождений для элементов выходного слоя
        discrepancies=lib.discr_calc(neurons_coefficients,layers_count,deltas[i],hidden_layers_count,neurons_per_layer,layers_elements,alfa)       
    #---------------------------------------------------------------------------------------------------
    #Корректировка весовых коэффициентов
        neurons_coefficients=lib.new_weights(neurons_coefficients,input_val[i],layers_elements,discrepancies,neurons_per_layer,layers_count,train_speed)
    #---------------------------------------------------------------------------------------------------
    el_er=lib.elem_err(deltas,epoch)
    com_er=lib.com_err(deltas,epoch)
#    lib.save_coef(neurons_coefficients,neurons_per_layer)
    deltas=[]
    for i in range(len(el_er)):
        print("Ошибка элемента "+str(i+1)+"равна: "+ str(el_er[i])+"\n")
    
    print("Общая ошибка эпохи " + str(epoch)+" равна: "+str(com_er)+"\n")
    print("~"*100)
    epoch+=1
    fin-=1
#    train_speed/=2
    if fin==0:
        fin=int(input("Сколько эпох повторить ?: "))
        if fin==0:
            break
    
    lib.save_coef(neurons_coefficients,neurons_per_layer)
    
    
        
""" 
    print("\nВходные Данные:")
    print(input_val[1:])
    print("-"*100)
    print("Коэффициенты:")
    i=1
    for x in neurons_coefficients:
        print("Слой "+ str(i))
        for y in x:
            print(y)
        print("\nВыход слоя "+str(i)+":",layers_elements[i-1])    
        print("~"*100)
        i+=1
    print("Выходной слой:")    
    print(layers_elements[layers_count-1],"\n")  
"""    


