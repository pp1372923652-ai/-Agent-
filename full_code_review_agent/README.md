# 多 Agent 自动化代码审查系统

## 功能
- 多 Agent 协作检查代码风格、性能、安全问题
- Manager 汇总结果生成报告
- 可生成 GitHub Pull Request 或本地报告
- 可扩展新的 Agent

## 使用方法
1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```
2. 设置 GitHub Token (可选, 用于生成 PR):
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```
3. 运行:
   ```bash
   python main.py
   ```

## 目录结构
- agents/: 各检查 Agent
- utils/: 工具函数
- main.py: 项目入口
- config.json: 配置文件
