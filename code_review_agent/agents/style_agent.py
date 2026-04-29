def check_style(file_content):
    issues = []
    for i, line in enumerate(file_content.splitlines(), start=1):
        if len(line) > 120:
            issues.append(f"Line {i}: exceeds 120 characters")
        if " " * 4 != line[:4] and line.strip():
            issues.append(f"Line {i}: indentation not 4 spaces")
    return issues
