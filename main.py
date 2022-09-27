from cleaner import DataCorrector

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = DataCorrector('assignment_datahandling_wine_exercise.csv')
    parser.step_01_clean_raw_file()
    parser.step_02_load_and_check_types()
