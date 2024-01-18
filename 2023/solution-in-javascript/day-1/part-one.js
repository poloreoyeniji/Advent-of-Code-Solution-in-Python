const fs = require('fs');

const filePath = 'C:/Users/HP/Desktop/advent-of-code-solution/2023/puzzle-input/day2.txt';
const fileContent = fs.readFileSync(filePath, 'utf-8');
const lines = fileContent.split('\n');

for(;;){
    console.log(lines);
}

// let list_of_calibration_values = [];

// lines.forEach((line) => {
//   const inner_values = [];
//   for (let i = 0; i < line.length; i++) {
//     if (!isNaN(parseInt(line[i]))) {
//       inner_values.push(line[i]);
//     }
//   }
//   const value = inner_values[0] + inner_values[inner_values.length - 1];
//   const int_value = parseInt(value);
//   list_of_calibration_values.push(int_value);
// });

// const calibration_values = list_of_calibration_values.reduce((acc, val) => acc + val, 0);
// console.log(calibration_values);
