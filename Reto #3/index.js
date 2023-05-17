#!/usr/bin/node
const generate_password = () => {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = lowercase.toUpperCase();
    const digits = '0123456789';

    const allCharacters = lowercase + uppercase + digits;

    const length = Math.random() * (16 - 8) + 8;

    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allCharacters.length);
        const randomElement = allCharacters[randomIndex];
        password += randomElement;
    }

    return password;
}

console.log(generate_password())