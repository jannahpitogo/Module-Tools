const fs = require("fs");

const currentDir = __dirname;

fs.readdir(currentDir, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  files.forEach((file) => {
    console.log(file);
  });
});
