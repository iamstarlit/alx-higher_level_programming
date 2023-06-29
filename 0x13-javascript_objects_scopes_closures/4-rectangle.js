#!/usr/bin/node

// Rectangle class definition
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print rectangle
  print () {
    for (let i = 0; i < this.height; i += 1) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to rotate the Rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Method to double the Rectangle size
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// export Rectangle module
module.exports = Rectangle;
