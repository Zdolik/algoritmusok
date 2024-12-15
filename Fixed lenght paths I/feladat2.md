# Rekurzív Út Számlálás a Fában

## **Feladat Leírása**  
Adott egy **fa**, amelyben **n csomópont** és **n-1 él** található. A csomópontok sorszámai **1**-től **n**-ig terjednek.  
A feladat az, hogy számoljuk meg, hány **különböző út** létezik a fában, amelyek pontosan **k él hosszúságúak**.

---

## **Bemenet**  
A bemenet a következő:  
- Az **első sorban** két egész szám szerepel:  
  - `n`: a csomópontok száma,  
  - `k`: a kívánt út hossz (élek száma).  
- A **következő n-1 sor** tartalmazza a fa éleit. Minden sor két egész számot ad meg:  
  - `a` és `b`, amely azt jelenti, hogy van egy él az `a` és `b` csomópont között.