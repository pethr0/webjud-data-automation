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
        
        try:
    
            logger.info("Conseguiu ler o arquivo")
    
            # Filtrar por data de tratativa
            hoje = datetime.today().strftime('%d/%m/%Y')
            df_hoje = df[df["Data de tratativa"] == hoje].copy()
    
            logger.info("Filtrou a data de tratativa")
    
            # CNPJs a serem filtrados
            cnpj_1 = ['12.345.678/0000-99', '12.345.678/0000-99', '12.345.678/0000-99']
            cnpj_2 = '12.345.678/0000-99'
    
            # Converte a coluna 'Valor Executado' de string para float
            df['Valor Executado'] = pd.to_numeric(df['Valor Executado'], errors='coerce')
            logger.info("Conseguiu converter o valor de string para float")
    
            # Banco
            df_banco = df_hoje[df_hoje["CPF/CNPJ Envolvido"].astype(str).isin(cnpj_1)]
            qtd_banco = len(df_banco)
            total_banco = df_banco["Valor Executado"].replace(np.nan, 0).sum() if not df_banco.empty else 0
            float_banco = total_banco
            logger.info(float_banco)
    
            # Banco 2
            df_banco_2 = df_hoje[df_hoje["CPF/CNPJ Envolvido"].astype(str) == cnpj_2]
            qtd_banco_2 = len(df_banco_2)
            total_banco_2 = df_banco_2["Valor Executado"].replace(np.nan, 0).sum() if not df_banco_2.empty else 0
            float_banco_2 = float(total_banco_2)
            logger.info(float_financeira)
    
            # Totais gerais
            qtd_total = len(df_hoje)
            total_geral = df_hoje["Valor Executado"].replace(np.nan, 0).sum()
            float_geral = float(total_geral)
            logger.info(float_geral)
            
            # Construir corpo em HTML
            corpo_email = f"""
            <div style="margin: 0; padding: 0; line-height: 1.2;">
    
            <p>Prezados, bom dia,</p>
    
            <p>Segue resumo das transferências do WebJUD do dia <strong>{hoje}</strong>:</p>
    
            <ul>
                <li><strong>📊 Total de transferências:</strong> {qtd_total:,}</li>
                <li><strong>💰 Valor total das transferências:</strong> R$ {float_geral:,.2f}</li>
            </ul>
    
            <ul>
                <li><strong>🏦 Transferências do Banco:</strong> {qtd_banco:,}</li>
                <li><strong>💵 Valor total de transferências do Banco:</strong> R$ {float_banco:,.2f}</li>
                {"<li>❌ Não houve transferências do banco hoje.</li>" if qtd_banco == 0 else ""}
            </ul>
    
            <ul>
                <li><strong>🏛️ Transferências do Banco 2:</strong> {qtd__banco_2:,}</li>
                <li><strong>💵 Valor total de transferências do Banco 2:</strong> R$ {float_banco_2:,.2f}</li>
                {"<li>❌ Não houve transferências da financeira hoje.</li>" if qtd_banco_2 == 0 else ""}
            </ul>
            </div>
            """
    
            if not df_banco_2.empty:
                corpo_email += """
                <p><strong>📄 Detalhamento das transferências do Banco 2:</strong></p>
                <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                    <tr>
                        <th>Nº Processo</th>
                        <th>CNPJ</th>
                        <th>Valor</th>
                        <th>Data da Transação</th>
                    </tr>
                """
                for _, row in df_financeira.iterrows():
                    processo = row.get("Número Processo", "N/A")
                    cnpj = row["CPF/CNPJ Favorecido"]
                    valor = row["Valor Executado"]
                    data_transacao = row["Data de tratativa"]
                    corpo_email += f"""
                    <tr>
                        <td>{processo}</td>
                        <td>{cnpj}</td>
                        <td>R$ {valor}</td>
                        <td>{data_transacao}</td>
                    </tr>
                    """
                corpo_email += "</table>"

        # Enviar email via Outlook
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'pedro.hsantos@agi.com.br'
        mail.Subject = f"[WebJUD] Relatório de Transferências - {hoje}"
        mail.HTMLBody = corpo_email.replace('\n', '<br>')
        mail.Attachments.Add(Source=novo_nome_arquivo)             
        mail.Send()

        logger.info("Email enviado com sucesso")
