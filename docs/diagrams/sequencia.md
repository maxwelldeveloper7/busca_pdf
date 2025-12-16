@startuml
title Diagrama de Sequência - Busca com Revalidação Dinâmica

actor Usuario
participant MenuCLI
participant AmbienteObservable
participant ContextoBusca
participant SistemaArquivos

Usuario -> MenuCLI : Seleciona "Realizar busca"
MenuCLI -> AmbienteObservable : total_pdfs()

AmbienteObservable -> SistemaArquivos : listar *.pdf
SistemaArquivos --> AmbienteObservable : quantidade atual

AmbienteObservable --> MenuCLI : total_pdfs

alt Nenhum PDF encontrado
    MenuCLI -> Usuario : Exibe mensagem de bloqueio
else PDFs disponíveis
    MenuCLI -> Usuario : Solicita termo de busca
    Usuario -> MenuCLI : Informa termo
    MenuCLI -> AmbienteObservable : verificar_pdfs()

    AmbienteObservable -> SistemaArquivos : listar *.pdf
    SistemaArquivos --> AmbienteObservable : quantidade atual

    AmbienteObservable -> ContextoBusca : atualizar_total(total)
    AmbienteObservable -> ContextoBusca : set_estado()

    AmbienteObservable -> MenuCLI : notify()

    MenuCLI -> Usuario : Exibe atualização de estado
    MenuCLI -> Usuario : Executa busca nos PDFs
end

@enduml
