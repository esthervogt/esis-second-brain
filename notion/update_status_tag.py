import pandas as pd
import notion.utils as u
import os
from dotenv import load_dotenv
from datetime import date
import requests

# the below snipped tries to manipulate the tags field in Notion DB

load_dotenv()
databaseId = os.getenv('DB_ID_ACTION_ITEMS')

db = u.readDatabase(databaseId)
db_df = pd.json_normalize(db, record_path=['results'])

page_ids_to_update = list(db_df.loc[(db_df['properties.Do Date.date.start'] == date.today().strftime('%Y-%m-%d')) &
                                    (db_df['properties.Tags.status.name'] != 'To Do'), 'id'])
for page_id in page_ids_to_update[:1]:
    update_data = pd.DataFrame([{'properties.Tags.status.name':'To Do'}])
    update_data_json = u.df_to_formatted_json(update_data)[0]
    u.updatePage(page_id, update_data_json)

# there seems to be some error with the formatting of the payload
# maybe check this page for reference: https://medium.com/@pratikdeshmukhlobhi2004/notion-api-with-python-916024cb9138
HEADERS = {
    "Authorization": "Bearer " + os.getenv('NOTION_INTEGRATION_TOKEN'),
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}
payload = {"properties":
               {"Status": {"status": {"name": "To Do"}}}}

updateUrl = f"https://api.notion.com/v1/pages/{'952598965f96415aab791170188ab0a0'}"
response = requests.patch(updateUrl, json=payload, headers=HEADERS)
response.text

# if __name__=="__main__":
