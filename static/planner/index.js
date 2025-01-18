//import{getCookie, } from "./cookies.js"
import getCookie from './cookies.js';
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.google-body').style.display = 'none';
    /*if(document.querySelector('.google-body').style.display === 'block'){
        slidePhoto(); 
    }*/
    slidePhoto();  
    //initAutocomplete()
    //create_a_trip();
    document.querySelector('.form').addEventListener('submit', create_a_trip);
   
});


const slidePhoto = ()=>{
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: 1,
        spaceBetween: 25,
        centeredSlides: true,
        loop: true,
        fade: true,
        slidesPerGroupSkip: 1,
        grabCursor: true,
        loopFillGroupWithBlank: true,
        keyboard: {
            enabled: true,
        },
        breakpoints: {
            0:{
                slidesPerView: 1,
                slidesPerGroup: 1,
            },
            768: {
                slidesPerView: 3,
                slidesPerGroup: 3,
            },
            968: {
                slidesPerView: 3,
                slidesPerGroup: 3,
            },
        },
        scrollbar: {
            el: ".swiper-scrollbar",
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
            dynamicBullets: true,
        },
    });
    
}


const create_a_trip  = async (event) =>{
    event.preventDefault()
    const destination = document.querySelector('#cityInput')
    const purpose = document.querySelector('#reason')
    const departure = document.querySelector('#departure-date')
    const arrival = document.querySelector('#arrival-date')
    const csrftoken = getCookie('csrftoken');
    console.log('CSRF Token:', csrftoken); 

    console.log('Form Data:', {
        destination: destination.value,
        purpose: purpose.value,
        departure: departure.value,
        arrival: arrival.value,
    });
   
    try{
      const response = await fetch('createTrip', {
        method: 'POST',
        credentials: 'same-origin',
        
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken},
        body: JSON.stringify({
            destination: destination.value,
            purpose:  purpose.value,
            departure: departure.value,
            arrival: arrival.value,
        })
       })
       if (response.ok) {
           const data = await response.json();
           console.log(data.trip);
           console.log(data.trip.destination);
           console.log('Places:', data.places);
    
           const content = document.querySelector('.card-content');
        
           // Use map to create an array of HTML strings
           const placesHTML = data.places.map(place => {
               console.table(place.name + ':' + place.formatted_address);
              
               // Return the HTML string for each place
               return `
                   <div class="cards swiper-slide">
                       <a href="${place.maps_link}" target="_blank">
                           <img src="${place.photo_url}" alt="Place Photo" style="height: 300px;" class="img-fluid">
                       </a>
                       <div class="title">
                           <h3>${place.name}</h3>
                       </div>
                       <div class="content">
                           <p>${place.formatted_address}</p>
                           <!-- Add a button to show place on the map -->
                           <button class="btn btn-primary" onclick="showPlaceOnMap(${place.geometry.location.lat}, ${place.geometry.location.lng})">Show on Map</button>
                       </div>
                   </div>
               `;
           });
    
           // Join the array of HTML strings and set as innerHTML
           content.innerHTML = placesHTML.join('');

           //update the h1 containing the city title
           document.querySelector('.citiy-header').innerHTML = `Your trip to ${data.trip.destination} is saved`;
           document.querySelector('.google-body').style.display = 'block'
       } else {
        console.error('Error:', response.statusText);
       }
            
    }catch(err){
      console.log(err)
    }
  }

