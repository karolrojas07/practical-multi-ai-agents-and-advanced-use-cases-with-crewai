from typing import List
from pydantic import BaseModel, Field
from .milestone import Milestone
from .taskEstimate import TaskEstimate

class ProjectPlan(BaseModel):
    tasks: List[TaskEstimate] = Field(..., description="List of tasks with their estimates")
    milestones: List[Milestone] = Field(..., description="List of project milestones")