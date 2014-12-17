from matplotlib.pyplot import *
from scipy.optimize import leastsq
from scipy.integrate import quad
from scipy.special import gamma


f = lambda r,q,xi,d: 2 * r**(d-1)*np.exp(-r/xi)*np.sinc(q*r)

F = np.vectorize(lambda q,xi,d: quad(f, 0, np.inf, args=(q,xi,d))[0])

qs = np.logspace(-2,2,25)

figure('Empirical', figsize=(4.875, 3.25))

for d,c in zip([1,1.5,2], 'rgb'): 
    plot(qs, 1/(1+((d+1)*qs)**2)**(0.5*d), color=c)
    plot(qs, F(qs, 1, d)/(2*gamma(d)), 'o', color=c)

gca().set_position([0.16, 0.16, 0.76, 0.76])

xscale('log'); yscale('log')
xlabel(r'$\xi q$')
ylabel(r'$S(q)/(2\chi\Gamma(d))$')
savefig('empirical_fractal.pdf')
