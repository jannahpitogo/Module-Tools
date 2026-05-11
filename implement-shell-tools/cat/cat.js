const fs = require("fs");

const data = process.argv[2];

try {
  const content = fs.readFileSync(data, "utf8");
  process.stdout.write(content);
} catch (err) {
  console.error(`cat: ${data}: No file available`);
}
