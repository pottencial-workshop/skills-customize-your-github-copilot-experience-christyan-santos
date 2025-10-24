# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Mensagens de Commit

Todas as mensagens de commit devem seguir o padrão [Conventional Commits](https://www.conventionalcommits.org/pt/v1.0.0/). Isso facilita o entendimento das mudanças e a automação de processos.

**Exemplos de Conventional Commits:**
- `feat: adiciona seção de próximos exercícios na página principal`
- `fix: corrige erro de carregamento dinâmico das tarefas`
- `docs: atualiza instruções para agentes de IA`
- `refactor: reorganiza estrutura dos arquivos de tarefas`
- `chore: atualiza dependências do projeto`