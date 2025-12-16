@startuml
title Arquitetura Integrada - State + Observer + CLI

' ===== Interfaces =====
interface EstadoBusca {
  + pode_buscar() : bool
  + mensagem() : str
}

interface Observer {
  + update(total_pdfs: int) : void
}

interface Subject {
  + attach(observer: Observer) : void
  + detach(observer: Observer) : void
  + notify() : void
}

' ===== Estados =====
class EstadoComPDFs {
  + pode_buscar() : bool
  + mensagem() : str
}

class EstadoSemPDFs {
  + pode_buscar() : bool
  + mensagem() : str
}

EstadoBusca <|.. EstadoComPDFs
EstadoBusca <|.. EstadoSemPDFs

' ===== Contexto =====
class ContextoBusca {
  - estado : EstadoBusca
  - total_pdfs : int
  + set_estado(estado: EstadoBusca) : void
  + atualizar_total(total: int) : void
  + pode_buscar() : bool
  + mensagem() : str
}

ContextoBusca o-- EstadoBusca

' ===== Observable =====
class AmbienteObservable {
  - observers : List<Observer>
  - contexto : ContextoBusca
  + verificar_pdfs() : void
  + total_pdfs() : int
  + attach(observer: Observer) : void
  + notify() : void
}

Subject <|.. AmbienteObservable
AmbienteObservable --> ContextoBusca

' ===== CLI =====
class MenuCLI {
  - ambiente : AmbienteObservable
  + update(total_pdfs: int) : void
  + exibir_menu() : void
}

Observer <|.. MenuCLI
MenuCLI --> AmbienteObservable

@enduml
