# 🛠️ Sistema Help Desk

Sistema web simples para registro, acompanhamento e atualização de chamados internos. Desenvolvido como MVP com foco em melhoria de processos internos e acompanhamento de solicitações de suporte técnico.

---

## 🎯 Visão do Produto

O **Sistema Help Desk** foi idealizado para resolver um problema comum em empresas de qualquer porte: a desorganização no fluxo de chamados internos.  
Com uma interface simples e direta, o sistema permite abrir, visualizar e atualizar chamados, facilitando a comunicação entre equipes e aumentando a eficiência no atendimento.

---

## 👨‍💻 Meu Papel como Product Manager

Atuei como **Product Manager e desenvolvedor** neste projeto:

- Levantamento de requisitos com base em dores reais do dia a dia de suporte
- Definição de escopo e priorização de funcionalidades (MVP)
- Planejamento de roadmap e backlog
- Organização de documentação para time técnico e stakeholders
- Prototipação funcional com entrega contínua

---

## 🧩 Funcionalidades do MVP

✅ Criar chamados com:
- Título  
- Descrição  
- Setor  
- Responsável  
- Status (Aberto, Em andamento, Resolvido)

✅ Visualizar lista de chamados  
✅ Atualizar o status dos chamados  
✅ Interface responsiva (desktop e mobile)  
✅ Armazenamento com SQLite + SQLAlchemy  

---

## 🔮 Funcionalidades Futuras (Backlog)

- [ ] Login e autenticação de usuários (admin, operador, solicitante)  
- [ ] Filtros por status, data, setor e responsável  
- [ ] Comentários internos nos chamados  
- [ ] Dashboard com KPIs e gráficos  
- [ ] Integração com Slack / E-mail / WhatsApp  
- [ ] Exportação de relatórios em PDF ou Excel  
- [ ] Upload de arquivos e anexos

---

## 📊 Métricas e KPIs (previstos)

- 📌 Volume de chamados por período  
- ⏱️ Tempo médio de resolução  
- 📁 Chamados por status e setor  
- 👤 Chamados por responsável  
- 📈 Cumprimento de SLA

---

## 💻 Tecnologias Utilizadas

| Camada       | Ferramenta            |
|--------------|-----------------------|
| Backend      | Python + Flask        |
| Banco de Dados | SQLite + SQLAlchemy |
| Frontend     | HTML + Bootstrap 5    |
| Templates    | Jinja2                |
| Controle de Versão | Git + GitHub    |

---

## 📁 Estrutura do Projeto

```plaintext
Sistema Help Desk/
├── app.py                 # Arquivo principal do Flask
├── models.py              # Modelagem do banco de dados
├── requirements.txt       # Dependências do projeto
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── create_ticket.html
│   └── update_ticket.html
├── static/
│   └── style.css          # Estilos customizados
├── database/
│   └── helpdesk.db        # Banco de dados SQLite
```


## 🗺️ Roadmap

| Versão | Funcionalidade                     | Status       |
| ------ | ---------------------------------- | ------------ |
| 1.0    | Criar, listar e atualizar chamados | ✅ Concluído  |
| 1.1    | Autenticação de usuários           | 🔜 Planejado |
| 1.2    | Comentários e histórico            | 🔜 Planejado |
| 1.3    | Dashboard e KPIs                   | 🔜 Planejado |
| 2.0    | Integrações externas               | 🔜 Futuro    |

## 📸 Screenshots

01.
![01](https://github.com/user-attachments/assets/65d80841-599a-416e-92c8-e9c21f019512)

02.
![02](https://github.com/user-attachments/assets/c34cc90b-ee1f-4baf-8a3c-b9263232ec2b)

03.
![03](https://github.com/user-attachments/assets/18486b8c-99f8-4deb-ac51-231afa9707d0)

## 🤝 Contribuindo

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

📬 Contato

🌐 LinkedIn: https://www.linkedin.com/in/pablosantos01/


