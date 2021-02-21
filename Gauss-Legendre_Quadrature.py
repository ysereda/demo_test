#!/usr/bin/env python
# coding: utf-8

# # Gauss-Legendre quadrature

# In[1]:


# https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature


# In[7]:


def Gauss_Legendre_quadrature(f,a,b,o): # integrand f(x), lower and upper integration limits
    w=np.zeros(o+1); x=np.zeros(o+1); X=np.zeros(o+1);
    c=(b-a)/2; In=0;
    if o==1: # 1-point Gaussian
        In = 2*f((a+b)/2);
    elif o==2: # 2-point Gaussian
        w[1]=1; w[2]=1; x[2]=1/math.sqrt(3); x[1]= -x[2];
    elif o==3:
        w[1]= 5/9; w[2]= 8/9; w[3]= 5/9; x[1]=-math.sqrt(3/5); x[2]=0; x[3]=math.sqrt(3/5);
    elif o==4:
        w[4]= 1/2-1/36*30**(1/2); w[3]= 1/2+1/36*30**(1/2); w[2]=w[3]; w[1]=w[4];
        x[3]= math.sqrt(3/7-2/7*math.sqrt(6/5)); x[4]= math.sqrt(3/7+2/7*math.sqrt(6/5)); x[2]=-x[3]; x[1]=-x[4];
    elif o==5:
        w[3]=128/225; w[4]=161/450+13/900*70**(1/2); w[5]=161/450-13/900*70**(1/2); w[2]=w[4]; w[1]=w[5];
        x[3] = 0; x[4]=math.sqrt(5-2*math.sqrt(10/7))/3; x[5]=math.sqrt(5+2*math.sqrt(10/7))/3;
        x[1] = -x[5]; x[2] = -x[4];
    elif o==6:
        #w[4]:=max(fsolve( w[4]^3-w[4]^2+2797/9000*w[4]-14641/506250 = 0 ));
        w[4] = .4679139345726910473898703439895509948116556057692105353116253199639142016203981270311100925847919823;
        #X[4] := -16/33+1/231*(145369-277200*w[4])^(1/2); x[4]:=sqrt(X[4]);
        X[4] = 0.0569391159670073532371751168037721197227028892033080364096921542939602701674029743237527080956929680;
        x[4] = .2386191860831969086305017216807119354186106301400213501813951645742749342756398422492244272573491313;
        #w[5] := -1/2*w[4]+1/2+1/300*(-67500*w[4]^2+45000*w[4]-5470)^(1/2);
        w[5] = .3607615730481386075698335138377161116615218927467454822897392402371400378372617183209622019888193477;
        #X[5] := -1/77*(680-315*X[4]+231*X[4]^2-1200*w[5])/(-7+3*X[4]); x[5]:=sqrt(X[5]);
        X[5] = .4371978527510939418006878729474220341226577947572340251494209799533122691708250835278994246509161683;
        x[5] = .6612093864662645136613995950199053470064485643951700708145267058521834966071431009442864037464614570;
        #w[6] := 1-w[4]-w[5];
        w[6] = .1713244923791703450402961421727328935268225014840439823986354397989457605423401546479277054263886700;
        #X[6] := 15/11-X[5]-X[4]; x[6]:=sqrt(X[6]);
        X[6] = .8694993949182623413257733738851694825182756796758215748045232293890910970254083057847115036170272277;
        x[6] = .9324695142031520278123015544939946091347657377122898248725496165266135008442001962762887399219259849;
        w[3] = w[4]; w[2] = w[5]; w[1] = w[6];
        x[1] = -x[6]; x[2] = -x[5]; x[3] = -x[4];
    elif o==7:
        #X[5]:=Re(evalf(allvalues(RootOf(-35+315*_Z-693*_Z^2+429*_Z^3)))[1]);
        X[5] = .1647102868965424215227963860030182354392804846697769434790280637358337458975567814589362472336898770;
        #X[6] := 21/26-1/2*X[5]-1/286*sqrt(-6699+66066*X[5]-61347*X[5]^2);
        X[6] = .5498684992164435639085994625610349345151732352867266411465070381521297749138857470357090747002970182;
        #X[7] := 21/13-X[6]-X[5];
        X[7] = .9008058292716293991839887668205622146609308954281117999898495134966518638039420868899700626813977200;
        #x[5]:=sqrt(X[5]); x[6]:=sqrt(X[6]); x[7]:=sqrt(X[7]);
        x[4]=0;
        x[5] = .4058451513773971669066064120769614633473820140993701263870432517946638132261256553283126897277465878;
        x[6] = .7415311855993944398638647732807884070741476471413902601199553519674298746721805137928268323668632472;
        x[7] = .9491079123427585245261896840478512624007709376706177835487691039130633303548401408057307700279257239;
        x[1]=-x[7]; x[2]=-x[6]; x[3]=-x[5];
        w[4] = 512/1225;
        w[5] = -1859/8400*X[5]*X[5]+7947/19600-1573/14700*X[5];
        w[6] = 2783/4900-143/400*X[5]-27313/58800*X[6]+1859/8400*X[5]*X[5]+1859/8400*X[5]*X[6];
        w[7] = -143/784+27313/58800*X[5]+27313/58800*X[6]-1859/8400*X[5]*X[6];
        w[1]=w[7]; w[2]=w[6]; w[3]=w[5];
    for i in range(1, o+1):
        X[i]=c*(x[i]+1+a);
        In=In+w[i]*f(X[i]);
    In=c*In;
    return In;


# In[8]:


# Test function
a=0; b=2.4; # integration interval
def f(x):
    return 2*x/(x**2+1); # integrand


# In[9]:


n_max=7; # maximum order of approximation
I=[0]*(n_max+1); E=[0]*(n_max+1);
I[0]=1.911022890054872722905456; # Exact value of I = int(f(x),x=a..b)
for n in range(1, n_max+1):
    I[n] = Gauss_Legendre_quadrature(f,a,b,n);
    E[n] = abs(I[n]/I[0]-1);
E[1:]


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111)
ax.set_yscale("log", nonposy='clip')
x = np.linspace(0, n_max, n_max+1)
plt.plot(x[1:],E[1:])

