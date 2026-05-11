const fs = require("fs");

const path = "sample-files/3.txt";
const content = fs.readFileSync(path);
console.log(content.length, path);
