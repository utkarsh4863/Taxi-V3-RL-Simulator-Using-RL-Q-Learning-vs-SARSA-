# 🚖 RL Taxi Project: Q-Learning vs SARSA

A Reinforcement Learning simulator for the **Taxi-v3 environment** implementing **Q-Learning** and **SARSA** algorithms.   
Compare the performance of both RL algorithms and visualize results interactively with **Streamlit**.

---

## 🔹 Features

- **Q-Learning** and **SARSA** algorithms for Taxi-v3.
- Performance comparison using pre-trained models.
- Interactive **Streamlit app**:
  - Real-time taxi environment visualization.
  - Choose algorithm (Q-Learning or SARSA).
  - Step-by-step agent behavior observation.

---

## 📁 Project Structure

```
RL-Taxi-Project/
│── models/            # Pre-trained models
│   ├── qlearning.npy
│   ├── sarsa.npy
│── app/               # Streamlit app
│   ├── streamlit_app.py
│── notebooks/         # Experiment notebooks
│   ├── taxi_comparison.ipynb
│── README.md          # Project documentation
│── requirements.txt   # Python dependencies
```

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/utkarsh4863/RL-Taxi-Project.git
cd RL-Taxi-Project
```

**2. Create and activate a virtual environment**

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the Streamlit App**
```bash
streamlit run app/streamlit_app.py
```
Open `http://localhost:8501` to interact with the app.  
Select **Q-Learning** or **SARSA** and watch the Taxi agent in action!

---

## 🌐 Live Demo

App deployed via Streamlit Community Cloud:  
[https://h4bkdodtnc5jdses5axvj9.streamlit.app/](https://h4bkdodtnc5jdses5axvj9.streamlit.app/)

---

## 📊 Notebooks & Models

- **Experiment Notebook:** `notebooks/taxi_comparison.ipynb`
- **Pre-trained Models:**  
  `models/qlearning.npy`  
  `models/sarsa.npy`

Models are loaded within the Streamlit app for fast simulation.

---

## 📌 Notes

- `venv/` is **excluded** from source control via `.gitignore`.
- Ensure all dependencies are installed before running locally.
- Models are stored in `.npy` format (lightweight transfers).
- Compatible with Python 3.7+.

---


## 👨‍💻 Author

**Utkarsh Kashyap**  
[GitHub Profile](https://github.com/utkarsh4863)
