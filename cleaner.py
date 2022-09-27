import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter


class DataCorrector:
    def __init__(self, filepath):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        matplotlib.use('TkAgg')

        self.filepath = filepath
        file = open(filepath, 'r')
        self.unparsed_lines = file.readlines()
        self.data = None

    def step_01_clean_raw_file(self):
        raw_data = []
        prepared_data = pd.DataFrame()
        bad_rows = pd.DataFrame()

        for line in self.unparsed_lines:
            if ";" in line or "," in line:
                raw_data.append(line)

        for line in raw_data:
            semicolon_count = sum(v for k, v in Counter(line).items() if k in ';')
            comma_count = sum(v for k, v in Counter(line).items() if k in ',')
            tmp = pd.DataFrame(data=[[line, comma_count, semicolon_count]], columns=['line', 'commas', 'semicolons'])
            prepared_data = pd.concat([prepared_data, tmp], ignore_index=True)

        if np.any(prepared_data.iloc[:, 2] != int(np.quantile(prepared_data.iloc[:, 2], 0.75))) == np.bool_(
                True) or np.any(
                prepared_data.iloc[:, 1] != int(np.quantile(prepared_data.iloc[:, 1], 0.75))) == np.bool_(True):
            bad_rows = pd.concat(
                [prepared_data[prepared_data.semicolons != int(np.quantile(prepared_data.iloc[:, 2], 0.75))],
                 prepared_data[
                     prepared_data.commas != int(np.quantile(prepared_data.iloc[:, 1], 0.75))]]).drop_duplicates()

        for index, row in bad_rows.iterrows():
            if row.semicolons != int(np.quantile(prepared_data.semicolons, 0.75)):
                prepared_data.at[index, 'line'] = row.line.replace(',', ';')
                prepared_data.at[index, 'semicolons'] = int(np.quantile(prepared_data.semicolons, 0.75))
                prepared_data.at[index, 'commas'] = 0
            elif row.commas != int(np.quantile(prepared_data.commas, 0.75)):
                prepared_data.at[index, 'line'] = row.line.replace(',', '.')
                prepared_data.at[index, 'commas'] = 0

        filewriter = open(self.filepath.replace('.csv', '.tmp.csv'), 'w')
        filewriter.writelines(prepared_data.line)
        filewriter.close()

    def step_02_load_and_check_types(self):
        self.data = pd.read_csv(self.filepath.replace('.csv', '.tmp.csv'), delimiter=';')

        self.data.hist()
        plt.show()
