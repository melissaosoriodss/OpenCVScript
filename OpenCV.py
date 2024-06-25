import cv2

#carregar os algoritmos do opencv
carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('fotos/imagem 2.jpg')

#converter a imagem rbg para a escala de cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagemCinza)

print(faces)


#quadradinho de detecção
for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255, 0), 2)


cv2.imshow('Faces', imagem)
cv2.waitKey()

