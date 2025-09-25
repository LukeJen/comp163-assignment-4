student_name = "Luke Jensen"
current_gpa = 3.9
study_hours = 5
social_points = 25
stress_level = 25

print("Welcome, these are your Starting Stats", student_name, study_hours, social_points, stress_level)

if choice == "A": 
    if current_gpa >= 3.5:
        study_hours = study_hours - 6
        stress_level = stress_level - 30
    elif (current_gpa <= 3.4) and (current_gpa > 2.5):
        study_hours - 3
        stress_level - 20
    elif current_gpa < 2.4:
        print("Harder Path Recommened")
elif choice == "B": 
    if current_gpa >= 3.5: 
        study_hours = study_hours - 4
        stress_level = stress_level - 20
    elif (current_gpa <= 3.4) and (current_gpa > 2.5):
        study_hours = study_hours - 2
        stress_level = stress_level - 10
    elif current_gpa < 2.4:
        study_hours = study_hours + 1
        stress_level = stress_level - 5
elif choice == "C": 
    if current_gpa >= 3.5:
        study_hours = study_hours + 8
        stress_level = stress_level + 5
    elif (current_gpa <= 3.4) and (current_gpa > 2.5):
        study_hours = study_hours + 4
        stress_level = stress_level + 10
    elif current_gpa < 2.4:
        study_hours = study_hours + 10
        stress_level = stress_level + 20
else: 
    print("Invalid")
