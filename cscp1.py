
CyberSecurityCp.ipynb
CyberSecurityCp.ipynb_
[1]
import random
import pandas as pd
import requests
import numpy as np
[ ]
from google.colab import drive
drive.mount('/content/drive')

Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
[2]
logfile = '/content/drive/MyDrive/conn.log'
sample_percent = .09
num_lines = sum(1 for line in open(logfile))
slines = set(sorted(random.sample(range(num_lines), int(num_lines * sample_percent))))
print (('%s lines in %s, using a sample of %s lines') %(num_lines, logfile, len(slines)))

22694356 lines in /content/drive/MyDrive/conn.log, using a sample of 2042492 lines
[ ]
w = open('/content/drive/MyDrive/outfile.txt', 'w+')
r = open(logfile, 'r+')
linecount = 0
for line in r:
    if linecount in slines:
        w.write(line)
    linecount += 1
w.close()
r.close()
[ ]
outfile = '/content/drive/MyDrive/outfile.txt'
df = pd.read_csv(outfile, sep="\t", header=None, names=['ts','uid','id.orig_h','id.orig_p','id.resp_h','id.resp_p','proto','service','duration','orig_bytes','resp_bytes','conn_state','local_orig','missed_bytes','history','orig_pkts','orig_ip_bytes','resp_pkts','resp_ip_bytes','tunnel_parents','threat','sample'])
[ ]
df.head()


[ ]
df.describe()


[ ]
df.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2042492 entries, 0 to 2042491
Data columns (total 22 columns):
 #   Column          Dtype  
---  ------          -----  
 0   ts              float64
 1   uid             object 
 2   id.orig_h       object 
 3   id.orig_p       int64  
 4   id.resp_h       object 
 5   id.resp_p       int64  
 6   proto           object 
 7   service         object 
 8   duration        object 
 9   orig_bytes      object 
 10  resp_bytes      object 
 11  conn_state      object 
 12  local_orig      object 
 13  missed_bytes    int64  
 14  history         object 
 15  orig_pkts       int64  
 16  orig_ip_bytes   int64  
 17  resp_pkts       int64  
 18  resp_ip_bytes   int64  
 19  tunnel_parents  object 
 20  threat          float64
 21  sample          float64
dtypes: float64(3), int64(7), object(12)
memory usage: 342.8+ MB
[ ]
df.dtypes

ts                float64
uid                object
id.orig_h          object
id.orig_p           int64
id.resp_h          object
id.resp_p           int64
proto              object
service            object
duration           object
orig_bytes         object
resp_bytes         object
conn_state         object
local_orig         object
missed_bytes        int64
history            object
orig_pkts           int64
orig_ip_bytes       int64
resp_pkts           int64
resp_ip_bytes       int64
tunnel_parents     object
threat            float64
sample            float64
dtype: object
[ ]
from datetime import datetime
df['ts'] = [datetime.fromtimestamp(float(date)) for date in df['ts'].values]
[ ]
df.dtypes

ts                datetime64[ns]
uid                       object
id.orig_h                 object
id.orig_p                  int64
id.resp_h                 object
id.resp_p                  int64
proto                     object
service                   object
duration                  object
orig_bytes                object
resp_bytes                object
conn_state                object
local_orig                object
missed_bytes               int64
history                   object
orig_pkts                  int64
orig_ip_bytes              int64
resp_pkts                  int64
resp_ip_bytes              int64
tunnel_parents            object
threat                   float64
sample                   float64
dtype: object
[ ]
float(len(df[df.proto=='tcp']))/len(df.proto)*100.0

98.21497464861551
[ ]
df.dtypes


ts                datetime64[ns]
uid                       object
id.orig_h                 object
id.orig_p                  int64
id.resp_h                 object
id.resp_p                  int64
proto                     object
service                   object
duration                  object
orig_bytes                object
resp_bytes                object
conn_state                object
local_orig                object
missed_bytes               int64
history                   object
orig_pkts                  int64
orig_ip_bytes              int64
resp_pkts                  int64
resp_ip_bytes              int64
tunnel_parents            object
threat                   float64
sample                   float64
dtype: object
[ ]
df.infer_objects()


[ ]
df["orig_bytes"]=pd.to_numeric(df["orig_bytes"],errors='coerce')
df["resp_bytes"]=pd.to_numeric(df["resp_bytes"],errors='coerce')

[ ]
df.dtypes

ts                datetime64[ns]
uid                       object
id.orig_h                 object
id.orig_p                  int64
id.resp_h                 object
id.resp_p                  int64
proto                     object
service                   object
duration                  object
orig_bytes               float64
resp_bytes               float64
conn_state                object
local_orig                object
missed_bytes               int64
history                   object
orig_pkts                  int64
orig_ip_bytes              int64
resp_pkts                  int64
resp_ip_bytes              int64
tunnel_parents            object
threat                   float64
sample                   float64
dtype: object
[ ]
import numpy as np
df_without = df.drop(['threat','sample'], axis=1)
df.drop(df.columns[[0, 1, 2, 4, 11, 18, 19]], axis=1) 
df_without.describe(include=[np.number])


[ ]

df_without.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2042492 entries, 0 to 2042491
Data columns (total 20 columns):
 #   Column          Dtype         
---  ------          -----         
 0   ts              datetime64[ns]
 1   uid             object        
 2   id.orig_h       object        
 3   id.orig_p       int64         
 4   id.resp_h       object        
 5   id.resp_p       int64         
 6   proto           object        
 7   service         object        
 8   duration        object        
 9   orig_bytes      float64       
 10  resp_bytes      float64       
 11  conn_state      object        
 12  local_orig      object        
 13  missed_bytes    int64         
 14  history         object        
 15  orig_pkts       int64         
 16  orig_ip_bytes   int64         
 17  resp_pkts       int64         
 18  resp_ip_bytes   int64         
 19  tunnel_parents  object        
dtypes: datetime64[ns](1), float64(2), int64(7), object(10)
memory usage: 311.7+ MB
[ ]

df.median()

/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:2: FutureWarning: DataFrame.mean and DataFrame.median with numeric_only=None will include datetime64 and datetime64tz columns in a future version.
  
id.orig_p        44316.0
id.resp_p        10180.0
orig_bytes           0.0
resp_bytes           0.0
missed_bytes         0.0
orig_pkts            1.0
orig_ip_bytes       48.0
resp_pkts            1.0
resp_ip_bytes       40.0
threat               NaN
sample               NaN
dtype: float64
[ ]
df.var()

id.orig_p        2.350955e+08
id.resp_p        4.260830e+08
orig_bytes       8.413449e+14
resp_bytes       2.677017e+13
missed_bytes     7.200396e+11
orig_pkts        1.309312e+04
orig_ip_bytes    4.037324e+08
resp_pkts        1.662522e+04
resp_ip_bytes    1.609648e+10
threat                    NaN
sample                    NaN
dtype: float64
[ ]

print('The mode of the ORIG bytes :')
print(df.orig_ip_bytes.mode())
print('The mode of the RESP bytes:')
print(df.resp_ip_bytes.mode())
print('The mode of the the entire dataframe:')
print(df.mode())

The mode of the ORIG bytes :
0    60
dtype: int64
The mode of the RESP bytes:
0    40
dtype: int64
The mode of the the entire dataframe:
                             ts                 uid  ... threat  sample
0       2012-03-16 19:43:02.080   C0000U2aeVZCwcI89  ...    NaN     NaN
1                           NaT   C0009QleXQKhPKNc5  ...    NaN     NaN
2                           NaT  C000H245gFqN2bPUDh  ...    NaN     NaN
3                           NaT  C000Pf1XxL5HFWtSWe  ...    NaN     NaN
4                           NaT  C000Xo3XnfYHKQQzZ7  ...    NaN     NaN
...                         ...                 ...  ...    ...     ...
2042487                     NaT  CzzzE01Hd3ABxs29ph  ...    NaN     NaN
2042488                     NaT  CzzzaU1DAkEjUoCXpa  ...    NaN     NaN
2042489                     NaT  Czzzlh2K8tL19QcG6d  ...    NaN     NaN
2042490                     NaT  Czzzuc19BA6TXwoPuc  ...    NaN     NaN
2042491                     NaT  CzzzvD21fSEaiX3Lej  ...    NaN     NaN

[2042492 rows x 22 columns]
We can conclude from the Mode that the local IP addresses are being used most, i.e, the local traffic is more. The protocol TCP and port numbers 80 are being used the most and TCP uses port number 80. orig_ip_bytes is 60, a SYN packet is of 60-bit in size. history is Sr that means that the SYN packet is being sent the most. resp_ip_bytes is 40, a FIN packet is of 40-bit in size.

These confirm that a SYN flood attack is targetting the network, which is one of the most common form of a DDoS attack.

SYN flood is a form of denial-of-service attack in which an attacker sends a succession of SYN requests to a target's system in an attempt to consume enough server resources to make the system unresponsive to legitimate traffic.

[ ]
print('The Range of the ORIG IP bytes is: ')
origin_range = df.orig_ip_bytes.max() - df.orig_ip_bytes.min()
print(origin_range)
print('Mean is: ', df.orig_ip_bytes.mean())
print('Max is: ', df.orig_ip_bytes.max())
print('Minimum is: ', df.orig_ip_bytes.min())
print('-------------')
print('The Range of the RESP IP bytes is: ' )
resp_range = df.resp_ip_bytes.max() - df.resp_ip_bytes.min()
print(resp_range)


The Range of the ORIG IP bytes is: 
20557460
Mean is:  156.39453912181787
Max is:  20557460
Minimum is:  0
-------------
The Range of the RESP IP bytes is: 
101111954
Mean is:  361.6881417405796
Max is:  101111954
Min is:  0
[ ]
df_grouped = df.groupby(by='proto')
print(df_grouped.service.count())
print('---------------------------------------')
#print('---------------------------------------')
#print(df_grouped.service.sum() / df_grouped.service.count())
df_grouped_diff=df.groupby(by='service')
print(df_grouped_diff.service.count())

proto
icmp      16270
tcp     2006033
udp       20189
Name: service, dtype: int64
---------------------------------------
service
-           1982537
dhcp            255
dns           14464
ftp             262
ftp-data        270
http          39824
pop3              1
smtp             19
ssh             406
ssl            4454
Name: service, dtype: int64
[ ]
df[df['service'] == 'http'].describe()


From the above table we can see that the traffic from http resp_ip_bytes is a lot more than orig_ip_bytes. This confirms an HTTP Flood attack.

HTTP flood is a type of Distributed Denial of Service (DDoS) attack in which the attacker exploits seemingly-legitimate HTTP GET or POST requests to attack a web server or application.

HTTP flood attacks are volumetric attacks, often using a botnet “zombie army”—a group of Internet-connected computers, each of which has been maliciously taken over, usually with the assistance of malware like Trojan Horses.

[ ]
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
%matplotlib inline
ax = df.boxplot(column='orig_ip_bytes')
ax


[ ]
df[df.orig_ip_bytes < 100].boxplot(column='orig_ip_bytes')



[ ]
ay = df.boxplot(column='resp_ip_bytes')
ay


[ ]

df[df.resp_ip_bytes < 50].boxplot(column='resp_ip_bytes')


[ ]
orig_norm = (df.orig_ip_bytes-df.orig_ip_bytes.mean())/(df.orig_ip_bytes.std())
resp_norm = (df.resp_ip_bytes-df.resp_ip_bytes.mean())/(df.resp_ip_bytes.std())
print('The normalized values of the originated bytes and the response bytes are:')
print('Originated Bytes:')
print(orig_norm.min(), orig_norm.max(), orig_norm.mean())
print('----------------------------------------------')
print('Response Bytes:')
print(resp_norm.min(), resp_norm.max(), resp_norm.mean())

The normalized values of the originated bytes and the response bytes are:
Originated Bytes:
-0.00778349697777859 1023.102925350542 -3.238821372398589e-14
----------------------------------------------
Response Bytes:
-0.002850813624436458 796.9581296305183 -1.543543936706034e-14
[ ]
df[df.orig_ip_bytes < 100].boxplot(column='orig_ip_bytes', by='service')
df[df.resp_ip_bytes < 100].boxplot(column='resp_ip_bytes', by='service')
from pandas.plotting import scatter_matrix
df.plot(kind = 'scatter', x='orig_ip_bytes', y = 'resp_ip_bytes')


The preceding box plots shows that huge amount of packets being sent under unidentified services (probably applications specific protocols) and the large number of packets being send via DNS shows DNS Flooding is taking place.

The scatter plot is showing a reationship between RESP bytes and ORIG bytes that was invisible earlier using box plots. When the overflow packets are being send that are larger in size the buffer overflow on the receiver's side does not allow the receiver to send a response confirming a Ping of Death attack. SYN Flood occuring when the size of ORIG and RESP packets is small and large in count.

[ ]
df.boxplot(column='id.resp_p', by='service')
df.boxplot(column='id.orig_p', by='service')


[ ]
from pandas.plotting import scatter_matrix
df.plot(kind='scatter',x='resp_ip_bytes', y='id.resp_p')


[ ]
import seaborn as sns
cmap = sns.diverging_palette(220, 10, as_cmap=True) 
g = sns.pairplot(df, height=5,
           x_vars=["id.orig_p", "id.resp_p"],
               y_vars=["orig_ip_bytes", "resp_ip_bytes"])


[ ]
sns.set(style="whitegrid")

f, ax = plt.subplots(figsize=(13, 13))

sns.heatmap(df_grouped_diff.corr(), cmap=cmap, annot=True)

f.tight_layout()


[ ]
df[df['service'] == 'ssl'].head()


[ ]
ssldf = df[df['service'] == 'ssl']
ssldf[ssldf['id.resp_p'] != 443]


[ ]
httpdf = df[df['service'] == 'http']
httpdf[httpdf['id.resp_p'] != 80]


[ ]
ssldf['resp_ip_bytes'].mean()

8450.355410866638
[ ]
httpdf['resp_ip_bytes'].mean()

4987.246961631177
SSL bytes size is more than normal, confirming malicious behaviour.

Loading…