import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
dataset_size = 120

cap = cv2.VideoCapture(1)
for j in range(number_of_classes):
    letter = chr(j + 65)
    if not os.path.exists(os.path.join(DATA_DIR, letter)):
        os.makedirs(os.path.join(DATA_DIR, letter))

    print('Collecting data for class {}'.format(letter))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Press "Q" to start capturing {letter}', (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(33)
        cv2.imwrite(os.path.join(DATA_DIR, letter, '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()