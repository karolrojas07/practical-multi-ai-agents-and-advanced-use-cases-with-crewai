from .crew import AutomatedProjectCrew
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    project = 'Website'
    industry = 'Technology'
    project_objectives = 'Create a website for a small business'
    team_members = """
    - John Doe (Project Manager)
    - Jane Doe (Software Engineer)
    - Bob Smith (Designer)
    - Alice Johnson (QA Engineer)
    - Tom Brown (QA Engineer)
    """
    project_requirements = """
    - Create a responsive design that works well on desktop and mobile devices
    - Implement a modern, visually appealing user interface with a clean look
    - Develop a user-friendly navigation system with intuitive menu structure
    - Include an "About Us" page highlighting the company's history and values
    - Design a "Services" page showcasing the business's offerings with descriptions
    - Create a "Contact Us" page with a form and integrated map for communication
    - Implement a blog section for sharing industry news and company updates
    - Ensure fast loading times and optimize for search engines (SEO)
    - Integrate social media links and sharing capabilities
    - Include a testimonials section to showcase customer feedback and build trust
    """
    
    inputs = {
        'project_type': project,
        'project_objectives': project_objectives,
        'industry': industry,
        'team_members': team_members,
        'project_requirements': project_requirements
    }

    try:
        crew = AutomatedProjectCrew().crew()
        result = crew.kickoff(inputs=inputs)
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        
        costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
        print(f"Total costs: ${costs:.4f}")
        import pandas as pd

        """
        # Convert UsageMetrics instance to a DataFrame
        df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
        df_usage_metrics
        """
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    
if __name__ == "__main__":
    run()