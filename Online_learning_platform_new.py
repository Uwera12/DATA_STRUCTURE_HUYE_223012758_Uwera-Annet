from collections import deque


enrollment_stack = []

available_lessons = {   
                      'Data base' : {'course_name': 'Data base', 'students': []},
                      'Web designing' : {'course_name': 'Web designing', 'students': []},
                      'Web development' : {'course_name': 'Web development', 'students': []},
                    }

lesson_queue = deque()

def display_lesson():
    if available_lessons:
        print("Available lessons:")
        for lesson in available_lessons:
            print(f"- {lesson}")
    else:
        print("No lessons available.")

def display_student_course(course):
    if course in available_lessons:
        students = available_lessons[course]['students']
        if students:
            print(f"Students in {course}:")
            for student in students:
                print(f"- {student}")
        else:
            print(f"No students enrolled in {course}.")
    else:
        print(f"Course '{course}' not available.")


def add_lesson(lesson):
    if lesson not in available_lessons:
        available_lessons[lesson] = {'course_name': lesson, 'students': []}
        print(f"Added lesson: {lesson}")
    else:
        print(f"Lesson '{lesson}' already exists.")

def remove_lesson(lesson):
    if lesson in available_lessons:
        del available_lessons[lesson]
        print(f"Removed lesson: {lesson}")
    else:
        print(f"Lesson '{lesson}' is unavailable.")

def lesson_request(student_name):
    lesson_queue.append(student_name)
    print(f"{student_name} requested lesson.")

def process_lesson(lesson):
    if lesson_queue:
        student_name = lesson_queue.popleft()
        enroll(lesson, student_name)
    else:
        print("No student requested a lesson ")

def enroll(course, student_name):
    if course in available_lessons:
        enrollment_stack.append((course, student_name))
        available_lessons[course]['students'].append(student_name)
        print(f"{student_name} is enrolled in: {course}")
    else:
        print(f"Course '{course}' is not available.")

def undo_enrollment():
    if enrollment_stack:
        course, student_name = enrollment_stack.pop()
        available_lessons[course]['students'].remove(student_name)
        print(f"Undid enrollment of {student_name} from {course}")
    else:
        print("No enrollment to undo.")


def main():
    while True:
        print("\nMenu: ")
        print("1. Display available lessons")
        print("2. Display students in courses")
        print("3. Add a lesson")
        print("4. Remove a lesson")
        print("5. Request a lesson")
        print("6. Process a lesson")
        print("7. Enroll in a course")
        print("8. Undo enrollment")
        print("9. Exit")

        choice = input("Choose an option: ")


        if choice == '1':
           display_lesson()

        elif choice == '2':
            course_name = input("Enter course name: ")
            display_student_course(course_name)

        elif choice == '3':
            lesson = input("Enter lesson name to add: ")
            add_lesson(lesson)

        elif choice == '4':
            lesson = input("Enter lesson name to remove: ")
            remove_lesson(lesson)

        elif choice == '5':
            student_name = input("Enter Student name to request a lesson: ")
            lesson_request(student_name)

        elif choice == '6':
            lesson = input("Enter lesson name to be processed: ")
            process_lesson(lesson)
        elif choice == '7':
            course = input("Enter course name to enroll: ")
            student_name = input("Enter student name: ")
            enroll(course, student_name)

        elif choice == '8':
            undo_enrollment()

        elif choice == '9':
            print(" exit see you!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()









