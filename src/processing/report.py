def generate_report(consolidated_df):
    output = "data/relatorio_consolidado.xlsx"
    consolidated_df.to_excel(output, index=False)
    return output