print("DIABETIC PATIENTS LIST")
print("------------------------")

borrespatients = {"Rhea":(96,120,105), "Ana":(70,180,100)}
borresnormal= 120
for borrespname, borressugar in borrespatients.items():
    if(borrespname=="Rhea"):
        print("Name: Rhea")
        print("BLOOD SUGAR SUMMARY:")
        for borresvalue in borressugar:
            if borresvalue<borresnormal:
                print(borresvalue,"not Normal")
            else:
                print(borresvalue,"Normal")

    if (borrespname == "Ana"):
        print("\nName: Ana")
        print("BLOOD SUGAR SUMMARY:")
        for borresvalue in borressugar:
            if borresvalue < borresnormal:
                print(borresvalue, "not Normal")
            else:
                print(borresvalue, "Normal")

    borreshighest = max(borressugar)
    print("\nHighest Blood Sugar: ", borreshighest)
    borreslowest=min(borressugar)
    print("Lowest Blood Sugar: ", borreslowest)
    borresdiff= borreshighest-borreslowest
    print("Difference: ", borresdiff)
    borresaverage = sum(borressugar)/len(borressugar)
    print("Average: ",f"{borresaverage:.2f}")
    def sort(borressugar):
        borressorted_values = sorted(borressugar)
        print("Sugar List (Lowest-Highest):",borressorted_values)
    sort(borressugar)
