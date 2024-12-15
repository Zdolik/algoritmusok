# Minimum Total Cost for Equal Elements in a Window

## **Feladat leírása**  
Adott egy `n` egész számot tartalmazó tömb, és egy `k` méretű csúszóablak.  
A feladat az, hogy **balról jobbra** haladva minden `k` elemű ablakra számoljuk ki a minimális teljes költséget, amely szükséges az ablak összes elemének egyenlővé tételéhez.  

### **Költségszámítás**  
Egy elem növelésének vagy csökkentésének költsége **x**, ahol **x** az új és az eredeti érték különbsége.  
A teljes költség az ilyen költségek összege.  

---

## **Bemenet**  
- Az első sor két egész számot tartalmaz: `n` (a tömb elemeinek száma) és `k` (az ablak mérete).  
- A második sor `n` db egész számot tartalmaz: a tömb elemeit (x₁, x₂, ..., xₙ).  

**Korlátok**:  
1 ≤ k ≤ n ≤ 2⋅10⁵  
1 ≤ xᵢ ≤ 10⁹  

---

## **Kimenet**  
- Ki kell írni **n-k+1** számot: a költségeket minden egyes `k` méretű csúszóablakra. 