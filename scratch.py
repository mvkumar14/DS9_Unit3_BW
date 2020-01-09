import pandas as pd

track_list = pd.DataFrame()
df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
track_list = track_list.append(df)

print(track_list.head())
print(df.head())


# Test using sqlalchemy (OG not flask version)
# to read from the orgiinal database
# Reference: https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html

Base = automap_base()

# engine for mapping
engine = create_engine("sqlite:///songs_df.sqlite3")

# reflect Tables
Base.prepare(engine,reflect=True)

# pull out songs from the database

print(type(Base.classes))
print(Base.classes)
Songs = Base.classes

metadata = MetaData()
metadata.create_all(engine)
print(metadata.sorted_tables)
print(Base.metadata)
