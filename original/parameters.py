# Exogenous parameters

# | agent      | parameter | description                                    |
# |------------|-----------|------------------------------------------------|
# | consumers  | N         | population                                     |
# | consumers  | W         | wages at the centre                            |
# | consumers  | t         | marginal cost of primary commute               |
# | consumers  | t_        | fixed cost of alternative commute              |
# | consumers  | θ         | job centralisation weight                      |
# | consumers  | a         | coefficient for log utility of housing, H      |
# |------------|-----------|------------------------------------------------|
# | developers | r_        | land rent at the urban/rural boundary          |
# | developers | δ         | cost elasticity of building height             |
# | developers | c0        | cost scalar for building height                | 
# |------------|-----------|------------------------------------------------|
# | landlords  | t_I       | marginal tax rate for rental income            |
# | landlords  | t_CG      | marginal tax rate for capital gains income     |
# | landlords  | t_ID      | rate of tax deductibility                      |
# | landlords  | t_R       | average tax rate for local government          |
# | landlords  | f         | maintenance costs of housing                   |
# | landlords  | β         | share of debt financing vs equity              |
# | landlords  | π         | general price inflation (nominal)              |
# | landlords  | g         | house price inflation net of general inflation |
# | landlords  | i         | interest rate on borrowing                     |
# | landlords  | φ         | equity risk prem                               |

## Consumers
N = 1
W = 5
t = 2.5
t_ = 0
θ = 0.2
a = 1

## Developers
r_ = 1
δ = 1.6
c0 = 1

## Landlords
t_I = 0.33
t_CG = 0.15
t_ID = t_I
t_R = 0.0033
f = 0.01
β = 0.5
π = 0.015
g = 0.015
i = 0.045
φ = 0.03