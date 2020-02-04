from flask import Flask, request, jsonify
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.

app = Flask(__name__)

#how to store club objects?
test = soupify(get_clubs_html())
get_clubs(test)

clubList = []
counter = 1
for elt in get_clubs(test):
    currClub = elt
    # print(get_club_name(currClub))
    currName = get_club_name(currClub)
    # print(get_club_tags(currClub))
    currTags = get_club_tags(currClub)
    # print(get_club_description(currClub))
    currDescription = get_club_description(currClub)
    currClub = Club(currName, currTags, currDescription, counter)
    counter = counter + 1
    clubList.append(currClub)

clubDictList = [elt.__dict__ for elt in clubList]

clubString = json.dumps([elt.__dict__ for elt in clubList], indent=2)

# print(clubString)

jen = User('jen', 'jen@seas.upenn.edu')
userList = []
userList.append(jen)


testUser = User('TEST', 'test@sas.upenn.edu')
userList.append(testUser)

userDictList = [elt.__dict__ for elt in userList]

commentList = []

commentDictList = [elt.__dict__ for elt in commentList]


ratingList = []

ratingDictList = [elt.__dict__ for elt in ratingList]

@app.route('/')
def main():
    return "Welcome to Penn Club Review!"


@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."


@app.route('/api/clubs', methods=['GET'])
def clubs():
    return jsonify(clubDictList)


# the POST is not working
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


@app.route('/api/clubs/<string:name>', methods=['GET'])
def oneclub(name):
    club = [club for club in clubList if club.name == name]
    return jsonify({'club' : club[0]})


@app.route('/api/user/<string:username>', methods=["GET"])
def getuser(username):
    for user in userList:
        if user.name == username:
            return jsonify(user.__dict__)


@app.route('/api/user', methods=['GET'])
def getAllUsers():
    return jsonify(userDictList)


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

    #returns the new list of clubs with the new comments made
    return jsonify(newClubDictList)


@app.route('/api/allcomments', methods=['GET'])
def allcomments():
    return jsonify(commentDictList)


@app.route('/api/rating/hello', methods=['POST'])
def testRate():
    clubID = request.json['clubID']
    rating = request.json['score']

    newRating = Rating(1, rating, "test club")

    ratingList.append(newRating)

    newRatingDictList = [elt.__dict__ for elt in ratingList]

    for elt in clubList:
        if elt.clubID == clubID:
            elt.rating = 3333

    newClubDictList = [elt.__dict__ for elt in clubList]

    return jsonify(newClubDictList)


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

    currClub.rating = currRating.totalSum / currClub.ratingCount

    newClubDictList = [elt.__dict__ for elt in clubList]

    return jsonify(newClubDictList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
