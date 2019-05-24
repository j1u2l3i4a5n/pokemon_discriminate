# 神奇寶貝圖形辨識

## 組員
- 黃妍心 生傳三 b05610046
- 王博群 地理四 b04208021
- 林鴻儒 心理四 b04207001

## 題目簡介
　　神奇寶貝是許多朋友的童年回憶，其中的神奇寶貝圖鑑能夠藉由拍下神奇寶貝的照片便能夠辨識出是哪種神奇寶貝，並且說出這種神奇寶貝的習性、特徵、屬性等等。基於對神奇寶貝的熱情，因此我們想要實作出這個神奇寶貝圖鑑。

## 資料集簡介
　　資料主要來自於kaggle上的<a href='https://www.kaggle.com/hannesrosenbusch/6036-labeled-pokemon-pictures?fbclid=IwAR07pt_Ewv1iv0PEIJqLeMAVdPu51MGXHrfGIwSDAPLHkh25ucI3A7F3g8U#names_and_strengths.csvhttps://www.kaggle.com/hannesrosenbusch/6036-labeled-pokemon-pictures?fbclid=IwAR07pt_Ewv1iv0PEIJqLeMAVdPu51MGXHrfGIwSDAPLHkh25ucI3A7F3g8U#names_and_strengths.csv'>6036 labeled pokemon pictures</a>。由於這個資料集的資料量略少，模型可能不易訓練，因此考慮整合其他資料集，或是使用轉移學習先抓特徵。
  
  
## 實作方法
- 運用CNN做圖形辨識
- (optional) 運用轉移學習解決資料量不足的問題
- (optional) 運用GAN去生成新的神奇寶貝
- (optional) 做出神奇寶貝圖鑑的介面
- (optioanl) 圖鑑附上口語輸出

## 專案排程(進度)
- 5/27 (執行中) 以現有資料嘗試訓練出一個模型 
- 5/31 找額外資料補足，並整理成相同格式。目標16000張圖(800種，每種約20張)
- 6/5 重新訓練模型
- 6/6 撰寫結果報告
- 6/6 (optional) 額外嘗試，例如使用轉移學習、GAN
- 6/7 報告繳交
- 6/13 (optioanl)報告demo準備
- 6/14 (optional)報告


