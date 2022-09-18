# Import libraries
from pydantic import BaseSettings

# Configuration class
class Configuration(BaseSettings):
    '''Config class'''

    # The name of the project
    PROJECT_NAME: str = "NER service"

    # The name of the folder where the saved model is located
    # (uploaded via docker and has a correspondingly named docker folder)
    MODEL_NAME: str = 'ner_model/'  

    class Config:
        case_sensitive = True

# Configuration сlass creation
CONFIGURATION = Configuration()
