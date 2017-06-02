import numpy as np
import matplotlib.pyplot as plt
########################################
inp=400
l=300
o=10
tr=50000
learnspeed=0.1
reg=0.001
#######################################
w1=np.random.randn(inp,l)
layer=np.zeros(tr,l)
w2=np.random.randn(l,o)
out=np.zeros(tr,o)
b1=np.zeros(1,l)
b2=np.zeros(1,o)
########################################
def act(n):
    n1=np.exp(2*n)
    return(n1-1)/(n1+1)
def dact(n):
    return 4/(np.exp(-n)+np.exp(n))**2
def forward(self,i):
    layer=np.dot(inp,w1)
    self.lays=act(layer)
    self.out=np.dot(lays,w2)
    self.outs=act(out)
def loss(y):
    return 0.5*np.sum((y-outs)**2)
def back(i):
    delta2=(outs-y)*dact(out)
    delta1=np.dot(delta2,w2.T)*dact(layer)
    deltaw2=np.dot(lays.T,delta2)
    deltaw1=np.dot(i.T,delta1)
    deltab2=np.sum(delta2)
    deltab1=np.delta2.sum(axis=0)
    w1=w1-learnspeed*deltaw1
    w2=w2-learnspeed*deltaw2
    b1=b1-learnspeed*deltab1
    b2=b2-learnspeed*deltab2

def execute(i):
    n=0
    while n<i:
        forward(pichere)
        loss()
        back(pichere)
        if n%100==1:
            print loss()
        n+=1




