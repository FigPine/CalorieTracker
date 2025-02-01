document.getElementById("foodForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    // Get input values
    const foodName = document.getElementById("foodName").value;
    const servingSize = document.getElementById("servingSize").value;
    const calories = document.getElementById("calories").value;

    // Create a new list item for the food entry
    const foodList = document.getElementById("foodList");
    const foodItem = document.createElement("li");
    foodItem.textContent = `${foodName} (${servingSize}g) - ${calories} calories`;

    // Add the new food item to the list
    foodList.appendChild(foodItem);

    // Update the total calories
    updateTotalCalories(parseInt(calories));

    // Clear form inputs
    document.getElementById("foodForm").reset();
});

let totalCalories = 0;

function updateTotalCalories(calories) {
    totalCalories += calories;
    document.getElementById("totalCaloriesCount").textContent = totalCalories;
}
