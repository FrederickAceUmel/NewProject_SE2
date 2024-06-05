function validateBoxes(checkbox) {
    var checkboxes = document.querySelectorAll('input[name="special-categories"]');
    var isChecked = Array.from(checkboxes).some(cb => cb.checked);
    var errorDiv = document.getElementById('checkbox-error');

    checkboxes.forEach(function(cb) {
      cb.setCustomValidity('');
    });

    if (!isChecked) {
      errorDiv.style.display = 'block';
      checkboxes.forEach(function(cb) {
        cb.setCustomValidity('Please select at least one option.');
      });
    } else {
      errorDiv.style.display = 'none';
    }
  }