from agents.style_agent import check_style
from agents.performance_agent import check_performance
from agents.security_agent import check_security

def run_agents(file_content, config):
    results = {}
    if config.get("check_style", True):
        results["style"] = check_style(file_content)
    if config.get("check_performance", True):
        results["performance"] = check_performance(file_content)
    if config.get("check_security", True):
        results["security"] = check_security(file_content)
    return results
