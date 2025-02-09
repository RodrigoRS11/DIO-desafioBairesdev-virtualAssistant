# **DIO-desafioBairesdev-virtualAssistant**

Este projeto é um assistente virtual simples ativado por voz, desenvolvido em Python e adaptado a partir dp modelo que o Prof. Dr. Diego Renan Bruno disponibilizou na aula do bootcamp BairesDev na DIO. Ele permite que os usuários interajam com o sistema usando comandos de voz e executa várias ações com base nesses comandos. O assistente utiliza reconhecimento de fala e síntese de texto para fala para facilitar a comunicação e inclui uma variedade de recursos, como navegação na web, busca no Wikipedia, reprodução de músicas, contação de piadas, entre outros.

O código utiliza diversas bibliotecas populares em Python para criar um assistente virtual funcional. A principal delas é a SpeechRecognition, que permite ao assistente capturar e reconhecer áudio a partir do microfone do usuário, convertendo a fala em texto. Caso o áudio não seja compreendido ou ocorra algum erro, o assistente informa o usuário por meio da função speak(), que usa a biblioteca gTTS para converter texto em fala e reproduzi-lo. A biblioteca pygame.mixer é utilizada para tocar os arquivos de áudio gerados pela conversão de texto em fala, proporcionando uma experiência interativa.

## **Funcionalidades**

#### **De Fala para Texto:** Converte palavras faladas em texto para processamento posterior.
#### **De Texto para Fala:** Converte texto em fala e reproduz em voz alta.
#### **Busca na Web:** Permite que o usuário faça buscas no Google e no YouTube por comando de voz.
##### Busca no Wikipedia: Recupera resumos do Wikipedia para consultas específicas.
##### Piadas: Conta piadas aleatórias utilizando a biblioteca pyjokes.
##### Reprodução de Música: Toca músicas a partir de um diretório específico no computador.
##### Lixeira: Esvazia a lixeira.
##### Hora: Informa a hora atual.
##### Comando de Saída: Encerra o assistente com uma mensagem de despedida.
