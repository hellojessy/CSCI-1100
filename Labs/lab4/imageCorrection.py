from PIL import Image
from imageCorrectionHelper import make_square

im = Image.new('RGB', (512,512))

im1 = Image.open('ca.jpg')
imsquare = make_square(im1)
im1 = imsquare.resize((256,256))

im2 = Image.open('im.jpg')
imsquare = make_square(im2)
im2 = imsquare.resize((256,256))

im3 = Image.open('hk.jpg')
imsquare = make_square(im3)
im3 = imsquare.resize((256,256))

im4 = Image.open('bw.jpg')
imsquare = make_square(im4)
im4 = imsquare.resize((256,256))

im.paste(im1, (0,0))
im.paste(im2, (0, 256))
im.paste(im3, (256, 0))
im.paste(im4, (256,256))
im.show()