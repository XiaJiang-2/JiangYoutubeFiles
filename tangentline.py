#!/usr/bin/env python
# coding: utf-8

# In[38]:


import matplotlib.pyplot as myplot
import numpy as np
#gradient function below is used to compute the gradient or slope that is passing a point (x, y) on
#the curve of a function f(x). Author:Xia Jiang. Inital draft date: Jan 2, 2021
def gradient(x,y,f,delta_l):
    #Since gradient is defined as a result when delta_l approches 0, we'd like to assign a very small
    #value to delta_l
    if delta_l is None:
        delta_l = 0.000000001
    else:
        delta_h = f(x+delta_l)-y
        grad=delta_h/delta_l
    return grad
def compute_y_on_slope(grad, x1,y1,x2):
    return grad*(x2-x1)+y1
# the draw_slope function below will draw the curve of function f based on an numpy array of given input values
# xvalues_curve, and the tangent line of the curve passing a point (x1, y1) on the curve. The length of the
# tangent line is determined based the input numpy array xvalues_slope. curve_string defines the color and shape 
#of the curve that represents function f. For example, if curve_string = 'm-', the curve would be solid purple line,
#and 'm-' is also the default value to curve_string. #Similarly, slope_string defines the color and shape of the slope 
#that passes the point (x1, y1) on the curve.The default value to slope_string is 'g--'
def draw_slope(x1, y1, dot_string, xvalues_curve, curve_string, xvalues_slope,slope_string, f):
    grad= gradient(x1,y1,f, 0.000000001)
    yvalues_curve = f(xvalues_curve)
    dot_string_used = 'go'
    curve_string_used = 'm-'
    slope_string_used = 'g--'
   
    if dot_string is not None:
        dot_string_used = dot_string
    if curve_string is not None:
        curve_string_used = curve_string
    if slope_string is not None:
        slope_string_used = slope_string
    
    myplot.plot(xvalues_curve,yvalues_curve, curve_string_used, lw=2)
    myplot.plot(x1,y1,dot_string_used,lw=3)
    yvalues_slope = compute_y_on_slope(grad, x1,y1, xvalues_slope)
    myplot.plot(xvalues_slope,yvalues_slope, slope_string_used,lw=3)
    myplot.show()
    return myplot
#An example for calling draw_slope
if __name__=="__main__":
    import time
    fig = myplot.figure()
    ax = myplot.axes(xlim=(-10, 15), ylim=(0, 600))
    #x1=12.5
    x1 =-8.5
    f = lambda w: w**2*4-20*w+25
    xvalues_curve= np.arange(-10, 15.5, 0.5)
    yvalues_curve = f(xvalues_curve)
    myplot.xlabel ('w', fontsize=12, fontweight='medium' )
    myplot.ylabel ('Loss(w)',fontsize=12, fontweight='medium')
    i=3  # This is to set the length of the tangent.
    if x1>2.5:  #when w starts on the right side of the curve
        t = ax.text(
        8, 50, "w decreases", ha="left", va="center", rotation=0, size=15,
        bbox=dict(boxstyle="larrow,pad=0.3", fc="orange", ec="b", lw=1))
        while x1>=2.5:
            y1=f(x1)
            start_point = x1-i
            stop_point = x1+i
        
            xvalues_slope = np.arange(start_point, stop_point, 0.2)
            grad= gradient(x1,y1,f, 0.000000001)
            yvalues_slope = compute_y_on_slope(grad, x1,y1, xvalues_slope)
            myplot.plot(xvalues_curve,yvalues_curve, 'm-', lw=2)
            myplot.plot(xvalues_slope,yvalues_slope, 'g-',lw=2)
            myplot.plot(x1,y1,'go',lw=3)
            x1-=2
            i+=0.5
    elif x1 <2.5: #when w starts on the right side of the curve
        t = ax.text(
        -9.5, 50, "w increases", ha="left", va="center", rotation=0, size=15,
        bbox=dict(boxstyle="rarrow,pad=0.3", fc="orange", ec="b", lw=1))
        while x1<=2.5:
            y1=f(x1)
            start_point = x1-i
            stop_point = x1+i
        
            xvalues_slope = np.arange(start_point, stop_point, 0.2)
            grad= gradient(x1,y1,f, 0.000000001)
            yvalues_slope = compute_y_on_slope(grad, x1,y1, xvalues_slope)
            myplot.plot(xvalues_curve,yvalues_curve, 'm-', lw=2)
            myplot.plot(xvalues_slope,yvalues_slope, 'g-',lw=2)
            myplot.plot(x1,y1,'go',lw=3)
            i+=0.5
            x1+=2
        
            
        #myplot.show()
        time.sleep(2)
    myplot.show()
    
    #draw_slope(x1, y1, None, xvalues_curve, None,xvalues_slope,None, f)


# In[ ]:




