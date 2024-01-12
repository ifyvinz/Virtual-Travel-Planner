# Virtual Travel Planner


---

[**Watch the full Youtube vidoe demomostration of this project**](https://youtu.be/d33pjNPezWQ).

---

The inspiration behind the creation of this web app was my girlfriend. She loves travels and trip planning. So i created this web app so users can create a virtual trip, have sight seeings sugessted to them and  write a blog post about their expirence and share it with other users who might interested in visiting.

#### The main features:

- Create trips

- Create a blog post

- Explore for other users experience

- Leave comments

- Edit a post

- Delete a post

- See your trip history

#### Directories and files

* The media folder contains all the images

* Planner folder
  - .github
   - workflows
    - ci.yml - Contains configuration of the github Action.

* Migrations - Contains migrated files

* Static
 -planner
  - blog.js - Contains javaScript code for DOM manupulation of blog.html
  - cookies.js - Contains javaScript for implementation cookies to be send inside an ajax function.
  - profile.js - Contains javaScript for DOM manupulation of the profile.html
  - styles.css - Contains codes for styling web pages

* templates
  - planner
   - aframe.html - This page enable a 360 view of an image using aframe library
   - allPosts.html - Displays all the blog posts
   - blog.html - Display the content of a certain post and also enable edit of the blog post.
   - comments.html - Users can leave and read comments here.
   - createPost.html - A user if Authenticated can create a blog post.
   - index.html - If a user is logged in the page displays the form that enables them to save a trip
   - layout.html - This is the base page 
   - login,html - Login Page
   - profile.html - The user's profile page. Their written blogs and trips history can be found here
   - register.html - The register page
   - save_a_trip.html - Displays suggested sight seeing images and address, map and weather of the destination
   - search.html - Displays the result of a search qury

* admin.py - Registerd the models her for the admin page

* forms.py - Contains the implementaion of classes like TripForm, PostForm, ProfileForm, CommentForm

* models.py - Contains the implementaion of classes likes User, Post, Trip, Comment for ORM

* serializer.py - Contains the implementaion of classes likes UserSerializer, PostSerializer, TripSerializer, CommentSerializer for Django rest_framework

* tests.py -  Contains the implementaion to test the Comment model

* urls.py - Contains all url paths

* views.py - Contains all view functions like login, register, logout, pagination, get_google_places_data, googlePlace, index, saveTrip,  createPost, submitPost, blogs, userProfile, editProfile, readBlog, likePost, comment_detail, editBlog, deleteBlog, search etc.

#### Justification and complexity

* I created more models and more complex relationship within like the Comment model refrencing itself as parent for replies.
* I made use of external apis, like the google place api for sight seeing suggestion and google geo location api to get a coordinate of a city and also google map api to display a map and Openweather api to get the weather data of a city

* I have mutiple javaScript file and made use of the fetch api when a user edits its profile or toggle the like button

* I used boostrap classes for styling and to make the web app responsive.

## How to run this application

---

* To install a new environment - pip install pipenv

* To activate a new environment - pipenv shell

* Install project dependencies by running pip install -r requirements.txt

* Run python manage.py makemigrations and python manage.py migrate for migration.

