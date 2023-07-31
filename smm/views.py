# views.py
from django.shortcuts import render, redirect
from bot.models import BotUsers
from .models import Post
from .forms import PostFormModel1
from time import sleep
from .tasks import send_photo, send_photo_by_id
from bot.credentials import THE_HOST_URL

def smm(request):
    form = PostFormModel1(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()

        post = Post.objects.last()
        title = f'<b>{post.post_title}</b>'
        userModel = BotUsers.objects.all()

        # Initialize the bot
        
        
        if str(post.image) == 'default.jpg':
            method_name = "video"
            method = "sendVideo"
            media_file = f'/media/{post.videofile}'
        else:
            method_name = "photo"
            method = "sendPhoto"
            media_file = f'/media/{post.image}'

            # Send the image to the first user and get the file_id
            if userModel:
                first_user = userModel[0]
                file_id = send_photo(f"./media/{post.image}", first_user.user_id, f'{title}\n{post.post_body}')
                # Now that the image has been sent and we have the file_id, we can delete the local copy

                # Send the image to the remaining users using the file_id
                count = 1
                for user in userModel[1:]:
                    send_photo_by_id.delay(file_id, user.user_id, f'{title}\n{post.post_body}')
                    sleep(0.1)
                    count += 1
        return redirect('success')

    return render(request, 'admin_lte/general.html', {"form": form})

def success(request):
    return render(request, "success.html")