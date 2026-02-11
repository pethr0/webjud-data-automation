import win32com.client as win32
import pandas as pd
import pyodbc
from utils.logger import get_logger


logger = get_logger(__name__)


class OutlookSender:

    def __init__(self, db_path: str):

        self.conn_str = (
            r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
            rf"DBQ={db_path};"
        )

    def send_daily_report(self, process_date: str, attachment: str):

        logger.info("Preparando reporte de email")

        conn = pyodbc.connect(self.conn_str)
        df = pd.read_sql("SELECT * FROM Base_Transf_WebJud", conn)
        conn.close()

        df_today = df[df["Data de tratativa"] == process_date]

        total = df_today["Valor Executado"].sum()

        body = f"""
        <h3>WebJUD Daily Report</h3>
        <p>Datd: {process_date}</p>
        <p>Total de Transferencias: {len(df_today)}</p>
        <p>Valor Total: R$ {total:,.2f}</p>
        """

        outlook = win32.Dispatch("outlook.application")
        mail = outlook.CreateItem(0)
        mail.Subject = f"[WebJUD] Daily Report - {process_date}"
        mail.HTMLBody = body
        mail.Attachments.Add(attachment)
        mail.Send()

        logger.info("Email enviado com sucesso")
