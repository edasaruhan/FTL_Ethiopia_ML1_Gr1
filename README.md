# AI-Driven Hybrid Cyber Defensive System for Intelligent Malware Detection and Threat Insight

## Overview
The proposed project is an AI-based intelligent cyber defense tool that integrates **Malware Detection** with **Natural Language Processing (NLP)** for **Threat Intelligence Insights**. The system uses a hybrid AI model, combining **Machine Learning (ML)** and **Deep Learning (DL)** techniques to enhance cybersecurity defenses. Its primary goal is to detect, analyze, and mitigate cyber threats proactively, helping organizations prevent and respond to cyberattacks in real-time.

### 🧠 Key Features:
- **AI-powered malware detection**
- **NLP-driven threat intelligence**
- **hybrid based malware detection models**
- **Feature-based classical ML classifier**
- **Multithreaded processing for performance**
- **Custom GUI/icon support**
- **Jupyter Notebook for training and analysis**
- **Modular and extensible codebase**
- **Behavioral analysis**
- **Automated response mechanisms**
- **Explainable AI (XAI)** for decision-making transparency
## 🗂️ Project Structure

```bash
Project/
│
├── dataset/ # Malware and benign sample data
├── doc/ # Documentation report
├── model/ # Pretrained models (CNN, LSTM, etc.)
├── notebook/ # Jupyter notebook for training
├── src/ # Source code (scripts and icons)
│ ├── Malware_detection_tool.py
│ ├── multithreading.py
│ └── *.ico # Custom icons for UI
│
├── .gitignore
├── README.md
├── requirements.txt
```

## SDG Alignment
This project aligns with the following **Sustainable Development Goals (SDGs)**:
- **Goal 9**: Strengthening digital infrastructure security
- **Goal 16**: Protecting institutions from cybercrime
- **Goal 4**: Promoting cybersecurity education

By developing a robust AI-based cyber defense system, this project contributes to a safer digital environment, reduces cyber threats, and fosters cybersecurity innovation.

## Literature Review
- **Kim et al. (2021)**: Proposed a deep learning-based malware detection framework using behavioral analysis.
- **Zhang et al. (2022)**: Explored NLP for cyber threat intelligence extraction, which this project enhances by combining it with AI-driven threat detection.

## Methodology

### Dataset
The dataset includes **Malware Samples** collected from public sources like:
- VirusTotal
- MalwareBazaar
- Cybersecurity research repositories

It includes:
- **CSV**: Structured logs
- **JSON**: Threat intelligence feeds
- **Text**: For NLP processing

### Approach
The hybrid deep learning model integrates various techniques for enhanced threat detection:
- **CNNs** or **RNNs** for malware classification
- **Transformer models** (e.g., BERT) for NLP-based threat intelligence
- **LSTMs** or **Autoencoders** for behavioral anomaly detection
- **Hybrid model**:Use hybrid of CNN and LSTM

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: TensorFlow, PyTorch, Scikit-learn, etc.
- install from requirments.txt
```bash
pip install -r requirements.txt
```

### ▶️ Run the Tool
-  Clone the repository:
   ```bash
   git clone https://github.com/edasaruhan/FTL_Ethiopia_ML1_Gr1.git
   ```
- test the malware detection model
```bash
cd src
python Malware_detection_tool.py
```
- 📓 Model Training: To retrain the model or analyze data:

```bash
cd notebook
jupyter notebook Training_Model.ipynb
```