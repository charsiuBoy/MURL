import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1, 1000, dtype="float64")

#initial data
u0 = -x
'''
fig, ax = plt.subplots()
ax.plot(x, u0)
plt.show()
'''
def d_dx(x, u):
    du = x

    #return 1D derivative 
    
    #at boundary:
    du[0]=(u[1]-u[0])/(x[1]-x[0])
    du[len(x)-1] = (u[len(x)-1] - u[len(x)-2])/(x[len(x)-1] - x[len(x)-2])

    for i in range(1,len(x)):
        du[i]=(u[i]-u[i-1])/(x[i]-x[i-1])
    return du

du = d_dx(x, u0)
fig, ax = plt.subplots()
ax.plot(x, du)
plt.show()


def solver(x,u,t):
    #return the next step of the system, given current state (u,t), x is space
    pass


def integrator(x, u, T):
    #return the whole evolution of t=0 to t=T, given initial data x lives on space x.
    pass



