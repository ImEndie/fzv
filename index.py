from sympy import symbols, diff
from sympy.parsing.mathematica import parse_mathematica
import numpy as np
import math
def solve(a,b,r,h,ort,dast,lyam,sig_oquv,p,govaklik,sxema=1):
    if r>b and r<a :
        print("Radius noto'g'ri kiritildi");
    govaklik=0;
    za=0;
    zb=0;
    z=0;
    match sxema:
        case 1:
            za=0;
            zb=0;
        case 2:
            za=h/2;
            zb=h/2;
        case 3:
            za=0;
            zb = h;
        case 4:
            za=h/2;
            zb=h;
    def kse(x):
        res = -0.5772;
        for i in range(1,x):
            res+=1/i;
        return res;
    def fakt(n):
        fact=1;
        for i in range(1, n+1):
            fact = fact * i
        return fact
    for n in range(1,11):
        p_oq = -2/3*sig_oquv*math.sqrt((1-ort)**3/ort);
        p_dif = p_oq+lyam*p_oq;
        p_yon = p_oq*(1-1.5*ort);
        x = -(ort-dast)*(1-ort)/((1-dast)*(p_yon-p_oq));
        alfa = math.sqrt(math.fabs(x/(p_dif)));
        D_a = 2/(math.pi*n)*p_yon*(math.cos(math.pi*n)+1-2*math.cos(math.pi*n*za/h))
        D_b = -2*p_yon*(math.cos(math.pi*n)+1-2*math.cos(math.pi*n*zb/h))/(n*math.pi);
        
        
        def I_0_1(radius):
            I_0 = 0; I_1=0;
            for j in range(10):
                I_0+=(alfa*math.pi*radius/(2*h))**(2*j)/(kse(j+1)**2);
                I_1+=(alfa*math.pi*radius/(2*h))**(1+2*j)/(kse(j+1)*kse(j+2));
            return I_0,I_1
        def K_0_1(radius):
            K_0 = 0; K_1=0;
            for j in range(1,11):
                K_0+=(alfa*math.pi*radius/(2*h))**(2*j)/(math.pow(fakt(j),2))*(math.log(alfa*math.pi*j*radius/(2*h))-kse(j+1));
                K_1+=pow((alfa*math.pi*radius/(2*h)),(1+2*j))/(fakt(j)*fakt(j+1))*(2*math.log(alfa*math.pi*j*radius/(2*h))-kse(j+1)-kse(j+2));
            K_1*=0.5;
            K_0*=-1;
            return K_0,K_1
        K_0_a,K_1_a = K_0_1(a)
        K_0_b,K_1_b = K_0_1(b)
        I_0_a,I_1_a = I_0_1(a)
        I_0_b,I_1_b = I_0_1(b)
        K_0_r,K_1_r = K_0_1(r)
        I_0_r,I_1_r = I_0_1(r)
        f1 = (K_1_b*D_a-K_1_a*D_b)/(I_1_a*K_1_b-I_1_b*K_1_a)
        f2 = (I_1_b*D_a-I_1_a*D_b)/(I_1_b*K_1_a-I_1_a*K_1_b)
        z+=h/10;
        govaklik+=math.cos(math.pi*n*(z/h))*p*math.sqrt(alfa)/p_dif*(f1*I_0_r-f2*K_0_r);
    return math.abs(govaklik)
