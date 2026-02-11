def consolidate_by_cnpj(df):
    consolidated = (
        df.groupby("cnpj", as_index=False)
        .agg(total_valor=("valor", "sum"))
    )

    return consolidated