import itertools
import numpy as np
import png
import sys

import intrinsic
import poisson

if __name__ == '__main__':
    filepath = sys.argv[1]
    
    reader = png.Reader(filepath)
    w, h, pngdata, params = reader.read()
    image = np.vstack(itertools.imap(np.uint16, pngdata))
    if image.size == 3*w*h:
        image = np.reshape(image, (h, w, 3))

    H, W, C = image.shape
    
    mask = np.ones((H, W))
    threshold = 0.1
    
    shading, reflectance = intrinsic.color_retinex(image, mask, threshold, threshold, True)
    
    reflectance = (reflectance / np.max(reflectance))*255
    shading = (shading / np.max(shading))*255

    # est_refl = np.where(mask, est_refl ** (1./2.2), 1.)
    # est_shading = np.where(mask, est_shading ** (1./2.2), 1.)

    reflectance = reflectance.astype(int)
    shading = shading.astype(int)
    
    print shading.shape
    print reflectance.shape
    print np.amax(shading)
    print np.amax(reflectance)
    print np.amin(shading)
    print np.amin(reflectance)
    
    with open('reflectance.png', 'wb') as f:
        writer = png.Writer(width=W, height=H, greyscale=True)
        writer.write(f, np.reshape(reflectance, (-1, W*1)))
        
    with open('shading.png', 'wb') as f:
        writer = png.Writer(width=W, height=H, greyscale=True)
        writer.write(f, np.reshape(shading, (-1, W*1)))
