from datetime import datetime
import pandas as pd

test=pd.read_csv('data.csv', index_col=0, header=None, squeeze=True).to_dict()
now=datetime.now()
d1={}
d2={}
for key, value in test.items():
    initial=datetime.strptime(str(value),'%Y%m%d')
    k=(initial-now).days+1
    print(k)
    if k>0:
        d1[key]=k
    if k==0:
        d2[key]=k

df = pd.DataFrame(list(d1.items())) 
df.to_csv (r'future.csv', index = False, header=False)
df1 = pd.DataFrame(list(d2.items())) 
df1.to_csv (r'today.csv', index = False, header=False)