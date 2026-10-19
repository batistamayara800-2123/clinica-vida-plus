# Clínica Vida+ — Projeto acadêmico

Aplicação web responsiva em português que reúne os cinco passos da atividade: quadro Kanban inspirado no Trello, programa de cadastro em Python, lógica proposicional e tabelas-verdade, fila FIFO e diagrama de casos de uso UML.

## Arquivos

- `index.html` — conteúdo das cinco seções e interface.
- `style.css` — estilos responsivos e impressão.
- `app.js` — quadro interativo, tabelas-verdade, exportações e simulação FIFO.
- `clinica_vida.py` — programa real de terminal solicitado.
- `README.md` — estas instruções.

## Executar localmente

### Aplicação web
Abra `index.html` no navegador. Para hospedar no GitHub Pages, publique os arquivos na raiz do repositório e habilite Pages nas configurações do repositório.

### Programa Python
Instale Python 3 e execute no terminal dentro da pasta do projeto:

```bash
python clinica_vida.py
```

Em alguns sistemas, o comando é:

```bash
python3 clinica_vida.py
```

O programa usa listas e dicionários e mantém os cadastros apenas enquanto estiver aberto. Não foi incluída persistência em banco de dados.

## Publicar no GitHub

1. Entre em https://github.com/ e crie um repositório novo, por exemplo `clinica-vida-plus`.
2. Envie `index.html`, `style.css`, `app.js`, `clinica_vida.py` e `README.md` para a raiz do repositório.
3. No repositório, abra **Settings → Pages**.
4. Em **Build and deployment**, escolha **Deploy from a branch**.
5. Selecione a branch `main` e a pasta `/ (root)`; salve.
6. Aguarde a publicação e abra o endereço apresentado pelo GitHub Pages.

O quadro Kanban é local ao navegador e não cria nem sincroniza automaticamente um quadro na conta real do Trello. Para reproduzi-lo no Trello, acesse https://trello.com/, crie um quadro e as listas `Backlog`, `Sprint Atual`, `Em Progresso` e `Concluído`, e copie os cartões e checklists.

## Conteúdo e cuidados

- As tabelas-verdade percorrem as 16 combinações de A, B, C e D.
- A expressão normal é `(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)`.
- A expressão de emergência é `C ∧ (B ∨ D)`.
- O quadro inclui dados demonstrativos, datas, checklist, comentários e relatório por sprint.
- Todos os dados pessoais demonstrativos são fictícios. Não utilizar esta aplicação para gerir pacientes reais nem para decisões clínicas.
