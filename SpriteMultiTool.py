from PIL import Image
import sys, os

#If all sprites are not the same size it will cause unexpected behavior like cuting off the excess pieces of sprites that were bigger
#SpritePath (Can be a single image file or a folder full of image files)
# x,y (The start position that the the sprite starts at)
# width, height (The width and height of the sprite all sprites should be the same size)
# spacing ((Left,Right,Top,Bottom) If there is padding between the sprites if you are cutting a sheet input it at spacing

class MultiTool:
    def __init__(self, spritePath,x,y,width,height,spacing):
        self.spritePath = spritePath
        self.x, self.y = x,y
        self.width, self.height = width,height
        self.spacing = spacing

    def makeSpriteSheet(self):
        if os.path.isdir(self.spritePath):
            if self.spritePath[-1] != "\\":
                if self.spritePath[-1] != "/":
                    self.spritePath += "\\"
            
            sprites = os.listdir(self.spritePath)
            spriteSheet = Image.new("RGBA", (self.width*len(sprites)+self.spacing[0]+self.spacing[1],self.height+self.spacing[2]+self.spacing[3]), (255,255,255))

            xOffset = 0
            for sprite in sprites:
                sprite = Image.open(self.spritePath+sprite)
                spriteSheet.paste(sprite, (xOffset,0))
                xOffset += self.width
                sprite.close()

            spriteSheet.save(self.spritePath+"SpriteSheet.png", "PNG")
            spriteSheet.close()
        else:
            print("Please enter a folder with multiple images and not just a single image.")

    def cutSpriteSheet(self):
        if os.path.isfile(self.spritePath):
            spriteSheet = Image.open(self.spritePath)
            sheetWidth, sheetHeight = spriteSheet.size
            left,upper,right,bottom = 0,0,0,0
            x,y = 0,0
            index = 0

            for r in range(0, round(sheetWidth/self.width)):
                for c in range(0, round(sheetHeight/self.height)):
                    sprite = spriteSheet.crop((x,y,x+self.width,y+self.height))
                    sprite.save(self.spritePath[:-4]+"Frame"+str(index)+self.spritePath[-4:])
                    sprite.close()

                    y += self.height+self.spacing[2]+self.spacing[3]
                    index += 1

                x += self.width+self.spacing[0]+self.spacing[1]
                y = 0
            spriteSheet.close()
        else:
            print("Please enter a valid image file path!")

