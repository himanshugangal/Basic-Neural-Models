#Gerstner electrical equivalent of the integrate and fire model , please refer to his literature for the electrical models 

from numpy import *
from pylab import *

T       = 100                  # Simulation Time (msec)
dt      = 0.25               # Time step (msec)
time    = arange(0, T, dt) 
tau   = 1 
t_rest  = 0 
  
 ## LIF properties
Vop      = zeros(len(time))-65    # potential (V) trace over time [ keeping the base voltage to be set at -65mV ] 
R      = 1                   # resistance (kOhm)
C     = 10                  # capacitance (uF)
tau   = R*C             # time constant (msec)
tau_ref = 4                   # refractory period (msec)
Vth     = -60                   # spike threshold (V)
V_spike = 70                 # spike delta (V)

 ## Stimulus
I       = 10                # input current (A)

 ## iterate over each time step
for i, t in enumerate(time):
   if t > t_rest:
     Vop[i] = Vop[i-1] + (I*R) / tau * dt #Integration Process 
   if Vop[i] >= Vth:                         # The neuron spikes when it reaches the threshold
     Vop[i] += V_spike + Vop[i]
     t_rest = t + tau_ref

 ## plot 
plot(time, Vop)
title('Integrate and Fire neuron on stimulation by a constant current')
ylabel('Membrane Potential (V)')
xlabel('Time(msec)')
ylim([-70,50])
show()