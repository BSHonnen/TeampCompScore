import csv

def read_csv_rows_to_dict(filename):
        with open(filename) as f:
            return [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]