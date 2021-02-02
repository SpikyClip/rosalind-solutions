AA, Aa, aa = 19,20,15
total_population = AA + Aa + aa

aa_aa = (aa / total_population) * ((aa - 1)/(total_population - 1))
aa_Aa = (aa / total_population) * (Aa / (total_population - 1)) + (Aa / total_population) * (aa / (total_population - 1))
Aa_Aa = (Aa / total_population) * ((Aa - 1)/(total_population - 1))

total_recessive_children = aa_aa + (aa_Aa * 0.5) + (Aa_Aa * 0.25)
total_dominant_children = 1 - total_recessive_children

print(total_dominant_children)