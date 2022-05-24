document.addEventListener("DOMContentLoaded", function(event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
    // Your code to run since DOM is loaded and ready
    });

    // Expandable divs on mouse hover events
    if (document.getElementsByClassName("auto")) {
        var autos = document.getElementsByClassName("auto");
        for (var i=0; i<autos.length; i++) {
          autos[i].addEventListener("mouseover", autoOver);
          autos[i].addEventListener("mouseout", autoOut);
        }
      }
      
      function autoOver() {
        this.style.height = this.scrollHeight + "px";
      }
      
      function autoOut() {
        this.style.height = "50px";
      }

// Get users actual location on clicking get-location button. 
const findMyState = () =>{
  const location = document.querySelector('.location');

  // Success function : if location is gotten correctly...
  const success = (position) => {
    console.log(position);
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Pass the latitude and longitude to an API that will give us back the location.
    const geoApiUrl = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en'

    // Fetch data from the API.
    fetch(geoApiUrl)
    .then(res => res.json())
    .then(data => {
      console.log(data);
    })
  }

  // Error function : if location is gotten correctly...
  const error = (position) => {
    location.textContent = 'location not found.'
  }

  navigator.geolocation.getCurrentPosition(success);
}

document.querySelector('.get-location').addEventListener('click', findMyState);
