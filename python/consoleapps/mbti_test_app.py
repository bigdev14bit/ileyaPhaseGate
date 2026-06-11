print("Welcome to MBIT TEST!!!")
print()

mbti_questions = [{1: "expend energy, enjoy groups", "conserve energy, enjoy one-on-one"}, {2: "inteprete literally", "look for meaning and possibility"},
                  {3: "logical, thinking, questioning", "empathetic, feeling, accomodating"}, {4: "organized, orderly", "flexible, adaptable"},
                  {5: "more outgoing, think out loud", "more reserved, think to yourself"}, {6: "practical, realistic, experiential", "imaginative, innovative, theoritical"},
                  {7: "candid, straightforward, frank", "tactful, kind, encouraging"}, {8: "plan, schedule", "unplanned, spontaneous"},
                  {9: "seek many tasks, public activities, interactions with others", "seek private, solitary activities with quiet to concentrate"}, {10: "standard, usual, conventional", "differential, novel, unique"},
                  {11: "firm, tend to critisize, hold the line", "gentle, tend to appreciate, concilitate"}, {12: "regulated, structured", "easy-going,live and lets live"},
                  {13: "external, communitative, express yourself", "internal reticent, keep to yourself"}, {14: "focus on here-and-now", "look to the future, global perspetive, big picture"},
                  {15: "tough-minded, just", "tender-hearted, mercyful"}, {16: "preparation, plan ahead", "go with the flow, adapt as-you-go"},
                  {17: "active, initiate", "reflective, deliberate"}, {18: "facts, things, what is", "ideas, dreams, what could be, philosophical"},
                  {19: "matter of fact, issue-oriented", "sensitive, people-oriented, compassionate"}, {20: "control, govern", "latitude, freedom"}
                  ]
a_count = 0
b_count = 0

name = input("What is your name?: ")
for questions in mbti_questions:
    print(questions)
