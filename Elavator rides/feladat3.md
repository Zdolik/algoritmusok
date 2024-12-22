# Liftoptimalizálás – Minimum Liftutak Száma

## **Feladat Leírása**  
Adott egy **n** fős csoport, akik egy épület tetejére szeretnének jutni egy **lifttel**. A lift egyszerre csak korlátozott **maximális súlyt** bír el, és ismerjük minden személy egyéni súlyát.  
A célunk, hogy meghatározzuk, **mi a minimális számú liftút**, amely elegendő ahhoz, hogy az összes ember feljusson a célba.

---

## **Bemenet**  
A bemenet a következő:  
1. Az **első sorban** két egész szám szerepel:  
   - `n`: a személyek száma,  
   - `x`: a lift maximális teherbírása (kg).  
2. A **második sor** `n` darab egész számot tartalmaz:  
   - `w_1, w_2, \dots, w_n`: az egyes személyek súlya (kg).