// This is the scss entry file
import "../styles/index.scss";

// We can import other JS file as we like
import Jumbotron from "../components/jumbotron";

window.document.addEventListener("DOMContentLoaded", function () {
  window.console.log("dom ready");

  // Find elements and initialize
  for (const elem of document.querySelectorAll(Jumbotron.selector())) {
    new Jumbotron(elem);
  }
});
