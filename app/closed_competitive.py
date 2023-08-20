import numpy as np
from scipy.integrate import quad
from scipy.optimize import newton
import pandas as pd


def closed_competitive(beta, i, f, t_R, t_ID, phi, g, pi, t_CG, t_I, theta, t, delta, a, c0, N, r_, W, t_, d):
    j = ((beta * i + f + t_R) * (1 - t_ID) + (1 - beta) * (i + phi) - (g + pi) * (1 - t_CG)) / (1 - t_I)

    # solve for equilibrium city radius
    B = -theta * t * delta / (a * (delta - 1))
    A = lambda d_: 2 * np.pi / a * delta * j * r_ / (delta - 1) * np.exp(-B * d_)
    city_radius_eqn = lambda d_: A(d_) / B * (d_ * np.exp(B * d_) - (np.exp(B * d_) - 1) / B) - N
    d_ = newton(city_radius_eqn, 1)

    # Solve initial condition for rent at the centre
    p0 = delta * c0 ** (1 / delta) * j * (r_ / (delta - 1)) ** ((delta - 1) / delta) * np.exp(theta * t * d_ / a)

    # Rent and house prices
    p = p0 * np.exp(-theta * t * d / a)
    P = p / j

    # Land prices
    r_func = lambda _d: r_ * np.exp(-B * (d_ - _d))
    
    # Land quantity
    L = a * (delta * c0 * j) ** (1 / (delta - 1)) * p ** (delta / (1 - delta))
    L_density = 1 / L

    # Housing quantity
    H = a / p
    h = H / L

    # Utility
    #U = W - (1 - theta) * t_ - a + a * np.log(a) - a * np.log(p0)

    # Differential land rents
    diff_land_rents, error = quad(lambda _d: 2 * np.pi * _d * (r_func(_d) - r_), 0, d_)

   
    eq = pd.DataFrame({'p(d)': p,
                    'P(d)': P,
                    'r(d)': r_func(d),
                    'L(d)': L,
                    '1/L(d)': L_density,
                    'H(d)': H,
                    'h(d)': h,
                    'r_': r_})
    eq.index = d

    return eq, d_, diff_land_rents