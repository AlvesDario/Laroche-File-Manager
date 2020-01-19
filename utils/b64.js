const fs = require('fs');

const MEMORY_MAX = 15;
const MEMORY_MAX_MB = MEMORY_MAX * 1048576;

const help = () => console.log("usage: b64.js <command> [<arg1>] [<arg2>]\n\tencode\tEncode a file to another file.\n\tdecode\tDecode a file to another file.");

const printPercentage = (atual, fim) => 
    process.stdout.write(`${Math.floor((atual/fim)*100)}% ${atual} ${fim}\r`);


const encode = (entrada, saida) => {
    let destineFile = fs.createWriteStream(saida);
    let originalFile = fs.createReadStream(entrada, {encoding:'base64'});
    originalFile.pipe(destineFile);
}

const decode = (entrada, saida) => {
    let encodedFile = fs.readFileSync(entrada);
    fs.writeFileSync(saida, encodedFile.toString(), {encoding: 'base64'});
}


encode('image.jpg','bbb')
// console.log(fs.statSync('bbb'))
// decode('bbb', 'ccc.jpg');