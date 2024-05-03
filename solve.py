from sympy import symbols, diff
from sympy.parsing.mathematica import parse_mathematica
import numpy as np
import math
def solve(f1,f2,a,b):
    x, y = symbols('x y')
    f = x**2 + 3*y**2 + 2*x*y
    f_partial_x = diff(f, x)
    f_partial_y = diff(f, y)
    my_array = np.arange(a, b, 0.1)
    func1 = parse_mathematica(f1)
    func2 = parse_mathematica(f2)
    df1_x = diff(func1,x)
    df1_y = diff(func1,y)
    df2_x = diff(func2,x)
    df2_y = diff(func2,y)
    def findZeroValues():
        for i in my_array:
            for j in my_array:
                res1 = func1.subs({x: i, y: j})
                res2 = func2.subs({x: i, y: j})
                if math.fabs(res1-res2)<=0.1:
                    return [i,j]
        return "Yechim topilmadi"
    xn=0; yn=0
    def yaqinlashish(x0, y0):
        while True:
            jak = df1_x.subs({x: x0,y: y0})*df2_y.subs({x: x0,y: y0}) - df1_y.subs({x: x0,y: y0})*df2_x.subs({x: x0,y: y0})
            if jak!=0:
                F = func1.subs({x: x0, y: y0})
                G = func2.subs({x: x0, y: y0})
                dx = F*df2_y.subs({x: x0,y: y0}) - G*df1_y.subs({x: x0,y: y0})
                dy = G*df1_x.subs({x: x0,y: y0}) - F*df2_x.subs({x: x0,y: y0})
                xn = x0-dx/jak
                yn = y0-dy/jak
                if math.fabs(xn-x0)<0.001 and math.fabs(yn-y0)<0.001:
                    x0 = xn
                    y0 = yn
                else:
                    break
            else:
                break
        return [xn,yn]

    [x0,y0] = findZeroValues()
    return yaqinlashish(x0,y0)
