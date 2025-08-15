# 🎵 ToneTango — Speech Emotion Recognition

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![Librosa](https://img.shields.io/badge/Librosa-Audio%20Processing-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

ToneTango is a **Speech Emotion Recognition (SER)** system that detects human emotions from voice inputs using a **CNN-based deep learning** model.  
It processes audio, extracts features like **MFCC**, **Chroma**, and **Mel Spectrogram**, and classifies emotions such as:

> 😊 Happy | 😢 Sad | 😡 Angry | 😨 Fear | 😖 Disgust | 😐 Neutral | 😌 Calm | 😲 Surprised

---

## 🚀 Features

- 🎤 Audio preprocessing & augmentation *(noise addition, pitch shift, time stretch)*
- 📂 Integration of **RAVDESS**, **TESS**, **CREMA-D**, and **SAVEE** datasets
- 🧠 CNN architecture for high-accuracy classification
- 📈 Achieves **~85% accuracy** on test data
- 🔌 Modular code for easy extension & real-time applications

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** TensorFlow/Keras, Librosa, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn



1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/ToneTango.git
cd ToneTango
```

2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

3️⃣ Open **ToneTango.ipynb** to view the final implementation and run code  
```bash
jupyter notebook notebooks/ToneTango.ipynb
```

---

## 🎯 Applications

- 🤖 Virtual assistants  
- 📞 Call center sentiment monitoring  
- 🏥 Healthcare & mental wellness tracking  
- 🎓 Emotion-aware e-learning platforms  
- 🎮 Gaming & interactive media  


---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

> 💡 **Note:** For the complete implementation, refer to **`ToneTango.ipynb`** 
