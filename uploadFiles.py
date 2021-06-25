import dropbox 
import os 
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,local_path, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'PNNpxshkYQIAAAAAAAAAAYWK_Q_Z0DyXNKZw8sv3XQJEY4dxyE-KTrfUNP9YP8JD'
    transferData = TransferData(access_token)

    file_from = '/Users/kushaanagarwal/Desktop/Python/Project101/project101.txt'
    file_to = '/test_dropbox/project101.txt'

    transferData.upload_file(file_from, file_to)

main()




