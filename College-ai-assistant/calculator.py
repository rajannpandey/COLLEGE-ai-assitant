def calculate_attendance(classes_attended, total_classes):
    if total_classes <= 0:
        raise ValueError("Total classes must be greater than zero.")

    percentage = (classes_attended / total_classes) * 100

    return {
        "classes_attended": classes_attended,
        "total_classes": total_classes,
        "attendance_percentage": round(percentage, 2)
    }


def calculate(expression):
    """
    Basic calculator.

    Example:
        calculate("10 + 20")
    """

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