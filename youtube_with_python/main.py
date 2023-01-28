from pytube import YouTube

url = YouTube("https://www.youtube.com/watch?v=pn4XSDnaiPY")

print("***Streams***\n")
# for i in url.streams:
#    print(i)

print("\n***Download process***")
print("We will download this -> " +
      str(url.streams.filter(progressive=True).first()))
# url.streams.filter(progressive=True).first().download() # You can set resolution via filter
url_title = url.title
url_author = url.author
url_length = url.length
url_rating = url.rating
print("*" * 25)
print(
    f"Title: {url_title}\nAuthor: {url_author}\nLength: {url_length}\nRating: {url_rating}")
