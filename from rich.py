from rich.console import Console

console = Console()
students = []
def add():
	name = input("Student name: ")
    grade = float(input("Student grade: "))
    students.append({
     "name": name,
      "grade": grade
       })

        console.print(
            "Student added successfully!",
            style="bold green"
        )

def show():
	 if len(students) == 0:
            console.print("No students found!", style="red")
        else:
            console.print("\nStudents List:", style="bold cyan")

            for student in students:
                console.print(
                    f"{student['name']} - {student['grade']}",
                    style="yellow"
                )
                
while True:
    console.print("\nStudent Management System", style="bold blue")
    console.print("1. Add student")
    console.print("2. Show students")
    console.print("3. Calculate average")
    console.print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add()
    elif choice == "2":
    	show()
    elif choice == "3":
        if len(students) == 0:
            console.print("No grades available!", style="red")
        else:
            total = 0

            for student in students:
                total += student["grade"]

            average = total / len(students)

            console.print(
                f"Average grade: {average:.2f}",
                style="bold green"
            )

    elif choice == "4":
        console.print("Goodbye!", style="bold blue")
        break

    else:
        console.print("Invalid option!", style="bold red")