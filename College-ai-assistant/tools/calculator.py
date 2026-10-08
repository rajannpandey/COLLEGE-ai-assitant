def calculate_attendance(classes_attended, total_classes):
    if total_classes <= 0:
        raise ValueError("Total classes must be greater than zero.")
    if classes_attended < 0:
        raise ValueError("Classes attended cannot be negative.")
    if classes_attended > total_classes:
        raise ValueError("Classes attended cannot be greater than total classes.")
    percentage = (classes_attended / total_classes) * 100
    return {
        "classes_attended": classes_attended,
        "total_classes": total_classes,
        "attendance_percentage": round(percentage, 2)
    }
def calculate(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return {
            "expression": expression,
            "result": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }
