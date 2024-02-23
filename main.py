import pandas as pd


def read_file(file):
    data_db = pd.read_csv(file, sep='\t', index_col=0)
    return data_db


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    disease_sing = read_file('data/Disease_Signatures_MECFS.tsv')
    snp_table = read_file('data/SNP_table_MECFS.tsv')
    print(disease_sing)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
