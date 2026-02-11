import pandas as pd


def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.lower().str.strip()

    df["cnpj"] = df["cnpj"].astype(str).str.zfill(14)
    df["valor"] = (
        df["valor"]
        .astype(str)
        .str.replace(",", ".")
        .astype(float)
    )

    return df