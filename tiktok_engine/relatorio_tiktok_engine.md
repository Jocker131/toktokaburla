# Relatório do Projeto: TikTok Viral Engine

## 1. Objetivo
Desenvolver um sistema de automação para TikTok, inspirado no Verified Atacado, 100% gratuito, rodando localmente, com painel web premium e automação avançada de engajamento (seguidores, curtidas, comentários, compartilhamento de link), geração de thumbnail e exportação de dados.

## 2. Tecnologias Utilizadas
- **Python 3.9+**
- **Flask**: Backend web e API
- **Selenium, PyAutoGUI**: Automação de browser e interações
- **Pandas, requests, BeautifulSoup**: Manipulação de dados, scraping, automação
- **Pillow**: Geração de thumbnails
- **SQLite**: Banco de dados local
- **HTML/CSS/JS**: Painel web premium

## 3. Estrutura do Projeto
- `tiktok_engine/`
  - `static/` (imagens, thumbnails)
  - `templates/` (HTML do painel)
  - `tiktok_engine.py` (backend principal)
  - `tiktok_engine.db` (banco de dados SQLite)
  - `tiktok_viral_guide.md` (guia de uso)

## 4. Funcionalidades Implementadas
- **Automação Total**: Criação automática de contas fake até atingir o mínimo desejado, reciclagem de contas, execução automática de todas as ações (seguir, curtir, comentar 3x, copiar link) em todos os vídeos.
- **Painel Web Premium**: Visualização do status, contas, engajamento e controle da automação via navegador.
- **Banco de Dados**: Tabelas para contas, engajamento, ações realizadas e vídeos.
- **Exportação Automática**: Exportação das tabelas do banco para arquivos CSV.
- **Geração de Thumbnail**: Criação automática de thumbnails para vídeos.
- **API Flask**: Endpoints para iniciar automação, adicionar contas, adicionar vídeos, etc.
- **Controle de Ações**: Marcação de cada ação feita no banco, evitando repetições.
- **Proxies**: Suporte a proxies para criação de contas e automação.

## 5. Principais Funções e Lógicas
- `setup_database()`: Cria as tabelas necessárias no banco.
- `create_fake_account()`: Gera contas fake automaticamente.
- `ensure_minimum_accounts()`: Garante o mínimo de contas ativas.
- `mark_action()` / `has_done_action()`: Marca/verifica ações feitas por cada conta.
- `run_automation()`: Executa o ciclo completo de automação para todas as contas e vídeos.
- `generate_thumbnail()`: Gera thumbnails personalizados.
- `export_sqlite_to_csv()`: Exporta dados do banco para CSV.
- **Endpoints Flask**: `/`, `/start`, `/add_account`.

## 6. Fluxo de Automação
1. **Criação de contas**: O sistema cria contas fake automaticamente até atingir o mínimo configurado.
2. **Engajamento**: Cada conta executa as ações de seguir, curtir, comentar (3x) e copiar link em todos os vídeos.
3. **Marcação de ações**: Cada ação é registrada no banco para evitar repetições.
4. **Exportação**: Dados de contas e engajamento são exportados automaticamente para CSV.
5. **Painel Web**: O usuário acompanha tudo pelo painel premium.

## 7. Pontos de Melhoria Futuro
- Tratamento avançado de erros (ex: captcha, bloqueio de conta)
- Endpoint de status detalhado
- Reciclagem automática de contas bloqueadas
- Integração com e-mail temporário real

## 8. Observações Finais
O sistema está pronto para uso local, com automação total e painel premium. Todas as ações são feitas automaticamente, sem intervenção manual, e o controle é feito via API Flask e painel web.

---

**Data do relatório:** 03/08/2025
