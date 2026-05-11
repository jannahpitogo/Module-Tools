const fs = require("fs");
const path = require("path");

const dir = "sample-files";
const files = fs
  .readdirSync(dir)
  .filter((f) => f.endsWith(".txt"))
  .sort(); //for order of files

let lineNumber = 1;

for (const file of files) {
  const filePath = path.join(dir, file);
  const lines = fs.readFileSync(filePath, "utf-8").split("\n"); //read and split by new line

  for (const line of lines) {
    console.log(`${lineNumber}\t${line}`);
    lineNumber++;
  }
}
