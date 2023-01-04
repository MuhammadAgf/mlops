import logging
from google import auth
from google.cloud import storage


class GCS:

    def __init__(self, project_name):
        credentials, project = auth.default()
        self.client = storage.Client(credentials=credentials, project=project_name)

    def download_blob(self, bucket_name, file_name, remote_file_name):
        print('download',  bucket_name, file_name, remote_file_name) 
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(remote_file_name)
        blob.download_to_filename(file_name)
        return file_name

    def upload_blob(self, bucket_name, file_name, remote_file_name):
        print('upload',  bucket_name, file_name, remote_file_name) 
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(remote_file_name)
        blob.upload_from_filename(file_name)
