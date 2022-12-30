import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

HEADERS = {
    "Accept": "application/json",
    "Authorization": "Bearer " + os.environ['NOTION_INTEGRATION_TOKEN'],
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def read_database(databaseId: str):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
    res = requests.request("POST", readUrl, headers=HEADERS)
    return res.json()


def update_database(databaseId: str, properties: json):
    updateUrl = f"https://api.notion.com/v1/databases/{databaseId}"
    res = requests.request(method="PATCH", url=updateUrl, headers=HEADERS, json={'properties': properties})
    return res.status_code


def read_page(pageId: str):
    readUrl = f"https://api.notion.com/v1/pages/{pageId}"
    res = requests.request("GET", readUrl, headers=HEADERS)
    return res.json()


def get_page_title(page_dict: dict):
    return page_dict['properties']['Name']['title'][0]['plain_text']


def persist_db_as_json(db):
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(db, f, ensure_ascii=False)


def create_page(databaseId):
    createUrl = 'https://api.notion.com/v1/pages'

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Description": {
                "title": [
                    {
                        "text": {
                            "content": "Review"
                        }
                    }
                ]
            },
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Amazing"
                        }
                    }
                ]
            },
            "Status": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Active"
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(newPageData)
    # print(str(uploadData))

    res = requests.request("POST", createUrl, headers=HEADERS, data=data)

    print(res.status_code)
    print(res.text)


def update_page(pageId, updateData):
    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"
    data = json.dumps(updateData)
    response = requests.request("PATCH", updateUrl, headers=HEADERS, data=data)
    print(response.status_code)
    print(response.text)


def df_to_formatted_json(df, sep="."):
    """
    The opposite of json_normalize
    """
    result = []
    for idx, row in df.iterrows():
        parsed_row = {}
        for col_label, v in row.items():
            keys = col_label.split(".")

            current = parsed_row
            for i, k in enumerate(keys):
                if i == len(keys) - 1:
                    current[k] = v
                else:
                    if k not in current.keys():
                        current[k] = {}
                    current = current[k]
        # save
        result.append(parsed_row)
    return result
