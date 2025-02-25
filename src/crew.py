from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
import yaml

@CrewBase
class ProjectAdvisor():
    """Project advisor crew"""

    # Load configurations
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def advisor(self) -> Agent:
        #Creates and returns a project advisor agent
        return Agent(
            config=self.agents_config['advisor'],
            verbose=True
        )

    @agent
    def reviewer(self) -> Agent:
        #Creates and returns a project reviewer agent
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    @task
    def project_evaluation_task(self) -> Task:
        #Creates and returns a project evaluation task
        return Task(
            config=self.tasks_config['project_evaluation_task'],
        )

    @task
    def project_guidance_task(self) -> Task:
        #Creates and returns a project guidance task
        return Task(
            config=self.tasks_config['project_guidance_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Assembles the project advisory crew with agents and tasks"""

        # Creates the crew by combining agents and tasks
        return Crew(
            agents=self.agents,  # Automatically created by @agent decorator
            tasks=self.tasks,    # Automatically created by @task decorator
            process=Process.sequential,  # Execute tasks one after another
            verbose=True,
        )
