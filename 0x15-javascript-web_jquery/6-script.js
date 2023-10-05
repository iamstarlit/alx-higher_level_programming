$(document).ready(() => {
  const updateHeaderButton = $('div#update_header');

  updateHeaderButton.click((event) => {
    const header = $('header');

    // Update header element text
    header.text('New Header!!!');
  });
});
