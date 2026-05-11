const fs = require("fs");
const path = require("path");

const folder = "sample-files";

const dir = path.join(__dirname, folder);
let total = 0;

fs.readdirSync(dir).forEach((f) => {
  const p = path.join(dir, f);
  if (!fs.statSync(p).isFile()) return;

  const lines = fs.readFileSync(p, "utf-8").split("\n").length;
  total += lines;

  console.log(lines, f);
});

console.log(total, "total");
