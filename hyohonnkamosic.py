import matplotlib.pyplot as plt  #matplotlibインポート、名前はplt
import cv2  #Open CVインポート
import numpy as np  #numpyインポート、名前はnp


org=cv2.imread("Lenna.png");     #画像の読み込み

h = org.shape[0]   #高さ取得
w = org.shape[1]    #幅取得

#画像表示
cv2.imshow("MT.Tubakurodake",org)
cv2.waitKey(0)
cv2.destroyAllWindows()

#縮小200
size=(200,200)
small=cv2.resize(org,size)
zoom=cv2.resize(small,(h,w),interpolation=cv2.INTER_AREA)
cv2.imshow("MT.Tubakurodake",zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()

#縮小100
size=(100,100)
small=cv2.resize(org,size)
zoom=cv2.resize(small,(h,w),interpolation=cv2.INTER_AREA)
cv2.imshow("MT.Tubakurodake",zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()

#縮小80
size=(80,80)
small=cv2.resize(org,size)
zoom=cv2.resize(small,(h,w),interpolation=cv2.INTER_AREA)
cv2.imshow("MT.Tubakurodake",zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()

#縮小50
size=(50,50)
small=cv2.resize(org,size)
zoom=cv2.resize(small,(h,w),interpolation=cv2.INTER_AREA)
cv2.imshow("MT.Tubakurodake",zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()

#縮小10
size=(10,10)
small=cv2.resize(org,size)
zoom=cv2.resize(small,(h,w),interpolation=cv2.INTER_AREA)
cv2.imshow("MT.Tubakurodake",zoom)
cv2.waitKey(0)
cv2.destroyAllWindows()
