from pandas import DataFrame
from beartype import beartype

@beartype
def file_compare(df1: DataFrame,df2: DataFrame,keys: str|list[str],
                 matching_cols: str|list[str],field_map1:dict=None,field_map2:dict=None):
    """
    
    """
    # Field map check
    def field_map(df,field_map,df_name):
        if field_map:
            assert all(key in df.columns for key in field_map), "ERROR: {df_name} field mapping failed. All fields in the field mapping must be in the DataFrame."
            return df.rename(field_map)
    
    # Map fields to df1
    df1 = field_map(df1,field_map1,"df1")
    
    # Map fields to df2
    df2 = field_map(df2,field_map2,"df2")

    # Merge
    df1.merge(df2,how="inner",on=keys,suffixes=("_left","_right"))

    # Map fields to df2
    for col in matching_cols:
        pass 
    # Return results
    results = True
    return results