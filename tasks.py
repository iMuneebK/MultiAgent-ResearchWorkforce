from crewai import Task

class ResearchTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f'Conduct comprehensive research on the topic: "{topic}". Focus on recent advancements, key architectures, and real-world applications. Summarize the findings clearly.',
            expected_output='A detailed 3-4 paragraph summary of the latest trends, architectures, and applications related to the topic.',
            agent=agent
        )

    def writing_task(self, agent, topic):
        return Task(
            description=f'Using the research provided, draft a comprehensive technical report on "{topic}". Ensure it has an introduction, body paragraphs with bullet points, and a conclusion.',
            expected_output='A well-structured technical markdown document, highly readable and engaging.',
            agent=agent
        )

    def review_task(self, agent, topic):
        return Task(
            description=f'Review the drafted technical report on "{topic}". Check for technical accuracy, grammatical correctness, and flow. Suggest and apply necessary edits.',
            expected_output='The final, polished markdown report ready for publication.',
            agent=agent
        )
