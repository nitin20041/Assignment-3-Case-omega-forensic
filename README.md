# CASE OMEGA – Simple Digital Forensics Project

## 1. Project overview
Case Omega is an academic simulation of a ransomware incident in a fictional healthcare network. The project demonstrates first response, evidence records, SHA-256 hashing, safe ransomware-like file transformation, log analysis, timeline creation and forensic reporting. All hospital details, users, logs and records are synthetic.

## 2. Folder guide
| Folder | What it contains |
|---|---|
| `01_Case` | One short case brief with the incident summary, objectives and scope. |
| `02_First_Responder` | First responder SOP, scene notes, evidence tags and scene/network diagrams. |
| `03_Evidence` | Evidence inventory, Chain of Custody, hash manifest/results and a synthetic evidence ZIP. |
| `04_Malware` | Harmless ransomware behaviour simulator, sample files, IOC list and simulation activity log. |
| `05_Logs` | Synthetic Windows, email, USB, firewall, file and helpdesk logs; generated timeline and graph. |
| `06_Report` | Final report in PDF and editable DOCX formats. |
| `07_Visuals` | Generated visual demonstrations (not screenshots from FTK Imager or Autopsy). |
| `08_Tool_Docs` | Reserved for optional tool notes; not required for the simplified version. |
| `scripts` | Python scripts for SHA-256 hashing and timeline generation. |
| `.github/workflows` | GitHub Actions validation workflow. |

## 3. Requirements
- Windows 10/11
- Python 3.10 or newer
- Internet is needed only to install Python packages

Install dependencies from PowerShell in this project folder:

```powershell
py -m pip install -r requirements.txt
```

## 4. Run the project

### Generate SHA-256 hashes
```powershell
py scripts\hash_evidence.py
```
The script updates `03_Evidence/hash_manifest.csv`.

### Run the safe ransomware demonstration
```powershell
py 04_Malware\ransomware_simulator.py
```
It transforms only the synthetic text files inside `04_Malware/test_data` using reversible Base64 encoding. It does not spread, persist, access the network or touch files outside that folder.

Restore the sample files:
```powershell
py 04_Malware\ransomware_simulator.py --restore
```
**Note:** Base64 is encoding, not encryption. This is not real ransomware.

### Build the event timeline
```powershell
py scripts\build_timeline.py
```
Outputs are saved in `05_Logs/results/attack_timeline.csv` and `05_Logs/results/attack_timeline.png`.

## 5. Important forensic limitations
- The evidence ZIP is a collection of synthetic files, not a raw disk image.
- FTK Imager and Autopsy have not been used to acquire or examine a real forensic image in this package.
- The screenshots/visuals are generated illustrations, not genuine screenshots of forensic software.
- The logs are simulated and cannot prove a real-world attack or identify a real attacker.
- A matching SHA-256 hash supports byte-integrity checking; it does not by itself prove authenticity, source or legal admissibility.

## 6. Suggested investigation order
1. Read `01_Case` records.
2. Review `02_First_Responder/FIRST_RESPONDER_SOP.md` and scene diagrams.
3. Review evidence inventory and Chain of Custody in `03_Evidence`.
4. Run the hash script.
5. Run and restore the safe simulator.
6. Review synthetic logs and build the timeline.
7. Read the final PDF/DOCX report and update student details in the authorship declaration.

## 7. Academic use
This is a learning simulation. Clearly identify synthetic evidence and generated visuals in any submission. Do not describe the ZIP as a forensic disk image or claim FTK/Autopsy acquisition was completed unless you perform those steps and add your own genuine screenshots.
