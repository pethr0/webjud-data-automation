import pandas as pd
import re
import os
from utils.logger import get_logger


logger = get_logger(__name__)


class DataCleaner:

    def __init__(self, output_path: str):
        self.output_path = output_path
        os.makedirs(self.output_path, exist_ok=True)

    def process(self, input_file: str, process_date: str) -> str:

        logger.info("Iniciando processo de limpeza de dados")

        df = pd.read_excel(input_file)

        df["Data de tratativa"] = process_date

        df = self._apply_document_mask(df)
        df = self._normalize_currency(df)

        output_file = os.path.join(
            self.output_path,
            f"TRATADO_TRANSFERENCIAS_{process_date.replace('/', '-')}.xlsx"
        )

        df.to_excel(output_file, index=False)

        logger.info("Limpeza de dados finaizada")

        return output_file

    def _apply_document_mask(self, df):

        def mask(doc):
            if pd.isna(doc):
                return None

            doc = re.sub(r"\D", "", str(doc))

            if len(doc) <= 11:
                return f"{doc[:3]}.{doc[3:6]}.{doc[6:9]}-{doc[9:]}"
            if len(doc) > 11:
                return f"{doc[:2]}.{doc[2:5]}.{doc[5:8]}/{doc[8:12]}-{doc[12:]}"
            return doc

        if "CPF/CNPJ Envolvido" in df.columns:
            df["CPF/CNPJ Envolvido"] = df["CPF/CNPJ Envolvido"].apply(mask)

        return df

    def _normalize_currency(self, df):

        if "Valor Executado" in df.columns:
            df["Valor Executado"] = (
                df["Valor Executado"]
                .astype(str)
                .str.replace("R$", "", regex=False)
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float)
            )

        return df
