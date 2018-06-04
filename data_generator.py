# Author Surajudeen Abdulrasaq

# University of Lyon/University Jean Monnet France

"""
============================================================
Generate data, convert to seconds and generate new features
============================================================

"""


import pandas as pd
import datetime, time
#
# activity = pd.read_csv('./datas/novin.csv', sep = ',')

def convertTime(t):
    x = time.strptime(t,'%H:%M')
    return str(int(datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()))

activity = pd.read_csv('./evaluate/thirty_days.csv', sep=',',converters={'activity_end': convertTime,
                                                                'activity_begin': convertTime})

activity = pd.read_csv('./evaluate/thirtydays_final.csv', sep=',')

#generate new features
activity['activity_length'] = activity['activity_end'].subtract(activity['activity_begin'])
activity['walk_duration'] = activity['activity_length'].subtract(activity['pause'])
activity['tiredness'] = activity['pause'].divide(activity['walk_duration'])
activity['speed'] = activity['step_count'].divide(activity['walk_duration'])

activity.to_csv('./evaluate/thirtydays_final.csv', index= False)

print(activity.head())