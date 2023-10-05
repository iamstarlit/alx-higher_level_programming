$(document).ready(() => {
  // Make a GET request to the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: (data) => {
      // Get character name
      const characterName = data.name;

      // Add character name to div element with character ID
      const character = $('div#character');
      character.text(characterName);
    },
    error: (xhr, status, error) => {
      // Handle the error here
      console.error('Error:', error);
      const character = $('div#character');
      character.text('Error fetching character data.');
    }
  });
});
