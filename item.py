from dataclasses import dataclass
from datetime import datetime
from enum import Enum


#TODO: This needs to be configured in the database. Hardcoding workitem types is not a good idea
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

#all plannable objects will have a time span property, both a planned and actual start/end date. UTC time will be used for all dates
@dataclass
class time_span:
    start: datetime
    end: datetime
    planned_start: datetime
    planned_end: datetime
    
@dataclass
class workFlowSteps:
    id: int
    name: str
    

#A work flow object is an indiaction of the state of that object(for example, a work item might be New, refining, on hold etc). These workflows should be configurable
@dataclass
class workflow:
    id: int
    name: str
    

@dataclass
class workItem:
    id: int
    title: str
    description: str
    workItem: workItemType
    schedule: time_span
    

   