## The Black Pearl – KU Leuven Datathon 2025

Our team, The Black Pearl, consists of Michael Carlo, Giovanni Dettori, Fabrizio Sacco, Keith Atienza, and Seamus Conlon. We are participating in the KU Leuven Datathon, analyzing World War I propaganda posters using LLMs for historical interpretation, theme identification, sentiment analysis, and trend detection.

## Project Overview

The goal of this project is to perform sentiment analysis and identify temporal trends in World War I propaganda poster data using Large Language Models (LLMs). The dataset consists of OCR-extracted text files stored in the `data/` folder. We utilize both local and cloud-based models for analysis:
- **Local Inference**: Running LLMs locally using Ollama.
- **Cloud-Based Inference**: Using pre-trained models via the Hugging Face API.

To facilitate exploration and analysis, the project structure is as follows:
- `data/` – Contains the OCR-extracted text files.
- `notebooks/` – Jupyter notebooks for statistical analysis and visualization.
- `src/` – Source code directory:
  - `Ollama.py` – Runs a model locally using Ollama and conducts text analysis.
  - `HF_text_analysis.py` – Uses the Hugging Face API for analysis.

## Project Setup

To get started with The Black Pearl's analysis of WWI propaganda posters, follow the steps below to set up the necessary tools and dependencies.

### 1. Setting Up Hugging Face API
We use Hugging Face's pre-trained models for text analysis. Follow these steps to create an API key:

1. **Register on Hugging Face**: Go to [Hugging Face](https://huggingface.co/) and sign up for an account.
2. **Generate an API Key**:
   - Click on your profile icon in the top right corner.
   - Navigate to "Settings" > "Access Tokens."
   - Click "New Token," name it appropriately (e.g., `datathon-project`), and choose "Write" permissions.
   - Copy and save the API key securely.
3. **Store the API Key**:
   - Export it as an environment variable in your terminal power shell in vscode:
     ```bash
     $env:HF_API_KEY="your_api_key_here"
     ```
   - Or store it in a `.env` file:
     ```
     HUGGINGFACE_API_KEY=your_api_key_here
     ```

### 2. Installing and Running Ollama Locally
To analyze text files locally, we use [Ollama](https://ollama.ai/) for running LLMs without requiring cloud-based inference.

#### **Installation**
1. **Download Ollama**:
   - MacOS: `brew install ollama`
   - Linux: Follow instructions at [Ollama Install](https://ollama.ai/docs)
   - Windows (WSL recommended): Set up a compatible environment following [Ollama's guide](https://ollama.ai/docs/windows)

2. **Install Required Models**:
   - Run the following command to install a model like `mistral`:
     ```bash
     ollama pull mistral
     ```
   - To see available models:
     ```bash
     ollama list
     ```

3. **Run a Model**:
   - Start a local instance with:
     ```bash
     ollama run mistral
     ```
   - Or interact with the model in a script:
     ```python
     import ollama
     response = ollama.chat(model='mistral', messages=[{"role": "user", "content": "Analyze this text..."}])
     print(response['message'])
     ```

### 3. Cloning the Repository & Running the Project
1. **Clone the GitHub Repository**:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis**:
   - Using Ollama:
     ```bash
     python src/ollama_runner.py
     ```
   - Using Hugging Face API:
     ```bash
     python src/huggingface_runner.py
     ```

This setup ensures you have everything needed to analyze WWI propaganda texts efficiently. If you run into issues, check the official documentation for Hugging Face and Ollama or reach out to the team!

