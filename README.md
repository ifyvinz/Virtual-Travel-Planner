# Virtual Travel Planner


---

[**Watch the full Youtube vidoe demomostration of this project**](https://youtu.be/0fkz_RKFdwY).

---


#### The main features:

- Create trips

- Create a blog 

- Explore for other users experience

- Read and write comments

- Edit a blog

- Delete a blog

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
   - blog.html - Displays the content of a perticular blog post of a user experience in a city and also   enable edit and delete of the blog post if the user is the one who published the post.
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

* forms.py - Contains the implementaion of classes such as:
- TripForm: This uses the Trip model to create a djang model form for a trip
- PostForm: This uses the Post model to create a djang model form for a post
- ProfileForm: This uses the User model to create a djang model form for a user profile
- CommentForm: This uses the Comment model to create a djang model form for comments

* models.py - Contains the implementaion of classes likes:
- User: This enbales the creation of a user
- Post: This model was created so a user can save their experince 
- Trip: This model allow users to save their trips 
- Comment: This model allow user to save comments and replies of a post

* serializer.py - Contains the implementaion of classes likes UserSerializer, PostSerializer, TripSerializer, CommentSerializer for Django rest_framework

* tests.py -  Contains the implementaion to test the Comment model on push

* urls.py - Contains all url paths.

* views.py - Contains all view functions such as:
- login : This function enables registered users to login with their credentials
- register: allows first time users to register
- logout: logout users
- pagination: this function was created to enable the use of pagination which was used on multiple pages. - get_google_places_data: This function makes call to google place api and returns must see places and things to do in a given city
- googlePlace: This function calls the get_google_places_data function and returns the name, address and photos
- index: This is landing page of a user after they have logged in, it displays the trip form to user 
- get_lat_long: This function calls the google geoloaction api and returns the logtitude and latitude of a givien city to be used by javascript in the front end to display a location on google map
- weather: This functuntion uses the open weather api to get the weather forcast of a giving location,- saveTrip: This function saves the user created trip to the database
- createPost: This function enbale the render of the django model form for PostForm to be rendered in the template
- submitPost: This function enables the user to create and save a blog post of the expeience in a particular city.
- blogs: This function returns every blog post with pagination
- userProfile: This function returns and renders the users profile, saved trips and blog experince created of a particular user
- editProfile: This function enables a user to edit or update their profile:
- readBlog: This function enables the user to read a blog post, comment on it, edit and delete it if ther user was who created the post and it also suggest similar posts to user, using django-taggit.
- likePost: allows a user to like or dislike a post and updates the count number using fetch api in the front-end
- comment_detail: This function enables users to read, write and reply to comments on a particular post. - editBlog: This function saves the edited blog post
- deleteBlog: This function enables the delete of a particular post if the user is permitted
- search: This function enbales the user to serach for a city and get every written blog post about it,its uses icontains to filter so that searching can be easier for thr user.
- aframe: This function returns a particular post to the template to use to display image in 360 view.

#### Justification and complexity

* The inspiration behind the creation of this web app was my girlfriend. She loves travels and trip planning. So i created this web app so users can create a virtual trip, have sight seeings sugessted to them and  write a blog post about their expirence and share it with other users who might interested in visiting.

### complexity

* Four django models were created. The Comment model has more complexity with the relationship within the Comment model refrencing itself as parent for replies.

* I made use of external apis, like the google place api which returns sight seeing and things to do as a suggestion,  google geo location api was aslo use to get a coordinate of a city and google map api was used in the front-end to display google map.
Openweather api was incoporated to get the weather data forcast of a city

* I made use of the aframe library to display a photo in a 360 view

* I made use of javaScript in the front-end to enhance user friendlyness and made use of the fetch api when a user edits its profile or toggle the like button

* I used boostrap classes for styling and to make the web app responsive.

* I believe my app is distinguishable from other project in the course and complex enough for the reasons stated above.

## How to run this application

---

* To install a new environment - pip install pipenv

* To activate a new environment - pipenv shell

* Install project dependencies by running pip install -r requirements.txt

* Run python manage.py makemigrations and python manage.py migrate for migration.

