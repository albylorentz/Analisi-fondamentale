#Obiettivo: Scrivi uno script che calcoli il P/E ratio (Prezzo/Utile) e P/B ratio (Prezzo/Valore Contabile).

prezzo_azione = 150.50
utile_per_azione = 6.15  # EPS
valore_contabile_per_azione = 25.80  # Book value per azione

pe_ratio=prezzo_azione/utile_per_azione
pb_ratio=prezzo_azione/valore_contabile_per_azione

print("P/E Ratio:",pe_ratio)
print("PB Ratio",pb_ratio)


