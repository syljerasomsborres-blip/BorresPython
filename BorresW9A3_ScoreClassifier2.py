print("   BORRES SCORE CLASSIFIER  ")
print(" ")
print("=== GRADE CLASSIFICATION ===")
print("   4.0           96-100     ")
print("   3.5           90-95      ")
print("   3.0           84-89      ")
print("   2.5           78-83      ")
print("   2.0           72-77      ")
print("   1.5           66-71      ")
print("   1.0           60-65      ")
print("    R           below 60    ")
print("============================")
print(" ")

#variables
borres_a = str("96-100")
borres_b = str("90-95")
borres_c= str("84-89")
borres_d= str("78-83")
borres_e= str("72-77")
borres_f= str("66-71")
borres_g= str("60-65")

#input
borres_name = str(input("Name: "))
borres_grade = float(input("Grade: "))

#process
match borres_grade:
    case 4.0:
        print(f'Equivalent: {borres_a}')

    case 3.5:
        print(f'Equivalent: {borres_b}')

    case 3.0:
        print(f'Equivalent: {borres_c}')

    case 2.5:
        print(f'Equivalent: {borres_d}')

    case 2.0:
        print(f'Equivalent: {borres_e}')

    case 1.5:
        print(f'Equivalent: {borres_f}')

    case 1.0:
        print(f'Equivalent: {borres_g}')

    case _:
        print("Not in Range")
