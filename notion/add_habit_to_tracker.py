import sys
import os

sys.path.append(os.getcwd())
import pandas as pd
from dotenv import load_dotenv
import notion.utils as u

if __name__ == "__main__":

    load_dotenv()

    # TODO: support deletion of properties

    # get source df
    databaseId_src = os.environ['DB_ID_HABITS']
    habits_db = u.read_database(databaseId_src)
    habits_df = pd.json_normalize(habits_db, record_path=['results'])

    # filter on entries relevant for tracking
    habits_df = habits_df[(habits_df['properties.Add to tracking.checkbox'] == True) &
                          (habits_df['properties.Frequency.select.name'] == 'daily') &
                          (habits_df['archived'] == False)]

    # get page title to be added to tracking
    habit_titles = habits_df['id'].apply(u.read_page).apply(u.get_page_title)

    # get target df
    databaseId_target = os.environ['DB_ID_HABIT_TRACKER']
    habits_tracker_db = u.read_database(databaseId_target)
    habits_tracker_df = pd.json_normalize(habits_tracker_db, record_path=['results'])
    habits_tracked = set(
        [i.replace('properties.', '').split('.')[0] for i in habits_tracker_df.columns if 'properties' in i])

    # filter out existing habits
    habits_to_add = [i for i in habit_titles if i not in habits_tracked]

    # add habits to tracker db
    if len(habits_to_add) > 0:
        update_responses = {i: u.update_database(databaseId_target, properties={i: {'checkbox': {}}}) for i in
                            habits_to_add}
        print(f'Status codes for responses added to tracker: {update_responses}')
    else:
        print(f'No new habits found to add to tracker.')
