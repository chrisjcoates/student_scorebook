import os
import time


class StudentScores:
    def __init__(self):

        self.student_scores = []

    def clear_console(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def help(self):
        self.clear_console()
        help_on = True
        while help_on:
            print(
                "\nIn the menu type 'quit' to exit or enter a menu number to select an option.\n"
            )
            exit_help = input("Type 'q' to exit help: ").lower()
            if exit_help == "q":
                help_on = False
                self.clear_console()
            else:
                self.clear_console()
                continue

    def add_record(self):
        self.clear_console()
        add_record_on = True
        while add_record_on:
            name_on = True
            while name_on:
                name = input("Enter name of student: ").title()
                if len(name) == 0:
                    print("No name supplied, try again.")
                    time.sleep(2)
                    self.clear_console()
                    continue
                else:
                    name_on = False
                    break
            grades_on = True
            while grades_on:
                check = 0
                try:
                    math = int(input("Enter math score (0-100): "))
                    english = int(input("Enter english score (0-100): "))
                    science = int(input("Enter science score (0-100): "))
                except ValueError:
                    print("One or more grades was entered incorrectly, try again.")
                    time.sleep(3)
                    self.clear_console()
                    continue
                for score in [math, english, science]:
                    if score < 0:
                        check += 1
                    elif score > 100:
                        check += 1
                    else:
                        pass
                if check > 0:
                    print("One or more score has been entered incorectly, try again.")
                    time.sleep(2)
                    self.clear_console()
                    continue
                else:
                    break

            student_grade = (name, math, english, science)
            self.student_scores.append(student_grade)
            print("\nStudent grades sucessfully recorded.\n")
            print(f"{name}, Math: {math}, English: {english}, Science: {science}")
            time.sleep(2)
            self.clear_console()
            add_record_on = False
            break

    def view_records(self):
        if len(self.student_scores) > 0:
            view_on = True
            while view_on:
                self.clear_console()
                for index, student in enumerate(self.student_scores):
                    print(
                        f"{index+1}: {student[0]}, Math: {student[1]}, English: {student[2]}, Science: {student[3]}"
                    )
                exit_view = input("\nType 'q' to exit view: ").lower()
                if exit_view == "q":
                    view_on = False
                    self.clear_console()
                    break
                else:
                    print("\nCommand not recognised.")
                    time.sleep(2)
                    self.clear_console()
                    continue
        else:
            print("\nNo student records available.\n")
            time.sleep(2)
            self.clear_console()

    def grade_statistics(self):
        if len(self.student_scores) > 0:
            statistics_on = True
            while statistics_on:
                self.clear_console()
                if len(self.student_scores) > 0:
                    lowest_avg_name = []
                    lowest_average = 100
                    highest_avg_name = []
                    highest_average = 0

                    for student in self.student_scores:
                        name = student[0]
                        average_grade = (student[1] + student[2] + student[3]) / 3
                        if average_grade < lowest_average:
                            lowest_average = average_grade
                            lowest_avg_name = [name]
                        if average_grade > highest_average:
                            highest_average = average_grade
                            highest_avg_name = [name]

                    print(
                        f"\nLowest average student is {lowest_avg_name[0]}, average score is {round(lowest_average, 2)}\n"
                    )
                    print(
                        f"\nHighest average student is {highest_avg_name[0]}, average score is {round(highest_average, 2)}\n"
                    )
                else:
                    print("\nNo student records available.\n")
                    time.sleep(2)
                    self.clear_console()

                exit_statistics = input("Type 'q' to exit: ").lower()

                if exit_statistics == "q":
                    exit_statistics = False
                    self.clear_console()
                    break
                else:
                    continue
        else:
            print("\nNo student records available.\n")
            time.sleep(2)
            self.clear_console()

    def run(self):
        self.clear_console()

        system_on = True

        menu_items = ["Add record", "View records", "View score statistics"]

        while system_on:
            print("STUDENT SCOREBOOK")
            print("-----------------\n")

            print("Select an option below:\n")

            for index, item in enumerate(menu_items):
                print(f"{index+1}: {item}")

            print("\nType 'help' for list of commands.\n")

            menu_choice = input("What would you like to do? ")

            match menu_choice:

                case "1" | "Add record":
                    self.add_record()
                case "2" | "View records":
                    self.view_records()
                case "3" | "View score statistics":
                    self.grade_statistics()
                case "quit" | "q":
                    system_on = False
                    break
                case "help" | "h":
                    self.help()
                case _:
                    print(
                        "\nCommand not recognised, type 'help' for list of commands.\n"
                    )
                    time.sleep(2)
                    self.clear_console()


program = StudentScores()
program.run()
