import sys 
from pathlib import Path # Add the src folder to the Python path 
sys.path.append(str(Path(__file__).resolve().parent / 'src'))
from cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainningPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model_piepeline import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainningPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     
STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

