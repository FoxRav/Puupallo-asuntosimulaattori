# simulaatio.py

import pandas as pd

def annuity_payment(principal, annual_rate, years):
    """
    Annuiteettilainan kuukausierä.
    principal: lainan määrä
    annual_rate: vuosikorko (esim. 0.03 = 3 %)
    years: laina-aika vuosina
    """
    r = annual_rate / 12.0
    n = years * 12
    if r == 0:
        return principal / n
    return principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)


def simulate_detailed(
    years,
    house_price,
    down_payment,
    loan_interest_annual,
    loan_years,
    maintenance_fee,
    house_appreciation_annual,
    rent_initial,
    rent_increase_annual,
    initial_investment,
    stock_return_annual,
    transfer_tax_rate,
    sale_cost_rate,
    property_tax_rate_annual,
    renovation_yearly_eur,
    owner_other_monthly,
    renter_other_monthly,
    allow_negative_saving=False,
):
    """
    Palauttaa pandas.DataFrame-taulukon, jossa on
    kuukausittaiset arvot ja nettovarallisuudet.
    """

    months = years * 12
    loan_amount = house_price - down_payment

    # Kuukausikertoimet
    loan_rate_m = loan_interest_annual / 12.0
    house_app_m = (1 + house_appreciation_annual) ** (1 / 12.0) - 1
    rent_growth_m = (1 + rent_increase_annual) ** (1 / 12.0) - 1
    stock_return_m = (1 + stock_return_annual) ** (1 / 12.0) - 1

    # Lainan vakioerä
    loan_payment_const = annuity_payment(loan_amount, loan_interest_annual, loan_years)

    # Upfront-kustannus omistajalle: varainsiirtovero
    owner_upfront_cost = house_price * transfer_tax_rate

    # Remonttivara kuukausitasolle
    owner_renovation_monthly = renovation_yearly_eur / 12.0

    # Alkutilat
    loan_balance = loan_amount
    house_value = house_price
    rent = rent_initial
    portfolio = initial_investment

    rows = []

    for m in range(1, months + 1):
        # Lainan lyhennys
        if loan_balance > 1e-6:
            interest = loan_balance * loan_rate_m
            principal = loan_payment_const - interest
            if principal > loan_balance:
                principal = loan_balance
            loan_balance -= principal
            loan_payment = interest + principal
        else:
            interest = 0.0
            principal = 0.0
            loan_payment = 0.0

        # Omistajan kulut
        owner_property_tax_monthly = house_value * property_tax_rate_annual / 12.0

        owner_total_monthly_cost = (
            loan_payment
            + maintenance_fee
            + owner_property_tax_monthly
            + owner_renovation_monthly
            + owner_other_monthly
        )

        # Vuokralaisen kulut
        renter_total_monthly_cost = rent + renter_other_monthly

        # Säästö (vuokra + sijoitukset -skenaario)
        raw_saving = owner_total_monthly_cost - renter_total_monthly_cost
        monthly_saving = raw_saving if allow_negative_saving else max(raw_saving, 0.0)

        # Salkku kasvaa
        portfolio = (portfolio + monthly_saving) * (1 + stock_return_m)

        # Päivitä asunto ja vuokra
        house_value *= (1 + house_app_m)
        rent *= (1 + rent_growth_m)

        # Nettovarallisuus
        effective_house_value = house_value * (1 - sale_cost_rate)
        networth_owner = effective_house_value - loan_balance - owner_upfront_cost
        networth_renter = portfolio

        rows.append(
            dict(
                month=m,
                year=m / 12.0,
                loan_balance=loan_balance,
                house_value=house_value,
                rent=rent,
                owner_total_monthly_cost=owner_total_monthly_cost,
                renter_total_monthly_cost=renter_total_monthly_cost,
                monthly_saving_renter=monthly_saving,
                portfolio=portfolio,
                networth_owner=networth_owner,
                networth_renter=networth_renter,
            )
        )

    return pd.DataFrame(rows)

