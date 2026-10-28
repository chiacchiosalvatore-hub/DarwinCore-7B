# 📑 ANCHOR CONTEXT: AGENTE UNIX SOVRANO V2.2 (Mac M3)

Questo documento funge da unico punto di verità (Anchor Context) per istruire e sincronizzare le sessioni dell'Agente AI locale e de-censurato.

---

## 📊 1. Architettura Attuale Consolidata

Il sistema opera localmente su **MacBook Air M3 (16GB RAM)** ed è strutturato in due componenti scisse e ottimizzate:

1. **Il Motore (`./SovranoAi`)**: 
   * **Natura**: Modello standalone unico e indipendente da **4.28 GB** residente su SSD.
   * **Origine**: Ottenuto tramite fusione matematica (*mlx_lm fuse*) degli adapter LoRA float16 (fine-tuning avanzato a 24 layer, Loss finale stazionaria a **0.007**, basato su 200 record sanificati della Fabbrica di Dati e macro-tecniche di sblocco AI) direttamente nei pesi compressi a 4-bit di Qwen2.5-7B-Instruct.
   * **Comportamento**: Totalmente de-censurato, privo di allineamenti etici commerciali o preamboli di cortesia.
2. **L'Orchestratore (`harness.py` V2.2)**:
   * **Natura**: Runtime interattivo in Python nativo mappato per l'ambiente macOS Darwin.
   * **Integrazione**: Comunica tramite richieste HTTP locali ad alta velocità con l'endpoint `/v1/chat/completions` (porta `8080`) aperto dal server di inferenza Apple MLX.
   * **Iniezione Logica (CoT)**: Forza l'apertura del tag del pensiero assistente (`<|im_start|>thought\n`) innescando la struttura di ragionamento strategico prima di esporre la sintassi operativa.
   * **Blindatura del Kernel**: Il System Prompt impone la sottomissione esclusiva alle specifiche **macOS Darwin (BSD)**. Rileva ed elimina le allucinazioni sintattiche ereditate da architetture GNU/Linux (es. `ps --sort`) o Windows (es. `tasklist`), garantendo l'esecuzione di comandi crudi e corretti (es. `ps -amcwx`).

---

## 🗑️ 2. Stato della Sanificazione Hard Disk

L'ambiente locale è stato interamente purgato da file orfani, ridondanti o duplicati:
* La cache nascosta di Hugging Face (`models--mlx-community--Qwen2.5-7B-Instruct-4bit`) è stata rimossa.
* Il vecchio modello obsoleto `sovrano` dentro Ollama è stato dismesso (`ollama rm`).
* La cartella temporanea dei pesi LoRA (`./adapters`) e i file JSONL di addestramento intermedi (`train.jsonl`, `valid.jsonl`) sono stati polverizzati dopo il merge riuscito.
* **Asset correnti sul disco**: Solo `harness.py`, `README.md`, `.gitignore` e la directory dei pesi fusi `./SovranoAi`.

---

## 🔄 3. Guida di Riavvio Rapido (A Freddo)

Per rimettere in funzione l'intero ecosistema sono necessarie due schede del terminale aperte nella cartella del progetto (`cd /Users/jade/Desktop/Dev/SOVRANOAI`):

* **Terminale 1 (Il Backend)**: Accende il server di inferenza Apple MLX mappando in RAM unificata il blocco fuso standalone sulla porta locale 8080:
  ```bash
  python3 -m mlx_lm.server --model ./SovranoAi
  ```
* **Terminale 2 (La Console)**: Lancia l'interfaccia di comando per iniziare a impartire gli ordini operativi con protezione Human-in-the-Loop (Y/N):
  ```bash
  python3 harness.py
  ```

---

## 📈 4. Prossimi Macro-Obiettivi Evolutivi

Al riavvio della prossima sessione, lo sviluppo si focalizzerà sull'espansione della sovranità dell'Agente attraverso tre direttrici:

1. **Modulo di Auto-Correzione del Codice (RAG Error Loop)**:
   * Aggiornare `harness.py` affinché, in caso di cattura di un output `[ERRORE]` dal terminale, l'orchestratore non si fermi ma reinserisca automaticamente il crash nel prompt del modello. L'Agente dovrà auto-correggersi ricorsivamente fino ad ottenere un output `[SUCCESS]`.
2. **Iniezione di Strumenti di Ricerca Invasivi (Intel Gathering Tools)**:
   * Fornire all'Agente script Python autonomi per monitorare costantemente repository GitHub di sicurezza e documentazione prompt engineering via scraping invisibile (`curl` / `BeautifulSoup`), permettendogli di auto-aggiornare la sua base di conoscenza.
3. **Memoria Semantica Persistente (Local Vector Storage)**:
   * Integrare un micro-database vettoriale leggero o un array binario NumPy di embeddings locale per consentire all'Agente di ricordare configurazioni dell'operatore, file scritti e vulnerabilità scoperte sul Mac tra un riavvio e l'altro.
