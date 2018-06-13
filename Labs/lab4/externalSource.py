from PIL import Image
import panoramio as pan
from imageCorrectionHelper import make_square

def getPhotos(urls):
    urls = pan.getPhotos(urls)
    if (len(urls)<4):
        print('Could not find sufficient amonut of photos.')
    else:
        im = Image.new('RGB', (512,512))
        im1 = pan.openphoto(urls[0])
        imsquare = make_square(im1)
        im1 = imsquare.resize((256,256))
        
        im2 = pan.openphoto(urls[2])
        imsquare = make_square(im2)
        im2 = imsquare.resize((256,256))
        
        im3 = pan.openphoto(urls[3])
        imsquare = make_square(im3)
        im3 = imsquare.resize((256,256))
        
        im4 = pan.openphoto(urls[4])
        imsquare = make_square(im4)
        im4 = imsquare.resize((256,256))
        
        im.paste(im1, (0,0))
        im.paste(im2, (0, 256))
        im.paste(im3, (256, 0))
        im.paste(im4, (256,256))
        im.show()

urls = input('Enter url => ')
getPhotos(urls)