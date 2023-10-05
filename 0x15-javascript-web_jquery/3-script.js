// Get div element with a 'red_header' ID
const header = $('div#red_header');

// Add event handler to add class red when the user clicks
// the red_header
header.click((event) => {
  header.addClass('red');
});
