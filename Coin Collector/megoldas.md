# Megoldás Magyarázata – Maximum Érmegyűjtés Feladat

## **Feladat Leírása**  
Adott egy játék, amelyben **n szoba** és **m egyirányú alagút** található. Minden szobában van egy bizonyos számú érme. A cél az, hogy a lehető legtöbb érmét gyűjtsük össze az alagutakon keresztül haladva. A kezdő és végpontot szabadon választhatjuk.

---

## **Megközelítés**  

1. **Gráf Reprezentáció**  
   A szobák és alagutak **irányított gráfot** alkotnak. Az élek az egyirányú alagutakat jelzik.  
   - A gráfot egy **szomszédsági lista** segítségével reprezentáljuk.

2. **Dinamikus Programozás (DP)**  
   A DP tömbben tároljuk, hogy egy adott szobából indulva mi a maximális érmék száma, amit gyűjthetünk:  
   - `dp[node]` = maximális érmék száma a `node` szobából indulva.  

3. **Mélységi Keresés (DFS)**  
   A maximális érméket egy **DFS** segítségével számítjuk ki, amely a következőképpen működik:  
   - Minden szobából indulunk, ha még nem látogattuk.  
   - A DFS rekurzívan meghívja a szomszédokat, és frissíti a maximális érmék értékét.  

---

## **Lépések**  

1. **Gráf Építése**  
   Beolvassuk a bemenetet, és létrehozzuk a gráfot szomszédsági lista formában.  

2. **DFS + DP**  
   Minden csúcsra elindítunk egy DFS-t, amely kiszámolja az adott csúcsból induló maximális érmék számát.  

3. **Eredmény**  
   Az összes szobára kiszámolt maximális értékek közül kiválasztjuk a legnagyobbat.

---

## **Idő- és Térbeli Komplexitás**  
- **Időkomplexitás:** \( O(n + m) \), mivel minden csúcsot és élt egyszer dolgozunk fel.  
- **Térbeli Komplexitás:** \( O(n + m) \), a gráf tárolásához és a DP tömbhöz.

---