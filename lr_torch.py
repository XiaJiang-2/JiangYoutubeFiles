
'''
A script that demonstrates how we can use gradient descent to optimize
the parameters of a linear regression model.
author: Xia Jiang
date:2021.1.8
#! /usr/bin/env python
'''
import torch.nn as nn
import torch
x = torch.tensor([1,2,3,4,4,5,6,6,7,8])
y= torch.tensor ([2,3,4,3,4,6,5,7,8,8])
x=x.float()
x =x.reshape(-1,1)
y=y.float()
y=y.reshape(-1,1)
torch.manual_seed(5)
model = nn.Linear(1,1)
def getparas (model):
    [w1, w0] =model.parameters()
    return (w1,w0)
crit = torch.nn.MSELoss()
optm= torch.optim.SGD(model.parameters(),lr=0.01)
num_epochs= 3000
def model_run(epochs):
    for i in range(epochs):
        optm.zero_grad()
        pred_y_values = model(x)
        cur_loss =crit(pred_y_values, y)
        print('epoch: {}, loss: {}'.format(i, cur_loss.item()))
        cur_loss.backward()
        optm.step()
model_run(num_epochs)
print(getparas(model))



