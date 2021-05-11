import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Pick a city (chicago, new york city, or washington): ").strip().lower()
        if city not in CITY_DATA:
            print("Pick a city from the list")   
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Pick a Month (january-june), or input \"all\" for all months: ").strip().lower()
        if month not in months and month != "all":
            print("Please enter a month name from the list or enter \"all\" for all months")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Pick a Day (monday-sunday), or input \"all\" for all days: ").strip().lower()
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day not in days and day != "all":
            print("Please enter a vaild day or enter \"all\" for all days")
            continue
        else:
            break
              


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        df=df[df['month']==month]

    if day != "all":
        df=df[df["day_of_week"]==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()[0]
    print("For the criteria selected above, the most common month is: {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df["day_of_week"].mode()[0]
    print("For the criteria selected above, the most common day is: {}".format(most_common_day))

    # TO DO: display the most common start hour
    most_common_start_time = df["Start Time"].mode()[0]
    print("For the criteria selected above, the most common start hour is: {}".format(most_common_start_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("For the criteria selected above, the most common start station is: {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("For the criteria selected above, the most common end station is: {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["Most Common Combination"] = df["Start Station"] + " - " + df["End Station"]
    most_common_combination = df["Most Common Combination"].mode()[0]
    print("For the criteria selected above, the most common start-end station combination is: {}".format(most_common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df["Trip Duration"].sum()
    print("Total travel time = {}".format(travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time = {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df["User Type"].value_counts()
    print("The number of types of users for each user type are: \n{}".format(count_user_type))

    # TO DO: Display counts of gender
    if "Gender" in df:
        gender = df["Gender"].value_counts()
        print ("The gender distribution for the selected criteria is as follows: \n{}".format(gender))
   
               

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = df["Birth Year"].min()
        print("The earliest bith year is: {}".format(earliest_birth_year))
        recent_birth_year = df["Birth Year"].max()
        print("The most recent birth year is: {}".format(recent_birth_year))
        common_birth_year = df["Birth Year"].mode()
        print("The most common birth year is: {}".format(common_birth_year))
        
              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
     
    row = 5
        raw_data = input('Would you like to see raw data? '
                         'Enter (yes / no) : ').lower()
        df['Start Time'] = df['Start Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        while raw_data == 'yes':
            
            print(json.dumps(df.head(row).to_dict('index'), indent=1))
            raw_data = input('Would you like to see more '
                             'raw data? Enter (yes / no) : ').lower()
            row += 5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
