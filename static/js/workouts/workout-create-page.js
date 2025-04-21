function addExercise(element, exerciseId, exerciseName) {
    // Prevent adding duplicates
    if (document.querySelector(`#selected-exercises [data-exercise-id="${exerciseId}"]`)) {
        return;
    }

    // Create a new list item for the selected exercise
    const li = document.createElement('li');
    li.setAttribute('data-exercise-id', exerciseId);
    li.innerHTML = `${exerciseName} <span onclick="removeExercise(this, ${exerciseId})" style="cursor: pointer; color: red;">[Remove]</span>`;

    // Add to selected exercises list
    document.getElementById('selected-exercises').appendChild(li);

    // Add hidden input to the form
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'exercises';
    input.value = exerciseId;
    document.getElementById('workout-form').appendChild(input);

    // Dim the selected exercise for visual feedback
    element.style.opacity = '0.5';
    element.onclick = null; // Prevent re-adding
}

function removeExercise(element, exerciseId) {
    // Remove the list item
    element.parentElement.remove();

    // Remove the corresponding hidden input
    const input = document.querySelector(`#workout-form input[name="exercises"][value="${exerciseId}"]`);
    if (input) {
        input.remove();
    }

    // Re-enable the exercise in the available list
    const availableItem = document.querySelector(`.exercise-item[data-exercise-id="${exerciseId}"]`);
    if (availableItem) {
        availableItem.style.opacity = '1';
        availableItem.onclick = () => addExercise(availableItem, exerciseId, availableItem.textContent.trim().split(' ')[0]);
    }
}