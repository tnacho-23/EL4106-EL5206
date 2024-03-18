#Importacion de librerias
import cv2
from matplotlib import pyplot as plt


#Pregunta 1
#Cargar y mostrar imagen "tomates.png"
tomates = cv2.imread("01_2024/tomates.png")
# cv2.imshow("Image", tomates)

#Transformo imagen a escala de grises
tomates_gray = cv2.cvtColor(tomates,cv2.COLOR_BGR2GRAY)

# cv2.imshow("Gray Image", tomates_gray)
# cv2.waitKey(0)

#Calculo histograma imagen gris
hist = cv2.calcHist([tomates_gray], [0], None, [256], [0, 256])
# plt.plot(hist, color='gray' )
# plt.show()

#Obtención de imagen binaria dependiente de un threshold "t"
# Define el umbral (t)
t = 125

# Aplica el thresholding
_, tomates_binary = cv2.threshold(tomates_gray, t, 255, cv2.THRESH_BINARY)

# Muestra la imagen binarias
# cv2.imshow('Binary Image', tomates_binary)

#Obtener canales BGR
# b, g, r = cv2.split(tomates)
r = tomates[:,:,0]
g = tomates[:,:,1]
b = tomates[:,:,2]

# Visualize with color mappings
f, axarr = plt.subplots(1, 3)
axarr[0].imshow(r, cmap="Reds")
axarr[1].imshow(g, cmap="Greens")
axarr[2].imshow(b, cmap="Blues")
plt.show()
# cv2.imshow('Red', r)
# cv2.imshow('Green', g)
# cv2.imshow('Blue', b)


# fixed_aji = g
# cv2.imshow('Image fixed', fixed_aji)


# new_t = 125
# _, aji_binary = cv2.threshold(r, new_t, 255, cv2.THRESH_BINARY)
# cv2.imshow('Binary Aji', aji_binary)



# cv2.waitKey(0)
# cv2.destroyAllWindows()
