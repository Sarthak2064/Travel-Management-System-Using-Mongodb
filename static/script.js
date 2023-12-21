(function () {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()

const costMap = {
    "Mumbai-Delhi": 1000.00,
    "Mumbai-Banglore": 2000.00,
    "Mumbai-Hydrabad": 1500.00,
    "Mumbai-Chennai": 1897.00,
    "Mumbai-Kolkata": 1699.00,
    "Mumbai-Pune": 2000.00,
    "Mumbai-Ahmedabad": 1200.00,
    "Delhi-Mumbai": 1000.00,
    "Delhi-Banglore": 2000.00,
    "Delhi-Hydrabad": 1500.00,
    "Delhi-Chennai": 1897.00,
    "Delhi-Kolkata": 1699.00,
    "Delhi-Pune": 1299.00,
    "Delhi-Ahmedabad": 1200.00,
    "Banglore-Mumbai": 1000.00,
    "Banglore-Delhi": 2000.00,
    "Banglore-Hydrabad": 1500.00,
    "Banglore-Chennai": 1897.00,
    "Banglore-Kolkata": 1699.00,
    "Banglore-Pune": 1299.00,
    "Banglore-Ahmedabad": 1200.00,
    "Hydrabad-Mumbai": 1000.00,
    "Hydrabad-Delhi": 2000.00,
    "Hydrabad-Hydrabad": 1500.00,
    "Hydrabad-Chennai": 1897.00,
    "Hydrabad-Kolkata": 1699.00,
    "Hydrabad-Pune": 1299.00,
    "Chennai-Ahmedabad": 1200.00,
    "Chennai-Mumbai": 1000.00,
    "Chennai-Delhi": 2000.00,
    "Chennai-Hydrabad": 1500.00,
    "Chennai-Chennai": 1897.00,
    "Chennai-Kolkata": 1699.00,
    "Chennai-Pune": 1299.00,
    "Chennai-Ahmedabad": 1200.00,
    "Chennai-Ahmedabad": 1200.00,
    "Kolkata-Mumbai": 1000.00,
    "Kolkata-Delhi": 2000.00,
    "Kolkata-Hydrabad": 1500.00,
    "Kolkata-Chennai": 1897.00,
    "Kolkata-Kolkata": 1699.00,
    "Kolkata-Pune": 1299.00,
    "Kolkata-Ahmedabad": 1200.00,
    "Pune-Mumbai": 1000.00,
    "Pune-Delhi": 2000.00,
    "Pune-Hydrabad": 1500.00,
    "Pune-Chennai": 1897.00,
    "Pune-Kolkata": 1699.00,
    "Pune-Pune": 1299.00,
    "Pune-Ahmedabad": 1200.00,
    "Ahmedabad-Mumbai": 1000.00,
    "Ahmedabad-Delhi": 2000.00,
    "Ahmedabad-Hydrabad": 1500.00,
    "Ahmedabad-Chennai": 1897.00,
    "Ahmedabad-Kolkata": 1699.00,
    "Ahmedabad-Pune": 1299.00,
    "Ahmedabad-Ahmedabad": 1200.00,
};

// Get references to your elements
const sourceDropdown = document.getElementById("source");
const destinationDropdown = document.getElementById("destination");
const totalCostDisplay = document.getElementById("totalCostDisplay");

// Add a "change" event listener to the source and destination dropdowns
sourceDropdown.addEventListener("change", updateCost);
destinationDropdown.addEventListener("change", updateCost);

// Define a function to calculate and update the cost
function updateCost() {
    const source = sourceDropdown.value;
    const destination = destinationDropdown.value;
    const route = source + "-" + destination;
    const cost = costMap[route];

    totalCostDisplay.value = cost;
}

// Optionally, you can call the updateCost function when the page loads
updateCost();


// document.getElementById("myForm").addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent the form from submitting

//     if (this.checkValidity()) {
//         alert("Form is valid. Submitting the form.");
//     }

//     this.classList.add("was-validated"); // Trigger Bootstrap's custom validation styles
// });
