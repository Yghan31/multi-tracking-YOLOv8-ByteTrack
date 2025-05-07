import cv2 # type: ignore
import copy
import threading

class Frames:
    instance = None
    lock = threading.Lock()
    
    def __new__(cls):
        if cls.instance is None:
            with cls.lock:
                if cls.instance is None:
                    cls.instance = super(Frames, cls).__new__(cls)
                    cls.instance._initialize()
        return cls.instance
    
    def _initialize(self):
        self.frame = None
        self.lock = threading.Lock()
        self.fator_redimensa = 1  
        self.evento_novo_frame = threading.Event()
    
    def atualizar_frame(self, frame):
        with self.lock:
            frame_reduzido = cv2.resize(frame, None, fx=self.fator_redimensa, fy=self.fator_redimensa)
            self.frame = frame_reduzido
            self.evento_novo_frame.set()
            
    
    def obter_frame(self):
        with self.lock:
            if self.frame is None:
                return None
            return copy.deepcopy(self.frame)
        
    def aguardar_novo_frame(self, timeout=None):
        self.evento_novo_frame.wait(timeout)
        return self.obter_frame()
    