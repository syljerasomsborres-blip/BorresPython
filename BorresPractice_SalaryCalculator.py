print("========== SALARY CALCULATOR ============")
borresnohour=float(input("Enter Hours: "))
borreschoice=int(input("1] Janitor 2] Clerk 3] Cashier 4] Manager \nChoice: "))
borresposition=""
borressalary=0
if borreschoice==1:
    borresposition= "Janitor"
    borressalary=1000
elif borreschoice==2:
    borresposition="Clerk"
    borressalary=2000
elif borreschoice==3:
    borresposition="Cashier"
    borressalary=24000
elif borreschoice==4:
    borresposition="Manager"
    borressalary=40000
else:
    print("Invalid")

borreshalfmonth=borressalary/2
borresrateperhour=borreshalfmonth/48
borresabsenceded=0
borresnetsalary=0
if borresnohour>=48:
    borresextrahours=borresnohour-48
    borresotrate=borresrateperhour*1.25
    borresovertimepay=borresotrate*borresextrahours
    borresnetsalary=borreshalfmonth+borresovertimepay
    print("Overtime Pay: " ,borresovertimepay)

elif borresnohour<48:
    borresabsence=48-borresnohour
    borrresabsenceded=borresrateperhour*1.10*borresabsence
    borresnetsalary=borreshalfmonth-borresabsenceded
    print(f"Absence Deduction: {borresabsenceded:,.2f}")
else:
    print("Invalid")
print(f"Net Salary: {borresnetsalary:,.2f}")
print("Position:" ,borresposition)
