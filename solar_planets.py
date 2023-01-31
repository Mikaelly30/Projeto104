import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sol",
                (100,80),
                cv2.FONT_HERSHEY_COMPLEX,
                2,
                (0,0,255)
                )

cv2.putText(img,
            "Mercurio",
                (110,170),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Venus",
                (200,170),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Terra",
                (290,170),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Marte",
                (390,170),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Jupiter",
                (550,60),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Saturno",
                (770,130),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Urano",
                (970,130),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )

cv2.putText(img,
            "Netuno",
                (1110,130),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                0.5,
                (255,255,255)
                )
cv2.imshow("resultado",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)

