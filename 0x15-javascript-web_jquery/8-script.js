$(document).ready(() => {
  // Make a GET request to the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: (data) => {
      const movieList = $('ul#list_movies');

      // Iterate through the movies and append their titles to the list
      data.results.forEach((movie) => {
        const listItem = $('<li></li>');
        listItem.text(movie.title);
        movieList.append(listItem);
      });
    },
    error: (xhr, status, error) => {
      // Handle the error here
      console.error('Error:', error);
      const movieList = $('ul#list_movies');
      movieList.text('Error fetching movie data.');
    }
  });
});
