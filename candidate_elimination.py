import pandas as pd

data = pd.read_csv('ce_data.csv', header=None)

count_attr = len(data.columns)-1
S = ['0',]*count_attr
G = [('?',)*count_attr]
print('G[0]=', G)
print('S[0]=', S)

#domain = [set(data[col]) for col in range(count_attr)]

def consistent(hypothesis, sample):
    for hx, sx in zip(hypothesis, sample):
        if hx != '?' and hx != sx:
            return False
    return True

def more_general(a, b):
    for xa, xb in zip(a, b):
        if xa!='?' and (xb=='?' or xb!=xa):
            return False
    return True

for row in range(len(data)):
    domain = [set(data.iloc[:row+1, col]) for col in range(count_attr)]
    x, cx = data.iloc[row, :-1], data.iloc[row, -1]
    if cx:
        for i in range(len(x)):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'              
    else:
        for g in list(G):
            if consistent(g, x):
                G.remove(g)
                for i in range(len(g)):
                    if g[i] == '?':
                        for dom in domain[i]:
                            h = list(g)
                            h[i] = dom
                            if not consistent(h, x):
                                G.append(tuple(h))
                
        general = []
        for i in range(len(G)-1):
            for j in range(i+1, len(G)):
               if more_general(G[i], G[j]):
                   general.append(G[j])
               elif more_general(G[j], G[i]):
                   general.append(G[i])
        for gen in general:
            G.remove(gen)
        
    for g in list(G):
    		for sx, gx in zip(S, g):
    			if gx == '?':
    				continue
    			if (sx == '?' or sx != gx) and sx != '0':
    				G.remove(g)
    				break
    print()       
    print('G[{0}]='.format(row+1), G)    
    print('S[{0}]='.format(row+1), S)
    



