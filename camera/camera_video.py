import cv2 # type: ignore
import time
import threading
import camera.frames as frames

class CameraGravacao:
    def __init__(self, show=False):
        self.cap = None
        self.fps = None
        self.show = show
        self.delay = None
        self.thread = None
        self.running = False
        
        self.iniciar()

    def iniciar(self):
        # Path to your video file
        video_path = './apoio/cows3.mp4'

        # Open the video file
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            print('Error: Could not open video file.')
            exit()

        # Get FPS from video properties
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        if self.fps == 0:
            self.fps = 25  # fallback to 25 if FPS is not available
        print(f'Video FPS: {self.fps}')
        self.delay = 1.0 / self.fps

        self.running = True
        self.thread = threading.Thread(target=self.play_video)
        self.thread.start()

    def play_video(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                self.running = False
                break

            frames.Frames().atualizar_frame(frame) 

            if self.show:
                cv2.imshow('Video Playback', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False
                    break
            time.sleep(self.delay)
        
        self.cap.release()
        if self.show:
            cv2.destroyAllWindows()
        self.running = False  # Ensure running is set to False when video ends

    def parar(self):
        self.running = False

if __name__ == "__main__":
    cam = CameraGravacao()
    try:
        while cam.running:
            time.sleep(1)
    except KeyboardInterrupt:
        cam.parar()