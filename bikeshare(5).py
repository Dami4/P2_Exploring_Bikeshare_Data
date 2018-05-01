## Import all necessary packages and functions
import csv
import datetime
import time
import calendar
import numpy as np
import pandas as pd
from collections import Counter

#filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

City_data = {'chicago': 'chicago.csv','new_york_city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    while True:
      if city.lower() not in ('chicago', 'new york', 'washington'):
        print("Not the appropriate choice!")
      else:
        break
        
    if city.lower() == 'chicago':
      return pd.read_csv(City_data['chicago'])
    elif city.lower() == 'new york':
      return pd.read_csv(City_data['new_york_city'])
    elif city.lower() == 'washington':
      return pd.read_csv(City_data['washington'])
    else:
      return "Select one of the listed cities"
      
def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        Fill out return type and description (see get_city for an example)
        (str) Specified filter for the bike share data
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    if time_period == 'month' or time_period == 'day' or time_period == 'none':
      start_time = time.time()
    else:
      return "ERROR"

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        Fill out return type and description (see get_city for an example)
        (str) Specified month for the data
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    while True:
      if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
        print("Not the appropriate choice!")
      else:
        break
        
    if month.lower() == 'january':
      return 'January'
    elif month.lower() == 'february':
      return 'February'
    elif month.lower() == 'march':
      return 'March'
    elif month.lower() == 'april':
      return 'April'
    elif month.lower() == 'may':
      return 'May'
    elif month.lower() == 'june':
      return 'June'
    else:
      return month

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        Fill out return type and description (see get_city for an example)
        (int) Specified day of the month for the data
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    if 1 <= int(day) <= 7:
      return day
    else:
      return "There is no such day!"
	

def popular_month(city, time_period):
    '''
    Returns the most popular month for the start time.
    
    Args:
    	time_period: start time
    Returns:
    	(str) popular month for the start time.
    Question: What is the most popular month for start time?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    city_file['month'] = city_file['Start Time'].dt.month
    popular_month = city_file['month'].mode()[0]
    print('Most Popular Start Month is:', popular_month)
    

def popular_day(city, time_period):
    '''
    Returns the most popular day of week for start time
    
    Args:
    	time_period: start time
    Returns:
    	(str) popular day of the week
    	
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    city_file['day_of_week'] = city_file['Start Time'].dt.weekday_name
    popular_day = city_file['day_of_week'].mode()[0]
    print('Most Popular Start day is:', popular_day)
		
def popular_hour(city, time_period):
    '''
    Returns the most popular hour of the day for start time
    
    Args:
    	time_period: start time.
    Returns:
    	(int) popular hour of day for start time
    	
    Question: What is the most popular hour of day for start time?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    city_file['Start Time'] = pd.to_datetime(city_file['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    city_file['hour'] = city_file['Start Time'].dt.hour
    popular_hour = city_file['hour'].mode()[0]
    print('Most Popular Start hour is:', popular_hour)
    

def trip_duration(city, time_period):
    '''
    Displays the total trip duration and the average trip duration
    
    Args:
    	city_file, time_period: trip duration.
    Returns:
    	(int) total trip duration and average trip duration.
    	
    Question: What is the total trip duration and average trip duration?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    #displays the total travel time
    total_travel_time = city_file['Trip Duration'].astype(int).sum()
    print('Total Time Travel:', total_travel_time)
    #displays the mean travel time
    mean_travel_time = city_file['Trip Duration'].astype(int).mean()
    print('Mean Time Travel:', mean_travel_time)

def popular_stations(city, time_period):
    '''
    Displays the popular start station and the popular end station
    
    Args:
    	city_file, time_period: start station and end station.
    Returns:
    	(str) popular start station and popular end station
    	
    Question: What is the most popular start station and most popular end station?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    freq = Counter(city_file['Start Station'])
    print('Popular Start Station:',freq.most_common()[0][0])
    
    popular = Counter(city_file['End Station'])
    print('Popular End Station:',freq.most_common()[0][0])
    
def popular_trip(city, time_period):
    '''
    Displays the most popular trip
    
    Args:
    	city_file, time_period: trip duration.
    Returns:
    	(str) popular trip
    	
    Question: What is the most popular trip?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    #creating journey column
    city_file['journey'] = city_file['Start Station'].str.cat(city_file['End Station'], sep=' to ')
    pop_trip = city_file['journey'].mode().to_string(index = False)
    # The 'journey' column is created in the statistics() function.
    print('Most popular trip is {}.'.format(pop_trip))

    
def users(city, time_period):
    '''
    Returns the count of each user type
    
    Args:
    	user type.
    Returns:
    	(int) counts of each user type
    	
    Question: What are the counts of each user type?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    user_types = city_file['User Type'].value_counts()
    
    print(user_types)


def gender(city, time_period):
    '''
    Returns the counts of gender
    
    Args:
    	gender.
    Returns:
    	(int) counts of gender.
    	
    Question: What are the counts of gender?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    gender = city_file['Gender'].value_counts()
    
    print(gender)

def birth_years(city, time_period):
    '''
    Returns the earliest, most recent and most popular birth years
    
    Args:
    	birth year.
    Returns:
    	(int) earliest, most recent and most popular birth years.
    	
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    city_file = pd.read_csv(chicago, dtype=str)
    earliest = city_file['Birth Year'].min()
    latest = city_file['Birth Year'].max()
    most_pop = city_file['Birth Year'].mode()
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, most_pop))


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        Fill out return type and description (see get_city for an example)
        (str)response to displaying data 
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    if display == "yes" or display == "no":
      return display
    else:
      return "ERROR"

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        popular_month(city, time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    start_time = time.time()
    popular_day(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")    
    start_time = time.time()

    # What is the most popular hour of day for start time?
    popular_hour(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    gender(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    birth_years(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()