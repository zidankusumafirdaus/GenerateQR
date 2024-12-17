document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".qr-button");
  const sections = document.querySelectorAll(".qr-section");

  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      const target = this.getAttribute("data-target");

      sections.forEach((section) => {
        if (section.id === target) {
          section.classList.remove("hidden");
        } else {
          section.classList.add("hidden");
        }
      });
    });
  });
});
