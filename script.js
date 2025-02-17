// Dark/light mode switch
const modeSwitch = document.getElementById("modeSwitch");
modeSwitch.addEventListener("change", function () {
  document.body.classList.toggle("dark", this.checked);
  document.body.classList.toggle("light", !this.checked);
});

// Dynamic rotating text for the position description
const positions = ["Engineer", "Pro Athlete", "Researcher", "Trader"];
let currentIndex = 0;
const positionText = document.getElementById("positionText");

function rotatePosition() {
  // Fade out
  positionText.style.opacity = 0;
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % positions.length;
    positionText.innerText = positions[currentIndex];
    // Fade in
    positionText.style.opacity = 1;
  }, 500); // Duration matches CSS transition
}

// Rotate text every 2.5 seconds
setInterval(rotatePosition, 2500);

// Section navigation: show selected section and hide others
const sectionButtons = document.querySelectorAll(".section-btn");
const sections = document.querySelectorAll(".section-content");

sectionButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const target = button.getAttribute("data-section");
    sections.forEach((sec) => {
      sec.style.display = sec.id === target ? "block" : "none";
    });
  });
});
