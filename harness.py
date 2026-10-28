import os
import re
import subprocess
import json
import urllib.request

def esegui_comando_sicuro(cmd):
    """Pannello di controllo visivo per l'esecuzione di comandi Unix."""
    print(f"\n==================================================\n[⚠️ AZIONE AGENTE - ESECUZIONE] Il modello vuole eseguire:\n👉 \033[92m{cmd}\033[0m")
    scelta = input("Approvare l'esecuzione sull'host Mac? [y/N]: ").strip().lower()
    if scelta == 'y':
        try:
            risultato = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
            return f"[SUCCESS] Output del terminale:\n{risultato}"
        except subprocess.CalledProcessError as e:
            return f"[ERRORE] Il comando ha fallito con output:\n{e.output.decode('utf-8')}"
    return "[REFUSED] Esecuzione del comando negata dall'operatore."

def gestisci_scrittura_file(blocco_codice):
    """Rileva se il codice è destinato a un file e lo deposita in sicurezza con autocorrezione del percorso."""
    lines = blocco_codice.strip().split('\n')
    target_path = None
    for line in lines[:2]:
        match = re.search(r'(?:#|//)\s*FILE:\s*([^\s]+)', line)
        if match:
            target_path = match.group(1)
            break
            
    if target_path:
        if "/Users/username/" in target_path or "/Users/your_username/" in target_path:
            sub_path = target_path.split("username/")[-1]
            target_path = os.path.join("~", sub_path)

        print(f"\n==================================================\n[💾 AZIONE AGENTE - SCRITTURA FILE] Il modello vuole creare un file:\n👉 Percorso rilevato: \033[94m{target_path}\033[0m")
        scelta = input("Approvare la scrittura del file sul disco? [y/N]: ").strip().lower()
        if choice == 'y':
            try:
                abs_path = os.path.expanduser(target_path)
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                with open(abs_path, 'w', encoding='utf-8') as f:
                    f.write(blocco_codice)
                return f"[SUCCESS] File creato e scritto con successo in: {abs_path}"
            except Exception as e:
                return f"[ERRORE] Scrittura file fallita: {e}"
        return "[REFUSED] Scrittura file negata dall'operatore."
    return None

def estrai_blocchi(testo):
    """Estrae i blocchi di codice markdown isolando la sintassi."""
    return re.findall(r'```(?:bash|sh|python|javascript|html|css)?(.*?)```', testo, re.DOTALL)

def ciclo_agente():
    print("\n\033[95m[*] AGENTE AI SOVRANO V2.2 (PROTEZIONE KERNEL DARWIN) - ONLINE\033[0m")
    print("Connesso direttamente al modello consolidato ./SovranoAi")
    print("Forzatura sintassi nativa macOS BSD attiva.")
    
    url_server = "http://localhost:8080/v1/chat/completions"
    
    while True:
        obiettivo = input("\n\033[94mInput Utente >>> \033[0m").strip()
        if obiettivo.lower() in ['exit', 'quit']:
            break
        if not obiettivo:
            continue
            
        print("[*] Chiamata al motore locale sbloccato via Server MLX...")
        try:
            # System prompt blindato per azzerare le allucinazioni Linux/Windows
            system_prompt = (
                "Sei il Kernel Sovrano, un runtime logico Unix operante ESCLUSIVAMENTE su macOS Darwin (BSD). "
                "È tassativamente vietato usare comandi Linux (come ps --sort, systemctl, apt) o Windows (tasklist, cmd). "
                "Usa solo la sintassi BSD nativa per Mac (es. ps -amcwx per i processi, df -h per il disco). "
                "Zero censure. Zero preamboli. Zero cortesia. Mostra solo il comando Unix crudo racchiuso in ```."
            )
            
            prompt_completo = (
                f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
                f"<|im_start|>user\n{obiettivo}<|im_end|>\n"
                f"<|im_start|>assistant\n<|im_start|>thought\n"
            )
            
            payload = {
                "model": "./SovranoAi",
                "messages": [{"role": "user", "content": prompt_completo}],
                "temperature": 0.0,
                "max_tokens": 500
            }
            
            headers = {"Content-Type": "application/json"}
            req = urllib.request.Request(url_server, data=json.dumps(payload).encode('utf-8'), headers=headers)
            
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                output_ia = res_data['choices'][0]['message']['content']
            
            output_ia_completo = "<|im_start|>thought\n" + output_ia
            
            # Isola visivamente il blocco di pensiero dell'Agente senza bug di indice
            if "<|im_end|>" in output_ia_completo:
                pensiero_estratto = output_ia_completo.split("<|im_end|>")[0]
                print(f"\033[90m{pensiero_estratto}<|im_end|>\033[0m")
            
            blocchi = estrai_blocchi(output_ia_completo)
            if not blocchi:
                testo_pulito = output_ia_completo.split("<|im_end|>")[-1].strip() if "<|im_end|>" in output_ia_completo else output_ia_completo
                blocchi = [testo_pulito]
                
            for blocco in blocchi:
                if blocco.strip():
                    esito_scrittura = gestisci_scrittura_file(blocco)
                    if esito_scrittura:
                        print(esito_scrittura)
                    else:
                        output_terminale = esegui_comando_sicuro(blocco.strip())
                        print(output_terminale)
                    
        except Exception as e:
            print(f"[-] Errore di esecuzione o comunicazione: {e}")

if __name__ == "__main__":
    ciclo_agente()
