#!/usr/bin/env python3
import requests
import json
import time
from datetime import datetime
import random

class FuriaDemarcacaoBot:
    def __init__(self):
        self.boutique_config = self.load_config()
        self.comunidade_avisos = []
        
    def load_config(self):
        try:
            with open('config/boutique.json', 'r') as f:
                return json.load(f)
        except:
            return {
                "nome": "FuriaDaNoitePlay",
                "numero": "31997319008",
                "hashtags": ["#FuriaBoutique", "#FuriaMarca", "#PlayNoControle"],
                "demarcacoes": {
                    "avisos": "🛍️ BOUTIQUE OFICIAL | FuriaDaNoitePlay",
                    "contato": "📞 31997319008", 
                    "comunidade": "🏷️ Demarcações exclusivas da comunidade"
                }
            }
    
    def gerar_demarcacao(self):
        """Gera mensagem de demarcação para marcar todo mundo"""
        hashtag = random.choice(self.boutique_config["hashtags"])
        
        demarcacoes = [
            f"🚨 @everyone | {hashtag} 🚨\n"
            f"{self.boutique_config['demarcacoes']['avisos']}\n"
            f"🔥 {self.boutique_config['demarcacoes']['comunidade']}\n"
            f"💎 {self.boutique_config['demarcacoes']['contato']}\n"
            f"⏰ {datetime.now().strftime('%H:%M - %d/%m')}",
            
            f"🔔 @all | {hashtag} 🔔\n"
            f"🛍️ BOUTIQUE FURIA DA NOITE PLAY\n"
            f"📱 {self.boutique_config['numero']}\n" 
            f"🏷️ Demarcação oficial da comunidade\n"
            f"🎯 Todos marcados para não perder!",
            
            f"📢 @everyone | DEMARCAÇÃO ATIVA 📢\n"
            f"{hashtag} | {self.boutique_config['nome']}\n"
            f"📞 Contato: {self.boutique_config['numero']}\n"
            f"👑 Boutique oficial do grupo\n"
            f"🕒 {datetime.now().strftime('%H:%M')}"
        ]
        
        return random.choice(demarcacoes)
    
    def gerar_aviso_comunidade(self):
        """Gera avisos para a comunidade"""
        avisos = [
            f"🏷️ AVISO DA COMUNIDADE 🏷️\n"
            f"Boutique oficial: {self.boutique_config['nome']}\n"
            f"Contato: {self.boutique_config['numero']}\n"
            f"Demarcações ativas a cada 15min!",
            
            f"🔔 CONFIGURAÇÃO DA COMUNIDADE 🔔\n"
            f"🛍️ {self.boutique_config['nome']}\n" 
            f"📱 {self.boutique_config['numero']}\n"
            f"🏷️ Sistema de demarcações: ATIVO\n"
            f"⏰ Frequência: 15 minutos",
            
            f"🎯 INFORMAÇÕES OFICIAIS 🎯\n"
            f"Boutique: {self.boutique_config['nome']}\n"
            f"WhatsApp: {self.boutique_config['numero']}\n"
            f"Status: Demarcações automáticas ON"
        ]
        
        return random.choice(avisos)
    
    def salvar_log(self, mensagem, tipo):
        """Salva log das ações"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "tipo": tipo,
            "mensagem": mensagem
        }
        self.comunidade_avisos.append(log_entry)
        print(f"📝 LOG [{tipo}]: {mensagem}")
    
    def executar_demarcacao_completa(self):
        """Executa todo o sistema de demarcações"""
        print("🤖 INICIANDO SISTEMA DE DEMARCAÇÕES FURIA...")
        
        # 1. Gerar demarcação para marcar todo mundo
        demarcacao = self.gerar_demarcacao()
        self.salvar_log(demarcacao, "DEMARCAÇÃO_TODOS")
        
        # 2. Gerar aviso da comunidade
        aviso = self.gerar_aviso_comunidade() 
        self.salvar_log(aviso, "AVISO_COMUNIDADE")
        
        # 3. Mostrar resumo
        print(f"🎯 DEMARCAÇÃO GERADA:\n{demarcacao}")
        print(f"📢 AVISO DA COMUNIDADE:\n{aviso}")
        print(f"🏷️ HASHTAGS: {', '.join(self.boutique_config['hashtags'])}")
        print(f"📞 CONTATO: {self.boutique_config['numero']}")
        
        return {
            "demarcacao": demarcacao,
            "aviso": aviso,
            "hashtags": self.boutique_config["hashtags"],
            "timestamp": datetime.now().isoformat()
        }

def main():
    print("🛍️ FuriaDaNoitePlay - Sistema de Demarcações")
    print("📱 Boutique: 31997319008")
    print("⏰ Iniciando em:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    bot = FuriaDemarcacaoBot()
    resultado = bot.executar_demarcacao_completa()
    
    print("✅ SISTEMA DE DEMARCAÇÕES EXECUTADO COM SUCESSO!")
    print("📊 Estatísticas:")
    print(f"   - Demarcações geradas: 1")
    print(f"   - Avisos da comunidade: 1") 
    print(f"   - Hashtags disponíveis: {len(resultado['hashtags'])}")
    print(f"   - Horário: {resultado['timestamp']}")

if __name__ == "__main__":
    main()
