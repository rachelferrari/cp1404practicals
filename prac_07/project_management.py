"""Project Management Program
Estimated: 2 hr
Actual: 5 hr 30 min
"""
from project import Project
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Show choices for the project management software"""
    projects = []
    texts = []
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            header = load_project(texts, projects)
        elif choice == 'S':
            save_file(header, texts)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects(projects, texts)
        elif choice == 'A':
            add_project(projects, texts)
        elif choice == 'U':
            update_project(projects, texts)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input('>>> ').upper()
    print("Thank you for using custom-built project management software.")


def update_project(projects, texts):
    """Update project details"""
    count = 0
    for line in projects:
        print(f"{count} {line}")
        count += 1
    is_valid_input = False
    while not is_valid_input:
        try:
            project_choice = int(input("Project choice: "))
            if project_choice < 0:
                print(f"Pick between 0-{len(projects) - 1}")
            else:
                is_valid_input = True
                print(projects[project_choice])
                try:
                    new_percentage = float(input("New percentage: "))
                    projects[project_choice].change_completion(new_percentage)
                    if new_percentage is not None:
                        texts[project_choice][4] = new_percentage
                    new_priority = int(input("New priority: "))
                    if new_priority is not None:
                        texts[project_choice][2] = new_priority
                except ValueError:
                    pass
        except ValueError:
            print("Invalid input")


def add_project(projects, texts):
    """Add new project into the program"""
    print("Let's add a new project")
    name = get_valid_input("Name: ")
    correct_date = False
    while not correct_date:
        try:
            date_string = get_valid_input("Date (d/m/yyyy): ")
            datetime.datetime.strptime(date_string, "%d/%m/%Y")
        except ValueError:
            print("Incorrect date format")
        else:
            correct_date = True
            is_valid_input = False
            while not is_valid_input:
                try:
                    priority = int(get_valid_input("Priority: "))
                    while priority <= 0:
                        print("Enter 1 or more")
                        priority = int(get_valid_input("Priority: "))
                    cost = float(get_valid_input("Cost estimate: $"))
                    while cost < 0:
                        print("Enter 0 or more")
                        cost = float(get_valid_input("Cost estimate: $"))
                    completion = int(get_valid_input("Percent complete: "))
                    while 0 < completion > 100:
                        print("Enter 0 to 100")
                        completion = int(get_valid_input("Percent complete: "))
                    else:
                        is_valid_input = True
                        parts = [name, date_string, priority, cost, completion]
                        texts.append(parts)
                        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                        projects.append(project)
                except ValueError:
                    print("Invalid input")


def get_valid_input(prompt):
    """Get valid input"""
    variable = input(prompt)
    while variable == '' or variable.isspace():
        print("Input cannot be empty")
        variable = input(prompt)
    return variable


def filter_projects(projects, texts):
    """Show projects after date"""
    # filter_date = get_valid_input("Show projects that start after date (dd/mm/yy): ")
    correct_date = False
    while not correct_date:
        try:
            filter_date = get_valid_input("Show projects that start after date (dd/mm/yy): ")
            datetime.datetime.strptime(filter_date, "%d/%m/%Y")
        except ValueError:
            print("Incorrect date format")
        else:
            correct_date = True
            filtered_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
            projects.sort()
            for i in range(len(projects)):
                start_date = datetime.datetime.strptime(texts[i][1], "%d/%m/%Y").date()
                if filtered_date >= start_date:
                    print(projects[i])


def save_file(header, texts):
    """Save file"""
    with open("projected.txt", 'w') as out_file:
        out_file.write(header)
        for i in range(len(texts)):
            texts[i][2] = str(texts[i][2])
            texts[i][3] = str(texts[i][3])
            texts[i][4] = str(texts[i][4])
        for parts in texts:
            out_file.writelines('\t'.join(parts))
            out_file.write('\n')


def load_project(texts, projects):
    """Load file"""
    with open("projects.txt") as in_file:
        header = next(in_file)
        for part in in_file:
            parts = part.split()
            parts[:-4] = [' '.join(parts[:-4])]
            texts.append(parts)
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)

    for i in range(len(texts)):
        texts[i][2] = int(texts[i][2])
        texts[i][3] = float(texts[i][3])
        texts[i][4] = int(texts[i][4])

    return header


def display_projects(projects):
    """Display and separate projects into incomplete projects and complete projects"""
    print("Incomplete projects:")
    for part in projects:
        if Project.is_not_complete(part):
            print(f"  {part}")
    print("Complete projects: ")
    for part in projects:
        if Project.is_complete(part):
            print(f"  {part}")


main()
