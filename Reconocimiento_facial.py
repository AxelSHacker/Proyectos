import cv2
import face_recognition as fr

#cargar imagen
foto_control = fr.load_image_file("fotoa.jpg")
foto_prueba = fr.load_image_file("fotoc.jpg")

#pasar imagen a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#localizar cara control
lugar_cara_a = fr.face_locations(foto_control)[0]
cara_codificada_a = fr.face_encodings(foto_control)[0]

#localiyar cara control
lugar_cara_b = fr.face_locations(foto_prueba)[0]
cara_codificada_b = fr.face_encodings(foto_prueba)[0]

#mostrar rectangulo
cv2.rectangle(foto_control,
              (lugar_cara_a[3], lugar_cara_a[0]),
              (lugar_cara_a[1],lugar_cara_a[2]),
              (0, 255, 0),
              2)

#mostrar rectangulo
cv2.rectangle(foto_prueba,
              (lugar_cara_b[3], lugar_cara_b[0]),
              (lugar_cara_b[1],lugar_cara_b[2]),
              (0, 255, 0),
              2)
#realizar comparacion
resultado = fr.compare_faces([cara_codificada_a], cara_codificada_b)

print(resultado)
#mostrar imagenes
cv2.imshow("Foto control", foto_control)
cv2.imshow("Foto prueba", foto_prueba)

#mantener programa abierto
cv2.waitKey(0)