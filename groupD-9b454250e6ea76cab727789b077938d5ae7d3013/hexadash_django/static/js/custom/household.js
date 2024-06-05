document.getElementById("validationServer06").addEventListener("change", function () {
  var totalMembers = parseInt(this.value);
  var memberInputs = document.getElementById("memberInputs");

  // Clear previous inputs
  memberInputs.innerHTML = "";

  // Create inputs for each member
  for (var i = 0; i < totalMembers; i++) {
      var inputGroup = document.createElement("div");
      inputGroup.classList.add("col-md-4", "mb-3", "px-15");

      var nameLabel = document.createElement("label");
      nameLabel.textContent = "Name of Member " + (i + 1);
      nameLabel.classList.add("il-gray", "fs-14", "fw-500", "align-center", "mb-10");
      inputGroup.appendChild(nameLabel);

      var nameInput = document.createElement("input");
      nameInput.setAttribute("type", "text");
      nameInput.setAttribute("class", "form-control");
      nameInput.setAttribute("required", "");

      nameInput.addEventListener('input', function() {
        // Regular expression to allow only letters and a single period
        var value = this.value;
        var regex = /^[A-Za-z]*\.?[A-Za-z]*$/;
        if (!regex.test(value)) {
        // Remove last character if it doesn't match the pattern
            this.value = value.slice(0, -1);
        }
      });

      inputGroup.appendChild(nameInput);

      var ageLabel = document.createElement("label");
      ageLabel.textContent = "Age of Member " + (i + 1);
      ageLabel.classList.add("il-gray", "fs-14", "fw-500", "align-center", "mb-10");
      inputGroup.appendChild(ageLabel);

      var ageInput = document.createElement("input");
      ageInput.setAttribute("type", "number");
      ageInput.setAttribute("class", "form-control");
      ageInput.setAttribute("required", "");
      ageInput.setAttribute("min", "1");
      ageInput.setAttribute("max", "100");
      ageInput.setAttribute("step", "1");

      ageInput.addEventListener('input', function() {
        // Remove non-digits
        this.value = this.value.replace(/[^0-9]/g, '');
        // Ensure the value does not exceed 150
        if (this.value > 100) this.value = 150; 
      });

      inputGroup.appendChild(ageInput);

      memberInputs.appendChild(inputGroup);
  }

  // Show the household members section
  document.getElementById("householdMembers").classList.remove("d-none");
});

document.getElementById("householdForm").addEventListener("submit", function (event) {
  event.preventDefault();
  // Handle form submission here
});