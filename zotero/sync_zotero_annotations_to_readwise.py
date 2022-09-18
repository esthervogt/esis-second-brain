from zotero2readwise.zt2rw import Zotero2Readwise
import os
from dotenv import load_dotenv

load_dotenv()

zt_rw = Zotero2Readwise(
    readwise_token=os.getenv('READWISE_ACCESS_TOKEN'),  # Visit https://readwise.io/access_token)
    zotero_key=os.getenv('ZOTERO2READWISE_ACCESS_TOKEN'),  # Visit https://www.zotero.org/settings/keys
    zotero_library_id=os.getenv('ZOTERO_USER_ID'),  # Visit https://www.zotero.org/settings/keys
    zotero_library_type="user",  # "user" (default) or "group"
    include_annotations=True,  # Include Zotero annotations -> Default: True
    include_notes=True,  # Include Zotero notes -> Default: False
)
zt_rw.run()

# save any highlight that failed to upload to Readwise in json file
zt_rw.readwise.save_failed_items_to_json("failed_readwise_highlights.json")
