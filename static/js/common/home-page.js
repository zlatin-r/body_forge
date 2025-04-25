document.addEventListener('DOMContentLoaded', function () {
    const workoutCards = document.querySelectorAll('.workout-card');

    workoutCards.forEach(function (card) {
        card.addEventListener('click', function () {
            const workoutId = card.getAttribute('data-workout-id');
            window.location.href = `/workouts/${workoutSlug}/details/`;
        });
    });
});