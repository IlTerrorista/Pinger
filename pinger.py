import os
import platform


print("""











                                                ██▓███   ██▓ ███▄    █   ▄████ ▓█████  ██▀███  
                                                ▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
                                                ▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
                                                ▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
                                                ▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
                                                ▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
                                                ░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
                                                    ░░        ▒ ░   ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
                                                        ░           ░       ░    ░  ░   ░     
                                                
                                                              author:IlTerrorista
                                                github:https://github.com/IlTerrorista/Pinger










""")

def ping_ip(ip):
    # Controlla se il sistema operativo è Windows o Unix (Linux/macOS)
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Comando per eseguire il ping
    command = f"ping {param} 150000000000000000000000000000000000000000000 {ip}"  # Il parametro 4 invia 4 pacchetti di ping

    # Esegui il comando
    response = os.system(command)

    # Controlla se il ping è riuscito
    if response == 0:
        print(f"{ip} è raggiungibile!")
    else:
        print(f"{ip} non è raggiungibile.")

# Usa la funzione con un esempio di IP
ping_ip("1.1.1.1")  # Ad esempio, ping a Google DNS
