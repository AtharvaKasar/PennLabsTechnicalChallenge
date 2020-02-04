import requests
import urllib.request
from bs4 import BeautifulSoup
import json


# Club Object, field are specified in the readme
class Club:

    def __init__(self, clubName='', clubCategories=[], clubDescription='', clubID=0, clubFavoriteCount=0, comments=[],
                 emailList=[], rating=0, userCount=0):
        self.name = clubName
        self.categories = clubCategories
        self.description = clubDescription
        self.favoriteCount = clubFavoriteCount
        self.comments = comments
        self.emailList = emailList
        self.clubID = clubID
        self.rating = rating
        self.ratingCount = userCount


# User Object, field are specified in the readme
class User:

    def __init__(self, userName='', email='', favoritedClubs=[], joinedClubs=[], categoriesOfInterest=[],
                 commentsMade=[]):
        self.name = userName
        self.favClubs = favoritedClubs
        self.joinedClubs = joinedClubs
        self.categories = categoriesOfInterest
        self.emailAddress = email
        self.commentsMade = commentsMade


# Comment Object, field are specified in the readme
class Comment:
    def __init__(self, user='', club='', comment=''):
        self.userName = user
        self.clubName = club
        self.comment = comment


# Rating Object, field are specified in the readme
class Rating:
    def __init__(self, count=0, sum=0, club='', userList=[]):
        self.userCount = count
        self.totalSum = sum
        self.clubName = club
        self.userList = userList


def get_html(url):
    """
    Retrieve the HTML from the website at `url`.
    """
    response = requests.get(url)
    return response.text

def get_clubs_html():
    """
    Get the HTML of online clubs with Penn.
    """
    url = 'https://ocwp.apps.pennlabs.org'
    return get_html(url)

def soupify(html):
    """
    Load HTML into BeautifulSoup so we can extract data more easily

    Note that for the rest of these functions, whenever we refer to a "soup", we're refering
    to an HTML document or snippet which has been parsed and loaded into BeautifulSoup so that
    we can query what's inside of it with BeautifulSoup.
    """
    return BeautifulSoup(html, "html.parser")


def get_elements_with_class(soup, elt, cls=""):
    """
    Returns a list of elements of type "elt" with the class attribute "cls" in the
    HTML contained in the soup argument.

    For example, get_elements_with_class(soup, 'a', 'navbar') will return all links
    with the class "navbar".

    Important to know that each element in the list is itself a soup which can be
    queried with the BeautifulSoup API. It's turtles all the way down!
    """
    return soup.findAll(elt, {'class': cls})

def get_clubs(soup):
    """
    This function should return a list of soups which each correspond to the html
    for a single club.
    """
    return get_elements_with_class(soup, 'div', 'box') # TODO: Implement this function

def get_club_name(club):
    """
    Returns the string of the name of a club, when given a soup containing the data for a single club.

    We've implemented this method for you to demonstrate how to use the functions provided.
    """
    elts = get_elements_with_class(club, 'strong', 'club-name')
    if len(elts) < 1:
        return ''
    return elts[0].text

#need to access em
def get_club_description(club):
    """
    Extract club description from a soup of
    """
    elts = get_elements_with_class(club, 'em')
    if len(elts) < 1:
        return ''
    return elts[0].text

def get_club_tags(club):
    """
    Get the tag labels for all tags associated with a single club.
    """
    elts = get_elements_with_class(club, 'span', 'tag is-info is-rounded')
    if len(elts) < 1:
        return ['']
    currList = []
    for elt in elts:
        currList += [elt.text]
    return currList
