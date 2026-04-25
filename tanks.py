import numpy as np
from matplotlib import pyplot as plt

def valid_input(inp,up_lim,low_lim=0):
    while True:
        try:
            if (low_lim <= int(inp) <= up_lim):
                return int(inp) # valid
        except:
            pass
        inp = input(f'Please input a digit {low_lim} - {up_lim}: ')

def tanks():
    loc = input('Where would you like to place your tank? (0-20) ')
    loc = valid_input(loc,20)
    for i in range(5):
        theta = input('What angle would you like to launch shoot at? (0 - 90) ')
        theta = valid_input(theta,90)
        power = input('What power would you like to shoot at? (1-100) ')
        power = valid_input(power,100)
        target = 255 # example
        if (target - 20) <= (power**2*np.sin(2*np.deg2rad(theta))/9.8) <= (target + 20):
            print('BOOM') # hit
            break
        else:
            print('miss')
    return

if __name__ == '__main__':
    tanks()
