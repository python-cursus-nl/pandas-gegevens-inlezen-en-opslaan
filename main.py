import pandas as pd

## SERIES
# Maak een Series aan zonder index
s = pd.Series(["aap", "noot", "mies"])
print(s)

# Maak een Series aan zonder index, met type `str`
s = pd.Series(["aap", "noot", "mies"], dtype="string")
# s = pd.Series(["aap", "noot", "mies"], dtype=pd.StringDtype())
print(s)

# Maak een Series aan met index
s = pd.Series(["aap", "noot", "mies"], index=["a", "b", "c"], dtype="string")
print(s)

# Haal waarde op index 'a' op
aap = s["a"]
print(aap)

# Maak een Serie op basis van een `dict`
d = {
    "a": "aap",
    "b": "noot",
    "c": "mies"
}

s = pd.Series(d).astype("string")   # Stel de dtype in op "string"

## DATAFRAMES

# Maak een DataFrame op basis van een `dict` van `Series`.
data = {
    "kolom1": s,
    "kolom2": s,
}
df = pd.DataFrame(data)
print(df.head())

# Maak een DataFrame op basis van een `dict` van lijsten
data = {
    "kolom1": [1, 2, 3],
    "kolom2": [4, 5, 6]
}
df = pd.DataFrame(data, index=["rij1", "rij2", "rij3"])
print(df.head())

# Haal een kolom op op basis van label
kolom1 = df["kolom1"]
print(kolom1)

# Haal een rij op op basis van index
rij_2 = df.loc["rij2"]
print(rij_2)
print(type(rij_2))

print(rij_2["kolom1"])

## WERKEN MET CSV
# Maak een DataFrame op basis van een `dict` van lijsten
data = {
    "kolom1": [1, 2, 3],
    "kolom2": [4, 5, 6]
}
df = pd.DataFrame(data, index=["rij1", "rij2", "rij3"])
print(df.head())

# Schrijf de DataFrame naar een CSV-bestand
df.to_csv("df1.csv", sep=";", index=False)

# Lees een CSV-bestand in naar een DataFrame
df1 = pd.read_csv("df1.csv", sep=";")
print(df1.head())

# Lees een CSV-bestand in met een datum kolom
df_datums = pd.read_csv("datums.csv", sep=";", parse_dates=["Datum"], date_format="%Y-%m-%d")
print(df_datums.dtypes)

# Lees een CSV-bestand met missende waarden in
df_missend = pd.read_csv("missend.csv", sep=";", na_values="?")
print(df_missend.head())

## EXCEL

# Lees het tweede werkblad van een Excel-bestand in
df_excel = pd.read_excel("excel.xlsx", sheet_name=1)
print(df_excel.head())

## JSON

# Maak een DataFrame en sla op als JSON
data = {
    "kolom1": [1, 2, 3],
    "kolom2": [4, 5, 6]
}
df = pd.DataFrame(data, index=["rij1", "rij2", "rij3"])
df.to_json("json-bestand.json")

# Lees een JSON bestand in
df_json = pd.read_json("json-bestand.json")
print(df_json.head())
