import cv2 as cv

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, rect

    if event == cv.EVENT_LBUTTONDOWN:  # Khi nhấn nút trái chuột
        drawing = True
        ix, iy = x, y  # Lưu tọa độ bắt đầu

    elif event == cv.EVENT_MOUSEMOVE:  # Khi di chuyển chuột
        if drawing:
            img_copy = img.copy()
            cv.rectangle(img_copy, (ix, iy), (x, y), (255, 0, 0), 2)
            cv.imshow('Image', img_copy)

    elif event == cv.EVENT_LBUTTONUP:  # Khi nhả nút trái chuột
        drawing = False
        rect = (min(ix, x), min(iy, y), abs(x - ix), abs(y - iy))  # Lưu rect
        cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        cv.imshow('Image', img)

# Đọc ảnh
img = cv.imread('./images/Lionel-Messi.jpg')
cv.imshow('Image', img)

img_copy = img.copy()  # Bản sao để chỉnh sửa
cv.imshow('Image', img_copy)

drawing = False
ix, iy = -1, -1
rect = None
cv.setMouseCallback('Image', draw_rectangle)
cv.waitKey(0)
cv.destroyAllWindows()

# Sau khi đóng cửa sổ, hiển thị lại ảnh với hình chữ nhật màu đỏ
if rect is not None:
    x, y, w, h = rect
    cv.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Hình chữ nhật màu đỏ
    cv.imshow('Final Image', img_copy)
    cv.waitKey(0)
    cv.destroyAllWindows()

print("Rect:", rect)  # In tọa độ của hình chữ nhật đã vẽ
