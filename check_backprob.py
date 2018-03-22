#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:43:30 2017

@author: sergey
"""

import generate
import lib

cnt_exampls=50
input_val=[]
req_out=[]
neurons_coefficients=[]
#input_val=generate.rnd_in(input_val,cnt_exampls)
#req_out=generate.rnd_out(input_val,cnt_exampls) 
input_val=lib.scan_inp(input_val)
req_out=lib.scan_rout(req_out)
neurons_coefficients=lib.scan_weights(neurons_coefficients)

deltas=[]
for i in range(cnt_exampls):
        y_calc=lib.neural_calc(input_val[i],neurons_coefficients)
        y_calc=y_calc[-1]
        deltas.append([req_out[i][x]-y_calc[x] for x in range(2)])

epoch=0
el_er=lib.elem_err(deltas,epoch)
com_er=lib.com_err(deltas,epoch)
print("Обратное распространение:")
for i in range(len(el_er)):
    print("Ошибка элемента "+str(i+1)+"равна: "+ str(el_er[i])+"\n")

print("Общая ошибка эпохи " + str(epoch)+" равна: "+str(com_er)+"\n")