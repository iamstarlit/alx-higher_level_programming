$(document).ready(() => {
  // Get the add button
  const addItemButton = $('div#add_item');

  addItemButton.click((event) => {
    // Get the existing list
    const list = $('ul.my_list');

    // Create a new item and append it to list
    const item = '<li>Item</li>';
    list.append(item);
  });
});
