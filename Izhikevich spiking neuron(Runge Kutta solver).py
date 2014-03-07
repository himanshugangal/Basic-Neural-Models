from numpy import* 
from pylab import*
# simulating the Eugene Izhikevich model 
# Governing differential equations 
# dv/dt = 0.04v^2 + 5v + 140 - u + 1 
# du/dt = a(bv - u) 

def funca(v,u,I):
    #Returns  dv/dt   
    result1 = 0.04*v*v + 5*v + 140 - u + I 
    return result1 
def funcb(v,u):
    #Returns du/dt 
    result2 = 0.02*(0.2*v - u)
    return result2
t_sim = 100 # simulation time 
dt = 0.25 #time step 
time = arange(0,t_sim,dt) 
V = zeros(len(time))
U = zeros(len(time))
V[0] = -70
U[0] = 0.2*V[0]
T1 = 1
i = 0 
for i in range(1,380):
    if i < 350:
        I = 14 
    else:
        I = 0
    f1a = dt*funca(V[i],U[i],I)
    f1b = dt*funcb(V[i],U[i])
    f2a = dt*funca(V[i] + 0.5*f1a , U[i] + 0.5*f1b,I)
    f2b = dt*funcb(V[i] + 0.5*f1a , U[i] + 0.5*f1b)
    f3a = dt*funca(V[i] + 0.5*f2a , U[i] + 0.5*f2b,I)
    f3b = dt*funcb(V[i] + 0.5*f2a , U[i] + 0.5*f2b)
    f4a = dt*funca(V[i] + f3a , U[i] + f3b,I)
    f4b = dt*funcb(V[i] + f3a , U[i] + f3b)
    V[i] = V[i-1] + 0.166*(f1a + 2*f2a + 2*f3a + f4a)
    U[i] = U[i-1] + 0.166*(f1b + 2*f2b + 2*f3b + f4b) 
    print "%f" % V[i]
    if (V[i] >= 30):
        V[i] = -65 
        U[i] = U[i] + 6
    i = i+1
            
plot(time, V )
title('Izhikevich Model')
ylabel('Membrane Potential (V)')
xlabel
show()        
    