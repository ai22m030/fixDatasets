import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
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

    def step_01_clean_raw_file(self):
        result_step_1 = []
        result_step_2 = pd.DataFrame()

        for line in self.unparsed_lines:
            if ";" in line or "," in line:
                result_step_1.append(line)

        for line in result_step_1:
            semicolon_count = sum(v for k, v in Counter(line).items() if k in ';')
            comma_count = sum(v for k, v in Counter(line).items() if k in ',')
            tmp = pd.DataFrame(data=[[line, comma_count, semicolon_count]], columns=['line', 'commas', 'semicolons'])
            result_step_2 = pd.concat([result_step_2, tmp], ignore_index=True)

        

        print(result_step_2.describe())
        print(result_step_2[result_step_2.semicolons == 0 and result_step_2.commas == 0])
        plt.hist(result_step_2)
        plt.show()

        # print(result_step_2.get(['semicolons']).max())
        # exit(0)

        # write_file = open('new_' + self.filepath, 'w')
        # write_file.writelines(result_step_1)
        # write_file.close()

