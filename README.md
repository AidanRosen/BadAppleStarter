# What is this?
I've seen Bad Apple memes on the internet but it always looked intimidating just to get started, and googling didn't make it seem like started code already existed. Fortunately, the process has two distinct parts: getting the Bad Apple data (abstracting it), then adapting it to whatever medium you're trying to put it on. The first part is what this repo is all about, providing all the tools that go into getting the data from downloading the video to having 3D arrays of each frame such that anyone can pull it out of the box or modify the process as needed.

<br>
To be really plain, you could just download the json file uploaded here if all you need is frame data. It's a 3D array of dimensions 6572x48x36, so:

- `len(json) = 6572`
- `len(json[0]) = 48`
- `len(json[0][0]) = 36`
<br>(something like that)

# Downloaded video
I downloaded the BadApple!!.mp4 with this yt-dlp command:
 <br>`yt-dlp -f "mp4" -o "BadApple!!.mp4" https://www.youtube.com/watch?v=FtutLA63Cp8 ` <br>
 You'll need yt-dlp downloaded and added to the path for it to work

# Convert the video to png frames
This command grabs all the frames as png files. Run this command from a terminal inside a folder called "frames" one directory deeper than BAmp4toFrames.py to work with my python code file (or edit the name idc). There'll be 6000+ files so run it in an empty folder. You can modify this command for whatever you need between the downloaded video and isolating the frames. For example, you could convert to .pbm, which encodes black and white as 1 and 0, like the Arduino repo below does.
<br>`ffmpeg -i BadApple!!.mp4 -r 30 frames\frame_%04d.png`<br>
I chose not to upload the png frames because it's a 6000+ file folder, you'll have to generate the frames yourself. But, I provide the empty frames folder at least.

# Process the png frames into usable data
For this, run
<br>`python3 BAmp4ToFrames.py`<br>
and you'll have a json (BAdata.json) and a txt (BAdata.txt) to work with. You could also modify BAmp4ToFrames.py to change or add intermediary steps for image processing, see my comments. Then, you can load the json or txt however you like in your environment. My code provides an example of loading the json in python, at the end where I validate the file's sizing.
<br>
<br>
It also features a progress bar!


# Reference Bad Apple repos
I came up with all this by referring others. Take a look, especially for C++ versions
<br>https://github.com/Felixoofed/badapple-frames/blob/main/create-frames<br>
<br>https://github.com/kevinjycui/bad-apple/blob/master/preprocess/main.py<br>
<br>https://github.com/postcanonical/Arduino-8x8-Bad-apple/blob/main/Scripts/ii.csv<br>
<br>https://deepwiki.com/mon/bad_apple_virus/3.1-preprocessing-pipeline-(python)<br>
<br>
<br>
<br><br>
Good luck! I hope this jumpstarts another unique Bad Apple playing.
