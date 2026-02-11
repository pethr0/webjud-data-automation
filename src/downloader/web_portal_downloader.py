import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from utils.logger import get_logger


logger = get_logger(__name__)


class WebJudDownloader:

    def __init__(self):
        self.user = os.getenv("WEBJUD_USER")
        self.password = os.getenv("WEBJUD_PASSWORD")
        self.driver_path = os.getenv("EDGE_DRIVER_PATH")

    def _create_driver(self):

        options = Options()
        options.add_argument("--headless")

        service = Service(self.driver_path)

        driver = webdriver.Edge(service=service, options=options)
        wait = WebDriverWait(driver, 20)

        return driver, wait

    def download_file(self):

        logger.info("Iniciando processo de download.")

        driver, wait = self._create_driver()

        try:
            driver.get(os.getenv("WEBJUD_URL"))

            # Esta etapa foi simplificada paara simular o processo de login
            # na página verdadeira, o qual é feito utilizando Selenium através de:
            # - Localização dos campos de usuário e senha via localização através de Ids
            # - Preenchimento automático através do usuário e senha salvos
            
            logger.info("Web portal accessed successfully")

            # Simulação de retorno de arquivo
            # Para esta etapa, o script original realiza a filtragrem das informações
            # através de filtros dentro do próprio site.
            # A tarefa é feita utilizando Selenium, também com localização de botões
            # via Id.
            # Ao final, é salvo o arquivo .xlsx que é utiizado posteriormente.
            filename = f"TRANSFERENCIAS_{datetime.now().strftime('%d-%m-%Y')}.xlsx"

            return f"data/{filename}"

        finally:
            driver.quit()
