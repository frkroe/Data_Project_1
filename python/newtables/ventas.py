def ventas(v, df_muebles, df_clientes, minq, maxq):
    # Importaciones
    import pandas as pd
    import csv
    import random
    import time
    from datetime import datetime

    #leemos customer_id y item_id de sus archivos y los guardamos como listas
    list_muebleId = df_muebles["product_id"].to_list()
    list_clienteId = df_clientes["customer_id"].to_list()
    #print(list_clienteId,list_muebleId)

    #creamos dataframe con nuevos ventas cada 1 segundo
    df_ventas = pd.DataFrame(columns= ["sales_id", "customer_id", "product_id", "date", "quantity"])
    for i in range(v):
        row = [id(i), random.choice(list_clienteId), random.choice(list_muebleId), datetime.now(),  random.randrange(minq, maxq+1)]
        df_ventas.loc[i] = row
    #print(df_ventas)
    #tambien guardamos los datos en csv por cada fila
        with open('results/ventas.csv', 'a', newline='', encoding='UTF8') as csv_file:  
                writer = csv.writer(csv_file)
                if csv_file.tell() == 0:
                    writer.writerow(["sales_id", "customer_id", "product_id", "date", "quantity"])
                writer.writerow(row)
        time.sleep(1)
    return df_ventas