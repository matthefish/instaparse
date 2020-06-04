# InstaParse
A module I made to aid in parsing instagram response data based off a username.

## Examples
### getprofile()
This will return a dictionary of profile data such as followers, following, is_verified...
```py
import instaparse

github = instaparse.insta('github')
print(github.getprofile())

```
#### This would return:

`{'followers': 112502, 'follows': 19, 'posts': 154, 'is_private': False, 'Verified': True, 'bio': 'How people build software. The home of GitHub design.', 'profile_pic': 'https://instagram.fxds1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/69749192_1006039403071976_3085797980561735680_n.jpg?_nc_ht=instagram.fxds1-1.fna.fbcdn.net&_nc_ohc=UEsMlPGjbLIAX8yqczX&oh=cd2f1d4fd874c8a1960b9d7d49d97610&oe=5F031DD3'}`

### getpost(index)
getpost will return a dictionary with data pertaining to the post you choose. Getpost can only retrieve up to the 7th most recent post.
```py
import instaparse

github = instaparse.insta('github')
print(github.getpost(1))

```
#### This would return:

`{'type_of_post': 'GraphSidecar', 'post_content': 'https://instagram.fxds1-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/63430826_120138045872791_614866485576038131_n.jpg?_nc_ht=instagram.fxds1-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=1A3m1kwEcbMAX9qxWpp&oh=1e203772870254a43f48f74e4404edf2&oe=5F02ACFF', 'caption': "Show your Pride �🌈 \nTake a peek at the inspiration f
 this year's 2019 Pride gear. Get yours today by visiting the GitHub Shop. All proceeds go to charities supporting the LGBTQIA+ community", 'likes': 1330, 'comments': 71}`

### Other methods
- getresponse() --> returns response.status_code
- loadprofile() --> used by other methodes to confirm that profile_json is not empty
