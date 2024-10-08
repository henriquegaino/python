from ultralytics import YOLO  # Importa a classe YOLO da biblioteca ultralytics para fazer a detecção de objetos.
import cv2  # Importa a biblioteca OpenCV para captura e manipulação de vídeo/imagem.
from collections import defaultdict  # Importa defaultdict para criar dicionários com valor padrão.
import numpy as np  # Importa NumPy para manipulação de arrays numéricos.

# Cria uma variável 'cap' para capturar vídeo da webcam (índice 0, que geralmente é a webcam interna).
cap = cv2.VideoCapture(0)  
# Alternativa para capturar vídeo de outra câmera (índice 1 ou usando DirectShow no Windows):
# cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  

# Carrega o modelo YOLO a partir de um arquivo de peso pré-treinado ('yolo11n.pt').
# YOLO (You Only Look Once) é uma técnica de detecção de objetos em tempo real.
model = YOLO("yolo11m.pt")  # Carrega o modelo YOLO para fazer a detecção de objetos no vídeo.

# 'track_history' é um dicionário com listas de histórico de rastreamento para cada objeto detectado.
track_history = defaultdict(lambda: [])  
seguir = True  # Controla se o rastreamento deve ser feito.
deixar_rastro = True  # Define se será desenhada uma linha para indicar o rastro do objeto.

# Inicia um loop infinito para processar o vídeo quadro a quadro.
while True:  
    # Lê o próximo frame do vídeo. 'success' indica se a captura foi bem-sucedida, e 'img' contém o frame capturado.
    success, img = cap.read()  

    # Se a captura foi bem-sucedida, processa o frame.
    if success:  
        if seguir:  # Se o rastreamento estiver habilitado:
            # Usa o modelo YOLO para detectar e rastrear objetos no frame.
            # 'persist=True' mantém o histórico de rastreamento de objetos entre frames.
            results = model.track(img, persist=True)  
        else:  # Caso contrário, faz apenas a detecção (sem rastreamento).
            results = model(img)  

        # Processa a lista de resultados da detecção.
        for result in results:  
            # Desenha as detecções (caixas delimitadoras, etc.) diretamente no frame de imagem.
            img = result.plot()  

            # Se o rastreamento estiver habilitado e o rastro for para ser desenhado:
            if seguir and deixar_rastro:  
                try:  
                    # Obtém as caixas delimitadoras ('boxes') e IDs de rastreamento ('track_ids') para cada objeto detectado.
                    boxes = result.boxes.xywh.cpu()  # Coordenadas das caixas (centro, largura, altura) no formato [x, y, w, h].
                    track_ids = result.boxes.id.int().cpu().tolist()  # IDs de rastreamento para cada objeto.

                    # Para cada caixa e ID, plota o rastro (trajetória) do objeto.
                    for box, track_id in zip(boxes, track_ids):  
                        x, y, w, h = box  # Desempacota as coordenadas da caixa.
                        track = track_history[track_id]  # Obtém o histórico de rastreamento para o objeto com o ID específico.
                        track.append((float(x), float(y)))  # Adiciona o ponto central da caixa atual ao histórico.

                        # Mantém o histórico de rastreamento limitado a 30 pontos para evitar que a linha fique muito longa.
                        if len(track) > 30:  
                            track.pop(0)  # Remove os pontos mais antigos do rastro.

                        # Desenha a linha do rastro no frame de vídeo.
                        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))  # Converte a lista de pontos para o formato adequado.
                        cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)  # Desenha as linhas do rastro.
                except:  
                    pass  # Se houver algum erro, simplesmente o ignora (o bloco 'try' previne falhas).

        # Mostra o frame processado em uma janela chamada "Tela".
        cv2.imshow("Tela", img)  

    # Aguarda 1 milissegundo por uma tecla pressionada. Se a tecla 'q' for pressionada, sai do loop.
    k = cv2.waitKey(1)  
    if k == ord('q'):  
        break  # Sai do loop.

# Libera a captura de vídeo e fecha todas as janelas abertas quando o loop for interrompido.
cap.release()  
cv2.destroyAllWindows()  
print("desligando")  # Exibe uma mensagem indicando que o programa terminou.
