from ast import Add
from cgitb import text
import pandas as pd

# Read column H in the result_combined_200_CSV file
# read specific columns of csv file using Pandas

df = pd.read_csv("updated_result_combined_200.csv")


# def replace_space_with_plus(text):
#     if isinstance(text, str):
#         new_text = text.replace(' ', '+')
#         return new_text
#     else:
#         return None

# df['updated_name'] = df['name'].apply(lambda x: replace_space_with_plus(x))
# print(df)

# df.to_csv('updated_result_combined_200.csv', index=False, encoding='utf-8')


def add_google_before_updated_name(text):
    if isinstance(text,str):
        req_google_url = "https://www.google.com/search?q="+text
        return req_google_url
    else:
        return None

df['google_url'] = df['updated_name'].apply(lambda x: add_google_before_updated_name(x))
df.to_csv('updated_result_combined_200.csv', index=False, encoding='utf-8')