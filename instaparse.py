import requests
import json 
import re

class insta(object):
    def __init__(self, username):
        self.username = username
        self.response = requests.get('https://www.instagram.com/'+ self.username)
        self.profile_json = None
        self.posts = None

    def getresponse(self):
        return self.response.status_code 
    
    def loadprofile(self):
        if self.response.status_code not in range(200, 299):
            return False
        else:
            json_match = re.search(r'window\._sharedData = (.*);</script>', self.response.text)
            profile_json = json.loads(json_match.group(1))
            profile_json = profile_json['entry_data']['ProfilePage'][0]['graphql']['user'] 
            self.profile_json = profile_json 
            return True

    def getprofile(self):
        if self.loadprofile() == False:
            return 'You must use method loadprofile() in order to be able to use getbio()'
        else:
            followers = self.profile_json['edge_followed_by']['count']
            follows = self.profile_json['edge_follow']['count']
            posts = self.profile_json['edge_owner_to_timeline_media']['count']
            self.posts = posts
            bio = self.profile_json['biography'] if self.profile_json['biography'] !='' else None
            profile_pic = self.profile_json['profile_pic_url']
            is_private = self.profile_json['is_private']
            is_verified = self.profile_json['is_verified']

            return {'followers':followers, 'follows':follows, 'posts':posts, 'is_private':is_private,'Verified':is_verified, 'bio':bio, 'profile_pic':profile_pic}

    def getpost(self, index):
        if self.loadprofile() == False:
            return 'You must use method loadprofile() in order to be able to use get_post()'
        elif index > 6:
            return 'can only fetch up to the 6th most recent post (actually the 7th but indexing amirite)'
        elif self.posts == 0:
            return 'This user has 0 posts'
        else:
            metrics = self.profile_json['edge_owner_to_timeline_media']['edges']
            type_of_post = metrics[index]['node']['__typename']
            pic = metrics[index]['node']['thumbnail_src']
            caption = metrics[index]['node']['edge_media_to_caption']['edges'][0]['node']['text']
            comments = metrics[index]['node']['edge_media_to_comment']['count']
            likes = metrics[index]['node']['edge_media_preview_like']['count']
            return {'type_of_post':type_of_post, 'post_content':pic, 'caption':caption,'likes':likes,'comments':comments}