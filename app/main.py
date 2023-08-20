
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import panel as pn
from scipy.integrate import quad
from scipy.optimize import newton

from plot import plot, symmetric_plot_data
from closed_competitive import closed_competitive

# scale the panel widgets to stretch to container width
pn.extension(sizing_mode="stretch_width")

pop_input = pn.widgets.IntInput(name='Population', value=1, start=1, end=1000000)
wages_input = pn.widgets.FloatInput(name='Wages at centre', value=5, start=0, end=1000000)
marginal_cost_input = pn.widgets.FloatInput(name='Marginal cost of primary commute', value=2.5, start=0, end=1000000)
fixed_cost_input = pn.widgets.FloatInput(name='Fixed cost of alternative commute', value=0, start=0, end=1000000)
job_centralisation_weight_input = pn.widgets.FloatInput(name='Job centralisation weight', value=0.2, start=0, end=1000000)
coefficient_input = pn.widgets.FloatInput(name='Coefficient for log utility of housing', value=1, start=0, end=1000000)

consumer_inputs = pn.WidgetBox(
    pn.pane.Markdown("### Consumer"), pop_input, wages_input, marginal_cost_input, fixed_cost_input, 
    job_centralisation_weight_input, coefficient_input)


boundary_rent_input = pn.widgets.FloatInput(name='Land rent at the urban/rural boundary', value=1, start=0, end=1000000)
cost_elasticity_input = pn.widgets.FloatInput(name='Cost elasticity of building height', value=1.6, start=0, end=1000000)
cost_scalar_building_height_input = pn.widgets.FloatInput(
    name='Cost scalar for building height', value=1, start=0, end=1000000)

developer_inputs = pn.WidgetBox(
    pn.pane.Markdown("### Developer"), boundary_rent_input, cost_elasticity_input, cost_scalar_building_height_input
    )

landlords_tax_input = pn.widgets.FloatInput(name='Landlords tax', value=0.33, start=0, end=1000000)
capital_gains_tax_input = pn.widgets.FloatInput(name='Capital gains tax', value=0.15, start=0, end=1000000)
tax_deductibility_input = pn.widgets.FloatInput(name='Tax deductibility', value=0.33, start=0, end=1000000)
local_government_tax_input = pn.widgets.FloatInput(name='Local government tax', value=0.0033, start=0, end=1000000)
maintenance_cost_input = pn.widgets.FloatInput(name='Maintenance cost', value=0.01, start=0, end=1000000)
debt_financing_share_input = pn.widgets.FloatInput(name='Debt financing share', value=0.5, start=0, end=1000000)
general_price_inflation_input = pn.widgets.FloatInput(name='General price inflation', value=0.015, start=0, end=1000000)
house_price_inflation_input = pn.widgets.FloatInput(name='House price inflation', value=0.015, start=0, end=1000000)
interest_rate_input = pn.widgets.FloatInput(name='Interest rate', value=0.045, start=0, end=1000000)
equity_risk_premium_input = pn.widgets.FloatInput(name='Equity risk premium', value=0.03, start=0, end=1000000)

go_button = pn.widgets.Button(
    name='Go', button_type='success', width=100, align=('center', 'center'))

landlord_inputs = pn.WidgetBox(
    pn.pane.Markdown("### Landlords"), landlords_tax_input, capital_gains_tax_input, tax_deductibility_input, 
    local_government_tax_input, maintenance_cost_input, debt_financing_share_input, general_price_inflation_input, 
    house_price_inflation_input, interest_rate_input, equity_risk_premium_input, width = 200)

plot_pane = pn.pane.Matplotlib(tight=True, width = 800)

all_inputs = pn.Row(
    pn.Column(
        pn.Row(
            pn.Column(consumer_inputs, developer_inputs, width=250), landlord_inputs),
        go_button, width = 450), plot_pane).servable(target="simple_app")

d = np.linspace(0, 1.5, 51)

def update(event):
        
    all_quantities, d_, diff_land_rents = closed_competitive(
        beta = debt_financing_share_input.value, i = interest_rate_input.value, 
        f = maintenance_cost_input.value, t_R = local_government_tax_input.value, 
        t_ID = tax_deductibility_input.value, phi = equity_risk_premium_input.value, 
        g = house_price_inflation_input.value, pi = general_price_inflation_input.value, 
        t_CG = capital_gains_tax_input.value, t_I = landlords_tax_input.value,
        theta = job_centralisation_weight_input.value, t = marginal_cost_input.value,
        delta = cost_elasticity_input.value, a = coefficient_input.value, 
        c0 = cost_scalar_building_height_input.value, N = pop_input.value,
        r_ = boundary_rent_input.value, W = wages_input.value, t_ = fixed_cost_input.value, 
        d = d)

    symmetric = symmetric_plot_data(all_quantities)

    fig = plot(symmetric, diff_land_rents, d_)

    plot_pane.object = fig


update(None)

go_button.on_click(update)

