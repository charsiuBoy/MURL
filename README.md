#MURL with Prof. Mimi Dai

So I've just add a script lib/1D.py

you can run my script in interact mode:
`python -i 1D.py`

You can create your own initial condition:
`x = np.linspace(0, 1, 1000)`
`init = np.sin(x)`

Then you just pass in my simulator (`Sol` class) like so:
`sim = Sol(engine, x, init, np.float64(1e-3)) ` (dt = 10^-3)

Then you can see how it evolves:
`visualizer(x, sim, 1)`
The '1' indicates the video speed. If you want twice the speed, then:
`visualizer(x, sim, 2)`
