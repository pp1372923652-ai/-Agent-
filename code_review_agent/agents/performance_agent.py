def check_performance(file_content):
    issues = []
    for i, line in enumerate(file_content.splitlines(), start=1):
        if "for i in range(len" in line:
            issues.append(f"Line {i}: consider using enumerate for better performance")
    return issues
