const fs = require("fs");

const path = "sample-files/3.txt";

const lines = fs.readFileSync(path, "utf-8").split("\n").length;

console.log(lines, "sample-files/3.txt");
