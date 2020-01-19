const fs = require('fs');

const help = () => console.log("usage: b64.js <command> [<arg1>] [<arg2>]\n\tencode\tEncode a file to another file.\n\tdecode\tDecode a file to another file.");

const printPercentage = (atual, fim) => 
    process.stdout.write(`${Math.floor((atual/fim)*100)}% ${atual} ${fim}\r`);


const encode = (entrada, saida) => {
    let destineFile = fs.createWriteStream(saida);
    let originalFile = fs.createReadStream(entrada, {encoding:'base64'});
    originalFile.pipe(destineFile);
}

const decode = (entrada, saida) => {
    let destineFile = fs.createWriteStream(saida, {encoding: 'base64'});
    let originalFile = fs.createReadStream(entrada,{encoding: 'binary'});
    originalFile.pipe(destineFile);
}