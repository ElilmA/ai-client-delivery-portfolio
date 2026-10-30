(() => {
  const buttons = Array.from(document.querySelectorAll("[data-filter]"));
  const rows = Array.from(document.querySelectorAll(".project-row"));
  if (!buttons.length || !rows.length) return;

  const applyFilter = (filter) => {
    for (const button of buttons) {
      button.classList.toggle("is-active", button.dataset.filter === filter);
    }
    for (const row of rows) {
      row.hidden = filter !== "all" && row.dataset.category !== filter;
    }
  };

  for (const button of buttons) {
    button.addEventListener("click", () => applyFilter(button.dataset.filter));
  }
})();
