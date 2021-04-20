# python program to get table from url
# and output the desired table content 
# to an html file
import pandas as pd
url="https://space-facts.com/mars/"
tables = pd.read_html(url)
df=tables[0]
df_output=df.rename(columns={0: "Description", 1: "Mars Values"})
df_output.to_html("pd_mars_facts.html",index=False)