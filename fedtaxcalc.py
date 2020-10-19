from bisect import bisect

net_income_mo = 0


def get_income():
    """Establish user's Taxable Income for tax expense estimation.
    Input user's estimated Taxable Income.
        Returns: Taxable Income amount as an integer.  Handles non-int errors.
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
    """Prints to user Taxable Income, Filing Status, estimated Federal Tax."""
    print(f"Annual Gross Income: $ {taxable_income:.2f}"
          f"\nFiling status: {filing_status.title()}"
          f"\n__________ "
          f"\n\nYour estimated federal income taxes are $ {fed_tax_yr:.2f}")


def get_filing_status():
    """Establish user's Filing Status for correct tax bracket.
    Input 'single' or 'married' when prompted.
        Returns: Filing Status.  Handles errors if incorrect input entered.
    """

    filing_status = ""
    while filing_status.casefold() not in ['single', 'married']:
        filing_status = input(
            "What is your filing status? "
            "\nEnter 'single' or 'married': ")
    return filing_status.casefold()


def calc_fed_tax(filing_status, taxable_income):
    """Income tax calculation (2020) for filing status: married or single.
    Input Taxable Income as an integer and insert Filing Status.
        Returns: Estimated tax on Taxable Income based on Filing Status.
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
    """Prints Yearly Net Income and Monthly Net Income to user."""
    print(f"Your yearly net income is $ {(net_income_mo * 12):.2f}")
    print(f"Your monthly net income is $ {net_income_mo:.2f}")


def net_income_func(taxable_income, fed_tax_yr):
    """Takes income before tax and subtracts estimated federal taxes.
    Input: Taxable income input and federal taxes calculation.
        Returns: Monthly net income.
    """
    net_income_mo = (taxable_income - fed_tax_yr) / 12
    return net_income_mo

def tax_calc():
    """Invokes functions above."""
    taxable_income = get_income()
    filing_status = get_filing_status()
    fed_tax_yr = calc_fed_tax(filing_status, taxable_income)
    net_income_mo = net_income_func(taxable_income, fed_tax_yr)
    print_data(taxable_income, filing_status, fed_tax_yr)
    print_net_income_mo(net_income_mo)

# tax_calc()