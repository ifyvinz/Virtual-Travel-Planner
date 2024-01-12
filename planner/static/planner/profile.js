import getCookie from './cookies.js';

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#edit-form').style.display="none";
    document.querySelector('#user-trips').style.display="none";

    if (document.querySelector('#edit-button')) {
        document.querySelector('#edit-button').addEventListener('click', () => {
            showEditForm();
            hideBlogs();
            hideTrips();
        });
    }

    if (document.querySelector('#trips-button')) {
        document.querySelector('#trips-button').addEventListener('click', () => {
            hideBlogs();
            hideEditForm();
            showTrips();
        });
    }

    if(document.querySelector('#blogs-button')){
        document.querySelector('#blogs-button').addEventListener('click', () => {
            showBlogs();
            hideTrips();
            hideEditForm();
        });
    }

    if (document.querySelector('#edit-profile-form')) {
        document.querySelector('#edit-profile-form').addEventListener('submit', (e) => {
            e.preventDefault();
            submitProfile();
            hideEditForm();
            showProfileContent();
            showBlogs();
        });
    }
});

const submitProfile = async () => {
    document.querySelector('#user-name').innerHTML = "";
    document.querySelector('#user-email').innerHTML = "";
    document.querySelector('#user-about').innerHTML = "";

    const firstname = document.querySelector("#firstName-input").value;
    const lastname = document.querySelector("#lastName-input").value;
    const aboutMe = document.querySelector("#about-input").value;
    const image = document.querySelector("#image-input");
    const userName = document.querySelector('#hidden').value;

    let formData = new FormData();
    formData.append('first_name', firstname);
    formData.append('last_name', lastname);
    formData.append('about', aboutMe);
    formData.append('photo', image.files[0]);
    const csrftoken = getCookie('csrftoken');

    try {
        const response = await fetch(`editProfile`, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        });

        if(response.ok){
            const data = await response.json();
            const avatarElement = document.querySelector('.avatar');
            if (avatarElement) {
                avatarElement.style.display = "none";
            }
            document.querySelector('#profile-image').src = `${data.profile.photo}`;
            document.querySelector('#user-name').innerHTML = `${data.profile.first_name} ${data.profile.last_name}`;
            document.querySelector('#user-email').innerHTML = `${data.profile.email}`;
            document.querySelector('#user-about').innerHTML = `${data.profile.about}`;
        } else {
            console.log('Error:', response.statusText);
        }
    } catch (err) {
        console.error('Error:', err);
    }
};

const hideBlogs = () => {
    document.querySelector('#user-blogs').style.display = "none";
};

const showBlogs = () => {
    document.querySelector('#user-blogs').style.display = "block";
};

const hideTrips = () => {
    document.querySelector('#user-trips').style.display = "none";
};

const showTrips = () => {
    document.querySelector('#user-trips').style.display = "block";
};


const hideEditForm = () => {
    document.querySelector('#edit-form').style.display = "none";
};

const showEditForm = () => {
    document.querySelector('#profile-content').style.display = "none";
    document.querySelector('#edit-form').style.display = "block";
};



const showProfileContent = () => {
    document.querySelector('#profile-content').style.display = "block";
};
