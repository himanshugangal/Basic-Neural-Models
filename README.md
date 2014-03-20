The repo gives an easy implementation of existing neural models in python . The following listed implementations have been done : 

1) Integrate and fire  

The python code implements the standard integrate and fire model , with a constant input current . The model includes a refractory period . Please note that the system does not accumulate the input current . 

2) Ihzhikevich Spiking Neuron ( regular firing ) 

The new Eugene Ihzhikevich Neuron , consisting of simultaneous solving of 2 differential equations . The numerical method , however employed here is not very efficient . 

3) Ihzhikevich Spiking Neuron(employing Runge Kutta)

Much more efficient method for implmenting the Ihzhikevich Model , the method used is Runge Kutta 4th order .  