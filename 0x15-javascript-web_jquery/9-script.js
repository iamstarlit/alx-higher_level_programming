$(document).ready(() => {
  // Make a GET request to the URL
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: (data) => {
      // Extract the translation of "hello" from the response
      const helloTranslation = data.hello;

      // Select the div#hello element and set its text content to the translation
      const helloDiv = $('#hello');
      helloDiv.text(helloTranslation);
    },
    error: (xhr, status, error) => {
      // Handle the error here
      console.error('Error:', error);
      const helloDiv = $('#hello');
      helloDiv.text('Error fetching translation.');
    }
  });
});
