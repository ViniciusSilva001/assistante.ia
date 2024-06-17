import pyttsx3
import webbrowser
import datetime
import urllib.parse
import pywhatkit as kit
import wikipedia

# Inicializar a síntese de voz
engine = pyttsx3.init()

# Função para a assistente falar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para obter o comando do usuário via entrada de texto
def get_command():
    command = input("Digite seu comando: ").lower()
    return command

# Função para salvar comandos em um arquivo de log
def save_command(command):
    with open("command_log.txt", 'a') as file:
        file.write(command + '\n')

# Função para criar uma lista
def create_list():
    speak("Qual o nome da sua lista?")
    list_name = input("Digite o nome da lista: ")
    if list_name:
        file_name = list_name + ".txt"
        with open(file_name, 'w') as file:
            speak("Lista criada. Pode adicionar itens. Digite 'fim' para encerrar.")
            while True:
                item = input("Digite um item para adicionar à lista ou 'fim' para encerrar: ").lower()
                if item == "fim":
                    break
                file.write(item + '\n')
                speak(f"{item} adicionado à lista {list_name}.")
        speak("Lista concluída.")

# Função para abrir um website
def open_website():
    speak("Qual website você quer acessar?")
    website = input("Digite o website (sem 'https://'): ").lower()
    if website:
        url = "https://" + website
        webbrowser.open(url)
        speak(f"Abrindo {website}")

# Função para pesquisar na Wikipedia
wikipedia.set_lang('pt')
def abrir_wikipedia(query=None):
    if not query:
        speak("O que você quer buscar na Wikipedia?")
        query = input("Digite a busca para a Wikipedia: ")
    
    if query:
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(f"Aqui está o resumo encontrado na Wikipedia: {result}")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Não Encontrado. Por favor, seja mais específico.")
        except wikipedia.exceptions.PageError as e:
            speak("Nenhuma página encontrada na Wikipedia. Por favor, tente novamente.")

# Função para buscar no YouTube
def abrir_youtube():
    speak("O que você quer buscar no YouTube?")
    search_query = input("Digite a busca para o YouTube: ")
    if search_query:
        query = urllib.parse.quote(search_query)
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Buscando por {search_query} no YouTube")

# Função para lembrar de compromissos
def remember_appointment():
    speak("Qual compromisso você quer que eu lembre?")
    appointment = input("Digite o compromisso: ")
    if appointment:
        speak("Quando é o compromisso? Por favor, digite a data no formato dia mês ano (ex: 24 05 2024).")
        date = input("Digite a data do compromisso: ")
        try:
            date = datetime.datetime.strptime(date, "%d %m %Y")
            with open("appointments.txt", 'a') as file:
                file.write(f"{appointment} - {date.strftime('%d/%m/%Y')}\n")
            speak(f"Compromisso '{appointment}' marcado para {date.strftime('%d/%m/%Y')}.")
        except ValueError:
            speak("Data inválida. Por favor, tente novamente.")

def encerrameto():
    speak('Quero encerrar o trabalho tocando um hino')
    kit.playonyt('https://www.youtube.com/watch?v=EcjESxx2ZRU')

# Função principal da assistente
def virtual_assistant():
    speak("Olá, como posso ajudar você hoje?")
    while True:
        speak('Você pode me pedir as seguintes coisas: ')
        print('- Criar uma nova lista')
        print('- Abrir um site')
        print('- Pesquisar no youtube')
        print('- Abrir Wikipedia')
        print('- Adicionar um Compromisso')
        print('- Encerrar Trabalho')
        command = get_command()
        if command:
            save_command(command)
            if "criar nova lista" in command:
                create_list()
            elif "abrir site" in command:
                open_website()
            elif "abrir no youtube" in command:
                abrir_youtube()
            elif 'abrir wikipedia' in command:
                abrir_wikipedia()
            elif "adicionar compromisso" in command:
                remember_appointment()
            elif "encerrar" in command:
                encerrameto()
                break

if __name__ == "__main__":
    virtual_assistant()