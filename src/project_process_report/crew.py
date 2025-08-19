from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, crew, task
from .tools.board_data_fetcher_tool import BoardDataFetcherTool
from .tools.card_data_fetcher_tool import CardDataFetcherTool
 
@CrewBase
class ProjectProcessReportCrew():
    """Crew to execute a Project planning"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_collection_agent(self) -> Agent:
        return Agent(
        config=self.agents_config['data_collection_agent'],
        tools=[BoardDataFetcherTool(), CardDataFetcherTool()]
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['analysis_agent']
        )

    # Creating Tasks
    @task
    def data_collection(self) -> Task:
        return Task(
            config=self.tasks_config['data_collection'],
        )

    @task
    def data_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['data_analysis'],
        )

    @task
    def report_generation(self) -> Task:
        return Task(
            config=self.tasks_config['report_generation'],
        )

    # Creating Crew
    @crew
    def crew(self) -> Crew:
        return  Crew(
        agents=[
            self.data_collection_agent(),
            self.analysis_agent()
        ],
        tasks=[
            self.data_collection(),
            self.data_analysis(),
            self.report_generation()
        ],
        verbose=True
        )