import cv2

def res_img_points():
    img = cv2.imread('./comic.jpg')
    cv2.imshow('Image', img)

    points = []

    def mouse_click(event, x, y, flags, parms):
        if (event == cv2.EVENT_LBUTTONDOWN):
            points.append((x, y))
            cv2.circle(img, (x, y), 4, (0, 255, 0), thickness=-1)
            cv2.imshow('Image', img)

    cv2.setMouseCallback('Image', mouse_click)
    print('sdjkashaj')
    return [img, points]


if (__name__ == '__main__'):
    [img, points] = res_img_points()
    copy = img.copy()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    [top_l, top_r, btm_l, btm_r] = points
    data = copy[top_l[1]: btm_l[1], top_l[0]: btm_r[0]]

    cv2.imshow('Piece', data)
    cv2.waitKey(0)