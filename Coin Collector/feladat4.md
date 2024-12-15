# Maximum Érmegyűjtés Feladat

## **Feladat Leírása**  
Egy játékban **n szoba** és **m alagút** található. Minden szobához egy bizonyos számú érme tartozik. Az alagutak egyirányúak, azaz csak egy adott irányba lehet rajtuk keresztülhaladni. A cél az, hogy a lehető legtöbb érmét gyűjtsd össze az alagutakon keresztülhaladva.  

Szabadon választhatsz **kiindulási** és **végpontot** a szobák közül.

---

## **Bemenet**  
A bemenet a következő:  
- Az első sorban két egész szám található: **n** (a szobák száma) és **m** (az alagutak száma).  
- A második sorban **n** egész szám szerepel: \( k_1, k_2, \dots, k_n \), ahol \( k_i \) az \( i \)-edik szobában található érmék száma.  
- A következő **m sor** mindegyikében két egész szám van: **a** és **b**, amelyek azt jelzik, hogy van egy alagút az **a** szobából a **b** szobába.

---

## **Kimenet**  
Egyetlen egész számot kell kiírni: a maximálisan összegyűjthető érmék számát.

---

## **Korlátok**  
- \( 1 \leq n \leq 10^5 \)  
- \( 1 \leq m \leq 2 \cdot 10^5 \)  
- \( 1 \leq k_i \leq 10^9 \)  
- \( 1 \leq a, b \leq n \)  

---