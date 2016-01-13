def human_readable_type(obj):
    if obj is None:
        return "None"
    if type(obj) in [int, float]:
        return "Number"
    if type(obj) == bool:
        return "Boolean"
    if type(obj) == str:
        return "String"
    return "Other"
