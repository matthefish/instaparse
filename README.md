# InstaParse
A module I made to aid in parsing instagram response data based off a username

##Examples

```py
import instaparse

github = instaparse.insta('github')
print(github.getprofile())

```
This would return:

`{'followers': 112502, 'follows': 19, 'posts': 154, 'is_private': False, 'Verified': True, 'bio': 'How people build software. The home of GitHub design.', 'profile_pic': 'https://instagram.fxds1-1.fna.fbcdn.net/v/t51.2885-19/s150x150/69749192_1006039403071976_3085797980561735680_n.jpg?_nc_ht=instagram.fxds1-1.fna.fbcdn.net&_nc_ohc=UEsMlPGjbLIAX8yqczX&oh=cd2f1d4fd874c8a1960b9d7d49d97610&oe=5F031DD3'}`
