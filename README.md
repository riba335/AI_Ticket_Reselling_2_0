# AI Ticket Reselling 2.0

Tento projekt analyzuje historické predaje lístkov, vypočíta AttractiScore a odporúča nákup. Keď je skóre vysoké a cena nízka, pošle upozornenie (napr. WhatsApp).

## Spustenie lokálne
```
uvicorn main:app --reload
```

## Endpointy
- POST `/analyze`: pošleš info o evente a vráti skóre a odporúčanie.