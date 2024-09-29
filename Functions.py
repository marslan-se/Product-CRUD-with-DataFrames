from os.path import exists
import pandas as pd

def add_product(file_name, product):
    df = pd.read_csv(file_name)
    df.loc[len(df)] = product
    df.to_csv(file_name, index=False)
    return df.loc[df.index[-1]]

def list_products(file_name):
    df = pd.read_csv(file_name)
    return df

def update_product_rating(file_name, pid, rating_value):
    df = pd.read_csv(file_name)
    if pid in df['pid'].values:
        df.loc[df['pid'] == pid, 'rating'] = float(rating_value)
        df.to_csv(file_name, index=False)
        return "Product Rating Updated"
    else:
        return "Product ID Not Exists"

def delete_product(file_name, pid):
    df = pd.read_csv(file_name)
    if pid in df['pid'].values:
        df = df[df['pid'] != pid]
        df.to_csv(file_name, index=False)
        return "Product Deleted Successfully"
    else:
        return "Product ID Not Exists"