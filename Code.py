
import numpy as np
import matplotlib.pyplot as plt

a = 0.002032
b = 0.001016
m = [1, 2, 0, 1]
n = [0, 0, 1, 1]
mur = 1
er = 1
mu = mur * 4 * np.pi * 1e-7
e0 = er * 8.854e-12

f = np.linspace(70*(10**9), 295*(10**9), 2000)



for j in range(4):
    fc = (1/(2 *np.pi*np.sqrt(mu*e0)))*(np.sqrt(((m[j]*np.pi)/a)**2+((n[j]*np.pi)/b)**2))
    w = 2*np.pi*f
    beta = np.zeros(2000)
    wl = np.zeros(2000)
    impedance = np.zeros(2000)

    for i in range(2000):
        beta[i] = w[i]*np.sqrt(mu*e0)*np.sqrt(1-(fc/f[i])**2)
        wl[i] = (2*np.pi)/beta[i]
        impedance[i] = (np.sqrt(mu/e0))/(np.sqrt(1-(fc/f[i])**2))

    print(f"Cutoff frequency : {fc/10**9} Ghz")

    plt.plot(f, np.real(wl), 'b')
    plt.xlabel('Frequency')
    plt.ylabel('Wavelength')
    plt.legend(['Real'])
    plt.title("Wavelength vs. Frequency TE" + str(m[j]) + str(n[j]))
    plt.show()

    plt.plot(f, np.real(beta), 'b', f, np.imag(beta), 'r')
    plt.xlabel('Frequency')
    plt.ylabel('Propagation const')
    plt.legend(['Imaginary', 'Real'])
    plt.title("Gamma. vs. Frequency TE" + str(m[j]) + str(n[j]))
    plt.show()
    
    plt.plot(f, np.real(impedance), 'b')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Impedance')
    plt.legend(['Real'])
    plt.title("Impedance vs. Frequency TE" + str(m[j]) + str(n[j]))
    plt.show()

