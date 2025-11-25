#Day2 Project on calculator
print("Welcome to the tip calculator!")
bill=float(input("what was the total bill? $ "))
tip=int(input("what % tip would you like to give ? 10 12 15"))
people=int(input("How many people to split the bill"))
bill_with_tip=bill + bill * (tip/100)
print(bill_with_tip)

#Flight ticket calculator
print("Welcome to flight calculator")
flight_bill=int(input("Enter Ticket price"))
flight_offer=int(input("Enter the % off"))
flight_pricer_after_off=flight_bill - flight_bill (flight_offer/100)
print(flight_pricer_after_off)