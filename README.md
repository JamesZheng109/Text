# License
The scripts are under the MIT License.
# Text.py
Creates a textbox with both dialouge to be displayed and name to indicate who is speaking (No images, only solid colors, and execulsively uses timesnewroman font)
### Parameters for initalization textbox()
- Make a textbox using Rect and Sysfont
- window=pass varibale used to make pygame window
- name=Name of the person who is speaking
- text=text for the texbox
- text_color=color the text variable will display as
- box_color=color the texbox will be
- box_x=x location the textbox will be placed
- box_y=y location the textbox will be placed
- width=How wide the texbox will be
- height=How high the texbox will be
- name_x=x location the name variable will be placed
- name_y=y location the name variable will be placed
- text_x=x location the text variable will be placed
- text_y=y location the text variable will be placed
### Parameters for textbox.draw()
- namefontsize=font size of the name
- textfontsize=font size of the text
## speech()
This function takes the parameters of textbox.__init__() and texbox.draw() and puts it all in one while loop.
### Additional parameters
- image=list of character portraits in order they should display
  - format:[(image,x,y),(imagen,xn,yn)]
- sound=list of sound effects to play in stated order
  - ''=play nothing (assuming default_sfx=None)
- default_sfx=sfx that one wishes to play by default
- background=background image
  - Also accepts any values that pygame's fill() accepts
  - Can be left blank but will result in:
      1. The last frame before function is called will still be there
      2. If one provides a list of images, the last image won't go away when the next one is called
- advance_button=pygame key event to advance the dialogue
# Wrapper.py
This take speech() from Text.py and wraps around it. This exists so you don't have to worry about inconsistencies with textbox design. You will need to fill in some paramters
### Parameters that need to be filled in
- window
- name
- dialogue
- image (defaults to empty list)
- background (defaults to None)
- sound (defaults to empty list)
- default_sfx
# Button.py
Creates a general button (No images, only solid colors.)
### Parameters
- Make a button using Rect
- window=pass variable used to make pygame window
- box_color=color the button will be
- x=x location the button will be placed
- y=y location the button will be placed
- width=How wide the texbox will be
- height=How high the texbox will be
- text=Words to display on button
- text_color=color text will be
# Audio.py
Handles playing sfx and music, and stopping music from playing
## play_sfx()
Plays the provided sfx file
### Paramters
- sound=sound file
## play_song()
Plays the provided song file
### Parameters
- song=song file
## pause_music()
Pauses, stops, or unpauses currently playing song based on provided state
### Paramters
-state=determines whether to unpause, pause, or stop music
  - 0=pause
  - 1=unpause
  - 2=stop
