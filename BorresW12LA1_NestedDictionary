print("------ EMPLOYEE LIST ------\n")

borressalary = {"E601" : {
                    "Employee Name": "Leona Syljera",
                    "Daily Hours": [8,9,10,9,8]
},
                "E602" : {
                    "Employee Name": "Riyana Ziella",
                    "Daily Hours": [9,7,8,9,9]
                }
}

borresEmpInfo = ""
borresOT = 0
borresWeeklyBasic = 9000
borresRateperHour = borresWeeklyBasic/40

for borresEmpID, borresEmpInfo in borressalary.items():
    print(f"ID: {borresEmpID} | Name: {borresEmpInfo['Employee Name']}")
    print()

borressearch = input("Enter Employee ID: ").upper()
print("Running Employee ID match for: ", borressearch)

borresfound = False

for borresEmpID, borresEmpInfo in borressalary.items():
    if borressearch == borresEmpID:
        print(f"Name: {borresEmpInfo['Employee Name']}"
              f"\nDuty Hours: {', '.join(map(str, borresEmpInfo['Daily Hours']))}")
        borresfound = True

        borresOT = 0
        for hours in borresEmpInfo['Daily Hours']:
            if hours > 8:
                borresOT += (hours - 8) * (1.5 * borresRateperHour)
                print(f"\nExcess Hours: {(hours - 8)}"
                      f"\nRate per Hour: {borresRateperHour}")

        borresGrossPay = (40 * borresRateperHour) + borresOT
        print(f"\nTotal Overtime Pay: {borresOT:,.2f}"
              f"\nWeekly Basic: {borresWeeklyBasic}"
              f"\nGross Pay: {borresGrossPay:,.2f}")

    if not borresfound:
        print("Invalid Employee ID.")
