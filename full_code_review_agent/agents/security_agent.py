def check_security(file_content):
    issues = []
    for i, line in enumerate(file_content.splitlines(), start=1):
        if "eval(" in line or "exec(" in line:
            issues.append(f"Line {i}: use of eval/exec is dangerous")
    return issues
