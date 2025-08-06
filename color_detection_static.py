import cv2
import numpy as np

# قراءة الصورة من الملف
# تأكد من تغيير 'blue_image.jpg' إلى اسم الصورة التي تستخدمها
image = cv2.imread('blue_image.jpg')

# التأكد من أن الصورة تم تحميلها بنجاح
if image is None:
    print("❌ خطأ: لم يتم العثور على الصورة. تأكد من أن اسم الملف صحيح وأنه في نفس المجلد.")
else:
    # تحويل الصورة من BGR إلى HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # تحديد نطاق اللون الأزرق في HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # إنشاء قناع (mask) للون الأزرق فقط
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # تطبيق القناع على الصورة الأصلية
    res = cv2.bitwise_and(image, image, mask=mask)

    # عرض الصور
    cv2.imshow('Original Image', image)
    cv2.imshow('Blue Detected', res)
    cv2.imshow('Mask', mask)

    # الانتظار حتى يضغط المستخدم على أي مفتاح لإغلاق النوافذ
    cv2.waitKey(0)
    cv2.destroyAllWindows()