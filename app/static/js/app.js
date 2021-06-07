const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  links.forEach(link => {
    link.classList.toggle("fade");
  });
});

const filter = document.querySelector(".filter-title-button")
const categorias = document.querySelector("#example");
const button_fil = document.querySelector(".button-filter");


filter.addEventListener("click", () => {
  categorias.classList.toggle("abrir");
  button_fil.classList.toggle("abrir");
});