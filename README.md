# Penn Labs Server Challenge

## Documentation

###Club object
* The Club object I created had lots of different components and fields to it that were necessary to keep track of.
* The first 3 fields it had were the components that were most important to scrape from the webpage.
* Another field I added was having a clubID which makes it easier to parse the JSON output to find a specific club objects, because I then dont have to deal with spaces which I would have dealt with if I searched by the name of the club.
* I added two components which were important to implement for the "favorite" part of the API. I made a favoriteCount variable which keeps track of how many Users favorite a particular club. I also made an emailList field which is a list filled with the email addresses of all of the people who favorite a club.
* I also added a comments field which is a list which keeps track of all of the comments that Users make on a specific club
* Finally, I have two fields for average rating and rating count which display what the clubs average rating is out of 5, and how many people have rated it.

###Part 1: Scraping the Data
* BeautifulSoup made scraping data from the Online Clubs with Penn easy by inspecting element and looking at the HTML. After parsing through the HTML data, I stored the clubs as a list in Python on memory of Club objects.
* Having direct access to all of the clubs through memory and then being able to loop through them on the spot made creating JSON data about the clubs easier. This also means that I can store information on the clubs in different places, both in the array and as JSON data on the webpage, relatively easily.
* I imported requests as well as urllib.request so that I could get the data from the webpage through BeautifulSoup.
* I imported the JSON dependency to convert the club data from the list into JSON

###User data
* When I created my User object, I created a few fields that I thought would be important
* The first two are the userName and emailAddress fields, which are personal information that I used to identify a particular User. The email address was particularly important in the favorite portion of the API, because I allowed a user's email address to be added to a club's mailing list if a User favorites that club.
* I also included a favoritedClubs field which is a list which contains all of the names of the clubs that a particular user favorites.
* I also have a commentsMade list which contains all of the comments that a particular user has made.
* Two of the fields that I have included I wasn't able to utilize or implement fully, but I included clubsJoined, which would be a list of the names of the clubs which a User has joined, as well as categoriesOfInterest which is a list of all of the tags that a User is interested in.

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
