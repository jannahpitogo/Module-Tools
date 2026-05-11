const fs = require("fs");

const data = process.argv.slice(4);

for (const file of data) {
  try {
    const content = fs.readFileSync(file, "utf8");
    process.stdout.write(content);
  } catch (err) {
    console.error(`cat: ${file}: No file available`);
  }
}
