# **VENV**

Para criar um ambiente virtual (venv) no Windows usando Python, siga os passos abaixo:

1. **Abra o Prompt de Comando ou o PowerShell** .
2. **Navegue até o diretório** onde você deseja criar o ambiente virtual. Use o comando `cd` para mudar de diretório:

   ```
   cd caminho\do\diretório
   ```
3. **Crie o ambiente virtual** com o seguinte comando:

   ```
   python -m venv nome_do_venv
   ```

   Substitua `nome_do_venv` pelo nome que você deseja dar ao seu ambiente virtual.
4. **Ative o ambiente virtual** . No Windows, você pode ativar o venv com o seguinte comando:

```
nome_do_venv\Scripts\activate
```

   Após ativar o ambiente virtual, você verá algo parecido com `(nome_do_venv)` aparecendo antes do caminho no prompt.

1. Para  **desativar o ambiente virtual** , basta rodar o comando:

   ```
   deactivate
   ```

Agora, o ambiente está configurado e você pode instalar pacotes e bibliotecas sem afetar o ambiente global do Python.

# **ENV**

Para criar um arquivo `.env` usando Python, você pode simplesmente abrir um arquivo de texto e gravar as variáveis de ambiente que você deseja definir. Aqui está um exemplo simples de como criar um arquivo `.env` com Python:

#### Passos:

1. **Crie um script Python** para gerar o `.env`.
2. **Escreva as variáveis de ambiente** no arquivo.

Exemplo:

```
OPENAI_API_KEY = fE#$nffk$EFefeg
```

# Requirements.txt

**Instale os pacotes** listados no `requirements.txt` utilizando o `pip`. Execute o seguinte comando na mesma pasta onde o arquivo `requirements.txt` está localizado:

```
pip install -r requirements.txt
```


# Run Streamlit


```
streamlit run app.py

```
