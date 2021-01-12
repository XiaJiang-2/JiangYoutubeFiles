#!/usr/bin/env python
# coding: utf-8
# %load "~/lr_torch.py"

'''
A script solely for the purpose of demonstrating how we can use gradient 
descent to optimize the parameters of a linear regression model. No error-handling
was considered when writing the script.
author: Xia Jiang
date:2021.1.8
#! /usr/bin/env python
'''
import torch.nn as nn
import torch

def getparas (model):
    [w1, w0] =model.parameters()
    return (w1,w0)
def model_run(epochs, lr, x, y, seed):
    torch.manual_seed(seed)
    model = nn.Linear(1,1)
    crit = torch.nn.MSELoss()
    optm= torch.optim.SGD(model.parameters(),lr=lr)
    for i in range(epochs):
        optm.zero_grad()
        pred_y_values = model(x)
        cur_loss =crit(pred_y_values, y)
        print('epoch: {}, loss: {}'.format(i, cur_loss.item()))
        cur_loss.backward()
        optm.step()
    return model
#example for usering model_run to train and return a linear model
x = torch.tensor([1,2,3,4,4,5,6,6,7,8])
y= torch.tensor ([2,3,4,3,4,6,5,7,8,8])
x=x.float()
x =x.reshape(-1,1)
y=y.float()
y=y.reshape(-1,1)
num_epochs=1000
lr=0.01
seed = 5
if __name__=="__main__":
    model=model_run(num_epochs, lr, x, y, seed)
    print(getparas(model))
