let container = document.getElementById("details");
let display = 1;

function detailsPopup() {
  if (display === 0) {
    container.style.display = "block";
    display = 1;
  } else {
    container.style.display = "none";
    display = 0;
  }
}
