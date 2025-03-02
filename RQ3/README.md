# RQ3 Directory

This directory contains PCART test projects, along with their configuration files, repair reports, and associated environment archives.

## :open_file_folder: Directory Structure
Each subdirectory in `RQ3/` corresponds to a **PCART test project** and contains:
- **`*.json`** → Configuration files required for running PCART.
- **`*.txt`** → Repair reports generated after executing PCART.

### **Example Directory Layout**
```bash
RQ3/
├── AIBO/
│   ├── AIBO.json      # PCART configuration file
│   └── AIBO.txt       # PCART repair report
├── allnews/
│   ├── allnews.json   # PCART configuration file
│   └── allnews.txt    # PCART repair report
```

## :package: Associated Environment Archives
A cloud storage link is provided for downloading the source code and virtual environments of the tested projects.
These archives are available at: [link1](https://drive.google.com/drive/folders/1E_8yLmzMew19R8Vs3OjetNDZvtyPMl0x) or [link2](https://pan.nuaa.edu.cn/share/91e95ef8fac3e71dd01f188b2f) (faster in China)

### :open_file_folder: Cloud Storage Structure
The cloud storage contains:
- **`*.zip`** → The source code of the tested projects.
- **`*.tar.gz`** → Virtual environments compressed using`conda pack` for both current and upgraded versions.

### **Example Directory Layout**
```bash
./
├── AIBO
│   ├── AIBO1.10.0.tar.gz   # Conda environment (upgraded version)
│   ├── AIBO1.7.3.tar.gz    # Conda environment (current version)
│   └── AIBO.zip            # Project source code
├── allnews
│   ├── allnews3.8.3.tar.gz # Conda environment (upgraded version)
│   ├── allnews4.0.0.tar.gz # Conda environment (current version)
│   └── allnews.zip         # Project source code
```

### :hammer_and_wrench: **Extracting and Using Conda Environments**
To extract and use a downloaded Conda environment, run:
```bash
cd /home/usr/anaconda3/envs
mkdir envName
tar -xzvf envName.tar.gz -C envName
```
