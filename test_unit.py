import pytest
import fedtaxcalc


@pytest.mark.parametrize("filing_status, taxable_income, expected",
                         [('single', 45000, 5690),
                          ('single', 100000, 18079.5),
                          ('single', 0, 0),
                          ('single', 100000000, 36964427),
                          ('married', 10000, 1000),
                          ('married', 600000, 159590),
                          ('married', 0, 0),
                          ('married', 100000000, 36937149)])
def test_calc_fex_tax(filing_status, taxable_income, expected):
    assert fedtaxcalc.calc_fed_tax(filing_status, taxable_income) == expected


@pytest.mark.parametrize("taxable_income, fed_tax_yr, expected",
                         [(45000, 5690, 3275.8333333333335),
                          (100000, 18079.5, 6826.708333333333),
                          (0, 0, 0),
                          (100000000, 36964427, 5252964.416666667),
                          (10000, 1000, 750),
                          (600000, 159590, 36700.833333333336),
                          (0, 0, 0),
                          (100000000, 36937149, 5255237.583333333)])
def test_net_income_func(taxable_income, fed_tax_yr, expected):
    assert  fedtaxcalc.net_income_func(taxable_income, fed_tax_yr) == expected

