# Helper Functions

def remove_outliers(df, column):
    q1 = df[column].quartile(0.25)
    q2 = df[column].quartile(0.75)
    iqr = q3 - q1
    
    up_limit = q3 + 1.5 * iqr
    low_limit = q1 - 1.5 * iqr
    
    filtered_df = df.loc[(df[column] > up_limit) & (df[column] < low_limit)]
    
    return filtered_df
    
