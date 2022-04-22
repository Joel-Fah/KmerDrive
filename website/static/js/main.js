/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.cssText = "top: 0; box-shadow: 5px 5px 15px #FFFFFF3D; transition: top 0.4s ease-in";
  } else {
    document.getElementById("navbar").style.cssText = "top: -80px; transition: top 0.4s ease-out";
  }
  prevScrollpos = currentScrollPos;
}