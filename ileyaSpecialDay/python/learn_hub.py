print("========   LEARN    HUB    ========")
print()

students_data = [] #list to hold all students record
#student_scores = []

numbers_of_student = int(input("Enter Number Of Students Enrolled: "))
numbers_of_quiz = int(input("Enter Number Of Quiz Taken: "))

for students in range(numbers_of_student): #loop through each students to gather there quiz scores
    print()
    print(f"=====   Student {students + 1}    =====")

    student_scores = [] #temporary list to hold score for current student loop
    total_score = 0

    for quiz in range(numbers_of_quiz): #loop to collect individual quiz score
        quiz_input = int(input(f"Score For Quiz {quiz + 1}: "))
        
        student_scores.append(quiz_input)
        total_score += quiz_input

    average_score = total_score / numbers_of_quiz #average score logic

    #structure data to save
    student_records = {
        "name": f"Student {students + 1}",
        "quiz_score": student_scores,
        "average": average_score
        }

    students_data.append(student_records) #save the record dictionary into student data list

print()
print("=====    QUIZ GRADE REPORT    =====")
print()

#creates a string with just word 'STUDENT' and 15 spaces after it
header_details = f"{'STUDENT':<15}"
#loop exactly as many times as the amount of quiz
for quiz_index in range(numbers_of_quiz):
    #this takes current header and add Q1, Q2, Q3........
    header_details += f"{f'Q{quiz_index + 1}':<10}" #nesting f-string, we use single quote

#once all quiz headers are added, glue the final 'AVG' column to the very end.
header_details += f"{'AVG':<10}"

#print the header
print(header_details)

#total width
total_width = 15 + (numbers_of_quiz * 10) + 10
print("-" * total_width)

#loop through 'student scores list to process and print each students data row by row
for students_record in students_data:
    #current row with students name on the far left and 15space
    current_row = f"{students_record['name']:<15}"

    #loop through the current students saved list of scores to add them to the row string
    for score in students_record['quiz_score']:
        #add each individual score to the right side of the row text and 10 spaces
        current_row += f"{score:<10}"

    #add the students final average to the end of the row and rounding up to 2decimal places
    current_row += f"{students_record['average']:<10.2f}"

    print(current_row)
print("-" * total_width)
