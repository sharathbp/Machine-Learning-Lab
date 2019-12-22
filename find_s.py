import pandas as pd

data = pd.read_csv('find_s.csv', header=None)

count_attr = len(data.columns)-1
S = ['0',]*count_attr
print('S[0]=', S)

for row in range(len(data)):
    x, cx = data.iloc[row, :-1], data.iloc[row, -1]
    if cx:
        for i in range(len(x)):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'              
    print()
    print('S[{0}]='.format(row+1), S)
    


