from bisect import bisect

net_income_mo = 0


def get_income():
    """Establish user's Taxable Income for tax expense estimation.

    Input: Users adjusted gross income (AGI) entered as a whole number.

    Note: Error handles any non-int and requests input again. Prints message
        and loops input again if non-int submitted.

    Returns: taxable_income (int)
    """
    while True:
        try:
            taxable_income = int(input(
                "Enter your Taxable Income as a whole number: "
            ))
            taxable_income = int(taxable_income)
            break
        except ValueError:
            print("Not a valid integer! Please try again ...")
    return taxable_income


def print_data(taxable_income, filing_status, fed_tax_yr):
    """Prints to user Taxable Income, Filing Status, estimated Federal Tax.

    Args:
        taxable_income (int), User input adjusted gross income (AGI)
        filing_status (str), User input 'single' or 'married'
        fed_tax_yr (int), Estimated federal tax calculation
    """
    print(f"Annual Gross Income: $ {taxable_income:.2f}"
          f"\nFiling status: {filing_status.title()}"
          f"\n__________ "
          f"\n\nYour estimated federal income taxes are $ {fed_tax_yr:.2f}")


def get_filing_status():
    """Establish user's Filing Status for correct tax bracket.

    Input: User enters filing status when prompted. Whole word required.

    Note: Error handles anything not 'single'/'married'; prints message
        and loops input again if not 'single'/'married'.

    Returns: filing_status.casefold() (str), 'single'/'married' in lowercase.
    """

    filing_status = ""
    while filing_status.casefold() not in ['single', 'married']:
        filing_status = input(
            "What is your filing status? "
            "\nEnter 'single' or 'married': ")
    return filing_status.casefold()


def calc_fed_tax(filing_status, taxable_income):
    """Provides calculated estimate of federal taxes based off of the 2020
    tax brackets and the filing statuses 'single' and 'married'.

    Args:
        filing_status (str), User input 'single' or 'married'.
        taxable_income (int), User input adjusted gross income (AGI).

    Attributes:
        rates (list): 2020 tax bracket rates.
        brackets (list): 2020 AGI numbers for 'married' and 'single' statuses.
        base_tax (list): Tax for the full amount of each tax brackets' AGI
        i (int): Index value for the bisection insertion point.
        rate (flt): Identified tax rate for the calculation.
        bracket (int/flt): Most immediate fully taxed bracket before the
            bracket where user's AGI lands (active bracket).
        income_in_bracket (int/flt): Total income in the user's active bracket.
        tax_in_bracket (flt): Total estimated tax in user's active bracket.
        fed_tax_yr (flt): Total estimated tax of all brackets.


    Returns: fed_tax_yr, Estimated federal tax on Taxable Income based on
        filing status.
    """
    rates = [.10, .12, .22, .24, .32, .35, .37]  # 2020 USA Tax Rates

    if filing_status == "married":
        brackets = [19750, 80250, 171050, 326600, 414700, 622050]
        base_tax = [1975, 9235, 29211, 66543, 94735, 167307.50]

    elif filing_status == "single":
        brackets = [9875, 40125, 85525, 163300, 207350, 518400]
        base_tax = [987.50, 4617.50, 14605.50, 33271.50, 47367.50, 156235]

    # else is unnecessary but remains for above if/elif readability
    else:
        print("Unknown filing status.")
        return 0

    i = bisect(brackets, taxable_income)
    # if in first tax bracket ONLY
    if i == 0:
        fed_tax_yr = taxable_income * rates[0]
        return fed_tax_yr
    # if in any other tax bracket
    rate = rates[i]
    bracket = brackets[i - 1]
    income_in_bracket = taxable_income - bracket
    tax_in_bracket = income_in_bracket * rate
    fed_tax_yr = base_tax[i - 1] + tax_in_bracket
    return fed_tax_yr


def print_net_income_mo(net_income_mo):
    """Prints Yearly Net Income and Monthly Net Income to user.

    Args: net_income_mo, returned from net_income_func(taxable_income,
        fed_tax_yr); estimated net income after federal taxes.
    """
    print(f"Your yearly net income is $ {(net_income_mo * 12):.2f}")
    print(f"Your monthly net income is $ {net_income_mo:.2f}")


def net_income_func(taxable_income, fed_tax_yr):
    """Takes income before tax and subtracts estimated federal taxes.

    Args: Taxable income input and federal taxes calculation.
        taxable_income (int), User input adjusted gross income (AGI).
        fed_tax_yr (flt), estimated federal taxes based off 2020 tax brackets.

    Returns: net_income_mo, monthly net income after estimated federal taxes.
    """
    net_income_mo = (taxable_income - fed_tax_yr) / 12
    return net_income_mo


def tax_calc():
    """Invokes functions above; runs program."""
    taxable_income = get_income()
    filing_status = get_filing_status()
    fed_tax_yr = calc_fed_tax(filing_status, taxable_income)
    net_income_mo = net_income_func(taxable_income, fed_tax_yr)
    print_data(taxable_income, filing_status, fed_tax_yr)
    print_net_income_mo(net_income_mo)

# tax_calc()
