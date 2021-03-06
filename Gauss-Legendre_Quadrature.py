#!/usr/bin/env python
# coding: utf-8

# # Gauss-Legendre quadrature

# In[1]:


# https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature


# In[15]:


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
    elif o==8:
        #6435*X[5]^4-12012*X[5]^3+6930*X[5]^2-1260*X[5]+35=0;
        #X[5]=RootOf(6435*_Z^4-12012*_Z^3+6930*_Z^2-1260*_Z+35,index = 1);
        X[5]=0.0336482680675068532985540048193035156251012783315979216647959801410143899311399752866725024184634830;
        #X[6]^3 = 5/429*(-35+315*X[5]+315*X[6]-9009*X[5]^3*X[6]+27027*X[5]^3*X[6]^2+429*X[5]^3-693*X[5]^2+13365*X[5]^2*X[6]-38115*X[5]^2*X[6]^2-693*X[6]^2+13365*X[5]*X[6]^2-5103*X[5]*X[6])/(-315*X[5]^2+105*X[5]-5+231*X[5]^3);
        #X[6] = RootOf(6435*_Z^4-12012*_Z^3+6930*_Z^2-1260*_Z+35,index = 2);
        X[6]= .2761843138724644405463052851573544729585481339919337657504201298272578525241587586123023799262448321;
        #X[7]^2 = 1/33*(((20790*X[7]-2079)*X[6]^2+(-19404*X[7]+2310)*X[6]-495+2310*X[7])*X[5]^2+((-19404*X[7]+2310)*X[6]^2+(-2700+19320*X[7])*X[6]+630-2700*X[7])*X[5]+(2310*X[7]-495)*X[6]^2+(630-2700*X[7])*X[6]-175+630*X[7])/((735*X[6]^2+63-630*X[6])*X[5]^2+(-70-630*X[6]^2+588*X[6])*X[5]+15-70*X[6]+63*X[6]^2);
        #X[7] = RootOf(6435*_Z^4-12012*_Z^3+6930*_Z^2-1260*_Z+35,index = 3);
        X[7]= .6346774762346366440178864667605024322530391037128209058907391016449949226465266045985527132650528105;
        X[8]= (105*X[5]*X[6]*X[7] - 63*X[5]*X[6] - 63*X[5]*X[7] - 63*X[6]*X[7] + 45*X[5] + 45*X[6] + 45*X[7] - 35)/(3*(105*X[5]*X[6]*X[7] - 35*X[5]*X[6] - 35*X[5]*X[7] - 35*X[6]*X[7] + 21*X[5] + 21*X[6] + 21*X[7] - 15));
        w[8]= 1/105*(7*(5*(3*X[5]-1)*X[6]-5*X[5]+3)*X[7]-7*(5*X[5]-3)*X[6]+21*X[5]-15)/(X[7]-X[8])/(X[6]-X[8])/(X[5]-X[8]);
        x[5]=math.sqrt(X[5]); x[6]=math.sqrt(X[6]); x[7]=math.sqrt(X[7]); x[8]=math.sqrt(X[8]);
        x[1]=-x[8]; x[2]=-x[7]; x[3]=-x[6]; x[4]=-x[5];
        w[7]= (5*(3*X[5]*(1-w[8])+3*w[8]*X[8]-1)*X[6]+15*w[8]*X[8]*(-X[8]+X[5])+3-5*X[5])/(15*(X[6]-X[7])*(X[5]-X[7]));
        w[6]= 1/3*(3*(1-w[8]-w[7])*X[5]+3*w[7]*X[7]+3*w[8]*X[8]-1)/(X[5]-X[6]);
        w[5]= 1-w[8]-w[7]-w[6];
        w[1]=w[8]; w[2]=w[7]; w[3]=w[6]; w[4]=w[5];
    elif o==9:
        #X[6] = RootOf(12155*_Z^4-25740*_Z^3+18018*_Z^2-4620*_Z+315,index=1);
        X[6]= .1051402825890897841204817514987030687806452430610058344577892387975329783200325594480270140058476728;
        #X[7] = RootOf(12155*_Z^4-25740*_Z^3+18018*_Z^2-4620*_Z+315,index=2);
        #1105*X[7]^3+65*(-36+17*X[6])*X[7]^2+13*(-180*X[6]+85*X[6]^2+126)*X[7]-420+1638*X[6]-2340*X[6]^2+1105*X[6]^3 = 0;
        X[7]= 0.3762245144531748949762019366655656931153031056707446735398897722522868281311740213796796176281964250;
        #X[8] = RootOf(12155*_Z^4-25740*_Z^3+18018*_Z^2-4620*_Z+315,index=3);
        #85*X[8]^2+5*(17*X[6]-36+17*X[7])*X[8]+85*X[6]^2-180*X[6]+85*X[7]*X[6]+85*X[7]^2-180*X[7]+126 = 0;
        X[8]= .6989480124178008184946440924950510933038331032822585644741861048376117449404636922770222168621479403;
        #X[9] = RootOf(12155*_Z^4-25740*_Z^3+18018*_Z^2-4620*_Z+315,index=4);
        X[9]= (((495-693*X[6])*X[7]+495*X[6]-385)*X[8]+(-385+495*X[6])*X[7]-385*X[6]+315)/(11*(63*X[8]-45+(63-105*X[8])*X[6])*X[7]+11*(63*X[8]-45)*X[6]-495*X[8]+385);
        x[6]=math.sqrt(X[6]); x[7]=math.sqrt(X[7]); x[8]=math.sqrt(X[8]); x[9]=math.sqrt(X[9]);
        x[1]=-x[9]; x[2]=-x[8]; x[3]=-x[7]; x[4]=-x[6]; x[5]=0;
        w[9]= 1/315*((63*X[6]-45+(63-105*X[6])*X[7])*X[8]+(-45+63*X[6])*X[7]+35-45*X[6])/((X[9]-X[8])*(X[9]-X[7])*(X[9]-X[6])*X[9]);
        w[8]= 1/105*((21-105*w[9]*X[9]*X[9]+(105*w[9]*X[9]-35)*X[7])*X[6]+(21-105*w[9]*X[9]*X[9])*X[7]-15+105*w[9]*X[9]*X[9]*X[9])/((X[8]-X[7])*(X[6]-X[8])*X[8]);
        w[7]= ((-1/3+w[9]*X[9]+w[8]*X[8])*X[6]-w[8]*X[8]*X[8]-w[9]*X[9]*X[9]+1/5)/(X[7]*(X[7]-X[6]));
        w[6]= (1/3-w[9]*X[9]-w[8]*X[8]-w[7]*X[7])/X[6];
        w[5]= 2*(1-w[6]-w[7]-w[8]-w[9]);
        w[1]=w[9]; w[2]=w[8]; w[3]=w[7]; w[4]=w[6];
    for i in range(1, o+1):
        X[i]=c*(x[i]+1+a);
        In=In+w[i]*f(X[i]);
    In=c*In;
    return In;


# In[12]:


# Test function
a=0; b=2.4; # integration interval
def f(x):
    return 2*x/(x**2+1); # integrand


# In[16]:


n_max=9; # maximum order of approximation
I=[0]*(n_max+1); E=[0]*(n_max+1);
I[0]=1.911022890054872722905456; # Exact value of I = int(f(x),x=a..b)
for n in range(1, n_max+1):
    I[n] = Gauss_Legendre_quadrature(f,a,b,n);
    E[n] = abs(I[n]/I[0]-1);
E[1:]


# In[17]:


import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111)
ax.set_yscale("log", nonposy='clip')
x = np.linspace(0, n_max, n_max+1)
plt.plot(x[1:],E[1:])

