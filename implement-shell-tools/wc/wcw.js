const fs = require("fs");

const path = "sample-files/3.txt";

const content = fs.readFileSync(path, "utf-8");
const words = content.trim() ? content.trim().split(/\s+/).length : 0;

console.log(words, "sample-files/3.txt");
