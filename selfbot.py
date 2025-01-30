import requests
import time
import threading

tokens = [
    "",  # Reemplaza con tu primer token
    "",  # Reemplaza con tu segundo token
    "",  # Reemplaza con tu tercer token
    "",  # Reemplaza con tu cuarto token
    "",  # Reemplaza con tu quinto token
]

channels = [
    "",  # ID del primer canal
    "",  # ID del segundo canal
    "",  # ID del tercer canal
]

def send_multiple_messages(token, channel_id, message, count, delay):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,  
        "Content-Type": "application/json",
    }

    for i in range(count):
        data = {
            "content": message,  
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200 or response.status_code == 204:
            print(f"✅ [{token[:10]}...] Mensaje {i + 1}/{count} enviado al canal {channel_id}.")
        else:
            print(f"⚠️ [{token[:10]}...] Error al enviar mensaje {i + 1}/{count} al canal {channel_id}: {response.status_code} - {response.text}")

        time.sleep(delay)

def send_messages_to_channels(token, message, count, delay):
    threads = []

    for channel_id in channels:
        thread = threading.Thread(target=send_multiple_messages, args=(token, channel_id, message, count, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def send_messages_with_all_tokens(message, count, delay):
    threads = []

    for token in tokens:
        thread = threading.Thread(target=send_messages_to_channels, args=(token, message, count, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("✅ Todos los mensajes han sido enviados a todos los canales.")

def main():
    while True:
        print("\n=== Enviar mensajes a múltiples canales con todos los tokens - C47CH-404 ===")
        print("0. Salir")

        try:
            message = input("Mensaje: ")
            count = int(input("¿Cuántos mensajes quieres enviar por token por canal?: "))
            delay = float(input("Tiempo de espera entre mensajes (en segundos): "))

            # Enviar mensajes con todos los tokens y canales
            send_messages_with_all_tokens(message, count, delay)
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
        except KeyboardInterrupt:
            print("\n👋 Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
