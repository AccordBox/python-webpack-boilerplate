class Jumbotron {
  static selector() {
    return "[data-jumbotron]";
  }

  constructor(node) {
    this.node = node;
    console.log(`Jumbotron initialized for node: ${node}`);
    // do something here
  }
}

export default Jumbotron;
