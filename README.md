# Sistema Help Desk

Sistema web simples para registro, acompanhamento e atualização de chamados internos. Desenvolvido como MVP com foco em melhoria de processos internos e acompanhamento de solicitações de suporte técnico.

---

## Visão do Produto

O Sistema Help Desk foi idealizado para resolver um problema comum em empresas de qualquer porte: a desorganização no fluxo de chamados internos.  
Com uma interface simples e direta, o sistema permite abrir, visualizar e atualizar chamados, facilitando a comunicação entre equipes e aumentando a eficiência no atendimento.

---

## Meu Papel como Product Manager

Atuei como Product Manager e desenvolvedor neste projeto:

- Levantamento de requisitos com base em dores reais do dia a dia de suporte  
- Definição de escopo e priorização de funcionalidades (MVP)  
- Planejamento de roadmap e backlog  
- Organização de documentação para time técnico e stakeholders  
- Prototipação funcional com entrega contínua  

---

## Funcionalidades do MVP

✅ Criar chamados com:  
- Título  
- Descrição  
- Setor  
- Responsável  
- Status (Aberto, Em andamento, Resolvido)  
- Upload de arquivos (PDF, DOCX, Imagens etc.)

✅ Visualizar lista de chamados com filtros por status, setor e responsável  
✅ Atualizar status do chamado  
✅ Visualizar detalhes do chamado com histórico de comentários internos  
✅ Adicionar comentários com registro de autor e data  
✅ Login e autenticação de usuários (com níveis básicos)  
✅ Interface responsiva (desktop e mobile)  
✅ Armazenamento com SQLite + SQLAlchemy  

---

## Funcionalidades Futuras (Backlog)

- [ ] Dashboard com KPIs e gráficos  
- [ ] Integração com Slack / E-mail / WhatsApp  
- [ ] Exportação de relatórios em PDF ou Excel  
- [ ] Controle mais granular de permissões de usuários  
- [ ] Melhorias na interface e usabilidade  

---

## Métricas e KPIs (previstos)

- Volume de chamados por período  
- Tempo médio de resolução  
- Chamados por status e setor  
- Chamados por responsável  
- Cumprimento de SLA  

---

## Tecnologias Utilizadas

| Camada            | Ferramenta             |
|-------------------|------------------------|
| Backend           | Python + Flask         |
| Banco de Dados    | SQLite + SQLAlchemy    |
| Frontend          | HTML + Bootstrap 5     |
| Templates         | Jinja2                 |
| Estilização extra | CSS customizado        |
| Controle de Versão| Git + GitHub           |

---

## 📁 Estrutura do Projeto

Sistema Help Desk/
├── app.py                 # Arquivo principal do Flask
├── models.py              # Modelagem do banco de dados
├── requirements.txt       # Dependências do projeto
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── create_ticket.html
│   ├── ticket_detail.html
│   ├── update_ticket.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/
│   └── style.css          # Estilos customizados
├── uploads/               # Arquivos anexados pelos usuários
├── database/
│   └── helpdesk.db        # Banco de dados SQLite


## 🗺️ Roadmap

| Versão | Funcionalidade                                           | Status       |
| ------ | -------------------------------------------------------- | ------------ |
| 1.0    | Criar, listar e atualizar chamados, upload e comentários | ✅ Concluído  |
| 1.1    | Autenticação de usuários                                 | ✅ Concluído  |
| 1.2    | Dashboard e KPIs                                         | 🔜 Planejado |
| 1.3    | Integrações externas                                     | 🔜 Futuro    |


## 📸 Screenshots

1. Tela de Login do Sistema
<img width="1522" height="1038" alt="Tela de Login do Sistema" src="https://github.com/user-attachments/assets/13049f8a-ee92-4469-82fd-18bf540439d1" />


2. Tela de Registro de Novo Usuário
<img width="1522" height="1037" alt="Tela de Registro de Novo Usuário" src="https://github.com/user-attachments/assets/feee2381-87c6-4dbc-a7a6-60d1b9a7d077" />


3. Tela Inicial (Home)
<img width="1521" height="1039" alt="Tela Inicial (Home)" src="https://github.com/user-attachments/assets/e12bed75-bb29-4af0-827e-cf2dfbb57986" />


4. Formulário para Abertura de Chamado
<img width="1522" height="1039" alt="Formulário para Abertura de Chamado" src="https://github.com/user-attachments/assets/1c3d29e0-8bbc-4ec3-92a3-1489db8bea51" />


5. Confirmação de Chamado Criado com Sucesso
<img width="1522" height="1037" alt="Confirmação de Chamado Criado" src="https://github.com/user-attachments/assets/859beecf-b5b2-4768-9d40-0fe807491ff4" />


6. Visualização Detalhada do Chamado
<img width="1522" height="1040" alt="Visualização Detalhada do Chamado" src="https://github.com/user-attachments/assets/5841c09e-4c00-43ea-b5ad-e41af1033038" />


7. Alteração de Status do Chamado
<img width="1518" height="1033" alt="Alteração de Status do Chamado" src="https://github.com/user-attachments/assets/a67fa9fc-9d5d-419c-88ea-f9f0dc239c2d" />


8. Painel de Dashboard com Visão Geral dos Chamados
<img width="1522" height="1037" alt="Dashboard com Visão Geral dos Chamados" src="https://github.com/user-attachments/assets/097b1e8d-c18c-4aca-955f-3666eb9afc5f" />


## 🤝 Contribuindo

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

📬 Contato

🌐 LinkedIn: https://www.linkedin.com/in/pablosantos01/


