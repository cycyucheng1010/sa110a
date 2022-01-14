## 什麼是軟體工程
* 在維基百科中的定義如下:
```Software engineering is an engineering approach on a software development of systematic application.```
* IEEE對軟體工程的定義則是:
```software engineering as the application of a systematic, disciplined, which is a computable approach for the development, operation, and maintenance of software.```
* 而大多數人的定義大致是:藉由分析客戶需求、去進行設計、實作到測試以及修正的整個過程

![image](https://user-images.githubusercontent.com/62127656/149441366-d1b37d65-bb96-495f-8a31-3c9028f0b2da.png)

## 原則
### 美國著名的軟體工程專家巴利·玻姆（Barry Boehm）綜合專家的意見，並總結了美國天合公司多年的開發軟體的經驗，於1983年提出了軟體工程的七條基本原理。
1. 用分階段的生命周期計劃嚴格管理 
2. 堅持進行階段評審
3. 實行嚴格的產品控制
4. 採納現代程式設計技術
5. 結果應能清楚地審查
6. 開發小組的人員應少而精
7. 承認不斷改進軟體工程實踐的必要性
## 軟體危機以及解決
###  Software Crisis
* 1968年，北大西洋公約組織（NATO）在聯邦德國的國際學術會議創造軟體危機（Software crisis）一詞。
 * 在1960年代許多的軟體開發失敗，原因在於許多軟體價格超出預算、不可靠且維護費用過高。
 * 很多軟體無法滿足客戶不斷的要求，軟體的複雜度也隨著硬體能力的提高而增加。
### Solution
* 在1968、1969年連續召開兩次著名的NATO會議，並提出軟體工程的概念。
* 透過將專案管理導入的方式，約束範圍、時間、預算、以及資源運用。
* 目前累積了大量的研究成果，廣泛地進行大量的技術實踐，藉由學術界和產業界的共同努力，軟體工程正逐漸發展成為一門專業學科。
## The Mythical Man-Month and No Silver Bullet
### The Mythical Man-Month
* 跟只為私人使用而單獨寫出來的組件程式相比，做出軟體系統產品所要付出的代價將是九倍以上。估計產品化的代價是三倍，若要對組件從事設計、整合、測試，進而凝聚成為一個系統，則代價也是三倍，而且這方面的成本計算基本是獨立的。
* 人力和時間並不呈現線性關係。指出以大量人員和較短的時間，並不能縮短軟體的開發進度，一窩蜂的作業方式無助於軟體生產，且會製造麻煩，產生出更差的軟體。
* 當有N個人必須在這群人之中進行溝通時（無階級關係），當N增加，其輸出M將抵消其效益，甚至倒退。

![image](https://user-images.githubusercontent.com/62127656/149439160-c89a9c28-0c48-4f77-b845-9ad3d1a58fe2.png)
![image](https://user-images.githubusercontent.com/62127656/149440534-cb859eb5-6f59-4986-98e1-d875ab3683c6.png)

### No Silver Bullet
* 複雜的軟體工程問題無法靠簡單的答案來解決，作者透過將軟體開發的困難分為兩類: essential task & accidental task
#### 本質性工作（essential task）是去創造出一種由抽象的軟體實體所組成的複雜概念結構，可再將其劃分成以下四種
  種類 | 內容
  ----- | ----
 複雜性（complexity）| 軟體要解決的問題，通常牽扯到計算步驟，這是一種人為、抽象化的智慧型活動，多半是複雜的。
 隱匿性（invisibility）| 尚未完成的軟體是看不見的，即使利用圖示說明，也常無法充分呈現其結構，使得人們在溝通上面臨極大的困難。
 配合性（conformity）| 在大型軟體環境中，各子系統的介面必須協同一致。由於時間和環境的演變，要維持這樣的一致性通常十分困難。
 易變性（changeability）| 軟體所應用的環境常是由人群、法規、硬體裝置、應用領域等，各因素所匯集而成，而這些因素皆會快速變化。
#### 附屬性工作（accidental task）則是用程式語言來表現這些抽象的實體，並在某些空間和速度的限制之下，將程式對應至機器語言。

## 心得
### 以專題為例
1. 這本篇期末心得中人月神話應該是讓我感觸最深的，原因在於正如同書中所寫人多不一定有用，人少不一定會做不完。
   * 我們這組共有4位成員但其中有部分成員連自己在做什麼都不知道，導致其他成員需要花更多時間去彌補他們的問題。
2. 我們的專題採用類似螺旋式開發的方式進行，一直重複 analysis design build test 的這個過程，透過這些過程我們發現可以很有效的去進行trouble-shooting

![image](https://user-images.githubusercontent.com/62127656/149443905-3109ba88-c97b-40c5-acaa-4df266a75724.png)

3. 但在重新省思的過程中也找到可以再去修正的地方:
   *  生命周期計劃嚴格管理，避免後續時間過度短缺
   *  若可以重新安排則小組的人員應少而精
   *  確立每次討論的議題，避免垃圾時間
   *  嚴格的品質控制，確保成功率達到預期
## 參考資料
* [What is Software Engineering? Definition, Basics, Characteristics](https://www.guru99.com/what-is-software-engineering.html)
* [Software engineering](https://en.wikipedia.org/wiki/Software_engineering)
* [Definition of 'Software Engineering'](https://economictimes.indiatimes.com/definition/software-engineering)
* [The Mythical Man-Month](https://en.wikipedia.org/wiki/The_Mythical_Man-Month)
* [No Silver Bullet](https://en.wikipedia.org/wiki/No_Silver_Bullet)
