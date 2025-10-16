# Plasmid Copy Number Analysis: Integrating Theory and Machine Learning

This repository contains the data and code for the manuscript **"Integrating theory and machine learning to reveal determinants of plasmid copy number"**.
##  Methodology

### 1. Data Acquisition
Genome assemblies were downloaded using NCBI dataset command line tools. The accession numbers are provided in `Preprocessing/ Accessions.txt`.

### 2. Plasmid Extraction
Plasmid sequences were extracted from genome assemblies using `Preprocessing/plasmids_extraction.py`.

### 3. Data Filtering
We filtered the extracted plasmids to include only those previously reported in Rohan Maddamsetti's studies, ensuring data quality and comparability.

**Reference:**  
**Maddamsetti, R.** *et al.* Scaling laws of bacterial and archaeal plasmids. *Nature Communications* **16**, 6023 (2025). https://doi.org/10.1038/s41467-025-6023-x
### 4. Feature Engineering Pipeline

#### Sequence Annotation:
- **Gene Prediction & CDS Identification**: Performed using `Prodigal.ipynb`
- **Protein Domain Analysis**: Conducted using `Hmmscan.ipynb`

*Both annotation scripts are located in: `Figure_2A/Sequence_Annotation_and_Feature_Extraction/`*

### 5. Model Training & Evaluation
Machine learning models were trained and evaluated using the code in `Figure_2C/Final_model_code.ipynb`.

### 6. Available Models
We trained two distinct models for plasmid copy number prediction:
- **Location**: `PCN_Prediction_Models/`
- **Format**: .pkl

## 🚀 Usage Pipeline

### Step 1: Preprocessing
Extract plasmid sequences from your genome assemblies following our methodology.

### Step 2: Feature Engineering
Run the feature extraction pipeline as described in Section 4.

### Step 3: PCN Prediction
Load the pre-trained models and apply them to your processed data.

### Example Implementation
See `4A/Clinical_isolates-PCN_predictions.ipynb` for a complete worked example using clinical isolate data.