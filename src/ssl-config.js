var path = require('path'),
    fs = require("fs");
exports.privateKey = fs.readFileSync(path.join(process.env.PRIVATE, '/privkey.pem')).toString();
exports.certificate = fs.readFileSync(path.join(process.env.PRIVATE, '/cert.pem')).toString();
exports.ca = fs.readFileSync(path.join(process.env.PRIVATE, '/chain.pem')).toString();
