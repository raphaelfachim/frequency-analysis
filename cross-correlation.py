import numpy as np
import matplotlib.pyplot as plt

def main():

    time = np.linspace(0, 2, 100)
    ang = time * 2 * np.pi
    # First signal 
    sig1 = np.sin(ang)
    # Seconds signal with pi/4 phase shift. Half the size of sig1
    sig2 = np.cos(ang)
    
    # npcorr = np.correlate(sig1, sig2)
    # print(f"sinal 1 {np.size(sig1)}: {sig1}")
    # print(f"sinal 2 {np.size(sig2)}: {sig2}")
    # print("correlação cruzada : ", npcorr)
    # print("máximo da correlação cruzada : ", np.max(npcorr))

    fig, [ax1, ax2, ax3] = plt.subplots(3, 1, sharex=False)
    ax1.xcorr(sig1, sig2, usevlines=True, maxlags=50, normed=True, lw=2)
    ax1.grid(True)

    ax2.plot(time, sig1, label="Seno")
    ax2.plot(time, sig2, label="Cosseno")
    ax2.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax2.grid(True)
    

    # delaying 12 samples
    sig2 = np.roll(sig2, 12)

    ax3.plot(time, sig1, label="Seno")
    ax3.plot(time, sig2, label="Cosseno")
    ax3.legend(loc='upper right', shadow=False, fontsize='x-small')
    ax3.grid(True)

    plt.show()
    
if __name__ == "__main__":
    main()