encantador_namoradeiro_descricao = "Adorável Namoradeiro. Mistura de madeira tufada de poliéster. 32 polegadas de altura x 40 polegadas de largura x 30 polegadas de profundidade. Vermelho ou branco."
encantador_namoradeiro_preco = 254,00

estilo_sofa_descricao = "Sofá elegante. Couro sintético de bétula. 29,50 polegadas de altura x 54,75 polegadas de largura x 28 polegadas de profundidade. Preto."
estilo_sofá_preco = 180,50

luxo_lampada_descricao = "Lâmpada luxuosa. Vidro e ferro. 36 polegadas de altura. Marrom com abajur creme."
luxo_lampada_preço = 52,15

imposto_vendas = 0,088

cliente_um_total = 0
cliente_um_itemizacao = ""

cliente_um_total += encantador_namoradeiro_preco
cliente_um_itemizacao += encantador_namoradeiro_descricao

cliente_um_total += luxo_lampada_price
cliente_um_itemizacao += luxo_lampada_descricao

cliente_um_tax = cliente_um_total * venda_taxa
cliente_um_total += cliente_um_taxa

print("Itens do cliente um:")
print(cliente_um_itemizacao)
print("Cliente Um Total:")
print(cliente_um_total)