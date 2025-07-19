document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("themeToggle");
  const body = document.body;
  const currentTheme = localStorage.getItem("theme");

  if (currentTheme === "light") {
    body.classList.add("light-mode");
    toggle.textContent = "🌞";
  }

  toggle.addEventListener("click", () => {
    body.classList.toggle("light-mode");
    if (body.classList.contains("light-mode")) {
      localStorage.setItem("theme", "light");
      toggle.textContent = "🌞";
    } else {
      localStorage.setItem("theme", "dark");
      toggle.textContent = "🌙";
    }
  });
});
