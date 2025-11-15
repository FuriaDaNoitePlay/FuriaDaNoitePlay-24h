#!/usr/bin/env python3
import pywhatkit
import time
from datetime import datetime

def conectar_whatsapp():
    print("🛍️ FuriaDaNoitePlay - WhatsApp Connection")
    print("📱 Iniciando conexão...")
    
    # Mensagem de demarcação
    mensagem = """🚨 @everyone | #FuriaBoutique 🚨
🛍️ BOUTIQUE OFICIAL | FuriaDaNoitePlay
📞 31997319008
🏷️ Demarcação automática da comunidade
⏰ """ + datetime.now().strftime("%H:%M - %d/%m")
    
    try:
        print("1. 🔍 Verificando configurações...")
        
        # ⚠️ **VOCÊ PRECISA CONFIGURAR ESTE ID!**
        grupo_id = "ID_DO_SEU_GRUPO"  # EXEMPLO: "558399999999-1599999999@g.us"
        
        if grupo_id == "ID_DO_SEU_GRUPO":
            print("❌ CONFIGURAÇÃO PENDENTE:")
            print("   📋 Você precisa configurar o ID do grupo!")
            print("\n💡 **COMO CONSEGUIR O ID:**")
            print("   1. Abra o grupo no WhatsApp Web")
            print("   2. Na URL, procure por 'code='")
            print("   3. O formato é: NUMERO-TIMESTAMP@g.us")
            print("   4. Exemplo: 558399999999-1599999999@g.us")
            return False
        
        print(f"2. ✅ Grupo configurado: {grupo_id}")
        print(f"3. 💬 Mensagem: {mensagem}")
        print("4. ⚠️ **IMPORTANTE:**")
        print("   - WhatsApp Web deve estar ABERTO no navegador")
        print("   - Já escaneou o QR Code com seu celular?")
        print("   - O grupo deve estar visível no WhatsApp Web")
        
        input("5. 🎯 Pressione ENTER para enviar...")
        
        print("6. 📤 Enviando mensagem...")
        
        # Enviar mensagem
        pywhatkit.sendwhatmsg_to_group_instantly(
            grupo_id, 
            mensagem,
            tab_close=True,
            wait_time=15
        )
        
        print("✅ DEMARCAÇÃO ENVIADA COM SUCESSO!")
        print("🎉 Sua boutique está agora no grupo!")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n🔧 **SOLUÇÕES:**")
        print("   1. Abra web.whatsapp.com no navegador")
        print("   2. Escaneie o QR Code com seu celular")
        print("   3. Entre no grupo desejado")
        print("   4. Verifique o ID do grupo")
        return False

if __name__ == "__main__":
    conectar_whatsapp()
