#!/usr/bin/env python3
import pywhatkit
import time
from datetime import datetime

def enviar_demarcacao():
    print("📱 Conectando ao WhatsApp...")
    
    # Sua mensagem de demarcação
    mensagem = """
🚨 @everyone | #FuriaBoutique 🚨
🛍️ BOUTIQUE OFICIAL | FuriaDaNoitePlay
📞 31997319008
🏷️ Demarcação automática da comunidade
⏰ """ + datetime.now().strftime("%H:%M - %d/%m")
    
    try:
        # ENVIAR PARA GRUPO - substitua pelo ID real do seu grupo
        grupo_id = "ID_DO_SEU_GRUPO"  # Você precisa pegar o ID do grupo
        
        pywhatkit.sendwhatmsg_to_group_instantly(
            grupo_id, 
            mensagem,
            tab_close=True
        )
        
        print("✅ Demarcação enviada com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("💡 Dica: Precisa do ID do grupo WhatsApp")
        return False

if __name__ == "__main__":
    enviar_demarcacao()
