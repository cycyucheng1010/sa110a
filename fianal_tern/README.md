# 期末作業更新日誌
### 程式碼及內容參考網路上之資料，出處及來源皆紀載於參考資料
## begining(v1.0)
* 建立Django專案並透過selenium呼叫chrome去執行Django server 再利用assert去判斷是否可成功如果可以show pass 然後關閉瀏覽器
* [begintest.py](mysite/mysite/begin_test.py)備註:此單元測只有當Django剛初始化尚未新增app時可成功執行
![1](img/1.PNG)
![2](img/2.PNG)
## helloworld (v1.1)
* 建立一個newapp，利用Django內建的單元測試功能:
     1. 測試程式碼是否正確
     2.  連線是否可以

* [tests](mysite/myapp/tests.py)

![3](img/3.PNG)
![4](img/4.PNG)
## myapp(v1.2)
* 新增會顯示即時時間的html然後利用selenium及Django test進行測試
* [testmyapp](mysite/mysite/testmyapp.py)

![5](img/5.PNG)
![6](img/6.PNG)
## 完成大部分測試(v1.4)
* 由於v1.3在修改時發生大規模錯誤導致捨棄原本的branch v1.3 ，版本直接跳躍到v1.4
* 此版本完成以下事項:
     1. 將myapp的路徑從副頁拉到主頁(原:http://127.0.0.1:8000/myapp/ ， 現:http://127.0.0.1:8000/)
     2. 新增html中的input功能
     3. 完成測試並成功
* 這個版本的測試有以下內容:
     1. 利用django test去進行assert判斷
     2. 利用selenium去進行模擬使用者使用並進行判斷:
          * html h1的內容是否正確
          * 是否可以成功input 內容到id = new item裡面
          * 是否可成功呈現輸入後儲存之內容

![7](img/7.PNG)
![8](img/8.PNG)
## 參考資料
* [Testing in Python(feat. Django)（一、單元測試及功能測試篇）](https://medium.com/into-the-night/testing-in-python-feat-django-%E4%B8%80-%E5%96%AE%E5%85%83%E6%B8%AC%E8%A9%A6%E5%8F%8A%E5%8A%9F%E8%83%BD%E6%B8%AC%E8%A9%A6%E7%AF%87-94d68ef465e3)
* [Python 3 Tutorial 第十一堂（2）使用 unittest 單元測試](https://openhome.cc/Gossip/CodeData/PythonTutorial/UnitTestPy3.html)