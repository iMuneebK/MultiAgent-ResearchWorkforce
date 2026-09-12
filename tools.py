# Tools configuration can go here.
# CrewAI supports Langchain tools (e.g. search APIs, calculators) out of the box.
# For simplicity, this template uses the agents' intrinsic knowledge.

from langchain_community.tools import DuckDuckGoSearchRun

def get_search_tool():
    """Returns a web search tool for agents to use."""
    return DuckDuckGoSearchRun()
