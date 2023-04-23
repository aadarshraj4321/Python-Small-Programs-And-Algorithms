import instaloader

# Create an instance of the Instaloader class
L = instaloader.Instaloader()

# Ask the user to enter the URL of the Reel they want to download
reel_url = input("Enter the URL of the Reel you want to download: ")

# Load the Reel metadata and download the video
print("Loading Reel metadata...")
post = instaloader.Post.from_shortcode(L.context, reel_url.split("/")[-2])
print("Downloading Reel video...")
L.download_post(post, target="#")

# Print a message to indicate that the download is complete
print("Download complete.")
