import cv2 # type: ignore
import camera.camera_video as gravacao
import core.processador as processador

def main():

    video = gravacao.CameraGravacao()
    proc= processador.TrackerProcessador()

    
    try:
        while True:
            
            frame_processado = proc.aguardar_novo_frame(timeout=0.01)
            if frame_processado is None:
                continue
            cv2.imshow('YOLO Detections (Left) | Tracking Results (Right)', frame_processado)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break            

    
    finally:        
        video.parar()         
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()