# Megoldás Magyarázata

## Algoritmus

A feladatot egy gráfként modelláljuk, ahol a kereszteződések csúcsok, az utcák pedig élek.  
Az él súlya az utca biztonsági valószínűségét reprezentálja, amit \( p/100 \)-ra konvertálunk.

### Algoritmus Lépései

1. **Gráf Felépítése**:
   - Egy szomszédsági listában tároljuk a gráfot.
   - Az élek kétirányúak, így mindkét csúcsot összekötjük az adott éllel és annak valószínűségével.

2. **Dijkstra Algoritmus Módosítása**:
   - Egy prioritási sor (max-heap) segítségével mindig az aktuálisan legnagyobb biztonsági valószínűségű csúcsot vizsgáljuk meg.
   - Ha egy szomszédos csúcs eléréséhez egy jobb (nagyobb valószínűségű) út található, frissítjük az adott csúcs maximális valószínűségét.

3. **Eredmény Számítása**:
   - A \( n \)-edik csúcs maximális biztonsági valószínűségét visszakonvertáljuk százalék formátumra és 6 tizedesjegyre kerekítjük.

---
