var path = require('path'),
    fs = require("fs");
exports.privateKey = fs.readFileSync( './cert/privkey.pem').toString();
exports.certificate = fs.readFileSync('./cert/cert.pem').toString();
exports.ca = fs.readFileSync('./cert/chain.pem').toString();
