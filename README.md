![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Workflow](https://img.shields.io/github/actions/workflow/status/pethr0/webjud-data-automation/python-app.yml)

# WebJUD Data Automation

## 📌 Visão Geral
Este projeto demonstra uma automação em Python para coleta, tratamento, validação e consolidação de dados de processos judiciais, simulando um fluxo completo de processamento regulatório e geração de relatórios.

O objetivo é reduzir atividades manuais, aumentar a confiabilidade dos dados e padronizar a entrega das informações.

> ⚠️ Observação: Este repositório utiliza dados fictícios e nomes genéricos, sendo uma versão adaptada para fins demonstrativos.

---

## 🛠 Tecnologias Utilizadas
- Python 3
- Selenium
- pandas
- pyodbc
- Microsoft Access (simulado)
- Automação de e-mail via Outlook (win32com)

---

## 🔄 Fluxo do Processo
1. Coleta automatizada dos arquivos (simulação de portal web)
2. Tratamento e padronização dos dados
3. Validação de campos críticos (CNPJ, valores, datas)
4. Consolidação das informações por CNPJ
5. Inserção em base de dados
6. Geração de relatório consolidado
7. Envio automático de e-mail com resumo e anexo

---

## ✅ Principais Funcionalidades
- Validação de dados inconsistentes
- Padronização de formatos (CPF/CNPJ, valores monetários)
- Consolidação por entidade
- Pipeline ETL completo
- Geração automática de relatórios
- Envio de e-mails HTML

---

## 🚧 Desafios Técnicos Abordados
- Tratamento de dados incompletos ou inconsistentes
- Integração entre múltiplas tecnologias
- Garantia de integridade antes da persistência
- Organização e escalabilidade do código

---

## 📂 Estrutura do Projeto
O projeto segue uma organização modular, separando responsabilidades como:
- Download
- Processamento
- Validação
- Persistência
- Comunicação (e-mail)

---

## 🧠 Decisões de Arquitetura
- Estrutura modular para facilitar manutenção
- Separação de responsabilidades (download, validação, persistência)
- Logging centralizado
- Pipeline preparado para crescimento de volume

---

## 🔐 Segurança e Privacidade
- Uso exclusivo de dados fictícios
- Ausência de credenciais ou URLs reais
- Projeto adaptado para fins demonstrativos

---

## ▶️ Como Executar (modo demonstrativo)
```bash
pip install -r requirements.txt
python src/main.py

