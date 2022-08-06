import pandas as pd

from robinho.const import (
    FANTACALCIO_DATA_PATH,
    LISTONE_PATH,
    QUOTE_SQUADRE_PATH,
    UNDERSTAT_DATA_PATH,
)


def main():
    listone = pd.read_csv(LISTONE_PATH, index_col=0)
    understat_data = pd.read_csv(UNDERSTAT_DATA_PATH, index_col=0)
    fantacalcio_data = pd.read_csv(FANTACALCIO_DATA_PATH, index_col=0)
    quote_squadre = pd.read_csv(QUOTE_SQUADRE_PATH, index_col=0)

    print(listone.head())


if __name__ == "__main__":
    main()
