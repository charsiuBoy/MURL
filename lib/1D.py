import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1, 100, dtype="float64")

#initial data 
u0 = -np.arctan(x)

def d_dx(x,u):
    #return np.gradient(u, x)
    du = np.empty(np.shape(x), dtype="float64")
    '''
    du[0] = (u[1]-u[0])/(x[1]-x[0])
    du[-1] = (u[-1]-u[-2])/(x[-1]-x[-2])
    '''
    #derivative at boundary is zero
    du[0] = 0
    du[-1] = 0

    for i in range(1, len(x)-1):
        du[i] = (u[i+1]-u[i-1])/(x[i+1]-x[i-1])
    return du 


def engine(x,u,dt):
    #return the next step of the system, given current state (u,t), x is space
    du = d_dx(x,u)

    #burgers equation
    u += - u*du*dt

    return u

class Sol:
    def __init__(self, engine, x, u, dt):
        self.engine = engine
        self.x = x
        self.init_data = u
        self.state = u
        self.dt = dt


    def __iter__(self):
        return self

    def __next__(self):
        self.state = self.engine(self.x, self.state, self.dt)
        return self.state


instance = Sol(engine, x, u0, np.float64(1e-3))

def energy(x, u):
    return 0.5*np.trapezoid(np.square(u))

def visualizer(x, instance, k=1):
    fig = plt.figure()
    for i in range(0, 10000):
        if i % k == 0: 
            plt.xlim(-1,1)
            plt.ylim(-1.5,1.5)
            state = next(instance)
            plt.plot(x, state)
            plt.text(0, 1, "energy"+str(energy(x, state)))
            plt.pause(1e-6)
        plt.clf()
    plt.show()

visualizer(x, instance, 1) 


