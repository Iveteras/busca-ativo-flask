def arruma_index(dataframe):
    datetime = []
    data =[]

    for timestamp in dataframe.index:
        datetime.append(timestamp.date())

    for date in datetime:
        data.append(date.strftime("%x"))

    return data


def retorna_ativo(nome_ativo, data_inicial, data_final):
    import yfinance as yf

    ativo = yf.Ticker(nome_ativo)
    df_ativo = ativo.history(start=data_inicial, end=data_final)

    df_ativo.index = arruma_index(df_ativo)

    df_ativo.insert(loc=0, column='Date', value=df_ativo.index)
    
    json_table = df_ativo.to_json()
    csv_table = df_ativo.to_csv()

    return json_table, csv_table