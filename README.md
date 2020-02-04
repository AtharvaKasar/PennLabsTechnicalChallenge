# Penn Labs Server Challenge

## Documentation

Club object
* The Club object I created had lots of different components and fields to it that were necessary to keep track of.
* The first 3 fields it had were the components that were most important to scrape from the webpage.
* Another field I added was having a clubID which makes it easier to parse the JSON output to find a specific club objects, because I then dont have to deal with spaces which I would have dealt with if I searched by the name of the club.
* I added two components which were important to implement for the "favorite" part of the API. I made a favoriteCount variable which keeps track of how many Users favorite a particular club. I also made an emailList field which is a list filled with the email addresses of all of the people who favorite a club.
* I also added a comments field which is a list which keeps track of all of the comments that Users make on a specific club
* Finally, I have two fields for average rating and rating count which display what the clubs average rating is out of 5, and how many people have rated it.

Part 1: Scraping the Data
* BeautifulSoup made scraping data from the Online Clubs with Penn easy by inspecting element and looking at the HTML. After parsing through the HTML data, I stored the clubs as a list in Python on memory of Club objects.
* Having direct access to all of the clubs through memory and then being able to loop through them on the spot made creating JSON data about the clubs easier. This also means that I can store information on the clubs in different places, both in the array and as JSON data on the webpage, relatively easily.
* I imported requests as well as urllib.request so that I could get the data from the webpage through BeautifulSoup.
* I imported the JSON dependency to convert the club data from the list into JSON

User data
* When I created my User object, I created a few fields that I thought would be important
* The first two are the userName and emailAddress fields, which are personal information that I used to identify a particular User. The email address was particularly important in the favorite portion of the API, because I allowed a user's email address to be added to a club's mailing list if a User favorites that club.
* I also included a favoritedClubs field which is a list which contains all of the names of the clubs that a particular user favorites.
* I also have a commentsMade list which contains all of the comments that a particular user has made.
* Two of the fields that I have included I wasn't able to utilize or implement fully, but I included clubsJoined, which would be a list of the names of the clubs which a User has joined, as well as categoriesOfInterest which is a list of all of the tags that a User is interested in.

API Implementation:
* one note I'd like to make is that the route parameter ":username" given in the stub files was not working for me for my GET method, so I changed it to "<string:username>" which accomplishes the same thing. It returns the profile information of the user requested by the username.

The Features which I added On:
1. The first feature which I added on was the ability to comment. I created a Comment class which had the fields of a User, the Club they comment on, and the string content of that Comment. For both the Club and User objects, I was able to create ways for them both to keep track of the comments that other Users make on it, and the comments that they made themselves, respectively. I made this another POST command with JSON input in the API.
2. The next feature I added was an add-on to the POST method for favorite in the API. Not only can a user mark a club as favorited, and will the club's favoritedCount increase, but more importantly, the user's email address will be added to the club's mailing list. One of my main comments/critiques about Penn Clubs or the clubs system in general is that there is no direct linkage between a person and the club that they're interested in. To me, Penn Clubs seems like a directory where people can just see what kinds of clubs fit the categories they're interested in, and then go "oh, cool". There is no direct way for the club to know that this person is interested or for them to contact the people who are interested. It would help both the club in getting more people to join, and for the person to have more incentive to join a club they'd potentially like if the club was able to email them easily. This is why I implemented this feature in Penn Club Review.
3. The third feature I implemented was a rating system similar to what Penn Course Review has right now where users can rate a club out of 5, which is another useful tool for users to use aside from comments to get a good feel for the overall perception of a club. I made a Rating class which keeps track of all of the ratings made for a specific club, and I used JSON input in a POST method in the API to implement this feature. Right now, this feature is a bit buggy because when a second user makes a rating for a club, it overwrites the first rating instead of averaging it with the first rating, so I would have completely implemented that with a bit more time.

Bonus Challenge (Docker Container):
* I attempted the Docker Container bonus challenge because I am also interested in the DevOps role in Labs.
* pipenv made creating a requirements.txt file really easy via some terminal commands.
* I needed to make some additional changes to index.py in order to get the Docker image to properly connect to the server. In app.run() on index.py, I needed to add the parameters host='0.0.0.0' and port=5000 in order to expose the port from the docker to the host.  
* The Dockerfile was then a continuation of these changes that I implemented. These series of instructions would be the way to go from the docker image to the actual Flask application itself, but I did not use GUnicorn to make this docker image
* On my system, I need to run the following commands in the terminal to create and run the docker image once in the correct directory:
* docker build --tag pennclubreview .
* docker run -it -d -p 5000:5000 pennclubreview
* docker ps
* ^ the above command gives the port which the image is running on, and that port is 0.0.0.0:5000. Putting this in the browser and in Postman allows us to run the API and see the final product



## Installation
1. Click the green "use this template" button to make your own copy of this repository, and clone it.
2. Change directory into the cloned repository.
3. Install `pipenv`
   * `brew install pipenv` if you're on a Mac with [`homebrew`](https://brew.sh/) installed.
   * `pip install --user --upgrade pipenv` for most other machines.
4. Install packages using `pipenv install`.

## Developing
1. Use `pipenv run index.py` to run the project.
2. Follow the instructions [here](https://www.notion.so/pennlabs/Server-Challenge-Spring-20-5a14bc18fb2f44ba90a61ba86b6fc426).
3. Document your work in this `README.md` file.

## Submitting
Follow the instructions at on the Technical Challenge page for submission.

## Installing Additional Packages
Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.
