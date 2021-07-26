const filter = document.querySelector(".filter-title-button")
const categorias = document.querySelector("#example");
const button_fil = document.querySelector(".button-filter");


filter.addEventListener("click", () => {
  categorias.classList.toggle("abrir");
  button_fil.classList.toggle("abrir");
});