from shapes import area_of_rectangle
import sys

#print(len(sys.argv))
#print(sys.argv)
width = int(sys.argv[1])
height = int(sys.argv[2])

print(area_of_rectangle(width, height))
