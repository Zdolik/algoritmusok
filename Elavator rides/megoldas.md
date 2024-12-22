# Megoldás Magyarázata – Liftoptimalizálási Feladat

## **Alapötlet**  
A feladat célja, hogy minimalizáljuk a liftutak számát, miközben minden személyt felviszünk úgy, hogy a lift súlykorlátját ne lépjük túl.

Mivel `n` maximum értéke **20**, a **bitmasking** technikát és dinamikus programozást használjuk a probléma megoldására.

---

## **Megközelítés**  

1. **Bitmask Állapotok**  
   A problémát bitmasking segítségével oldjuk meg, ahol az egyes állapotokat a személyek jelenléte határozza meg:  
   - Minden bit (`1` vagy `0`) azt jelzi, hogy egy adott személyt már felvettünk-e a liftbe.  
   - Összes állapot: \( 2^n \).  

2. **Dinamikus Programozás (DP)**  
   A DP tömb minden állapota tartalmazza:  
   - **Jelenlegi utak száma**,  
   - **Az aktuális lift súlya**.  

   Ha egy új személyt hozzáadunk, két esetet vizsgálunk:  
   - **Ugyanazon úton maradunk**, ha a személy súlya belefér a lift aktuális teherbírásába.  
   - **Új utat kezdünk**, ha a súlykorlátot túllépnénk.

---

## **Implementáció**  

### **Állapot Definíció**  
- `dp[mask]`: Az állapot, ahol a `mask` jelöli, hogy kiket vittünk fel a liftben.  
- Minden állapotot a `(current_rides, current_weight)` pár reprezentál.

### **Frissítés**  
1. **Iterálunk az összes állapoton** (bitmask kombinációk).  
2. Minden állapothoz kipróbáljuk, hogy egy új személyt fel tudunk-e venni.  
3. Frissítjük a következő állapotot:  
   - Ha a személy belefér a súlykorlátba, maradunk az úton.  
   - Ha nem, új utat kezdünk.  

---

## **Idő- és Térbeli Komplexitás**  
- **Időkomplexitás:** \( O(2^n \cdot n) \), mivel minden állapotot legfeljebb \( n \)-szer vizsgálunk.  
- **Térbeli Komplexitás:** \( O(2^n) \), mivel ennyi állapotunk lehet.

---