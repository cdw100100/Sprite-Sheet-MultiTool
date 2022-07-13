# Sprite-Sheet-MultiTool
This is a script using python that I developed to help me make games. It has two fucntions curently the first function is to join multiple image files into a single one so combining multiple sprites into a sprite sheet. The second function is to cut a sprite sheet into individual sprite image files.

(Please make sure all sprites are the same size if not can cause unwanted behavior like sprite cutting or extra whtie space.)

To join multiple sprites into a sprite sheet you would input a folder containg the images like so.
Below is a example of how to call the join function the arguments are as follows the folder path, the start x position of were there first sprite is, the start y position of the first sprite, the width of the sprite, the height of the sprite, and the final tuple is spacing (left,right,top,botom) so if there is spacing between the sprites you can input it and it ignores it. 

multi = MultiTool("FolderPath",x,y,width,height,(0,0,0,0))
multi.makeSpriteSheet()

To cut a sprite sheet you would do as follows.

multi = MultiTool("FolderPath",x,y,width,height,(0,0,0,0))
multi.cutSpriteSheet()
