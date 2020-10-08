# esterni_sw_emergenze
Tool python per inserimento massivo di utenti esterni al DB del sistema emergenze (https://github.com/comuneDiGenova/emergenze-pcge/)

- Il tool richiede come input un file csv con i nominativi dei volontari

- il tool richiede un file conn.py con le credenziali del DB a cui connettersi 

```
ip='XXXXXXX'
db='XXXXXXX'
user='XXXXXXX'
pwd='XXXXXXX'
port='XXXXXXX'
```

- il tool può essere personalizzato con altri campi. Nei commenti è specificato abbastanza bene come e dove

- i campi id1 e id2 sono relativi alle Unità Operative di primo e secondo livello. A titolo di esempio nel caso di *Gruppo Genova - Sezione Val Polcevera*:  *id1* corrisponde a *Gruppo Genova* (UO primo livello), *id2* corrisponde a *Sezione Val Polcevera* (UO secondo livello) e sono descritti meglio rispettivamente nelle seguenti tabelle del DB:
  - users.uo_1_livello 
  - users.uo_2_livello
  

- il tool crea automaticamente un file di log nella cartella tempooranea del sistema operativo

Per maggiori informazioni roberto.marzocchi@gter.it 
