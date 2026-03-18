from enum import Enum

class PipelineStepEnum(Enum):
    REFERENCE_COLLECTION = "Reference Collection"
    REFERENCE_EXTRACTION = "Reference Extraction"
    SIMPLE_MODEL_CONSTRUCTION = "Simple Model Construction"
    SIMPLE_MODEL_CHECKING = "Simple Model Checking"
    ADVANCED_MODEL_CONSTRUCTION = "Advanced Model Construction"
    ADVANCED_MODEL_CHECKING = "Advanced Model Checking"
    REPORT_GENERATION = "Report Generation"