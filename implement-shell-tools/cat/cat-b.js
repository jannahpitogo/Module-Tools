const fs = require("fs");

const filePath = "sample-files/3.txt";

const lines = fs.readFileSync(filePath, "utf-8").split("\n");

let lineNumber = 1;

lines.forEach((line) => {
  if (line.trim() !== "") {
    console.log(`${lineNumber}\t${line}`);
    lineNumber++;
  } else {
    console.log("");
  }
});
