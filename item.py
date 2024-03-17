from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class workItemType(Enum):
    Request=1
    Initiative=2
    Program=3
    Project=4
    Epic=5
    Feature=6
    Story=7
    Task=8
    Bug=9
    Issue=10

@dataclass
class time_span:
    start: datetime
    end: datetime
    planned_start: datetime
    planned_end: datetime
    
    
    
    

@dataclass
class workItem:
    id: int
    title: str
    description: str
    workItem: workItemType

   