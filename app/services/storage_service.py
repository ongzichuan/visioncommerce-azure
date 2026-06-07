import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

def upload_image(file_name, file_bytes):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER")

    blob_service_client = BlobServiceClient.from_connection_string(
        connection_string
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=file_name
    )

    blob_client.upload_blob(
        file_bytes,
        overwrite=True
    )

    return blob_client.url