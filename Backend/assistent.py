# main.py

from Head.wake_word import WakeWordDetector

def assistent():
    detector = WakeWordDetector()
    try:
        while True:
            # 1. Wait for wake word
            if detector.detect():
                # 2. Start Brain
                
                print("🛑 Session ended. Waiting for wake word again...")
    except KeyboardInterrupt:
        print("\n🛑 Exiting assistant...")
    finally:
        detector.cleanup()

if __name__ == "__main__":
    assistent()