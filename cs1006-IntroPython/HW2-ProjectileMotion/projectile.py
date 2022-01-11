import matplotlib.pyplot as plt

gravity = 9.81
G = 6.6742*10**-11
Me = 5.9736*10**24
Re = 6371000
delta_t = 0.05
v_0 = 300
n = 100
g_count = 0

def s_standard(t, v_0):
    s = -0.5*gravity*((t)**2)+ v_0*t
    return s
    

def grav(s):
    global g_count
    g_count = g_count + 1
    g = (G*Me)/((Re + s)**2)
    return g


def s_next(s_current, v_current, delta_t):
    return s_current + v_current*delta_t


def v_next(s_current, v_current, delta_t):
    return v_current - grav(s_current)*delta_t


def s_sim(t, v_0, s_0, delta_t):
    v = v_0
    s = s_0
    for i in range (0, n):
        s =  -0.5*grav(s)*((t)**2) + v_0*t
        temp_v = v
        v = v_next(v, s, delta_t)
        s2 = s_next(s, temp_v, delta_t)
    return s2


def plot_trajectories(y, z):
    print("\nNon-efficient number of calculations of gravity value: ", g_count)
    print("\n\n\n")
    x = list(range(0, len(z), 1))
    fig, ax1 = plt.subplots()
    ax1.plot(x, y, color = 'r')
    ax1.plot(x, z, color = 'b')
    plt.show()
    return
