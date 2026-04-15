const fs = require("fs");

const filePath = "sample-files/1.txt";

const lines = fs.readFileSync(filePath, "utf-8").split("\n");

lines.forEach((line, index) => {
  console.log(`${index + 1}\t${line}`);
});
