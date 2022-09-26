import pandas as pd


def save_to_file(file_name, jobs):
    df = pd.DataFrame(jobs, columns=['company', 'position', 'location', 'link'])
    df.to_csv(f'../files/{file_name}_jobs.csv', index=False)