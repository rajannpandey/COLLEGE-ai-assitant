from llm.router import choose_tool

from tools.calculator import calculate_attendance
from tools.attendance import mark_attendance
from tools.timetable import analyze_timetable


def main():
    print("=" * 50)
    print("       COLLEGE AI ASSISTANT")
    print("=" * 50)

    user_input = input("\nStudent: ")

    tool = choose_tool(user_input)

    print(f"\nTool selected: {tool}")

    if tool == "calculator":
        attended = int(input("Classes attended: "))
        total = int(input("Total classes: "))

        result = calculate_attendance(attended, total)

        print(
            f"\nAttendance percentage: "
            f"{result['attendance_percentage']}%"
        )

        print("Tool used: calculator")

    elif tool == "attendance":
        student_id = input("Student ID: ")
        date = input("Date (YYYY-MM-DD): ")
        subject = input("Subject: ")
        status = input("Status (present/absent): ")

        result = mark_attendance(
            student_id,
            date,
            subject,
            status
        )

        print(f"\n{result['message']}")
        print("Tool used: attendance")

    elif tool == "timetable":
        document_text = input(
            "Enter timetable text for testing: "
        )

        result = analyze_timetable(
            document_text,
            user_input
        )

        print("\nTimetable analysis:")
        print(result["message"])

        print("Tool used: timetable")

    else:
        print(
            "\nI don't know which tool to use "
            "for this request."
        )


if __name__ == "__main__":
    main()
