#!/usr/bin/env python3
from datetime import datetime
import random
import subprocess
import sys

def copiar_para_area_transferencia(texto):
    """Copia texto para área de transferência"""
    try:
        # Para Termux (Android)
        process = subprocess.Popen(['termux-clipboard-set'], stdin=subprocess.PIPE)
        process.communicate(input=texto.encode())
        return True
    except:
        try:
            # Fallback para outros sistemas
            import pyperclip
            pyperclip.copy(texto)
            return True
        except:
            return False

def gerar_demarcacao():
    print("🛍️ FuriaDaNoitePlay - Gerador de Demarcações")
    print("📋 BOTÃO COPIAR AUTOMÁTICO:")
    
    # Diferentes modelos de mensagem
    modelos = [
        f"""🚨 @everyone | #FuriaBoutique 🚨
🛍️ BOUTIQUE OFICIAL | FuriaDaNoitePlay
📞 31997319008
🏷️ Demarcação automática da comunidade
⏰ {datetime.now().strftime("%H:%M - %d/%m")}""",

        f"""🔔 @all | #FuriaMarca 🔔
🛒 BOUTIQUE FURIA DA NOITE PLAY
📱 31997319008
🎯 Demarcação oficial do grupo
🕒 {datetime.now().strftime("%H:%M - %d/%m")}""",

        f"""📢 MARCAÇÃO GERAL | #PlayNoControle 📢
💎 FuriaDaNoitePlay - Boutique
☎️ 31997319008
⚡ Demarcação ativa na comunidade
⏰ {datetime.now().strftime("%H:%M - %d/%m")}"""
    ]
    
    # Escolher modelo aleatório
    demarcacao = random.choice(modelos)
    
    print("═" * 50)
    print(demarcacao)
    print("═" * 50)
    
    # Copiar automaticamente
    if copiar_para_area_transferencia(demarcacao):
        print("\n✅ ✅ ✅ MENSAGEM COPIADA AUTOMATICAMENTE! ✅ ✅ ✅")
        print("📱 **PRONTO PARA COLAR NO WHATSAPP!**")
    else:
        print("\n📋 **COPIE A MENSAGEM ACIMA MANUALMENTE:**")
    
    print("\n🎯 **INSTRUÇÕES RÁPIDAS:**")
    print("1. Mensagem já está na ÁREA DE TRANSFERÊNCIA")
    print("2. Abra o grupo no WhatsApp Web")
    print("3. COLE (Ctrl+V) e envie!")
    print("4. Execute novamente para nova mensagem!")
    
    return demarcacao

if __name__ == "__main__":
    gerar_demarcacao()
