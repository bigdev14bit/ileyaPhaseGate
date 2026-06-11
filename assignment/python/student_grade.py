print("----STUDENTS    GRADER----")
print()

all_student_scores = []
#---------------------------------------------------------------------------------------COLLECTING INPUTS.
teacher_name = input("Enter Your Name(TEACHER): ")
print("SAVING>>>>>>>>>>>>>>>>>>>>>\nSAVED  SUCCESSFULLY.")
print()

students = int(input(f"\"{teacher_name}!\" Enter Number Of Students You Have: "))
print("SAVING>>>>>>>>>>>>>>>>>>>>>\nSAVED  SUCCESSFULLY.")
print()

subjects = int(input(f"\"{teacher_name}!\" Enter Numbers Of Subject For Each Students: "))
print("SAVING>>>>>>>>>>>>>>>>>>>>>\nSAVED  SUCCESSFULLY.")
print()
#----------------------------------------------------------------------------------------COLLECTING INPUTS.

#----------------------------------------------------------------------------------------COLLECTING SCORES FOR EACH SCTUDENTS
for student in range(students):
    print(f"Entering Score For Student {student + 1}")
    print()
    each_student_scores = []

    for subject in range(subjects):
        scores = int(input(f"Enter Score For Subject {subject + 1}: "))
        each_student_scores.append(scores)

    all_student_scores.append(each_student_scores)
    print()
    #print(all_student_scores)
#-----------------------------------------------------------------------------------------COLLECTING SCORES FOR EACH STUDENTS.

#-------------------------------------------HEADER.
print("=" * 80)
header = f"{'STUDENT':<12}"
for things in range(subjects):
    header += f"{'SUB' + str(things + 1):<10}"

header += f"{'TOT':<10}{'AVR':<13}{'POS':<10}"
print(header)
print("=" * 80)
print()
#-------------------------------------------HEADER.

#-------------------------------------------------------ASTERICKS.
#astericks = len(header)

# 3. Print the top borders using our new dynamic length
#print("=" * astericks)
#print(header)
#print("-" * astericks)
#-------------------------------------------------------ASTERICKS.

#-------------------------------------------TOTAL TOTAL.
all_total = []

for index in range(students):
    score = all_student_scores[index]

    total = 0
    for things in score:
        total += things
        #print(total)
    all_total.append(total)
    #print(all_total)
#---------------------------------------------TOTAL TOTAL.

#--------------------------------------------------------------------------------FINAL TABLE.
for ranges in range(students):
    scores = all_student_scores[ranges]
    current_score = all_total[ranges]

    average = current_score / subjects

    position = 1

    highest_point = 0
    for points in all_total:
        if points > current_score:
            highest_point += 1

    positions = position + highest_point
    row = f"STUDENT {ranges + 1:<5}"

    for numbers in scores:
        row += f"{numbers:<10}"
    row += f"{current_score:<10}{average:<10.2f}{positions:<10}"
    print(row)
    #print("=" * 80)
    print(astericks)
#--------------------------------------------------------------------------------FINAL TABLE.
