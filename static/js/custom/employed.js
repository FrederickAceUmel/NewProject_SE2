function handleEmployment(checkbox) {
    var incomeInput = document.getElementById('validationDefault02');
    var checkboxes = document.getElementsByName('employment');
    
    // Uncheck all other checkboxes except the one clicked
    checkboxes.forEach(function(box) {
        if (box !== checkbox) {
            box.checked = false;
        }
    });

    // Enable income input only if 'Employed' checkbox is checked
    if (document.getElementById('check-un5').checked) {
        incomeInput.disabled = false;
    } else {
        incomeInput.disabled = true;
        // Clear the input if disabled
        incomeInput.value = ''; 
    }
}