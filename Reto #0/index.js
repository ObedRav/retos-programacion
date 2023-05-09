#!/usr/bin/node
const fizzBuzz = (num) => {
  for (let i = 1; i <= num; i++) {
    const result = (i % 3 === 0 ? 'fizz' : '') + (i % 5 === 0 ? 'buzz' : '');
    console.log(result || i);
  }
};

// Call the func
fizzBuzz(100);
