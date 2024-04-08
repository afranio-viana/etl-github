from DadosRepositorios import DadosRepositorios

amazon_rep = DadosRepositorios("amzn")

ling_amazon = amazon_rep.criar_df_linguagens()

#print(ling_amazon)

afranio_rep = DadosRepositorios("afranio-viana")

ling_afranio = afranio_rep.criar_df_linguagens()
#print(f'{ling_afranio}')

apple_rep = DadosRepositorios("apple")

ling_apple = apple_rep.criar_df_linguagens()