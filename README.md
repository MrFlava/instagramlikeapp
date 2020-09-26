This app contains basic Instagram features - users (login/logout only), photos list, photo upload, stories list (implement only photos, read status required to filter only unread posts, also display only recent stories that created during last 24 hours), likes, comments tree and photo validation.

I used <a href='https://github.com/sunscrapers/djoser'>djoser</a> for register, login and logout functional and Django Rest Framework for the whole project.

Here are requests for this app:

    1. Authorization 
    
        POST
        /auth/users/ - for user's sign up.
    
        POST
        /auth/token/login - generate token for user. This request
        needs a password and a username.
    
        POST
        /auth/token/logout - logout. Need a user's token for this request.
        
    
    2. Posts
    
        POST
        api/posts/create - create a new post.
    
        GET
        api/posts/show-posts - list of all posts.
    
        POST
        api/posts/like-post - like the post you liked.
        
        POST
        api/posts/add-comment - leave a comment or reply for comment. 
    
    
    3. Stories
    
        POST
        api/stories/create - create a new story.
        
        GET
        api/stories/show-stories - list of resent unwatched stories.
        
        POST
        api/stories/watch-story - watch a story you picked.