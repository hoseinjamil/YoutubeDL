import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from pytube import YouTube, Playlist, StreamQuery, CaptionQuery
from pytube.exceptions import VideoUnavailable


def index_page(request):
    return render(request, 'index/index.html')


# def download_video(request):
#     if request.method == 'POST':
#         video_url = request.POST.get('q')
#
#         try:
#             # Download video using pytube
#             youtube_video = YouTube(video_url)
#             title = youtube_video.title
#             video_id = youtube_video.video_id
#
#             # Save video information to the database
#             video = Video(title=title, video_id=video_id, url=video_url)
#             video.save()
#
#             # Trigger the download process
#             stream = youtube_video.streams.get_highest_resolution()
#             stream.download()
#
#             return render(request, 'index/success.html')  # Render success template
#         except VideoUnavailable:
#             error_message = "The video is not available."
#             return render(request, 'index/error.html', {'error_message': error_message})
#         except Exception as e:
#             # Handle other errors
#             error_message = f"An error occurred: {str(e)}"
#             return render(request, 'index/error.html', {'error_message': error_message})
#
#     return HttpResponse("Invalid request method. Use POST to download videos.")

# defining function
# def download_video(request):
#     # checking whether request.method is post or not
#     if request.method == 'POST':
#         # getting link from frontend
#         link = request.POST['q']
#         video = YouTube(link)
#
#         # setting video resolution
#         stream = video.streams.get_lowest_resolution()
#
#         # downloads video
#         stream.download()
#
#         # returning HTML page
#         return render(request, 'index/index.html')
#     return render(request, 'index/index.html')


def submit(request):
    url = request.GET['inp']
    # print("This is main url"+url)
    url2 = url[17:]
    # print("This is second url"+url2)
    url3 = url[:11]
    # print("This is third url"+url3)
    obj = YouTube(url)
    streams = obj.streams.all()
    # list of resolutions
    res = []
    for i in streams:
        res.append(i.resolution)
    # list of resollutions with no duplicates
    res = list(dict.fromkeys(res))

    # embed = url.replace("watch?v=", "embed/")
    embed = url3 + "tube.com/embed/" + url2  # slicing the main url and added "tube.com/embed/" to it to get the embed url
    # print("This is embed url"+embed)
    return render(request, "index/index.html", {"url": url, "url2": url2, "embed": embed, "res": res})


# Specify the path
path = "C:/Downloads"

# Check if the directory exists, if not, create it
if not os.path.exists(path):
    os.makedirs(path)


def download(request, pixel):
    path = "C:/Downloads"
    pi = pixel[:4]
    val = pixel[4:]
    str = "www.youtube.com/watch?v=" + val
    obj = YouTube(str)
    obj.streams.filter(progressive=True, file_extension="mp4").get_by_resolution(pi).download(path)
    print("Video downloaded successfully")
    return render(request, "index/index.html")
