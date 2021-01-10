# BlackPinkClassifier

Using Flickrapi to download images of blackpink members to make a classifier of the BlackPink members.

Make sure to get the non-commercial code for the api from: https://www.flickr.com/services/api/misc.api_keys.html

Before running imageDownloader.py, make sure you have a directory called train and test. Inside both train and test, have folders of each members' name (jennie, lisa, rose, jisoo).
This will download images of each members from flickr website (up to 1000 images). After the download is complete, make sure you move 10 photos of each member in random from the train folder to the test folder. 

Then after, run imageClassifier.py to evaluate and train the model.

