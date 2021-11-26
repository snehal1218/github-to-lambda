import pandas as pd

def lambda_handler(event, context):
   d = {'col1': [5,10],'col2': [20,25]}
   df = pd.DataFrame(data=d)
   print(df)
   print('Done x1.1')
   return 0