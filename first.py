import cv2
img = cv2.imread(r"D:\vision01\images\photo.png")
# 先判断有没有读到，再往下用
# 缩小到原来的 50%
resized = cv2.resize(img, None, fx=0.1, fy=0.1)

if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:
    # 打印图片尺寸：高度 宽度 通道数
    print("图片尺寸：", resized.shape)

cv2.imshow("test", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(r"D:\vision01\images", resized)