import pandas as pd

def lambda_handler(event, context):
   d = {'col1': [1,3],'col2': [2,5]}
   df = pd.DataFrame(data=d)
   print(df)
   print('Done x1.1')
