import pyaudio

def record_audio(chunk=1024, format=pyaudio.paInt16, channels=1, rate=44100, record_seconds=5):

  """
  Records audio from the microphone for a specified duration.

  Args:
      chunk: The number of frames to read at a time (default 1024).
      format: The audio format (default pyaudio.paInt16).
      channels: The number of audio channels (default 1 for mono).
      rate: The sampling rate of the audio (default 44100 Hz).
      record_seconds: The duration of the recording in seconds (default 5).

  Returns:
      A list of audio frames recorded from the microphone.
  """

  p = pyaudio.PyAudio()

  stream = p.open(format=format,
                  channels=channels,
                  rate=rate,
                  input=True,
                  frames_per_buffer=chunk)

  frames = []

  print("Recording...")

  # Loop for the specified recording duration
  for _ in range(int(rate / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

  print("Finished recording.")

  # Stop the stream and close PyAudio
  stream.stop_stream()
  stream.close()
  p.terminate()

  return frames
