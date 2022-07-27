import pandas as pd


def main():
    df = pd.read_excel("../Quotazioni_Fantacalcio_Stagione_2022_23.xlsx", header=1)
    print(df.head())
    df = df[["Nome", "Squadra", "FVM"]]
    df.rename(columns={"FVM": "Valore"}, inplace=True)
    df.to_csv("../listone.csv")


if __name__ == "__main__":
    main()
