from agents.style_agent import check_style
from agents.performance_agent import check_performance
from agents.security_agent import check_security

def run_agents(file_content):
    results = {
        "style": check_style(file_content),
        "performance": check_performance(file_content),
        "security": check_security(file_content)
    }
    return results
