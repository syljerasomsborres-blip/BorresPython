print("   BORRES SCORE CLASSIFIER  ")
print(" ")
print("======== COLOR CODE ========")
print(" 97%-100%     Dark Green    ")
print(" 90%-96%      Light Green   ")
print(" 80%-89%      Yellow Green  ")
print(" 70%-79%      Yellow        ")
print(" 60%-69%      Orange        ")
print(" 59% below    Red           ")
print("============================")
print(" ")

#variables
borres_a = str("Dark Green")
borres_b = str("Light Green")
borres_c= str("Yellow Green")
borres_d= str("Yellow")
borres_e= str("Orange")
borres_f= str("Red")

#input
borres_name = str(input("Name: "))
borres_items = float(input("Total Items: "))
borres_score = float(input("Score: "))

#process
borres_percentage = (borres_score/borres_items) * 100
print(f'Score Percentage: {borres_percentage: .2f}')

if borres_percentage >= 97 and borres_percentage <= 100:
    print(f'Color: {borres_a}' )
    print("Remarks: Passed")

elif borres_percentage >= 90 and borres_percentage <= 96:
    print(f'Color: {borres_b}')
    print("Remarks: Passed")

elif borres_percentage >= 80 and borres_percentage <= 89:
    print(f'Color: {borres_c}')
    print("Remarks: Passed")

elif borres_percentage >= 70 and borres_percentage <= 79:
    print(f'Color: {borres_d}')
    print("Remarks: Passed")

elif borres_percentage >= 60 and borres_percentage <= 69:
    print(f'Color: {borres_e}')
    print("Remarks: Passed")

elif borres_percentage <= 59:
    print(f'Color: {borres_f}')
    print("Remarks: Failed")

else:
    print("Invalid")
