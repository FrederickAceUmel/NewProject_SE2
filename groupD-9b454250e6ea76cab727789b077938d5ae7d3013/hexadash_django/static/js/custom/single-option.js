function uncheckOthers(checkbox) {
    var checkboxes = document.querySelectorAll(`input[type="checkbox"][name="${checkbox.name}"]`);
    checkboxes.forEach(function(cb) {
      if (cb !== checkbox) {
        cb.checked = false;
      }
    });
  }

  function validateCheckboxes(checkbox) {
    var checkboxes = document.querySelectorAll(`input[type="checkbox"][name="${checkbox.name}"]`);
    var isChecked = Array.from(checkboxes).some(cb => cb.checked);
    checkboxes.forEach(function(cb) {
      cb.setCustomValidity(isChecked ? '' : 'Please select at least one option');
    });
  }