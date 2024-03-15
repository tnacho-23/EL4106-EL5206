#Importacion de librerias
import cv2
from matplotlib import pyplot as plt

#Cargar y mostrar imagen "tomates.png"
tomates = cv2.imread("01_2024/tomates.png")
cv2.imshow("Image", tomates)
cv2.waitKey(0)

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
t = 250

# Aplica el thresholding
_, tomates_binary = cv2.threshold(tomates_gray, t, 255, cv2.THRESH_BINARY)

# Muestra la imagen binaria
cv2.imshow('Binary Image', tomates_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()