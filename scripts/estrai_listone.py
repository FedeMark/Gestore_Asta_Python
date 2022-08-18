from pathlib import Path
import pandas as pd

RUOLI_MANTRA = ["Por", "Dd", "Ds", "Dc", "M", "E", "C", "W", "T", "A", "Pc"]


def main():
    listone = pd.read_excel("../Quotazioni_Fantacalcio_Stagione_2022_23.xlsx", header=1)

    df_c = listone[["R", "Nome", "Squadra", "FVM"]].copy()
    df_c.rename(columns={"FVM": "Valore"}, inplace=True)
    df_c.Valore = df_c.Valore.astype("int")

    path_slots = Path("C:\\Users\\feder\\GestoreAstaPython\\slots.xlsx")
    portieri = pd.read_excel(
        path_slots,
        sheet_name="Portieri",
        header=2,
    )
    difensori = pd.read_excel(
        path_slots,
        sheet_name="Difensori",
        header=2,
    )
    centrocampisti = pd.read_excel(
        path_slots,
        sheet_name="Centrocampisti",
        header=2,
    )
    attaccanti = pd.read_excel(
        path_slots,
        sheet_name="Attaccanti",
        header=2,
    )

    slots = pd.concat([portieri, difensori, centrocampisti, attaccanti])
    slots.reset_index(inplace=True, drop=True)

    df_c = df_c.merge(slots, on="Nome", how="left")
    df_c.Slot.fillna(100, inplace=True)
    df_c.SubSlot.fillna(100, inplace=True)
    df_c.Note.fillna(" ", inplace=True)
    df_c.Slot = df_c.Slot.astype("int")
    df_c.SubSlot = df_c.SubSlot.astype("int")

    df_c.to_csv("../listone_classic.csv")

    df_m = listone[["RM", "Nome", "Squadra", "FVM M"]].copy()
    df_m.rename(columns={"FVM M": "Valore"}, inplace=True)
    df_m.Valore = df_m.Valore.astype("int")

    path_slots = Path("C:\\Users\\feder\\GestoreAstaPython\\slots_mantra.xlsx")

    dfs = [
        pd.read_excel(path_slots, sheet_name=ruolo, header=3, index_col=0)
        for ruolo in RUOLI_MANTRA
    ]

    slots = pd.concat(dfs)
    slots.reset_index(inplace=True, drop=True)

    df_m = df_m.merge(slots, on="Nome", how="left")
    df_m.Fascia.fillna(100, inplace=True)
    df_m.Note.fillna(" ", inplace=True)
    df_m.Fascia = df_m.Fascia.astype("int")

    df_m.to_csv("../listone_mantra.csv")


if __name__ == "__main__":
    main()
