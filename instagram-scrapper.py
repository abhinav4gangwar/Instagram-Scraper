from instagramy import InstagramUser
import pandas as pd

session_id = "48338665931%3A8JccSUwl1mTGNh%3A15%3AAYfe4mQPQOGYa_Be59WWty8YFbsMfzIcPQQsBu42yQ"

username_list = []
category_list = []
followers_count_list = []
following_count_list = []
verified_list = []
post_count_list = []

post_likes_mean_list = []
post_comments_mean_list = []
oldest_post_list = []

def get_instagram_data(user, category):

    user = InstagramUser(user)

    username_list.append(user.user_data["username"])
    category_list.append(category)
    followers_count_list.append(user.user_data["edge_followed_by"]['count'])
    following_count_list.append(user.user_data["edge_follow"]['count'])
    verified_list.append(user.user_data["is_verified"])
    post_count_list.append(user.user_data["edge_owner_to_timeline_media"]['count'])
    

    post_list = user.user_data["edge_owner_to_timeline_media"]['edges']

    comments = 0
    likes = 0
    for i in post_list:
        comments = comments + int(i['node']["edge_media_to_comment"]['count'])
        likes = likes + int(i['node']["edge_liked_by"]['count'])

    mean_comments = comments/len(post_list)
    mean_likes = likes/len(post_list)
    
    post_likes_mean_list.append(mean_likes)
    post_comments_mean_list.append(mean_comments)

    oldest_post = post_list[-1]['node']["taken_at_timestamp"]
    oldest_post_list.append(oldest_post)
    


user_list = pd.read_csv("top-users.csv")

for col in user_list.columns:
    for user in user_list[col]:
        print (user)
        get_instagram_data(user, col)

df = pd.DataFrame()

df ['username'] = username_list
df ['category'] = category_list
df ['followers'] = followers_count_list
df ['following'] = following_count_list
df ['verified'] = verified_list
df ['posts'] = post_count_list

df ['avg_likes'] = post_likes_mean_list
df ['avg_comments'] = post_comments_mean_list
df ['oldest_posts'] = oldest_post_list


df.to_csv("user-data.csv")







