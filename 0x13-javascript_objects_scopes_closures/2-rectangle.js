#!/usr/bin/node

// Rectangle class definition
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

// export Rectangle module
module.exports = Rectangle;
