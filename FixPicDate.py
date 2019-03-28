'''
修改照片的拍摄时间(jpeg文件)
本例子中图片文件已经更改为其拍摄时间，主要利用该程序修改照片exif文件中的拍摄时间。
由于exif时间使用了多个验证？更改了'0th'和'exif'中的时间.
'''
from PIL import Image
import os
import piexif


PicList=['timewrong/%s'%_ for _ in os.listdir('timewrong') if 'DS_Store' not in _]
PicList.sort()
for _ in PicList:
    #只能处理jpeg格式的数据
    img = Image.open(_)
    # print(img.format)
    filename=_.split('/')[-1]
    year,month,day=filename.split('-')[:3]
    datestring=str.encode('%s:%s:%s 08:00:00'%(year,month,day))
    exif_dict={'0th': {306: datestring}, 'Exif': { 36867: datestring, 36868: datestring}}
    print(exif_dict)
    exif_bytes = piexif.dump(exif_dict)
    img.save('new/%s'%filename, "jpeg", exif=exif_bytes)


