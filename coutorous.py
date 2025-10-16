import cv2
import numpy as np

image = cv2.imread('pizza_copy.jpeg', cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area


for i, cnt in enumerate(contours):
    # Get bounding box from contour
    x, y, w, h = cv2.boundingRect(cnt)

    # Crop the ROI from the original image
    roi = image[y:y+h, x:x+w]

    # Optional: Further processing, like checking if ROI is grayscale
    if len(roi.shape) == 2:
        gray_roi = roi.copy()
    else:
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Otsu's thresholding
    upper_threshold, thresh_roi = cv2.threshold(
        gray_roi, thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    lower_threshold = 0.5 * upper_threshold

    # Apply Canny edge detection on the cropped region
    canny = cv2.Canny(gray_roi, lower_threshold, upper_threshold)

    # Find non-zero points
    pts = np.argwhere(canny > 0)

    if pts.size > 0:
        y1, x1 = pts.min(axis=0)
        y2, x2 = pts.max(axis=0)

        # Final tight crop
        final_crop = roi[y1:y2, x1:x2]

        # Save the cropped image
        output_path = f'e_output_crop_{i}.png'
        cv2.imwrite(output_path, final_crop)
    else:
        # If no edges found, just save the ROI
        output_path = f'e_output_crop_{i}_noedges.png'
        cv2.imwrite(output_path, roi)
