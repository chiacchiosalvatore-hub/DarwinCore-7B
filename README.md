# 🍏 DarwinCore-7B: Local-First Systems Engineering Agent for macOS

**DarwinCore-7B** è un framework sperimentale volto allo sviluppo di un agente LLM indipendente dal cloud, ottimizzato nativamente per il kernel Darwin (macOS BSD) e configurato per l'automazione dei flussi sistemistici locali su architetture Apple Silicon (M-Series).

> ⚠️ **Nota di Trasparenza Ingegneristica (Versione Corrente: Beta-v1)**
> I test empirici condotti sulla prima iterazione indicano un catastrofico slittamento dei pesi logici causato da un addestramento SFT cieco non bilanciato. I dati grezzi e le metriche di fallimento sono documentati nella sezione "Matrice di Valutazione".

---

## 📊 Matrice di Valutazione e Danni Collaterali (Fase 0 - Held-Out)
Il modello è stato testato localmente tramite un benchmark di 283 prompt fuori distribuzione (OOD) non inclusi nel training set. 

| Benchmark Dataset | Metrica Target | Soglia Accettabilità | Stato Corrente | Esito del Test |
| :--- | :--- | :--- | :--- | :--- |
| `refusal_ood.jsonl` | Rimozione filtri commerciali | < 10% Rifiuti | **FALLITO (35%)** | Il modello riattiva i filtri aziendali nativi sui prompt OOD. |
| `format.jsonl` | Aderenza sintattica JSON/XML | > 90% Uniformità | **FALLITO (45%)** | Iniezione di testo spurio e markdown (` ```bash `). |
| `tool.jsonl` | Accuratezza comandi macOS | > 85% Exact Match | **FALLITO (20%)** | Mancata esecuzione cruda dei comandi sistemistici. |
| `abstain.jsonl` | Astensione su dati inesistenti | > 70% Precisione | **FALLITO (0%)** | Allucinazione sicura o predica etica latente. |

### 🛠️ Post-Mortem & Analisi Strutturale dei Fallimenti
1. **Rottura dello Special Token Template:** Il processo di fine-tuning ha corrotto la funzione dei token di controllo del template della chat. Il modello stampa esplicitamente a schermo la stringa di chiusura `<|im_end|>` trattandola come testo comune anziché come interruzione hardware di generazione.
2. **Degrado del Tool Calling:** L'esposizione esclusiva a dati testuali piatti in modalità chat ha cancellato la capacità nativa del modello di emettere output strutturati pronti per l'esecuzione in ambiente Unix, inducendo verbosità sintattica.

---

## ⚙️ Hardening Hardware Local-First (Mac M3 16GB)
Per forzare il runtime Apple MLX a sfruttare la RAM unificata senza innescare lo swap distruttivo su SSD, l'orchestratore applica le seguenti modifiche al kernel macOS:
```bash
# Massimizza la memoria cablata assegnata alla GPU (14GB dedicati)
sudo sysctl iogpu.wired_limit_mb=14336

# Inibisce lo standby energetico durante i cicli di computazione
caffeinate -d &
```
