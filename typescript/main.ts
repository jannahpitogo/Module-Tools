import { Person } from "./person";
const fs = require("fs");
const raw = fs.readFileSync("./person.json", "utf-8");
const data = JSON.parse(raw);


// data.forEach((item, index) => {
//     people[`person${index + 1}`] = new Person(item.name, item.surname, item.age, item.address, item.gender);
//     console.log(item)
// });

const people: Person[] = data.map((data: any) => 
new Person(data.name, data.surname, data.age, data.address, data.gender))



// const myName = new Person("Jannah", "Pitogo", 21, "Barcelona", "Female"); 
// const Person2 = new Person("Alex", "Smith", 25, "Barcelona", "male"); 
// const Person3 = new Person("Claire", "Smith", 22, "Barcelona", "Female");

// console.log('\nFull Details:');
// console.log('Person 1:', myName);
// console.log("Person 2:", Person2);
// console.log("Person 3:", Person3);

console.log(people);
