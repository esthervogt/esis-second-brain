# esis-second-brain
Scripts for maintaining all processes within my Second Brain Setup, incl. all related apps and integrations

## Zotero

### Sync Zotero annotations to Readwise

Zotero annotations which include highlights and notes can be synced to Readwise. However, since the references per 
article are synced directly to Notion using Notero, a relation between both sources has to be generated per item.

Package: [zotero2readwise](https://pypi.org/project/zotero2readwise/)

Steps to take:
- get Readwise access token (and add it to your local .env file as READWISE_ACCESS_TOKEN): https://readwise.io/access_token
- create Zotero Key in profile settings: https://www.zotero.org/settings/keys
  - give library, notes and write access
  - don't forget to press "save key"
  - copy key to clipboard and save in local .env file as ZOTERO2READWISE_ACCESS_TOKEN
  - create a separate key for each application, i.e. Zoo for Zotero and Notero
- get your personal library ID (=user id) which is displayed above the table with API keys ("Your userID for use in API calls is xxxxxxx") and save it to local .env file as ZOTERO_USER_ID: https://www.zotero.org/settings/keys
- the script for running the export of annotations from Zotero to Readwise can be found in sync_zotero_annotations_to_readwise.py
  - specify whether you want to export highlights and/or notes
- Add the variables ZOTERO2READWISE_ACCESS_TOKEN, ZOTERO2READWISE_ACCESS_TOKEN, ZOTERO_USER_ID to your Github Actions Secrets
  - alternatives for syncing variables in .env: https://stackoverflow.com/questions/60176044/how-do-i-use-an-env-file-with-github-actions
- set up scheduling, i.e. using Github Actions
