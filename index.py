from flask import Flask, request, jsonify
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.

app = Flask(__name__)

# Scraping the web data from Online Clubs with Penn website
clubSoup = soupify(get_clubs_html())
get_clubs(clubSoup)

# Populating the clubList with Club objects
clubList = []
counter = 1
for elt in get_clubs(clubSoup):
    currClub = elt
    currName = get_club_name(currClub)
    currTags = get_club_tags(currClub)
    currDescription = get_club_description(currClub)
    currClub = Club(currName, currTags, currDescription, counter)
    counter = counter + 1
    clubList.append(currClub)

# Putting the Club objects into dictionary form for JSON output
clubDictList = [elt.__dict__ for elt in clubList]
clubString = json.dumps([elt.__dict__ for elt in clubList], indent=2)


# Populating the UserList with Users objects
jen = User('jen', 'jen@seas.upenn.edu')
userList = []
userList.append(jen)

testUser = User('TEST', 'test@sas.upenn.edu')
userList.append(testUser)

# Putting the User objects into Dictionary form for JSON output
userDictList = [elt.__dict__ for elt in userList]


# Creating a commentList for when commenting commands happen
commentList = []
commentDictList = [elt.__dict__ for elt in commentList]


# Creating a ratingList for when rating commands happen
ratingList = []
ratingDictList = [elt.__dict__ for elt in ratingList]

# Main Page
@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

# Penn Club Review API
@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

# Returns all of the clubs in JSON format
@app.route('/api/clubs', methods=['GET'])
def clubs():
    return jsonify(clubDictList)


# Adds a new club to the list of clubs and returns all of the clubs
@app.route('/api/clubs', methods=['POST'])
def addAClub():

    print(request.json)
    print(request.json['name'])
    print(request.json['categories'])
    print(request.json['description'])

    currLen = len(clubList)

    newClub = Club(request.json['name'], request.json['categories'], request.json['description'], currLen + 1)

    newClubDict = newClub.__dict__
    clubDictList.append(newClubDict)

    return jsonify(clubDictList)


# Returns the User who has the specified username in JSON format
@app.route('/api/user/<string:username>', methods=["GET"])
def getuser(username):
    for user in userList:
        if user.name == username:
            return jsonify(user.__dict__)


# Returns all of the Users in JSON format
@app.route('/api/user', methods=['GET'])
def getAllUsers():
    return jsonify(userDictList)


# A User and a Club are given, and the User favorites the Club, User's email address added to club mailing list
@app.route('/api/favorite', methods=['POST'])
def favoriteClub():
    username = request.json['username']
    clubName = request.json['club']
    alreadyFavorited = False
    currUser = userList[0]

    for user in userList:
        if user.name == username:
            if clubName in user.favClubs:
                alreadyFavorited = True
            else:
                user.favClubs = user.favClubs + [clubName]
                currUser = user
    for club in clubList:
        if club.name == clubName and not alreadyFavorited:
            club.favoriteCount = club.favoriteCount + 1
            club.emailList.append(currUser.emailAddress)

    newClubDictList = [elt.__dict__ for elt in clubList]

    return jsonify(newClubDictList)


# A User and a Club are given as inputs and a User comments on a specific club. The comment is added
# to both the lists of the User and the Club
@app.route('/api/comment', methods=['POST'])
def comment():
    username = request.json['username']
    clubName = request.json['club']
    commentString = request.json['comment']

    currUser = userList[0]
    currClub = clubList[0]

    for user in userList:
        if user.name == username:
            user.commentsMade = user.commentsMade + [commentString]
            currUser = user
    for club in clubList:
        if club.name == clubName:
            club.comments = club.comments + [commentString]
            currClub = club

    newClubDictList = [elt.__dict__ for elt in clubList]

    newComment = Comment(currUser.name, currClub.name, commentString)

    commentList.append(newComment)

    newCommentDict = newComment.__dict__

    commentDictList.append(newCommentDict)

    # Returns the new list of clubs with the new comments made
    return jsonify(newClubDictList)


# Given a User, a Club, and a score, this updates the rating that is given to a specific club
@app.route('/api/rating', methods=['POST'])
def rateclub():
    clubName = ''
    personAdded = False
    score = 0
    currClub = clubList[0]
    currRating = Rating()

    for club in clubList:
        if club.clubID == request.json['clubID']:
            clubName = club.name
            currClub = club

    for rating in ratingList:
        if rating.clubName == clubName:
            currRating = rating

    if 0 < request.json['score'] <= 5 and request.json['user'] not in currRating.userList:
        score = request.json['score']
        personAdded = True

    if personAdded:
        currRating.userCount = currRating.userCount + 1
        currClub.ratingCount = currClub.ratingCount + 1
        currRating.totalSum = currRating.totalSum + score
        currRating.clubName = currClub.name
        currRating.userList.append(request.json['user'])

    newScore = 0
    if currRating.userCount != 0:
        newScore = currRating.totalSum / currRating.userCount

    type(newScore)
    print(newScore)
    currClub.rating = newScore

    if currClub.ratingCount != 0:
        newScore = currRating.totalSum / currClub.ratingCount

    currClub.rating = newScore

    newClubDictList = [elt.__dict__ for elt in clubList]

    return jsonify(newClubDictList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
