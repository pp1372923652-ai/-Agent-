import os
from agents.manager import run_agents
from utils.github_utils import get_repo, create_pr
from utils.logger import log

def analyze_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return run_agents(content)

def main():
    repo_name = "your-org/your-repo"
    repo = get_repo(repo_name)
    
    # 扫描本地 example.py
    file_path = "example.py"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# Example Python file\nfor i in range(len([1,2,3])):\n    print(i)")

    results = analyze_file(file_path)
    log(results)
    
    body = ""
    for k, v in results.items():
        body += f"{k} issues:\n" + "\n".join(v) + "\n\n"
    
    # PR 创建（需要 GitHub Token 配置）
    # pr_url = create_pr(repo, "feature/code_review", body)
    # log(f"PR created: {pr_url}")

if __name__ == "__main__":
    main()
