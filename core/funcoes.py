import cv2 # type: ignore
import numpy as np # type: ignore

# Draw trajectory lines with unique color per track
def obter_cor(idx):
    np.random.seed(idx)
    color = tuple(int(x) for x in np.random.choice(range(50, 256), size=3))
    return color

def copia_frames(frame):
    # Create copies for visualization
    yolo_frame = frame.copy()
    track_frame = frame.copy() 
    return yolo_frame, track_frame   

def processa_resultado_yolo(self, pred_yolo):
    boxes = None
    scores = None
    lista_objetos_yolo = []
    if pred_yolo.boxes is not None and len(pred_yolo.boxes) > 0:
        boxes = pred_yolo.boxes.xyxy.cpu().numpy()
        scores = pred_yolo.boxes.conf.cpu().numpy()        
        if len(boxes) > 0:
            lista_objetos_yolo = np.hstack((boxes, scores[:, np.newaxis])).astype(np.float64)
    
    if boxes is None: return None

    # Store results for visualization
    self.ultimas_deteccoes = []    
    for box, score in zip(boxes, scores):
        self.ultimas_deteccoes.append((box, score))   

    return np.array(lista_objetos_yolo, dtype=np.float64) if len(lista_objetos_yolo) > 0 else np.empty((0, 5), dtype=np.float64)

def processa_tracking(self, targets, ids_atuais):
    self.ultimas_tracks = []
    if not hasattr(self, 'track_history'):
        self.track_history = {}
    if not hasattr(self, 'last_seen'):
        self.last_seen = {}
    self.frame_idx = getattr(self, 'frame_idx', 0) + 1

    for t in targets:
        self.IDs_unicos.add(t.track_id)
        self.ultimas_tracks.append((t.tlbr, t.track_id))
        ids_atuais.add(t.track_id)
        # Calculate centroid and store history with frame index
        x1, y1, x2, y2 = t.tlbr
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        if t.track_id not in self.track_history:
            self.track_history[t.track_id] = []
        self.track_history[t.track_id].append((cx, cy, self.frame_idx))
        # Remove points older than 50 frames
        self.track_history[t.track_id] = [pt for pt in self.track_history[t.track_id] if self.frame_idx - pt[2] <= 50]
        # Update last seen
        self.last_seen[t.track_id] = self.frame_idx    

def remove_linha_fora_cena(self, ids_atuais):
    # Remove trajectories for tracks that are no longer active after 3 seconds
    FPS = 30  # Set your video FPS here
    max_missing = 2 * FPS
    to_delete = [tid for tid in self.track_history if tid not in ids_atuais and self.frame_idx - self.last_seen.get(tid, 0) > max_missing]
    for tid in to_delete:
        del self.track_history[tid]
        if tid in self.last_seen:
            del self.last_seen[tid]    

def desenha_resultado_yolo(self, yolo_frame):
    # Draw YOLO detections
    for box, score in self.ultimas_deteccoes:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(yolo_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(yolo_frame, f"{score:.2f}", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)    
        
def desenha_resultado_tracking(self, track_frame):
    # Draw tracking results
    for tl, track_id in self.ultimas_tracks:
        cv2.rectangle(track_frame, (int(tl[0]), int(tl[1])), 
                        (int(tl[2]), int(tl[3])), (0, 255, 0), 2)
        cv2.putText(track_frame, f"ID: {track_id}", 
                    (int(tl[0]), int(tl[1]) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)    

def desenha_linha_tracking(self, track_frame):
    if hasattr(self, 'track_history'):
        for track_id, points in self.track_history.items():
            if len(points) > 1:
                color = obter_cor(track_id)
                for j in range(1, len(points)):
                    pt1 = (points[j-1][0], points[j-1][1])
                    pt2 = (points[j][0], points[j][1])
                    cv2.line(track_frame, pt1, pt2, color, 2)         

def imprime_resultado(self, yolo_frame, track_frame):
    # Combine frames
    vis_frame = np.hstack((yolo_frame, track_frame))
    vis_frame = cv2.resize(vis_frame, None, fx=0.5, fy=0.5)
    self.atualizar_frame_processado(vis_frame)            
    #self.atualizar_frame_processado(cv2.resize(track_frame, None, fx=0.7, fy=0.7))            

