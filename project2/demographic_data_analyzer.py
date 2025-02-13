import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts()['Bachelors']/df['education'].value_counts().sum() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[df['education'].isin(['Masters', 'Bachelors', 'Doctorate'])]['education'])/len(df['education'])*100
    lower_education = len(df[~df['education'].isin(['Masters', 'Bachelors', 'Doctorate'])]['education'])/len(df['education'])*100

    # percentage with salary >50K
    higher = df[df['education'].isin(['Masters', 'Bachelors', 'Doctorate'])]
    higher_50k = higher[higher['salary'].str.startswith('>50K')]
    higher_education_rich = round(len(higher_50k['salary'])/len(higher['salary']) *100, 1)

    lower = df[~df['education'].isin(['Masters', 'Bachelors', 'Doctorate'])]
    lower_50k = lower[lower['salary'].str.startswith('>50K')]
    lower_education_rich = round(len(lower_50k['salary'])/len(lower['salary']) *100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hrs = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_hrs['salary'])

    rich_percentage = round(len(min_hrs[min_hrs['salary'].str.startswith('>50K')]['salary'])/len(min_hrs['salary']) *100, 1)

    # What country has the highest percentage of people that earn >50K?
    gr_country = df.groupby('native-country', as_index=False).agg({
        'salary': ['count', lambda x: (x.str.startswith('>50K')).sum()]
    })
    gr_country.columns = ['country', 'total_count', 'over_50k_count']
    gr_country['ratio'] = round(gr_country['over_50k_count'] / gr_country['total_count']*100,1)
    cntry = gr_country[gr_country['ratio'] ==gr_country['ratio'].max()]['country']
    highest_earning_country = cntry.tolist()[0]
    highest_earning_country_percentage = gr_country['ratio'].max()

    # Identify the most popular occupation for those who earn >50K in India.
    with_50k = df[df['salary'].str.startswith('>50K')]
    top_IN_occupation = with_50k[with_50k['native-country']=='India']['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

