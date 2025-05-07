import torch # type: ignore

def obter_cpu_gpu():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("CUDA GPU disponivel::",  torch.cuda.is_available())  # Should print True
    print("CUDA device name:: ", torch.cuda.get_device_name(0))  # Should print your GPU name    
    return device

class ByteTrackerArgs:
    track_thresh = 0.5  # Detection confidence threshold
    track_buffer = 30   # Number of frames to keep lost tracks
    match_thresh = 0.8  # Matching threshold
    frame_rate = 30     # Video frame rate
    mot20 = False       # MOT20-specific flag (default False)

