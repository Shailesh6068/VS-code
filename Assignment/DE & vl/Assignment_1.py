student_scores = {}

def add_student(name,score):
    """Add a new student with their score."""
    if name in student_scores:
        print(f"Stuednt{name} already exists.Use update_score to update their score.")
    else:
        student_scores[name] = score
        print(f"Added stuednt {name} with score{score}.") 
        
def update_score(name,score):
    "Update the score for an existing student"
    if name in student_scores:
        student_scores[name] = score
        print(f"Updated {name}'s score to {score}.")
    else:
        print(f"Student {name} does not exist.Use add_student to add them first.")
        
def delete_student(name):
    """Delete the student from dictionary"""
    if name in student_scores:
        #del student_scores[name]
        student_scores.pop(name)
        print(f"Deleted student {name}.")
    else:
        print(f"Student {name} does not exist.")

def find_highest_score():
    """Find the student with highest score"""
    if not student_scores:
        print("No student in the record.")
        return None
    
    highest_score_student = max(student_scores , key = student_scores.get)
    highest_score = student_scores[highest_score_student]
    print(f"Student with highest score is {highest_score_student} with a score of {highest_score}.")
    return highest_score_student,highest_score

#example usage
add_student("Alice",85)
add_student("Bob",92)
update_score("Alice",88)
delete_student("Bob")
find_highest_score()