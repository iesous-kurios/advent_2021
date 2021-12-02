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
    console.log(counter);
    return counter;
};



console.log(count_increase(day1_data));


