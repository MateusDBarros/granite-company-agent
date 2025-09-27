# -*- coding: utf-8 -*-
import pandas as pd, os

def load_data(file_path):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.csv':
        df = pd.read_csv(file_path, on_bad_lines='skip')
        return [', '.join(row.astype(str)) for _, row in df.iterrows()]
    elif ext.lower() in ['.xlsx', '.xls']:
        xls = pd.ExcelFile(file_path)
        all_text = []
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            all_text.extend([', '.join(row.astype(str)) for _, row in df.iterrows()])
        return all_text
    elif ext.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return [f.read()]
    return None
