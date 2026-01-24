
function toggleText(btn) {
    const text = btn.previousElementSibling.querySelector('.more-text');
    if (text.style.display === "none" || text.style.display === "") {
        text.style.display = "inline";
        btn.textContent = "Скрыть";
    } else {
        text.style.display = "none";
        btn.textContent = "Читать подробнее";
    }
}

