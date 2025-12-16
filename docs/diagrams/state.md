@startuml
title Padrão State - Disponibilidade de Busca por PDFs

interface EstadoBusca {
  + pode_buscar() : bool
  + mensagem() : str
}

class EstadoComPDFs {
  + pode_buscar() : bool
  + mensagem() : str
}

class EstadoSemPDFs {
  + pode_buscar() : bool
  + mensagem() : str
}

class ContextoBusca {
  - estado : EstadoBusca
  + set_estado(estado: EstadoBusca) : void
  + pode_buscar() : bool
  + mensagem() : str
}

EstadoBusca <|.. EstadoComPDFs
EstadoBusca <|.. EstadoSemPDFs

ContextoBusca o-- EstadoBusca

@enduml
