const fs = require("fs");
const path = require("path");

const directory= path.join(__dirname, "sample-files");


fs.readdir(directory, { withFileTypes: false }, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(".");
  console.log("..");

  files.forEach((file) => {
    console.log(file);
  });
});
