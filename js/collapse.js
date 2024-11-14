document.addEventListener("DOMContentLoaded", function () {
  const collapses = document.querySelectorAll(".collapse");

  collapses.forEach((collapse) => {
    const checkbox = collapse.querySelector('input[type="checkbox"]');

    if (checkbox) {
      checkbox.addEventListener("change", function () {
        if (checkbox.checked) {
          collapse.classList.add("overflow-visible");
        } else {
          collapse.classList.remove("overflow-visible");
        }
      });
    }
  });
});
