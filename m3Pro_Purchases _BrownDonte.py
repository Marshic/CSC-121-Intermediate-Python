# This program calculates tuition for students
# 1/27/24
# CSC-121 m3Pro - Purchases
# Donte' Brown
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer System Foundations)", "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]
tuition = [460, 520.98, 500, 783.88]

def course_display():
# Displays course name and tuition
    print("Course Name                Tuition")
    print("-" * 50)
    for i in range(len(tuition)):
        print(f"{courses[i]:<42} ${tuition[i]:.2f}")
    print("-" * 50)

def calc_all_tuit():
    # Make a dictionaty for displaying
    stu_totals = {}
    print("Stu Name" + " " + "Tuition")
    print("-" * 50)
    for student in stu_names:
        total_cost = 0
        for i in range(len(courses)):
            print(f"Is {student} taking {courses[i]}?")
            choice = input("Enter y for yes (y/n): ")
            if choice == 'y':
                total_cost += tuition[i]
        stu_totals[student] = total_cost
    print("Stu Name                Tuition")
    print("-" * 35)
    for student, total in stu_totals.items():
        print(f"{student:<20} ${total:.2f}")


def calc_spec_tuit():
    print("Students:")
    for i in range(len(stu_names)):
        print(f"{i+1}) {stu_names[i]}")

    choice = int(input("Choose a student: "))
    student = stu_names[choice-1]
    total_cost = 0
    # I Had to use {course_taken} because {choice} was taken
    for i in range(len(courses)):
        course_taken = input(f"Is {student} taking {courses[i]}? (y/n): ")
        if course_taken == 'y':
            total_cost += tuition[i]
    print()
    print("Student Tuition Summary")
    print("Stu Name                Tuition")
    print("-" * 35)
    print(f"{student:<20} ${total_cost:.2f}")
    
    print(f"Total tuition for {student}: ${total_cost:.2f}")
def menu_display():
    while True:
        print("-" * 20 + "Menu" + "-" * 20)
        print("1) Calculate Tuition for ALL Students")
        print("2) Calculate Tuition For Specific Students")
        print("3) Exit")
        print("-"*30)

        choice = input("Enter your choice: ")

        if choice == '1':
            calc_all_tuit()
        elif choice == '2':
            calc_spec_tuit()
        elif choice == '3':
            print("Program Terminated")
            return
        else:
            print("That's not a valid number. Re-enter please..")



def main():
    course_display()
    menu_display()



if __name__ == "__main__":
    main()