document.addEventListener("DOMContentLoaded", function () {
    const clickLink = document.querySelector(".delete-link");
    const deleteBox = document.querySelector(".delete-box-wrapper");
    const backgroundOverlay = document.querySelector(".background-overlay");

    clickLink.addEventListener("click", function (event) {
        event.preventDefault();
        deleteBox.classList.add("active");
        backgroundOverlay.classList.add("active");
    });

    document.addEventListener("click", function (event) {
        const clickedOutside = !deleteBox.contains(event.target) && !clickLink.contains(event.target);

        if (clickedOutside) {
            deleteBox.classList.remove("active");
            backgroundOverlay.classList.remove("active");
        }
    });
});

