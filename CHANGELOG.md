# Changelog

## [1.1] - 2025-02-15

### Adicionado

* Modularização da aplicação em camadas **core**, **cli** e **utils**.
* Inicialização automática do ambiente via módulo `utils.bootstrap`.
* Criação automática das pastas `pdfs/` e `resultados/` quando inexistentes.
* Implementação do padrão **State** para representar a disponibilidade do sistema (com ou sem PDFs).
* Implementação do padrão **Observer** para notificação de mudanças no estado do ambiente.
* Revalidação síncrona do sistema de arquivos antes de operações críticas (busca em PDFs).
* Possibilidade de o usuário tentar novamente após adicionar PDFs, sem reiniciar o aplicativo.

### Alterado

* Separação clara entre regras de domínio, interface CLI e utilitários.
* Menu CLI passou a reagir dinamicamente à presença ou ausência de arquivos PDF.
* Remoção da dependência de estado estático para decisões críticas.

### Melhorado

* Robustez arquitetural do fluxo de execução.
* Clareza pedagógica do código, com responsabilidades bem definidas.
* Experiência do usuário ao lidar com mudanças no ambiente em tempo de execução.

---

## [1.0] - 2025-02-12

### Adicionado

* Busca textual em múltiplos PDFs.
* Barra de progresso (tqdm) com contagem total de páginas.
* Destaque visual do termo encontrado via códigos ANSI.
* Registro automático de logs de pesquisa.
* Menu interativo CLI.
* Tratamento de erros ao abrir PDFs corrompidos.
