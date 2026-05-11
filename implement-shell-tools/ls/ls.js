const fs = require("fs");

const directory = "sample-files"; 

fs.readdir(directory, (err, files) => {
  if (err) {
    console.error(err);
    return;
  }

  files.forEach((file) => {
    console.log(file);
  });
});
