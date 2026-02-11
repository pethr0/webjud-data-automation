import re

def is_valid_cnpj(cnpj):
    return bool(re.fullmatch(r"\d{14}", cnpj))

def validate_dataset(df):
    required_columns = {"cnpj", "valor", "data"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing}")

    if not df["cnpj"].apply(is_valid_cnpj).all():
        raise ValueError("CNPJ inválido encontrado")

    if (df["valor"] <= 0).any():
        raise ValueError("Valores inválidos encontrados")

    print("Validação concluída com sucesso.")