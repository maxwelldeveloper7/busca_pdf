@startuml
title Diagrama de Componentes - PDF Searcher Educacional

package "CLI" {
  [MenuCLI]
}

package "Core" {
  [AmbienteObservable]
  [ContextoBusca]
  [EstadoBusca]
  [EstadoComPDFs]
  [EstadoSemPDFs]
  [BuscaPDFService]
}

package "Utils" {
  [Bootstrap]
}

package "Infraestrutura" {
  [Sistema de Arquivos]
  [Biblioteca pdfplumber]
  [Biblioteca tqdm]
}

package "Aplicação" {
  [main.py]
}

' ===== Dependências =====

[main.py] --> [Bootstrap]
[main.py] --> [MenuCLI]

[MenuCLI] --> [AmbienteObservable]
[MenuCLI] --> [BuscaPDFService]

[AmbienteObservable] --> [ContextoBusca]
[ContextoBusca] --> [EstadoBusca]
[EstadoBusca] <|-- [EstadoComPDFs]
[EstadoBusca] <|-- [EstadoSemPDFs]

[BuscaPDFService] --> [Sistema de Arquivos]
[BuscaPDFService] --> [Biblioteca pdfplumber]
[BuscaPDFService] --> [Biblioteca tqdm]

[Bootstrap] --> [Sistema de Arquivos]

@enduml
