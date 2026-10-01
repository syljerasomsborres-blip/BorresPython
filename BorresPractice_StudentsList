borresstudents = {
    "Ana":85,
    "Ben":90,
    "Carlo":70,
    "Diana":95
}
print("STUDENT GRADES")
print("------------------")
print("Ana:",borresstudents["Ana"])
print("Ben:",borresstudents["Ben"])

#add new student
borresstudents["Ella"]=80

#update a student's grade
borresstudents["Carlo"]=82
borresstudents["Diana"]=91
borresname1 =input("\nEnter student name: ")
borresgrade1 = int(input("Enter grade: "))
borresstudents[borresname1]=borresgrade1
print(borresstudents)
print("\nUpdated Student Grades")
print("-----------------------")
for borresname,borresgrade in borresstudents.items():
    print(borresname, ":", borresgrade)

#search for a student
borressearch = input("\nEnter a student name to search: ")
if borressearch in borresstudents:
    print(borressearch, "has a grade of ", borresstudents[borressearch])
else:
    print("Student not found")
