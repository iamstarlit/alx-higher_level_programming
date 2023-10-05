$(document).ready(() => {
  // Get div element with a 'red_header' ID
  const toggleButton = $('div#toggle_header');

  // Toogle header color
  toggleButton.click((event) => {
    // Get header element
    const header = $('header');

    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    } else {
      header.addClass('red');
    }
  });
});
