ROI Drawer Project

Overview

This project contains a Python script (roi_drawer.py) that draws a Region of Interest (ROI) within an image based on user-specified parameters: angle of inclination, length, breadth, and the dimensions of the image. 
The implementation uses a derived formula to achieve a time complexity of O(4), ensuring efficiency compared to a brute-force approach, which would take O(n³). 
If the specified ROI exceeds the image boundaries, the script automatically generates a new ROI that fits within the image dimensions.

Features

Custom ROI Creation: Draws an ROI based on angle of inclination, length, and breadth.
Boundary Check: Ensures the ROI stays within the image dimensions; adjusts automatically if the initial ROI exceeds bounds.
Optimized Performance: Executes in O(4) time complexity using a derived formula, avoiding the O(n³) complexity of brute-force methods.
Single-File Implementation: All logic is contained in roi.py for simplicity.

Requirements

Python 3.x
Numpy 
Matplotlib
