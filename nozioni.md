
# Come fa il computer a rappresentare i numeri? Perché 255 era un bel numero?

## Perché vi ho detto che 255 era un numero che si trova spesso in informatica? 
contesto: l'abbiamo visto quando abbiamo parlato di rgb per i colori

i computer funzionano tramite un modello numero chiamato binario. Esso è formato da due cifre 0 e 1

per rappresentare i numeri un computer usa combinazioni di zero e uno, ma il primo paramentro da impostare è quanti di questi bit voglio usare per le mie rappresentazioni.

nel caso in cui io raggruppo 8 bit insieme ottengo 1 byte

dati n bit io posso rappresentare 2^n simboli, e se i simboli sono i numeri posso rappresentare 2^n numeri

nel caso di 1 byte (8 bit) si possono rappresentare 2^8 numeri = 256 numeri

## MA in programmazione si parte sempre da ZERO 

per cui con 1 byte posso rappresentare i numeri da 0 a 255

ad esempio 


- 00000000 = 0
- 00110111 = 55
- 11111111 = 255

ecco come il computer rappresenta i numeri e per questo esistono dei limiti in questa rappresentazione


