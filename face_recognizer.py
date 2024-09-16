import PIL.Image
import PIL.ImageDraw
import face_recognition

# importing the image
picture = face_recognition.load_image_file("image.jpeg")
face_locations = face_recognition.face_locations(picture)
# print(face_locations)

number_of_faces = len(face_locations)
print(f"Detected {number_of_faces} face(s) in this image")

# drawing rectangles around the images
pil_picture = PIL.Image.fromarray(picture)
draw_picture = PIL.ImageDraw.Draw(pil_picture)

for faces in face_locations:
    top, right, bottom, left = faces
    draw_picture.rectangle([left, top, right, bottom],
                           outline="#2fc21f", width=4)

pil_picture.show()