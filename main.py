from cleaner import DataCorrector
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    data = pd.read_csv('assignment_datahandling_wine_exercise.csv', skiprows=[0, 52, 53, 144], header=0, skipfooter=1,
                       engine='python', delimiter=';')
    print(data.head())
    print(data.columns)
    print(data.index)
    print(data.dtypes)
    print(data.alcohol.hist)
    print(data.describe())
    plt.hist(data)
    plt.title("Histogram mit default Anzahl an Bins")
    plt.xlabel("PS")
    plt.ylabel("Häufigkeit")
    plt.show()
    '''
    parser = DataCorrector('assignment_datahandling_wine_exercise.csv')
    parser.step_01_clean_raw_file()
