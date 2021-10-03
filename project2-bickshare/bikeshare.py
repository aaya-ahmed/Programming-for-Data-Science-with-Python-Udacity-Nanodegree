#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import datetime
import pandas as pd
import numpy as np


# In[2]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# In[3]:


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
    while(True):
        city=input("please write city : ");
        city=city.lower();
        if city in ['chicago','new york city','washington']:
            print("thank you")
            break;
        else:
            print("please : select valid city");
    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month=input("please write specific month or all : ");
        month=month.lower();
        if month in ['january','february','march','april','may','june','all']:
            print ("thank you")
            break;
        else:
            print("please : select valid month");

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day=input("please write specific day or all : ");
        day=day.lower();
        if day in['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday',  'all']:
            print ("thank you")
            break;
        else:
            print("please : select valid day");

    print('-'*40)
    return city, month, day


# In[4]:


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
    df=pd.read_csv(CITY_DATA[city]);
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime("%A")
    return df


# In[5]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].value_counts().idxmax()
    print("the most common month : ",common_month)
    # TO DO: display the most common day of week
    common_day_of_week =df['day'].value_counts().idxmax() 
    print("the most common day of week : ",common_day_of_week)
    # TO DO: display the most common start hour
    common_start_hour=df['Start Time'].dt.strftime("%H").value_counts().idxmax()
    print("the most common start hour : ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].value_counts().idxmax()
    print("most commonly used start station : ",start_station)
    # TO DO: display most commonly used end station
    end_station=df['End Station'].value_counts().idxmax()
    print("most commonly used end station : ",end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"            .format(most_common_start_end_station[0], most_common_start_end_station[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time : ",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("mean travel time : ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[8]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types=df['User Type'].value_counts()
    print("counts of user types :\n",counts_of_user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender=df['Gender'].value_counts()
        print("counts of gender :\n",counts_of_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest_year_of_birth = df['Birth Year'].min()
        recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print("earliest year of birth",earliest_year_of_birth)
        print("recent year of birth",recent_year_of_birth)
        print("most common year of birth",most_common_year_of_birth)
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def display_data(df):
    print("do you want see some of data ? [yes,no]")
    rdata =input().lower();
    if rdata == 'yes':
        print(df.head())
        print('-'*60)
    elif rdata == 'no':
        print('ok!')
        print('-'*60)
    counter =0; 
    while rdata == 'yes':
        print('do you want see more data ? [yes , no ]')
        rdata =input().lower();
        if rdata == 'yes':
            counter=counter+5
            print(df[counter:counter+5])
            print('-'*60)
        elif rdata == 'no':
            print('-'*60)
            break;


# In[10]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:




