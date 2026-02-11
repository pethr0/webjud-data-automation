import pyodbc
import pandas as pd
from utils.logger import get_logger


logger = get_logger(__name__)


class AccessRepository:

    def __init__(self, db_path: str):

        self.conn_str = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            rf"DBQ={db_path};"
        )

    def insert_from_excel(self, file_path: str):

        logger.info("Inserindo registros no banco de dados do Acesss")

        df = pd.read_excel(file_path)

        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()

        columns = df.columns.tolist()
        placeholders = ", ".join(["?"] * len(columns))

        query = f"""
            INSERT INTO Base_Transf_WebJud
            ({', '.join(f'[{col}]' for col in columns)})
            VALUES ({placeholders})
        """

        for _, row in df.iterrows():
            cursor.execute(query, list(row))

        conn.commit()
        conn.close()

        logger.info("Database atualizada com sucesso")
