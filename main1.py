import sounddevice as sd
def record_audio(duration=5, fs=44100):
  """Records audio from the microphone for a specified duration.

  Args:
      duration: The duration of the recording in seconds (default 5).
      fs: The sampling rate of the audio (default 44100 Hz).

  Returns:
      A NumPy array of the recorded audio data.
  """
  # This will record audio for 'duration' seconds and return it as a NumPy array.
  return sd.rec(int(duration * fs), samplerate=fs, channels=1)
while True:  # Loop for continuous prediction
  # Record audio for 5 seconds
  data = record_audio()
  sd.wait()  # Wait for recording to finish

  # Preprocess the recorded audio (extract features)
  X = np.array(extract_features(data))
  X = scaler.transform(X.reshape(1,-1))

  # Predict emotion using the loaded model
  pred_test = model.predict(np.expand_dims(X, axis=2))
  y_pred = encoder.inverse_transform(pred_test)

  # Print the predicted emotion
  print("Predicted Emotion:", y_pred[0][0])
  
  # Optionally, play an audio cue or display the emotion visually.
