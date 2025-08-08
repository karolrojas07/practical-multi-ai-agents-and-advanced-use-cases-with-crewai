import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .models.projectPlan import ProjectPlan
 
@CrewBase
class AutomatedProjectCrew():
    """Crew to execute a Project planning"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def project_planning_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['project_planning_agent']
        )
    
    @agent
    def estimation_agent(self) -> Agent:
        return Agent(
    config=self.agents_config['estimation_agent']
    )

    @agent
    def resource_allocation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['resource_allocation_agent']
        )

    # Creating Tasks
    @task
    def task_breakdown(self) -> Task:
        return Task(
            config=self.tasks_config['task_breakdown'],
        )

    @task
    def time_resource_estimation(self) -> Task :
        return Task(
            config=self.tasks_config['time_resource_estimation'],
        )

    @task
    def resource_allocation(self) -> Task:
        return Task(
            config=self.tasks_config['resource_allocation'],
            output_pydantic=ProjectPlan # This is the structured output we want
        )

    # Creating Crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.project_planning_agent(),
                self.estimation_agent(),
                self.resource_allocation_agent()
            ],
            tasks=[
                self.task_breakdown(),
                self.time_resource_estimation(),
                self.resource_allocation()
            ],
            verbose=True
        )