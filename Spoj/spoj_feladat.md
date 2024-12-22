# Legbiztonságosabb Út Chicagóba

## Feladat Leírása

A Blues Brothers-nek el kell jutniuk Chicagóba, miközben rendőrök, egy country zenekar és egy náci csoport üldözik őket.  
A legbiztonságosabb út az, amely maximalizálja annak valószínűségét, hogy nem kapják el őket. A feladatod ennek az útvonalnak a biztonsági valószínűségét meghatározni.

---

## Bemenet

- A bemenet több tesztesetet tartalmaz.  
- Minden teszteset az alábbiakból áll:
  - Két egész szám: \( n \) és \( m \):  
    - \( n \): kereszteződések száma (\( 2 \leq n \leq 100 \)).  
    - \( m \): utcák száma (\( 1 \leq m \leq n(n-1)/2 \)).  

  - A következő \( m \) sor az utcákat írja le:  
    - Minden sor három egész számot tartalmaz: \( a \), \( b \), \( p \):
      - \( a \) és \( b \) (\( 1 \leq a, b \leq n, a \neq b \)): az utca két végpontja.  
      - \( p \) (\( 1 \leq p \leq 100 \)): az utca biztonsági valószínűsége százalékban.  

- Az utcák kétirányúak, és két kereszteződés között legfeljebb egy utca található.

- A bemenet végét egyetlen "0" jelzi.

---

## Kimenet

- Minden tesztesethez egy sort kell kiírni:
  - A legbiztonságosabb út biztonsági valószínűsége százalékban, pontosan 6 tizedesjegy pontossággal.
  - Az értéket az alábbi formátumban kell kiírni:  
    ```
    XX.XXXXXX percent
    ```

---