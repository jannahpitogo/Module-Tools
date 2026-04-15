const fs = require("fs");

const args = process.argv.slice(2);

let displayLine = false;
let data;

if (args[0] === "-n") {
  displayLine = true;
  data = args[1]; //script path
} else {
  data = args[0]; //node path
}

try {
  const content = fs.readFileSync(data, "utf8"); //read the file
  const lines = content.split("\n"); //splitting it to new line

  lines.forEach((line, index) => {
    if (displayLine) {
      const number = String(index + 1).padStart(6);
      console.log(`${number}\t${line}`);
    } else {
      console.log(line);
    }
  });
} catch (err) {
  console.error(`cat: ${data}: No file available`);
}
