# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
import json
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_account_sas, AccountSasPermissions ,ResourceTypes

def main(options: str) -> str:
    blobOptions = (json.loads(options))
    container = blobOptions['container']
    blob =  blobOptions['blob']
    account_name= os.getenv('ACCOUNT_NAME')
    account_key= os.getenv('ACCOUNT_KEY')

    sas_token = generate_account_sas(
    account_name= account_name,
    account_key= account_key,
    resource_types=ResourceTypes(object=True),
    # container_name= container,
    # blob_name = blob,
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)
    sas_uri = f"https://ragrsemo.blob.core.windows.net/{container}/{blob}?{sas_token}"
    logging.info('Task_GetSASUri---------------> %s',sas_uri)
    return sas_uri