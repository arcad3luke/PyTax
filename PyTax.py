import time
import math

class PyPay:
    run_before = False
    
    def tax_rate(self):
        gross_income = input("How much was your gross pay?\n")
        def calculate_average(lower_limit, upper_limit):
            self.average = (lower_limit + upper_limit) / 2
            return average

        state_abbr_and_tax_rates = {
            'AL': range(calculate_average(.02, .05), 3 * 100),
            'AK': range(calculate_average(1, 1) * 100),
            'AZ': range(calculate_average(0.25, 0.25), 1 * 100),
            'AR': range(calculate_average(0, 0.047), 5 * 100),
            'CO': range(calculate_average(.044, 0.044), 1 * 100),
            'CA': range(calculate_average(.01, .123), 9 * 100),
            'CT': range(calculate_average(.03, .0699), 7 * 100),
            'DE': range(calculate_average(0, .066) * 100)   ,
            'DC': range(calculate_average(0.04, .1075), 7 * 100),
            'GA': range(calculate_average(.01,.0575), 6 * 100),
            'FL': range(calculate_average(1,1), 1 * 100),
            'HI': range(calculate_average(0.014,.11), 12 * 100),
            'ID': range(calculate_average(.058,.058), 1 * 100),
            'IL': range(calculate_average(.0495,.0495), 1 * 100),
            'IN': range(calculate_average(.0315,.0315), 1 * 100),
            'IA': range(calculate_average(.044,.06), 4 * 100),
            'KS': range(calculate_average(,),  * 100),
            'KY': range(calculate_average(,),  * 100),
            'LA': range(calculate_average(,),  * 100),
            'ME': range(calculate_average(,),  * 100),
            'MD': range(calculate_average(,),  * 100),
            'MA': range(calculate_average(,),  * 100),
            'MI': range(calculate_average(,),  * 100),
            'MN': range(calculate_average(,),  * 100),
            'MS': range(calculate_average(,),  * 100),
            'MO': range(calculate_average(,),  * 100),
            'MT': range(calculate_average(,),  * 100),
            'NE': range(calculate_average(,),  * 100),
            'NV': range(calculate_average(,),  * 100),
            'NH': range(calculate_average(,),  * 100),
            'NJ': range(calculate_average(,),  * 100),
            'NM': range(calculate_average(,),  * 100),
            'NY': range(calculate_average(,),  * 100),
            'NC': range(calculate_average(,),  * 100),
            'ND': range(calculate_average(,),  * 100),
            'OH': range(calculate_average(,),  * 100),
            'OK': range(calculate_average(,),  * 100),
            'OR': range(calculate_average(,),  * 100),
            'PA': range(calculate_average(,),  * 100),
            'RI': range(calculate_average(,),  * 100),
            'SC': range(calculate_average(,),  * 100),
            'SD': range(calculate_average(,),  * 100),
            'TN': range(calculate_average(,),  * 100),
            'TX': range(calculate_average(,),  * 100),
            'UT': range(calculate_average(,),  * 100),
            'VT': range(calculate_average(,),  * 100),
            'VA': range(calculate_average(,),  * 100),
            'WA': range(calculate_average(,),  * 100),
            'WV': range(calculate_average(,),  * 100),
            'WI': range(calculate_average(,),  * 100),
            'WY': range(calculate_average(,),  * 100)
        }

        for state in state_abbr_and_tax_rates:
            tax_bracket = { # as of 8/2/2023 via https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
                state : (0,  )
            }

        for lower, upper in state_abbr_and_tax_rates:
            average = calculate_average(lower, upper)
            print(f'Average for bracket {lower}-{upper}: {average}')
        
    def calculator():
        
        # Define constants for tax rates
        FEDERAL_TAX_RATE = 0.15  # Federal income tax rate (example rate)
        STATE_TAX_RATE = 0.05    # State income tax rate (example rate)
        SOCIAL_SECURITY_RATE = 0.062   # Social Security tax rate (6.2%)
        MEDICARE_RATE = 0.0145         # Medicare tax rate (1.45%)
        FEDERAL_STANDARD_DEDUCTION = 12550  # Federal standard deduction for 2021 (example)

        # Input employee details
        employee_name = input("Enter employee name: ")
        employee_salary = float(input("Enter employee salary: "))
        state = input("Enter state of residence: ")

        # Calculate federal income tax
        taxable_income = max(employee_salary - FEDERAL_STANDARD_DEDUCTION, 0)
        federal_income_tax = taxable_income * FEDERAL_TAX_RATE

        # Calculate state income tax (example: flat rate)
        state_income_tax = employee_salary * STATE_TAX_RATE

        # Calculate Social Security and Medicare taxes
        social_security_tax = employee_salary * SOCIAL_SECURITY_RATE
        medicare_tax = employee_salary * MEDICARE_RATE

        # Calculate total payroll tax
        total_payroll_tax = federal_income_tax + state_income_tax + social_security_tax + medicare_tax

        # Display results
        print("\nPayroll Tax Calculation for Employee:", employee_name)
        print("=======================================")
        print(f"Employee Salary: ${employee_salary:.2f}")
        print(f"Federal Income Tax: ${federal_income_tax:.2f}")
        print(f"State Income Tax: ${state_income_tax:.2f}")
        print(f"Social Security Tax: ${social_security_tax:.2f}")
        print(f"Medicare Tax: ${medicare_tax:.2f}")
        print(f"Total Payroll Tax: ${total_payroll_tax:.2f}")

        
    if run_before == True and not False:
        rerun = input('''It seems you've run this before, would you like to start again and use the same tax rate(s), or use new numbers?\n
                        (SAME or NEW)''')
        if rerun.upper == 'SAME':
            calculator.same()
        elif rerun.upper == 'NEW':
            calculator.new()

if __name__ == '__main__':
    PyPay.calculator()