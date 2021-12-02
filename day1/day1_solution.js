const fs = require('fs');
const text_input = require('./utils/loadText.js');


day1_data = text_input.getInputArray('day1.txt');



// iterate through array, add to a counter each time a number is greater than previous number
// if the number is greater than the previous number, add to the counter
var counter = 0;


// function that counts how many times a number is less than the next number
// if the number is less than the next number, add to the counter
function count_increase(input) {
    // iterate through array, add to a counter each time a number is less than previous number
    // if the number is less than the previous number, add to the counter
    var counter = 0;
    for (var i = 0; i < input.length; i++) {
        if (input[i] < input[i + 1]) {
            counter++;
        }
    }
    return counter;
};



console.log('Solution to part 1 is:', count_increase(day1_data));

function count_increase_part2(input) {
    // iterate through array, starting from second number, then add to a counter each time a group of three numbers
    // is less than the next group of three numbers
    // if the group of three numbers is less than the next group of three numbers, add to the counter

    var counter = 0;
    for (var i = 1; i < input.length; i++) {
        if ((input[i-1] + input[i] + input[i+1]) < (input[i] + input[i+1] + input[i + 2])) {
            counter++;
        }
    }
    return counter;
};

console.log('Solution to part 2 is:', count_increase_part2(day1_data));
