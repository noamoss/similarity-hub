import pandas
from scipy.spatial import distance

with open("data/example.csv", 'r') as csvfile:
    data = pandas.read_csv(csvfile)


distance_columns = ["תכונה א", "תכונה ב", "תכונה ג", "תכונה ג", "תכונה ד"] # set the relevant columns


def extract_similar_x(df, distance_columns, index_col_name, x=1):

    data.set_index(index_col_name)  # set the data frame index

    numeric_properties = df[distance_columns] # set numeric values
    normalized_properties = (numeric_properties - numeric_properties.mean()) / numeric_properties.std() # normalize numeric columns
    normalized_properties.fillna(1, inplace=True)  # fil nans in number columns

    item_normalized = normalized_properties.loc[0]   # select item (in its normalized shape)

    similar_items =  normalized_properties.apply(lambda row: distance.euclidean(row, item_normalized), axis=1)

    # Create a new dataframe with distances.
    distance_frame = pandas.DataFrame(data={"dist": similar_items, "idx": similar_items.index})
    distance_frame.sort_values("dist", inplace=True)

    # Find the most similar item
    closest = distance_frame.iloc[1:x+1]["idx"]
    most_similar_x = data.loc[closest][index_col_name]

    return most_similar_x