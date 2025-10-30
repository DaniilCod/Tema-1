text = "   tes.,?!t   "
mijlocul = len(text) // 2
prima_parte = text[:mijlocul].upper().strip()
a_doua_parte = text[mijlocul::-1].capitalize().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
combined_text = prima_parte + a_doua_parte

print(combined_text)