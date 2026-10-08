from tools.calculator import calculate_attendance
from tools.attendance import mark_attendance
from tools.timetable import analyze_timetable
def execute_tool(tool_request):
    tool_name = tool_request.get("tool")
    arguments = tool_request.get("arguments", {})
    if tool_name == "calculator":
        result = calculate_attendance(
            arguments["classes_attended"],
            arguments["total_classes"]
        )
        return {
            "tool_used": "calculator",
            "result": result
        }
    elif tool_name == "attendance":
        result = mark_attendance(
            arguments["student_id"],
            arguments["date"],
            arguments["subject"],
            arguments["status"]
        )
        return {
            "tool_used": "attendance",
            "result": result
        }
    elif tool_name == "timetable":
        result = analyze_timetable(
            arguments["document"],
            arguments["question"]
        )
        return {
            "tool_used": "timetable",
            "result": result
        }
    return {
        "tool_used": None,
        "result": "No valid tool was selected."
    }
