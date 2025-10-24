# 🔍 PDF Searcher Educacional

**Autor:** Maxwell de Oliveira Chaves  
**Ano:** 2025  
**Licença:** [CC BY-NC-SA 4.0 International](LICENSE.md)  
**Linguagem:** Python 3.x  

---

## 📘 Descrição do Projeto

O **PDF Searcher Educacional** é um aplicativo desenvolvido em **Python** para realizar **buscas textuais com filtros** em múltiplos arquivos PDF localizados em uma pasta específica.  

O sistema foi concebido para auxiliar em **estudos acadêmicos**, permitindo a localização rápida de termos, expressões ou conceitos dentro de materiais didáticos (como apostilas, aulas ou textos de referência).  

Este projeto surgiu da necessidade prática durante as **avaliações pedagógicas online da UNINTER**, nas quais o autor precisa consultar diversos arquivos PDF que contêm o conteúdo das aulas, mas sem indicação explícita da origem de cada questão.  

---

## 🧠 Objetivo Educacional

O aplicativo visa:

- Otimizar o processo de **busca e revisão de conteúdo educacional**;  
- Demonstrar **boas práticas de manipulação e leitura de PDFs em Python**;  
- Servir como **recurso didático** para alunos e professores que estudam automação de processos e análise de texto.  

---

## ⚙️ Requisitos

Para executar o projeto, é necessário possuir:

- **Python 3.8+**  
- Bibliotecas:

  ```bash
  pip install PyPDF2
  ```

* Sistema operacional compatível: **Windows, Linux ou macOS**

---

## 🚀 Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/maxwelldeveloper7/busca_pdf.git
   cd busca_pdf/
   ```

2. Crie as pastas esperadas pelo sistema:

   ```bash
   /pdfs          → onde ficam os arquivos PDF (não incluídos no repositório)
   /resultados    → onde serão salvos os logs e arquivos de saída
   ```

3. Execute o script principal:

   ```bash
   python buscar_pdfs.py
   ```

4. Informe o termo de busca quando solicitado:

   ```
   Digite o termo que deseja buscar: algoritmo
   ```

O sistema fará a varredura em todos os PDFs da pasta indicada e salvará os resultados em:

```
/resultados/log_busca.txt
```

---

## 🗂️ Estrutura de Pastas

```bash
📦 pdf-searcher-educacional
 ┣ 📂 pdfs/           # Arquivos PDF (não incluídos por direitos autorais)
 ┣ 📂 resultados/     # Logs e relatórios das buscas
 ┣ 📜 buscar_pdfs.py  # Código-fonte principal
 ┣ 📜 LICENSE.md      # Termos da licença (CC BY-NC-SA 4.0)
 ┣ 📜 .gitignore      # Arquivos e pastas ignorados pelo Git
 ┗ 📜 README.md       # Documentação do projeto
```

---

## 🧩 Funcionalidades

* Busca textual em múltiplos arquivos PDF;
* Filtragem de resultados por nome do arquivo e número de página;
* Log automático dos resultados em arquivo `.txt`;
* Organização automática de pastas (`pdfs/` e `resultados/`);
* Estrutura de código documentada e comentada para fins didáticos.

---

## 🧱 Boas Práticas Implementadas

* Uso de **tratamento de exceções** para PDFs corrompidos ou ilegíveis;
* Implementação de **logging estruturado** em arquivo de resultados;
* Separação lógica entre leitura, processamento e salvamento de dados;
* Comentários explicativos em **todas as linhas do código-fonte**;
* Conformidade com o padrão **PEP 8** (estilo de código Python).

---

## ⚠️ Aviso Legal e Ético

> Os arquivos PDF utilizados por este aplicativo **não estão incluídos no repositório** e **não devem ser redistribuídos**, pois são protegidos por direitos autorais de seus respectivos autores e instituições.
> Este software apenas processa **cópias locais** dos materiais de estudo, de forma **estritamente educacional e não comercial**.

---

## 📜 Licença

Este projeto é licenciado sob os termos da
**Creative Commons Atribuição–NãoComercial–CompartilhaIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

Você pode:

* **Compartilhar** — copiar e redistribuir o material em qualquer formato;
* **Adaptar** — remixar, transformar e criar a partir do material;

Desde que:

* **Dê crédito a Maxwell de Oliveira Chaves**;
* **Não utilize o material para fins comerciais**;
* **Distribua modificações sob a mesma licença**.

📄 Texto completo da licença:
[https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.pt](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.pt)

---

## 💬 Contato

* **Autor:** Maxwell de Oliveira Chaves
* **E-mail profissional:** [maxwellchaves1844@gmail.com]()
* **GitHub:** [https://github.com/maxwelldeveloper7](https://github.com/maxwelldeveloper7)
* **LinkedIn:** [https://www.linkedin.com/in/maxwell-oliveira-chaves/](https://www.linkedin.com/in/maxwell-oliveira-chaves/)
