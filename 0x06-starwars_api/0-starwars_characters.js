#!/usr/bin/node

const request = require('request');

// Get the movieID from the command line arguments
const movieID = process.argv[2];

// Check if a movie ID was provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// API URL for the specific movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API for the movie
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie with ID ${movieId}`);
    return;
  }

  // Parse the JSON response
  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // For each character URL, make a request to get their name
  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      
      // Parse the character data and print the name
      const charData = JSON.parse(charBody);
      console.log(charData.name);
    });
  });
});
