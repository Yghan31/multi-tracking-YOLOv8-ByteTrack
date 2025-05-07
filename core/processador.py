import threading
import apoio.utils as utils
from ultralytics import YOLO # type: ignore
import camera.frames as frames
import core.funcoes as funcoes
from core.ByteTrack.yolox.tracker.byte_tracker import BYTETracker


class TrackerProcessador:
    def __init__(self):
        self.frame_buffer = frames.Frames()  # Get singleton instance
        self.running = False
        self.thread = None
        
        # Load YOLOv8n model (nano version - fastest)
        self.model = YOLO("yolov8m.pt")
        self.model.to(utils.obter_cpu_gpu())
        
        # Initialize ByteTrack
        self.tracker = BYTETracker(utils.ByteTrackerArgs())
        
        # Set to store unique car track IDs
        self.IDs_unicos = set()
        
        # For visualization
        self.ultimas_deteccoes = []
        self.ultimas_tracks = []
        self.width = 0
        self.height = 0

        self.lock = threading.Lock()
        self.frame_processado = None
        self.evento_frame_processado = threading.Event()

        self.start()

    def atualizar_frame_processado(self, frame_proc):
        with self.lock:
            self.frame_processado = frame_proc
            self.evento_frame_processado.set()        

    def obter_frame_processado(self):
        with self.lock:
            if self.frame_processado is None:
                return None
            return self.frame_processado
        
    def aguardar_novo_frame(self, timeout=None):
        self.evento_frame_processado.wait(timeout)
        return self.obter_frame_processado()       
    
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.processar_frames)
        self.thread.daemon = True
        self.thread.start()
    
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
    
    def processar_frames(self):
        while self.running:
            frame = self.frame_buffer.aguardar_novo_frame(timeout=0.01)
            if frame is None:
                continue
            
            if self.width == 0:
                self.width = frame.shape[1]
                self.height = frame.shape[0]
            
            # Run YOLOv8 detection
            pred_yolo = self.model(frame, conf=0.4, classes=[19])[0]
            
            # Process detections
            lista_objetos_yolo = funcoes.processa_resultado_yolo(self, pred_yolo)

            if lista_objetos_yolo is None: continue
            
            # Update tracker
            img_info = (self.height, self.width)
            img_size = (self.height, self.width)
            lista_trackings = self.tracker.update(lista_objetos_yolo, img_info, img_size)
            
            ids_atuais = set()

            funcoes.processa_tracking(self, lista_trackings, ids_atuais)

            funcoes.remove_linha_fora_cena(self, ids_atuais)
            
            yolo_frame, track_frame = funcoes.copia_frames(frame)
            
            funcoes.desenha_resultado_yolo(self, yolo_frame)
            
            funcoes.desenha_resultado_tracking(self, track_frame)

            funcoes.desenha_linha_tracking(self, track_frame)
        
            funcoes.imprime_resultado(self, yolo_frame, track_frame)
