def pandas_decorator(func):
    def wrapper(*args):
        response = func(*args)
        response.to_parquet("./orders.parquet")
        return response

    return wrapper




@pandas_decorator
def cev_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df

response = cev_to_parquet("./orders.csv")
print(response.head())