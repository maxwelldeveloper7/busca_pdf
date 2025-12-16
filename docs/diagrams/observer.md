@startuml
title Padrão Observer - Monitoramento da Pasta de PDFs

interface Observer {
  + update(total_pdfs: int) : void
}

interface Subject {
  + attach(observer: Observer) : void
  + detach(observer: Observer) : void
  + notify() : void
}

class AmbienteObservable {
  - observers : List<Observer>
  - contexto : ContextoBusca
  + verificar_pdfs() : void
  + total_pdfs() : int
}

class MenuCLI {
  + update(total_pdfs: int) : void
}

Subject <|.. AmbienteObservable
Observer <|.. MenuCLI

AmbienteObservable o-- Observer
AmbienteObservable --> ContextoBusca

@enduml
