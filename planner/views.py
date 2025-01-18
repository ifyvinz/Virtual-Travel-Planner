from django.shortcuts import render
import requests
import json
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post, Trip, Comment
from .forms import TripForm, PostForm, ProfileForm, CommentForm
from .serializer import UserSerializer, PostSerializer, TripSerializer, CommentSerializer
from geopy.geocoders import Nominatim
#from amadeus import Client, ResponseError, Location
#import openai
from datetime import datetime, timedelta, date
import re

def login_view(request):
     
    if request.method == "POST":
        
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "planner/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "planner/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "planner/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "planner/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "planner/register.html")


# I implemented a method or fumction for to help paginate the pages to avoid repitition.
def pagination(request, posts, postNumber, page_param='page'):
    page_number = int(request.GET.get(page_param) or 1)
    paginator = Paginator(posts, postNumber)
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return page_obj




def get_google_places_data(api_key, city_name):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': f'must see places and things to do in {city_name}',
        'key': api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('results', [])

def googlePlace(request, city_name):
     # Retrieve Google API key from Django settings
    google_api_key = settings.GOOGLE_API_KEY
    
    # Set default city name
    #city_name = 'Budapest'
    
    # Get Google Places data
    places = get_google_places_data(google_api_key, city_name)
    
    # Limit the places to the first 10 results
    #places = places[:10]

    # Iterate through places and add photo URL and Google Maps link
    for place in places:
        if 'photos' in place and 'name' in place:
            # Extract photo reference
            photo_reference = place['photos'][0]['photo_reference']
            # Construct photo URL
            place['photo_url'] = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&maxheight=400&photoreference={photo_reference}&key={google_api_key}'
            
            # Construct Google Maps link
            if 'place_id' in place:
                place['maps_link'] = f'https://www.google.com/maps/place/?q=place_id:{place["place_id"]}'
    
    return places

@login_required(login_url='/login')
def index(request):
    # Retrieve Google API key from Django settings
    google_api_key = settings.GOOGLE_API_KEY
    
   
    form = TripForm()
    return render(request, "planner/index.html", {
      'form': form,
      'google_api_key' : google_api_key
    })


"""
def get_lat_long(request, location):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': location,
        'key':settings.GOOGLE_API_KEY
    }

    response = requests.get(google_url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        return lat, lng
    else:
        return None

"""
def weather(request, city, country):
    api_key = settings.OPEN_WEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    # Check if 'list' key is present in the data dictionary
    if 'list' not in data:
        # Handle the absence of 'list' key
        return []

    #Extract needed data from the API response
    weather_data = []
    today = datetime.now().date()
    next_two_days = [today + timedelta(days=i) for i in range(3)]  # Current day + next 2 days

    for entry in data['list'][:3]:
        # Check if the required keys are present in each entry
        if 'dt_txt' in entry and 'main' in entry and 'weather' in entry:
            date_obj = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
            day = date_obj.date()

            # Check if the entry is for today or the next two days
            if day in next_two_days:
                day_name = date_obj.strftime('%A')  # Format to get the day name
                time_of_day = date_obj.strftime('%H:%M')  # Format to get the time of the day

                weather_info = {
                    'day': day_name,
                    'time': time_of_day,
                    'temperature': round(entry['main']['temp'] - 273.15, 2),
                    'description': entry['weather'][0]['description'],
                    'icon': entry['weather'][0]['icon'],
                }

                weather_data.append(weather_info)

    return weather_data


def get_lat_long(request, location):
    google_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': location,
        'key': settings.GOOGLE_API_KEY
    }

    try:
        response = requests.get(google_url, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()
        
        # Log the response for debugging
        print(f"Geocoding API response: {data}")
        
        if data.get('status') == 'OK' and data.get('results'):
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return lat, lng
        else:
            # Log any issues with the API response
            print(f"Geocoding failed: {data.get('status')}, {data.get('error_message', 'No details')}")
    except Exception as e:
        # Log any exceptions during the request
        print(f"Error during geocoding: {e}")

    return None


@login_required
def saveTrip(request):
    if request.method != "POST":
        return render(request, "planner/index.html")

    form = TripForm(request.POST)

    if form.is_valid():
        trip = form.save(commit=False)
        trip.owner = request.user
        trip.save()

        coordinates = get_lat_long(request, trip.destination)
        if coordinates:
            coords = {
                "latitude": coordinates[0],
                "longitude": coordinates[1],
            }
            print(f"coordinates: {coords}")

            # Calling Google Place API with request as the first argument and trip destination as the second argument
            places = googlePlace(request, trip.destination)

            # Extract the city and country for weather API
            city, country, *_ = map(str.strip, re.split(r',|-', trip.destination))
            print(f"weather api key: {settings.OPEN_WEATHER_API_KEY}")
            weather_data = weather(request, city, country)

            return render(request, "planner/save_a_trip.html", {
                "trip": trip,
                "places": places,
                "weather": weather_data,
                "coordinates": coords,
                'google_api_key': settings.GOOGLE_API_KEY,
            })
        else:
            print(f"Failed to get coordinates for {trip.destination}")
            return render(request, "planner/error.html", {
                "message": "Unable to retrieve location data. Please check your input and try again."
            })


@login_required(login_url='/login')
def createPost(request):
     # Retrieve Google API key from Django settings
    google_api_key = settings.GOOGLE_API_KEY

    form = PostForm()
    return render(request, "planner/createPost.html", {
        'form': form,
        'google_api_key':google_api_key,
    })

@login_required(login_url='/login')
def submitPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data and save the post
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            # Without this next line the tags or mamy-tomany fields won't be saved.
            form.save_m2m()

            serilizer = PostSerializer(post)
            return HttpResponseRedirect(reverse("blogs"))  # Redirect to index for now
        else:
            # If the form is not valid, you can handle it accordingly
            # For example, you can render the form again with validation errors
            return render(request, 'planner/createPost.html', {'form': form})
    else:
        # For GET requests, render the form
        form = PostForm()
        return render(request, 'planner/createPost.html', {
            'form': form}
        )

def blogs(request):
    p = Post.objects.all()
    posts = pagination(request, p, 9, page_param='page')
    return render(request, 'planner/allPosts.html', {
        'posts': posts
    })
@login_required
def userProfile(request, userName):
    try:
        user = User.objects.get(username=userName)
    except User.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    
    #form = ProfileForm(request.POST, request.FILES, instance=user)
    form = ProfileForm(instance=user)

    #Get all the blog posts of the current user
    p = Post.objects.filter(author=user)
    posts = pagination(request, p, 9, page_param='blog_page')

    #Get all the trips of the current user
    trips = Trip.objects.filter(owner=user)
    #trips = pagination(request, t, 10, page_param='trip_page')
    #print(trips)
    
    return render(request, "planner/profile.html", {
        'profile': user,
        'form': form,
        'posts': posts,
        'trips': trips,
    })

@login_required(login_url='/login')
def editProfile(request, userName):
    try:
        user = User.objects.get(username=userName)
    except User.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            serialized_user = UserSerializer(user)
            return JsonResponse({'profile': serialized_user.data}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ProfileForm(instance=user)

   
    return render(request, "planner/profile.html", {
        'profile': user,
        'form': ProfileForm(instance=user)
    })


def readBlog(request, blog_id):
    # Retrieve Google API key from Django settings
    google_api_key = settings.GOOGLE_API_KEY
    try:
        post = Post.objects.get(pk=blog_id)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    tags =  post.tags.all()
    # Fetch posts with similar tags
    similar_posts = Post.objects.filter(tags__in=post.tags.all()).exclude(pk=blog_id).distinct()[:3]
    return render(request, "planner/blog.html", {
        "post": post,
        "tags": tags,
        "similar_posts": similar_posts,
        "form": PostForm(instance=post, initial={'photo': post.photo}),
        'google_api_key':google_api_key,
    })

@login_required
def likePost(request, postID):
    #user = User.objects.get(username = request.user)
    user = request.user
    if user.is_authenticated:
        post = Post.objects.get(pk=postID)

        likes = post.likes.all()

        if user in likes:
           post.likes.remove(user)
        else:
          post.likes.add(user)
    
        serialize = PostSerializer(post)
        response ={
           'post': serialize.data
  
        }
        return JsonResponse(response, status = 203)
    return JsonResponse({"errorMessage": 'Sign in Please'}, status = 401)

def aframe(request, postID):
    post = Post.objects.get(pk=postID)
    return render(request, "planner/aframe.html", {
        'post': post,
    })

@login_required(login_url='/login')
def comment_detail(request, postID):
    post =Post.objects.get(pk=postID)
    comments = Comment.objects.filter(post=post, parent=None)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            print("content:" + " " + content)
            parent_id = form.cleaned_data['hidden']
            print("parent ID:" + " " + parent_id)
           
            parent = Comment.objects.get(pk=parent_id) if parent_id else None

            # Use the form's save method to create and save the comment
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.parent = parent
            comment.save()

            return HttpResponseRedirect(reverse("comments", kwargs={"postID": postID}))
    else:
        form = CommentForm()

    return render(request, 'planner/comments.html', {'post': post, 'comments': comments, 'form': form})

@login_required(login_url='/login')
def editBlog(request, blog_id):
    try:
        post = Post.objects.get(pk=blog_id)
    except Post.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # Process the form data and save the post
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            # Without this next line the tags or mamy-tomany fields won't be saved.
            form.save_m2m()

            serilizer = PostSerializer(post)
            return HttpResponseRedirect(reverse("readBlog", kwargs={"blog_id": blog_id}))  # Redirect to index for now
        
    return HttpResponseRedirect(reverse("readBlog", kwargs={"blog_id": blog_id}))  # Redirect to index for now

def deleteBlog(request, blog_id):
    if request.method == "POST":
        try:
           post = Post.objects.get(pk=blog_id)
           post.delete()
        except Post.DoesNotExist:
           raise Http404("No MyModel matches the given query.")
    
    return HttpResponseRedirect(reverse("blogs"))

def search(request):
    if request.method == "POST":
        city = request.POST.get('city', None)
        try:
           p = Post.objects.filter(location__icontains=city)
        except Post.DoesNotExist:
           raise Http404("Does not exist.")
        place =  googlePlace(request, city)
        posts = pagination(request, p, 9, page_param='page')
        return render(request, "planner/search.html", {
            'posts': posts,
            'place': place
        })
    return HttpResponseRedirect(reverse("index"))
    


