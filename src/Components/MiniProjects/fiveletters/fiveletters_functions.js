/**
 * This file contains the functions related to the Five Letters game. 
 * 
 * original source and credit for words list:
 * https://github.com/dfm/wordle/blob/main/src/words.txt
 * 
 */

// Function to read the contents of the file and retrieve a random word

async function getRandomWord() {
    try {
        // Read the contents of the file
        const response = await fetch('FiveLetters.txt');
        // Check if the fetch was successful
        if (!response.ok) {
          throw new Error(`Failed to fetch file (status ${response.status})`);
        }
        // Read the response text
        const data = await response.text();

        // const data = await fetch('FiveLetters.txt', 'utf-8');
        // // Split the file contents into an array of words (assuming one word per line)
        const words = data.split('\n');
        // Remove any empty lines
        const nonEmptyWords = words.filter(word => word.trim() !== '');
        // Select a random index
        const randomIndex = Math.floor(Math.random() * nonEmptyWords.length);
        // Retrieve and return the random word
        const randomWord = nonEmptyWords[randomIndex].trim();
        return randomWord;
    } catch (error) {
        // Handle errors, such as file not found or read error
        console.error('Error reading file:', error.message);
        throw error;
    }
}

export default getRandomWord
