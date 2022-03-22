import numpy as np
import pandas as pd
import re

pd.set_option('display.max_colwidth', None)

# read csv file
df = pd.read_csv('dataset_jeopardy.csv')

# remove white spaces from column names
df.columns = df.columns.str.strip()
df = df.dropna()

# convert Question columns to string dtype
df['Question'] = df.Question.astype("string").apply(lambda x: re.sub(r"<[^<>]*>", "", x))

# Convert the "Value" column to floats
df['Value'] = df['Value'].dropna()
df['Value'] = pd.to_numeric(df['Value'].str.replace('\D', ''))

df.head(2)
df.info()

# Provide insights on questions difficulty and value
def difficulty_filter(dataset):
    """
    Function description
        Inputs:
            dataset > DataFrame with at least a 'Value' column
        Output:
            string with mean, max and mean values
    """
    difficulty_mean = 'Average value: $' + str(round(dataset['Value'].mean()))
    difficulty_max = 'Maximum value: $' + str(round(dataset['Value'].max()))
    difficulty_min = 'Minimum value: $' + str(round(dataset['Value'].min()))
    return difficulty_mean, difficulty_max, difficulty_min
# difficulty_filter(function_test)

# Match questions with word from list of words
def jeopardy_filter(dataset, words):
    """
    Function description
        Inputs:
            dataset > DataFrame with at least a 'Question' column
            words > list of words to look for in the 'Question' column
        Output:
            Filtered DataFrame with matching questions!
    """
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    new_df = dataset.loc[dataset["Question"].apply(filter)]
    return new_df

# returns the count of the unique answers to all of the questions in a dataset 
def count_unique_answers(df_filtered):
    """
     Function description
        Inputs:
            df_filtered > df filtered with jeopardy_filter()
        Output:
            size of Answer column and number of unique answers
    """
    count_answers = df_filtered['Answer'].size
    count_unique_answers = df_filtered['Answer'].unique().size
    return print('For a total of {c_answer} answers, {cu_answer} are unique'.format(c_answer=count_answers, cu_answer=count_unique_answers))

function_test = jeopardy_filter(df, ['king', 'england'])
count_unique_answers(function_test)
