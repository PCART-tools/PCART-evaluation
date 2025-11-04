# PCART Evaluation

This repository contains the evaluation results of **PCART**, assessing its **API compatibility detection and repair capabilities** across different datasets and scenarios.

## :open_file_folder: Directory Overview

- **`RQ1_and_RQ2/`**  
  Evaluates PCART's performance on **API parameter compatibility detection and repair**.  
  - Uses the **PCBench** and **MLCatchUp** datasets.  
  - Compares PCART against **MLCatchUp** and **Relancer**.
  - Evaluates PCART's ability to extract complex API invocation patterns 

- **`RQ3/`**  
  Assesses PCART's effectiveness in **real-world Python projects**.  
  - Evaluated on **30 real projects** collected from **GitHub**.  

- **`RQ4/`**  
  Compares **ChatGPT (GPT-4o) vs. PCART** on API compatibility detection and repair.  
  - Uses **58 test cases** from **PCBench** (29 compatible, 29 incompatible).  

- **`RQ5/`**  
  Measures **PCART's runtime efficiency**.  
  - Computes the **average runtime per API processed** across test cases.  

---

## :pushpin: Notes
- Each directory contains corresponding **experiment results and analysis**.
- For detailed evaluation metrics and results, refer to the **PCART research paper**:  
  :page_facing_up: **[PCART: Automated Repair of Python API Parameter Compatibility Issues](https://arxiv.org/abs/2406.03839)**  

:tada: **Happy Researching with PCART!** :rocket:

