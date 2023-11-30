import pyauti.FAILSAFE = True

def editar_dados():
    # Espere alguns segundos antes de começar
    pyautogui.PAUSE = 10
    
    # Lista de teclas a serem pressionadas
    teclas_para_pressionar = [
        "right", "right", "right", "right", "right", "right", "right", "right", "right", "right", "right", "right", 
        "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", "delete", 
        "down", "home"]  # Substitua com as teclas que você precisa

    # Ajustar o intervalo para um valor menor
    intervalo_entre_teclas = 0.01

    # Quantidade de vezes que as teclas serão pressionadas
    quantidade_de_vezes = 62258  # Substituidade desejada

    # Pressclas com o intervalo ajustado
    pyautogui.write(teclas_para_pressionar * quantidade_de_vezes, interval=intervalo_entre_teclas)

if __name__ == "__main__":
    editar_banco_dados()

    
