import matplotlib.pyplot as plt  #matplotlibインポート、名前はplt
import cv2  #Open CVインポート
import numpy as np  #numpyインポート、名前はnp


img=cv2.imread("Mt.Tsubakurodake.jpg");     #画像の読み込み
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)     #色配置の変換(RGB)

img_array=np.asarray(img)   #画像のRGBを配列（数値）として扱うための変数

"""
print(img_array)    #img_array（画像のRGB数値）表示
"""

h,w,c=img.shape #画像の高さ、幅、色の数値化
"""
#各数値表示
print(h)
print(w)
print(c)
"""
#R、G、Bの設定と平均を求めるためのカウンター
R=0
G=0
B=0
counter=0

rough=100 #モザイクの粗さ

#画像分割
for fh in range(0,int(h),int(h/rough)):
    fh_max=fh+(h/rough)
    for fw in range(0,int(w),int(w/rough)):
        fw_max=fw+(w/rough)
        #分割した画像のRGB値合成
        for fh2 in range(int(fh),int(fh_max)):
            for fw2 in  range(int(fw),int(fw_max)):
                #画像の範囲をオーバーするとfor文を抜け出す。
                if fh2>=h or fw2>=w:
                    break
                #RGB値合成
                R=R+img_array[fh,fw,(0)]
                G=G+img_array[fh,fw,(1)]
                B=B+img_array[fh,fw,(2)]
                counter=counter+1
        #平均値計算
        R=R/counter
        G=G/counter
        B=B/counter

        #分割した各画像にRGB平均値を入力
        for fh3 in range(int(fh),int(fh_max)):
            for fw3 in  range(int(fw),int(fw_max)):
                #画像の範囲をオーバーするとfor文を抜け出す。
                if fh3>=h or fw3>=w:
                    break
                #分割した各画像にRGB平均値を入力
                img_array[fh3,fw3,(0)]=R
                img_array[fh3,fw3,(1)]=G
                img_array[fh3,fw3,(2)]=B

        counter=0 #カウンターリセット


plt.imshow(img_array)   #画像データ指定
plt.show()  #データ出力
