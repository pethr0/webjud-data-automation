import os

from datetime import datetime

from downloader.web_portal_downloader import WebJudDownloader
from processing.data_cleaning import DataCleaner
from processing.validators import BaseValidator
from database.access_repository import AccessRepository
from email.outlook_sender import OutlookSender
from utils.logger import get_logger

logger = get_logger(__name__)

class WebJudPipeine:

    def __init__(self):
        self.today = datetime.today().strftime("%d/%m/%Y")
        self.temp_path = os.getenv("TEMP_PATH", "data/temp")
        self.database_path = os.getenv("ACCESS_DB_PATH")

    def run(self):

        logger.info("Iniciando processamento WebJUD")

        validator = BaseValidator(self.database_path)
        validator.validate_already_processed(self.today)

        downloader = WebJudDownloader()
        downloaded_file = downloader.download_file()

        cleaner = DataCleaner(self.temp_path)
        treated_file = cleaner.process(downloaded_file, self.today)

        repository = AccessRepository(self.database_path)
        repository.insert_from_excel(treated_file)

        email_sender = OutlookSender(self.database_path)
        email_sender.send_daily_report(self.today, treated_file)

        logger.info("Processo finalizado com sucesso.")

if __name__ == "__main__":
    pipeline = WebJudPipeline()
    pipeline.run()