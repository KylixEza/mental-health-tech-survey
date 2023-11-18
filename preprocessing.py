
def drop_unused_columns(df):
    return df.drop(['index', 'Timestamp', 'Country', 'state', 'comments', 'mental_vs_physical', 'mental_health_interview', 'phys_health_interview'], axis=1)

def rename_headhers(df):
    new_headers = {
        'Age': 'age',
        'Gender': 'gender',
    }
    return df.rename(columns=new_headers)

def preprocess_nan(df):
    df = df['work_interfere'].fillna(df['work_interfere'].mode()[0])
    #df.dropna(subset=['self_employed'])
    return df

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3-Q1
    return df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]

def apply_preprocessing(df):
    df = drop_unused_columns(df)
    df = rename_headhers(df)
    df = preprocess_nan(df)
    df = remove_outliers(df)
    return df