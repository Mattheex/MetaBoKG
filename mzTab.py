import pandas as pd
from collections import OrderedDict

path = './ENPKG/MouseLiver_negative.mzTab'


def mark():
    keys = ['SMH', 'SFH', 'SEH']
    header = OrderedDict((key, 0) for key in keys)
    with open(path, 'r') as f:
        n = 0
        for line in f:
            line = line.strip()
            if line:
                for key in header:
                    if line.startswith(key):
                        header[key] = n
                n += 1

    return header


def read_mz_tab(hs):
    pre_n, pre_h = None, None
    dfs = hs.copy()
    for h, n in hs.items():
        if pre_n:
            dfs[pre_h] = pd.read_csv(path, sep='\t', header=pre_n, nrows=n - pre_n - 1)
        pre_n, pre_h = n, h

    dfs[pre_h] = pd.read_csv(path, sep='\t', header=pre_n)
    return dfs


m = mark()
dfs = read_mz_tab(m)
with pd.ExcelWriter('MzTabEx.xlsx', mode='w') as writer:
    for key in dfs:
        dfs[key].to_excel(writer, sheet_name=key, index=False, na_rep='null')
