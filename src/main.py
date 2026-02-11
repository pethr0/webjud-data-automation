from downloader.web_portal_downloader import download_files
from processing.data_cleaning import load_and_clean_data
from processing.validators import validate_dataset
from processing.consolidations import consolidate_by_cnpj
from database.access_repository import insert_data
from email.outlook_sender import send_email_report
from utils.logger import get_logger
from processing.report import generate_report

logger = get_logger()

def main():
    logger.info("Iniciando processamento WebJUD")

    try:
	input_file = download_files()
        df = load_and_clean_data(input_file)

	validate_dataset(df)

	consolidated = consolidate_by_cnpj(df)

	insert_data(df)

	report_file = generate_report(consolidated)

	send_email_report(consolidated, report_file)

	logger.info("Processo finalizado com sucesso.")
   
    execept Exception as e:
        logger.error(f"Erro no processamento: {e}")
        raise

if __name__ == "__main__":
    main()