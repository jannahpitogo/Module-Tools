const fs = require("fs");
const path = require("path");

const dir = path.join(__dirname, "sample-files");
const files = fs.readdirSync(dir);

let tL = 0,
  tW = 0,
  tB = 0;

for (const f of files) {
  const p = path.join(dir, f);
  if (!fs.statSync(p).isFile()) continue;

  const c = fs.readFileSync(p, "utf-8");
  const l = c.split("\n").length;
  const w = c.trim() ? c.trim().split(/\s+/).length : 0;
  const b = Buffer.byteLength(c);

  tL += l;
  tW += w;
  tB += b;

  console.log(l, w, b, f);
}

if (files.length > 1) console.log(tL, tW, tB, "total");
