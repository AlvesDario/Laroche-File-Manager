from __future__ import print_function
import os.path, pickle
import dao.document as DAODOC

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


# The ID of a sample document.
DOCUMENT_ID = '1_4vWAKWhwPjGz_Bw0MTpPqcQE6PI-vK5ys3KnQLCRUs'

SCOPES = ['https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]

def readAllFile():
    return document.get('body')['content'][1]['paragraph']['elements'][0]['textRun']['content']

def writeFile():
    return None
        # text1 = open('./teste1', 'r').read()
    # requests = [
    #      {
    #         'insertText': {
    #             'location': {
    #                 'index': 1,
    #             },
    #             'text': text1
    #         }
    #     },
    # ]

    # result = service.documents().batchUpdate(
    #     documentId=DOCUMENT_ID, body={'requests': requests}).execute()

def main():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    print('The title of the document is: {}'.format(document.get('title')))

if __name__ == '__main__':
    main()