import pandas as pd
import mysql.connector as mys
from sql_queries import *
import csv

def extractAndTransform():
    """
        - Load file "teste_dados_ecommerce.csv" as Dataframe;
        - Changes columns names avoiding MySQL problems;
        - Changes file types;
        - Drops rows with negative values on quantitative data columns;
        - Creates a new CSV file with adequate data
    """
    # loading CSV file
    df = pd.read_csv('data/teste_dados_ecommerce.csv', sep=';', encoding='unicode_escape', parse_dates=['InvoiceDate'])
    
    # renaming columns
    df = df.rename(columns={'InvoiceNo':'invoice_number',\
                            'StoreId':'store_id',\
                            'StockCode':'stock_code',\
                            'Description':'description',\
                            'Quantity':'quantity',\
                            'InvoiceDate':'invoice_date',\
                            'UnitPrice':'unit_price',\
                            'CustomerID':'customer_id',\
                            'Country':'country'})
    
    # changing data types
    data_types_dict = {'store_id': object,\
                        'customer_id': object}
    df = df.astype(data_types_dict)
    
    # droping rows with negative values 
    df = df[(df.quantity > 0) & (df.unit_price > 0)]

    # dropping 'stock code' items that referred to discounts and freight values
    df = df[~df['stock_code'].str.contains("[a-zA-Z]").fillna(False)]

    # creating CSV file with adequate data
    df.to_csv('data/ecommerce.csv', sep=';', index=False)

    return df

def createDatabase():

    # creating conection with db
    cnx = mys.connect(user='root', password='root', host='localhost')

    # cursor object
    cursor = cnx.cursor()

    # executing queries 
    cursor.execute(drop_ecommerce)
    cursor.execute(create_ecommerce)
    cursor.execute(use_ecommerce)
    cursor.execute(drop_sales_table)
    cursor.execute(create_sales_table)

    # data insert 
    sales_data = 'data/ecommerce.csv'
    
    with open(sales_data, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=';')
        # to scape first row of CSV
        next(reader)
        csv_data_list = list(reader)
        rows=0
        for row in csv_data_list:
            cursor.execute(sales_insert, row)
            rows+=1
            print(rows)
        
    cnx.commit()
    cursor.close()
    cnx.close()
    print('Done')

    return cnx, cursor

def main():
    extractAndTransform()
    createDatabase()

if __name__ == '__main__':
    main()

