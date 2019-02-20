import cv2
import numpy as np
import math
import os
import re
import pygame

pygame.init()

os.system("clear")
detector = cv2.CascadeClassifier('cars.xml')
gray = (128,128,128)
red = (155,0,0)
blue = (0,0,155)
number = input("Video Value: ")
if number == 1:
  cap = cv2.VideoCapture('cars.mp4')
if number == 2:
  cap = cv2.VideoCapture('cars1.mp4')
if number == 3:
  cap = cv2.VideoCapture('IMG_1174.MOV')
cv2.useOptimized()
clock_value = 2
print_value = 0

detect = False
userExit = False

while not userExit:
  ret, frame = cap.read()
  frame = cv2.resize(frame, (900, 600), interpolation = cv2.INTER_LINEAR)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  clock_value += 1
  if clock_value % 3 == 0:
    cars = detector.detectMultiScale(gray, 1.1, 1)
    detect = True

  if clock_value % 3 != 0:
    low_threshold = 50
    high_threshold = 150
    blur_gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    rho = 1
    theta = np.pi / 280
    threshold = 10
    min_line_length = 20
    max_line_gap = 21
    line_image = np.copy(frame) * 2
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    try:
      for line in lines:
        for x1, y1, x2, y2 in line:
          cv2.line(frame, (x1, y1), (x2,y2), (255,255,255), 3)
    except Exception as e:
      print("Error: " + str(e))
  for (x, y, w, h) in cars:
    if w >= 70 and h >= 70:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (255,255,255), 1)
      print("Car: (" + str(x) + "," + str(y) + ")" + " | " + str(print_value))
      print_value += 1
      cv2.imshow('Frame', frame)
  cv2.imshow('Frame', frame)
  if clock_value % 4 != 0:
    detect = False
  if cv2.waitKey(1) & 0xFF == ord('q'):
    userExit = True
    break

cv2.destroyAllWindows()
quit()
