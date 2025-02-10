import pandas as pd

df = pd.read_csv("Street_Tree_List-2022-01-30_FILTERED.csv", dtype=str)

# count of each species, order most to least
species_counts = df["qSpecies"].value_counts()

# top 10 species
top_species = species_counts[:10].index  

# new filtered df
filtered_df = df[df["qSpecies"].isin(top_species)]

filtered_df.to_csv("filtered_trees.csv", index=False)
