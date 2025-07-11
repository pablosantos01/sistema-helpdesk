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

![01](https://github.com/user-attachments/assets/65d80841-599a-416e-92c8-e9c21f019512)

![02](https://github.com/user-attachments/assets/c34cc90b-ee1f-4baf-8a3c-b9263232ec2b)

![03](https://github.com/user-attachments/assets/18486b8c-99f8-4deb-ac51-231afa9707d0)

<img width="1519" height="1035" alt="telalogin" src="https://github.com/user-attachments/assets/87ea2cab-bd33-47ed-ac99-0c2dc8d262b0" />

<img width="1518" height="1040" alt="telaregistro" src="https://github.com/user-attachments/assets/de968313-0a0a-48f9-8ef3-583da08a62ba" />

<img width="1519" height="1039" alt="telainicial" src="https://github.com/user-attachments/assets/445d31d7-8393-492b-89a5-95837cfda4c9" />

<img width="1520" height="1037" alt="criarchamado" src="https://github.com/user-attachments/assets/e0a08691-7ca3-4d20-951f-ffd4674d48cf" />

<img width="1519" height="1039" alt="criarchamado2" src="https://github.com/user-attachments/assets/7a0fbda1-d5a8-482a-a217-1e8d5012efb4" />



## 🤝 Contribuindo

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

📬 Contato

🌐 LinkedIn: https://www.linkedin.com/in/pablosantos01/


