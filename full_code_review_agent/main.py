import os
import json
from agents.manager import run_agents
from utils.logger import log
from utils.github_utils import get_repo, create_pr

CONFIG_PATH = "config.json"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def analyze_file(file_path, config):
    with open(file_path, "r") as f:
        content = f.read()
    return run_agents(content, config)

def main():
    config = load_config()
    repo_name = config.get("repo_name")
    repo = get_repo(repo_name) if os.getenv("GITHUB_TOKEN") else None

    # 示例扫描本地 example.py
    example_file = "example.py"
    if not os.path.exists(example_file):
        with open(example_file, "w") as f:
            f.write("# Example Python file\nfor i in range(len([1,2,3])):\n    print(i)")

    results = analyze_file(example_file, config)
    log(results)

    report_body = ""
    for k, v in results.items():
        report_body += f"{k} issues:\n" + "\n".join(v) + "\n\n"

    if repo:
        branch_name = config.get("branch_prefix", "feature/code_review")
        pr_url = create_pr(repo, branch_name, report_body)
        log(f"PR created: {pr_url}")

if __name__ == "__main__":
    main()
