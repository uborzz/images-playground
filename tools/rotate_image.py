from pytesseract import Output
import pytesseract
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=False, help="path to output image. override if not given.")
ap.add_argument("-a", "--angle", required=True, help="rotation angle", type=int)
args = vars(ap.parse_args())

original = cv2.imread(args["image"])

if original is None:
    exit("Thats not an image =(")

# rotate the image and save to disk
angle = args["angle"]
rotated = imutils.rotate_bound(original, angle=args["angle"])
output = args.get("output")
if output:
    text = f"Saving rotated image (by {angle} degrees) into: {output}"
else:
    output = args["image"]
    text = f"Overwriting rotated image (by {angle} degrees) into: {output}"
print(text)
cv2.imwrite(output, rotated)