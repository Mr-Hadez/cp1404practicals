"""
CP1404
Created an electric bill estimator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
kwh_daily_use = float(input("Enter daily use in kWh: "))
billing_days = float(input("Enter number of billing days: "))
est_bill = tariff * kwh_daily_use * billing_days
print(f"Estimated bill: ${est_bill:.2f}")
