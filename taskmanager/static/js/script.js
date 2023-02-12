document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // due_date date picker from materialize

  document.addEventListener('DOMContentLoaded', function() {
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}
    });
  });

  // select initialisation

  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  // collapsible code for viewing tasks, taken from materialize

  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);


