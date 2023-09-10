document.querySelector(".exit").addEventListener("click", 
function () {
  document.querySelector(".popup").style.display = "none";
  document.querySelector(".heroContainer").style.filter = "none";
});

window.addEventListener("load", function () {
  this.setTimeout(function open(event) {
    document.querySelector(".popup").style.display = "block";
  }, 1000);
});
