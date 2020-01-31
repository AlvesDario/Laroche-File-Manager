const fs = require('fs');
const {google} = require('googleapis');

const credentials = require('../credentials.json')

require('../services/credsgen').generateCred();

const {client_secret, client_id, redirect_uris} = credentials.installed;
const oAuth2Client = new google.auth.OAuth2(
    client_id, client_secret, redirect_uris[0]);

oAuth2Client.setCredentials(require('../token.json'));

const main = (auth, saida, inicio, fim) => {
  const docs = google.docs({version: 'v1', auth});
  docs.documents.get({
    documentId: require('../settings.json').DOCUMENT_ID,
  }, (err, res) => {
    if (err) return console.log('The API returned an error: ' + err);
    let content = fim || inicio?
      res.data.body.content[1].paragraph.elements[0].textRun.content.substring(inicio,fim):
      res.data.body.content[1].paragraph.elements[0].textRun.content;
    saida?fs.createWriteStream(saida).write(content):console.log(content);
    console.log(`The title of the document is: ${res.data.title}`);
  });
}