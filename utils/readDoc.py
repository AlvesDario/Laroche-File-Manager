from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

# The ID of a sample document.
DOCUMENT_ID = '1_4vWAKWhwPjGz_Bw0MTpPqcQE6PI-vK5ys3KnQLCRUs'

def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    print('The title of the document is: {}'.format(document.get('title')))
    encoded_string=document.get('body')['content'][1]['paragraph']['elements'][0]['textRun']['content']
    with open('./saidab64', 'w+') as sai: 
        sai.write(encoded_string)

if __name__ == '__main__':
    main()