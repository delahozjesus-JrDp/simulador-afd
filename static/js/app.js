// Funciones generales de la interfaz.
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-confirm]").forEach((elemento) => {
        elemento.addEventListener("click", (evento) => {
            if (!confirm(elemento.dataset.confirm)) evento.preventDefault();
        });
    });
});
