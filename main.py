from crewai import Crew, Process
from agents import ResearchAgents
from tasks import ResearchTasks
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    
    print("Welcome to the Multi-Agent AI Research System!")
    topic = input("Enter a topic for the agents to research and write about: ")
    
    # Initialize agents
    agents_factory = ResearchAgents()
    researcher = agents_factory.researcher()
    writer = agents_factory.writer()
    reviewer = agents_factory.reviewer()
    
    # Initialize tasks
    tasks_factory = ResearchTasks()
    research_task = tasks_factory.research_task(researcher, topic)
    writing_task = tasks_factory.writing_task(writer, topic)
    review_task = tasks_factory.review_task(reviewer, topic)
    
    # Form the crew
    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=[research_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True
    )
    
    print(f"\n🚀 Kicking off research process on: {topic}...\n")
    result = crew.kickoff()
    
    print("\n==============================================")
    print("🎯 FINAL OUTPUT:")
    print("==============================================")
    print(result)
    
    # Save the output
    output_filename = f"report_{topic.replace(' ', '_')}.md"
    with open(output_filename, "w") as f:
        f.write(result)
    print(f"\nReport saved to {output_filename}")

if __name__ == "__main__":
    main()
