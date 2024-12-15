# Rekurzív Megoldás Magyarázata

## **Feladat Összefoglalása**
Adott egy **fa** (n csomópont és n-1 él), a feladatunk, hogy megszámoljuk, hány **különböző út** létezik, amely pontosan **k élből** áll.

---

## **Fa Tulajdonságai**
- A fa egy összefüggő, körmentes gráf.
- A fa csomópontjai élekkel kapcsolódnak egymáshoz.  
- Minden csomópontból egyértelmű utak vezetnek a többi csomópontba.

---

## **Rekurzív Megközelítés**  
A rekurzív megoldás alapja:  
1. **Kiindulópont választása:**  
   Minden csomópontot tekinthetünk **kiindulópontnak**, ahonnan elindulunk.
2. **Rekurzív útépítés:**  
   Az adott csomópontból minden szomszédos csomóponthoz tovább lépünk, amíg el nem érjük a pontosan **k él hosszúságot**.  
3. **Visszalépés (Backtracking):**  
   A rekurzió során a meglátogatott csomópontokat megjegyezzük, hogy elkerüljük a köröket (a fa körmentes, de biztosítjuk a helyes működést).  

---

## **Algoritmus Lépései**  
1. Olvassuk be a gráfot és építsük fel **adjacency list** formájában.  
2. A rekurzió elindul minden csomópontból, hogy megszámolja az összes olyan utat, amely k él hosszú.  
3. A rekurzió során:  
   - Lépjünk a szomszédos csomópontokba.  
   - Csökkentsük a hátralévő lépések számát (`k-1`).  
   - Ha a hátralévő lépések száma 0, akkor növeljük a talált utak számát.  
4. Összesítsük az összes kiindulópontból indított rekurzió eredményét.  

---