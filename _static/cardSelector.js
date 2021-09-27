document.querySelectorAll(".card").forEach((element) => {

    element.addEventListener("click", function (e) {
        let clicked = e.currentTarget;

        // Clear options
        clicked.closest('.row').querySelectorAll('.card').forEach((card) => {
            card.classList.remove("bg-success", "text-white");
            card.querySelector('input').checked = false;
        })

        // Active clicked
        let radio = clicked.querySelector("input");
        clicked.classList.add("bg-success", "text-white");
        radio.checked = true;

        event.stopPropagation();
    });
});