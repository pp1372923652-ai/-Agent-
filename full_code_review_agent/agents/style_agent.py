def check_style(file_content):
    issues = []
    for i, line in enumerate(file_content.splitlines(), start=1):
        if len(line) > 120:
            issues.append(f"Line {i}: exceeds 120 characters")
        if line.startswith(" ") and (len(line) - len(line.lstrip())) % 4 != 0:
            issues.append(f"Line {i}: indentation not multiple of 4")
    return issues
