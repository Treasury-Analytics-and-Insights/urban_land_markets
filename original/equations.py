## Third-party libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.optimize import newton

# Parameters ---------------------------------------------------------------

## Load exogenous parameters
exec(open('original/parameters.py', encoding="utf-8").read())

## Compute Poterba scalar
j = ((β*i + f + t_R)*(1 - t_ID) + (1 - β)*(i + φ) - (g + π)*(1 - t_CG)) \
                                / (1 - t_I)

## Define intermediate parameters
B = -θ*t*δ / (a*(δ-1))
A = lambda d_: 2*np.pi/a * δ*j * r_/(δ-1) * np.exp(-B*d_)

## Solve for equilibrium city radius
city_radius_eqn = lambda d_: A(d_)/B*(d_*np.exp(B*d_)-(np.exp(B*d_)-1)/B) - N
d_ = newton(city_radius_eqn, 1)

## Solve initial condition for rent at the centre
p0 = δ * c0**(1/δ) * j * (r_/(δ-1))**((δ-1)/δ) * np.exp(θ*t*d_/a)

# Equilibrium prices/quantities ----------------------------------------------

## Eq rent and house prices
p = lambda d: p0*np.exp(-θ*t*d/a)
P = lambda d: p(d)/j

## Eq land prices
r = lambda d: r_ * np.exp(-B*(d_-d))

## Eq quantity of land
L = lambda d: a * (δ*c0*j)**(1/(δ-1)) * p(d)**(δ/(1-δ))
L_density = lambda d: 1 / L(d)

## Eq quantity of housing
H = lambda d: a / p(d)
h = lambda d: H(d) / L(d)

## Utility
U = W - (1 - θ)*t_ - a + a*np.log(a) - a*np.log(p0)

## Differential land rents
diff_land_rents, error = quad(lambda d: 2*np.pi*d*(r(d)-r_), 0, d_)

# Solve the model ------------------------------------------------------------

d = np.linspace(0, 1.5, 301)

eq = pd.DataFrame({'p(d)' : p(d),
                   'P(d)' : P(d),
                   'r(d)' : r(d),
                   'L(d)' : L(d),
                   '1/L(d)' : L_density(d),
                   'H(d)' : H(d),
                   'h(d)' : h(d),
                   'r_' : r_})
eq.index = d

#eq.to_csv('original/original_output.csv')

eq['r(d)'].plot(label='Land price')
eq['P(d)'].plot(label='House price')
eq['r_'].plot(label='Farm land price')
eq['p(d)'].plot(label='House rents', c='gold')
plt.legend()
plt.show()


