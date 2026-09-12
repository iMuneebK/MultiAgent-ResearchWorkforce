from crewai import Agent
from langchain_openai import ChatOpenAI
import config

llm = ChatOpenAI(model=config.LLM_MODEL, temperature=0.7)

class ResearchAgents:
    def researcher(self):
        return Agent(
            role='Senior Technical Researcher',
            goal='Conduct in-depth research on AI topics and gather factual, up-to-date information.',
            backstory='An expert technical researcher with a PhD in Computer Science, specializing in digging deep into modern AI architectures and summarizing dense academic papers.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def writer(self):
        return Agent(
            role='Technical Content Writer',
            goal='Transform research findings into engaging, well-structured technical reports.',
            backstory='A former tech journalist who knows how to explain complex AI concepts to both technical and non-technical audiences.',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def reviewer(self):
        return Agent(
            role='Technical Reviewer',
            goal='Review the generated report for technical accuracy, clarity, and completeness.',
            backstory='A strict but fair senior AI engineer who reviews code and documentation meticulously, ensuring high standards.',
            verbose=True,
            allow_delegation=True,
            llm=llm
        )
