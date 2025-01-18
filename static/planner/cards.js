document.addEventListener('DOMContentLoaded', function(){
    slidePhoto();  
    //initAutocomplete()
   
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


/*function initAutocomplete() {
    const input = document.getElementById('cityInput');
    const autocomplete = new google.maps.places.Autocomplete(input);

    autocomplete.addListener('place_changed', function() {
        const place = autocomplete.getPlace();
        console.log('City Name:', place.name);
        console.log('City Place ID:', place.place_id);
        console.log('City Coordinates:', place.geometry.location.lat(), place.geometry.location.lng());
        // You can do something with the selected place details here
    });
}*/
