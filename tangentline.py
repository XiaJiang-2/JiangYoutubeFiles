import matplotlib.pyplot as myplot
#gradient function below is used to compute the gradient or slope that is passing a point (x, y) on
#the curve of a function f(x).
def gradient(x,y,f):
    delta_l = 0.00000000001
    #because gradient is defined as a result when delta_l approches 0, so we'd like to assign a very small
    #value to delta_l
    delta_h = f(x+delta_l)-y
    grad=delta_h/delta_l
    return grad
# the draw_slope function below will draw the curve of function f based on an numpy array of given input values
# xvalues_curve, and the tangent line of the curve passing a point (x1, y1) on the curve. The length of the
# tangent line is determined based the input numpy array xvalues_slope. slope_arrow is boolean value that determines
# whether the output slope has an arrow at the end along the direction of the gradient.
def compute_y_on_slope(grad, x1,y1,x2):
    return grad*(x2-x1)+y1

def draw_slope(x1, y1, xvalues_curve, xvalues_slope, f, slope_arrow):
    grad= gradient(x1,y1,f)
    yvalues_curve = f(xvalues_curve)
    myplot.plot(xvalues_curve,yvalues_curve)
    myplot.plot(x1,y1,'o',lw=2)
    yvalues_slope = compute_y_on_slope(grad, x1,y1, xvalues_curve)
    myplot.plot(xvalues_slope,yvalues_slope)




