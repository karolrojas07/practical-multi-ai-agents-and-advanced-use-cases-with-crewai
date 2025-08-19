from .crew import ProjectProcessReportCrew
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

    try:
        crew = ProjectProcessReportCrew().crew()
        result = crew.kickoff()
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        
        costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
        print(f"Total costs: ${costs:.4f}")
        
        """
        import pandas as pd
        # Convert UsageMetrics instance to a DataFrame
        df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
        df_usage_metrics
        """
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    
if __name__ == "__main__":
    run()