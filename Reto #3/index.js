#!/usr/bin/node
const generate_password = () => {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = lowercase.toUpperCase();
    const digits = '0123456789';

    const allCharacters = lowercase + uppercase + digits;

    const length = Math.random() * (16 - 8) + 8;

    let password = Array.from({ length }, () => allCharacters[Math.floor(Math.random() * allCharacters.length)]).join('');

    return password;
}

console.log(generate_password())