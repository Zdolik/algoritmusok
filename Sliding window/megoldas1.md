# Megoldás Magyarázata

## **Feladat Összefoglalása**  
A feladatunk, hogy egy `n` hosszú tömbben, minden `k` méretű ablakra kiszámoljuk a minimális költséget, amellyel az ablak összes elemét egyenlővé tehetjük. A költség az egyes értékek növelésének vagy csökkentésének összegéből adódik.  

---

## **Megközelítés**  
A megoldás alapja a **medián** használata.  
- A medián az a szám, amely minimalizálja a "különbségek összegét" egy adathalmazon belül.  
- Tehát egy ablak összes elemét **a mediánra** módosítva kapjuk a minimális költséget.  

### **Algoritmus Lépései**  
1. **Két halom használata (bal és jobb oldali heap):**  
   - A bal oldali heap (max heap) tartalmazza az ablak kisebb felét.  
   - A jobb oldali heap (min heap) tartalmazza az ablak nagyobb felét.  
2. **Egyensúly fenntartása:**  
   - Mindig ügyelünk arra, hogy a két heap mérete közel egyenlő legyen.  
   - Ez biztosítja, hogy a mediánt a bal oldali heap teteje tartalmazza.  
3. **Beszúrás és törlés:**  
   - Az ablak elemeinek mozgatása során az új értéket beszúrjuk, a régit töröljük, és frissítjük a heappek egyensúlyát.  
4. **Költségszámítás:**  
   - A medián és a heapek összegeinek segítségével kiszámítjuk az adott ablak költségét.  