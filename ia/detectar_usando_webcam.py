from ultralytics import YOLO  # Importa a classe YOLO para realizar a detecção e rastreamento de objetos
import cv2  # Importa a biblioteca OpenCV para manipulação de vídeo/imagens
from collections import defaultdict  # Importa defaultdict para criar dicionários com valores padrão
import numpy as np  # Importa NumPy para manipulação de arrays numéricos

cap = cv2.VideoCapture(0)  # Inicia a captura de vídeo da webcam

model = YOLO("yolo11m.pt")  # Carrega o modelo YOLO pré-treinado para detecção de objetos

track_history = defaultdict(lambda: [])  # Armazena o histórico de rastreamento de objetos
seguir = True  # Controla se o rastreamento deve ser realizado
deixar_rastro = False  # Controla se o rastro do objeto deve ser desenhado no vídeo

while True:
    success, img = cap.read()  # Captura um frame do vídeo

    if success:
        if seguir:
            results = model.track(img, persist=True)  # Realiza o rastreamento de objetos
        else:
            results = model(img)  # Apenas detecta objetos (sem rastreamento)

        for result in results:
            img = result.plot()  # Desenha as detecções no frame

            if seguir and deixar_rastro:
                try:
                    boxes = result.boxes.xywh.cpu()  # Obtém as coordenadas das caixas delimitadoras
                    track_ids = result.boxes.id.int().cpu().tolist()  # Obtém os IDs de rastreamento

                    for box, track_id in zip(boxes, track_ids):
                        x, y, w, h = box  # Extrai as coordenadas da caixa
                        track = track_history[track_id]  # Obtém o histórico de rastreamento para o objeto
                        track.append((float(x), float(y)))  # Adiciona a posição atual ao histórico

                        if len(track) > 30:  # Limita o histórico a 30 pontos
                            track.pop(0)  # Remove os pontos mais antigos

                        # Desenha a linha do rastro no frame
                        points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                        cv2.polylines(img, [points], isClosed=False, color=(230, 0, 0), thickness=5)
                except:
                    pass  # Ignora erros no rastreamento

        cv2.imshow("Tela", img)  # Exibe o frame processado

    k = cv2.waitKey(1)  # Aguarda por uma tecla pressionada
    if k == ord('q'):  # Se a tecla 'q' for pressionada, encerra o loop
        break

cap.release()  # Libera a captura de vídeo
cv2.destroyAllWindows()  # Fecha todas as janelas abertas
print("desligando")  # Imprime uma mensagem indicando que o programa terminou
