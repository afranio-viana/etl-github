import requests
import pandas as pd
from math import ceil
import sys
sys.path.append("..")
from config_token import token
import csv

class DadosRepositorios:

    def __init__(self,owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = token
        self.path = "../data_processed"
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'}
        
    def __lista_repositorios (self):
        repos_list = []
        response = requests.get(f'https://api.github.com/users/{self.owner}')
        #print(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)
        if num_pages==1:num_pages=2
        for page_num in range(1,num_pages):
            try:
                #print("oi")
                url_page = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                #print(url_page)
                response = requests.get(url_page,headers=self.headers)
                response_json = response.json()
            
                repos_list.append(response_json)
            except:
                repos_list.append(None)
        return repos_list
    
    def __repos_information (self,repos_list,info):
        repos_information = []
        for page in repos_list:
            for repo in page:
                try:
                    #print(repo[info])
                    repos_information.append(repo[info])
                except:
                    pass
        return repos_information
    

    def criar_df_linguagens(self):
        repositorios = self.__lista_repositorios()
        repos_name= self.__repos_information(repositorios,"name")
        repos_language = self.__repos_information(repositorios,"language")

        dados = pd.DataFrame()
        dados['repository_name'] = repos_name
        dados['language'] = repos_language
        self.__salvar_dados(dados)
        return dados
    
    def __salvar_dados(self,dados):
        caminho = f'{self.path}/linguagens_{self.owner}.csv'
        dados.to_csv(caminho)
        print(caminho)