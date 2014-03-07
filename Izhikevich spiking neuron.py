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
    V[i] = V[i-1] + dt*funca(V[i-1],U[i-1],I)
    U[i] = U[i-1] + dt*funcb(V[i-1],U[i-1])
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
    