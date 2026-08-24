# Write the python program to make an electricity bill generator.

#Input
name = input("Enter Consumer Name:")
id = input("Enter Consumer ID:")
pmr= float(input("Enter Previous Meter Reading(kWh):"))
cmr= float(input("Enter Current Meter Reading(kWh):"))
c = float(input("Enter Cost per unit(Rs.):"))

#Calculation
uc=cmr-pmr
ec=uc*c
ed=5*ec/100
fmc=100
net=ec+ed+fmc

#Display
print("------ Electricity Bill -----")
print("Consumer Name:", name)
print("Consumer ID:", id)
print("Previous Meter Reading:", pmr)
print("Current Meter Reading:", cmr)
print("Units Consumed:", uc)
print("Energy Cost:Rs.", ec)
print("Electricity Duty:Rs.", ed)
print("Fixed Meter Cost:Rs.", fmc)
print("Net Amount:Rs.", net)
print("------------------------------")
