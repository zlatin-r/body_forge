document.addEventListener("DOMContentLoaded", function () {
    const profileMenu = document.querySelector(".dropdown-content");
    const profilePic = document.querySelector(".profile-link");

    profilePic.addEventListener("click", function (event) {
        event.stopPropagation();
        profileMenu.classList.toggle("active");
    });

    document.addEventListener("click", function (event) {
        if (!profileMenu.contains(event.target)) {
            profileMenu.classList.remove("active");
        }
    });
});
