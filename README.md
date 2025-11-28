# Trabalho-6-Comp.-Distribuida

Origem:

  -REST — Representational State Transfer — é um estilo arquitetural para aplicações cliente-servidor, proposto por Roy Fielding para orientar o design da Web. 
  -Sua ideia surgiu durante a evolução da Web, buscando definir um padrão para troca de recursos via HTTP. 


Características principais:

  -Usa HTTP e seus verbos (GET, POST, PUT, DELETE etc.) para representar operações sobre “recursos” (por exemplo, usuários, músicas, playlists). 
  -Segue restrições como: cliente-servidor desacoplado; stateless (cada requisição tem que levar toda a informação necessária); interface uniforme; suporte a cache; arquitetura em camadas. 
  -É “agnóstico de linguagem” — pode ser implementado em praticamente qualquer linguagem/platforma que suporte HTTP/JSON. 


Vantagens:

  -Simplicidade e ampla familiaridade. A comunidade e ferramentas de integração, frameworks e bibliotecas são gigantes. 
  -Flexibilidade e compatibilidade: funciona facilmente em diferentes ambientes (web, mobile, IoT...). 
  -Escalabilidade: o estilo stateless + HTTP + cache favorece sistemas distribuídos e com muitos clientes. 


Desvantagens:

  -Pode haver “over-fetching” ou “under-fetching” de dados: ou você recebe mais dados do que precisa, ou precisa fazer múltiplas requisições para montar os dados desejados — o que pode gerar ineficiência. 
  -Cada recurso tipicamente exige seu próprio endpoint — para casos complexos ou com muitos relacionamentos, a API pode se tornar grande e difícil de manter. 
  -Statelessness exige que cada requisição traga todo contexto necessário, o que pode complicar operações que exigem estado/conta de sessão no servidor. 


SOAP

Origem:

  -SOAP — originalmente “Simple Object Access Protocol” — é um protocolo de mensagens para web services, baseado em XML. 
  -É mais antigo na história de APIs, sendo utilizado amplamente em sistemas corporativos e para integração entre plataformas diferentes. 


Características principais:

  -Comunica via mensagens XML estruturadas, geralmente sobre HTTP (mas pode usar outros protocolos como SMTP, TCP, etc.). 
  -Usa especificações formais para definir “contratos” da API: o serviço define tipos, operações, formato das mensagens — por exemplo via WSDL. 
  -Suporta extensões como segurança (WS-Security), transações, interoperabilidade entre sistemas heterogêneos, diferentes protocolos de transporte etc. 


Vantagens:

  -Contrato bem definido e formal: cliente e servidor sabem exatamente o formato e os tipos de dados esperados — bom para integração entre sistemas diferentes, legados ou corporativos. 
  -Suporte a segurança robusta, mensagens padronizadas, interoperabilidade e padrões maturados — úteis para cenários empresariais complexos. 


Desvantagens:

  -Verbosidade e complexidade: por usar XML e contratos rigorosos, as mensagens tendem a ser “pesadas” — mais dados, parsing mais lento, mais sobrecarga. 
  -Tempo de desenvolvimento maior e curva de aprendizado mais elevada — especialmente para quem não está acostumado com SOAP/WSDL/XML. 
  -Menos flexível em cenários modernos (web, mobile, microserviços), em comparação com APIs mais leves. 



GraphQL

Origem:

  -GraphQL foi criado pela Facebook e lançado publicamente em 2015. 
  -Surgiu para resolver problemas de APIs tradicionais (REST) no contexto de aplicações modernas — em especial aplicações com diversos clientes, front-ends múltiplos e necessidades de dados variadas. 

Características principais:

  -Usa uma única endpoint para todo o serviço — o cliente define o que quer buscar, com consultas precisas (query), e recebe exatamente os dados solicitados. 
  -É fortemente tipado — o “schema” da API define os tipos, as entidades e relacionamentos; o cliente escreve “queries” ou “mutations” conforme esse schema. 
  -Permite flexibilidade: o cliente decide quais campos quer, pode pedir dados aninhados, relações, etc. Isso evita tanto “over-fetching” quanto “under-fetching”. 


Vantagens:

  -Flexibilidade e eficiência para o cliente: só traz o que precisa — economiza banda, melhora performance e reduz quantidade de requisições. 
  -Muito bom para aplicações com clientes variados (web, mobile) e com dados complexos / relacionais. 
  -Facilita evolução da API sem multiplicação exagerada de endpoints — basta ajustar schema/resolvers. 

Desvantagens:

-Curva de aprendizado mais alta que REST — especialmente no design do schema, resolvers, e controle de performance. 
-Problemas de cache: por causa da flexibilidade e porque cada query pode ser diferente, fica mais difícil usar cache HTTP tradicional. 
-Sobrecarga no servidor: o backend precisa interpretar a query, resolver os dados conforme pedido, o que pode complicar otimizações e causar lentidão se não for bem implementado. 


gRPC

Origem:

  -gRPC é um framework de RPC (Remote Procedure Call) de alto desempenho, open-source. Ele foi criado pelo Google. 
  -É projetado para comunicação eficiente entre serviços — ideal para arquiteturas de microsserviços, sistemas distribuídos, aplicações com alta demanda de performance. 


Características principais:

  -Usa HTTP/2 para transporte + Protocol Buffers (protobuf) como formato de mensagem — isso resulta numa comunicação binária, compacta e rápida. 
  -Baseado em chamadas de “procedimento remoto” (RPC): cliente chama métodos definidos, passa parâmetros, recebe resposta. Diferente de REST, não lida diretamente com “recursos via URL”, mas com “métodos”. 
  -Tipagem forte, contratos via proto, boa definição de tipos e estruturas de dados. 


Vantagens:

  -Alta performance e eficiência: comunicação binária + HTTP/2 resulta em latência baixa, compactação e alto throughput — ideal para microserviços, sistemas distribuídos e comunicação interna. 
  -Tipagem forte e contratos bem definidos: facilita interoperabilidade, integridade de dados e manutenção em sistemas complexos. 
  -Bom para cenários de comunicação entre serviços (backend-backend), onde desempenho e eficiência são cruciais, especialmente em arquiteturas de microsserviços. 

Desvantagens:

  -Pode ser “overkill” para aplicações simples ou com poucos requisitos de desempenho — complexidade extra talvez não compense. 
  -Menos “plug-and-play” para aplicações web tradicionais ou front-end/browser — geralmente usado para comunicação backend-backend; pode exigir adaptação se quiser expor a API para clientes variados. 
  -Menor maturidade para algumas linguagens/ecossistemas, ou maior curva para configurar (thrift, proto, geração de stubs, versionamento) vs métodos simples como REST/JSON. 


Comparação:
<img width="1989" height="1181" alt="download (15)" src="https://github.com/user-attachments/assets/6774d6be-d355-46c7-966c-27c6c60b914b" />

<img width="1160" height="851" alt="download (16)" src="https://github.com/user-attachments/assets/af80ef1d-84a3-4047-90a2-b95c0934c21a" />


| **Protocolo** | **Latência (ms)** <br> *média* | **Latência (ms)** <br> *desvio padrão* | **Throughput (%)** <br> *média* | **Throughput (%)** <br> *desvio padrão* | **Uso de CPU (%)** <br> *média* | **Uso de CPU (%)** <br> *desvio padrão* |
| ------------- | ------------------------------ | -------------------------------------- | ------------------------------- | --------------------------------------- | ------------------------------- | --------------------------------------- |
| **GraphQL**   | 45.84                          | 4.93                                   | 76.99                           | 7.79                                    | 76.76                           | 25.96                                   |
| **REST**      | 26.80                          | 1.01                                   | 79.27                           | 8.86                                    | 45.40                           | 16.16                                   |
| **SOAP**      | 117.83                         | 34.10                                  | 66.79                           | 2.31                                    | 90.21                           | 8.30                                    |
| **gRPC**      | **19.31**                      | 4.92                                   | **90.00**                       | 4.74                                    | 50.70                           | 29.51                                   |


Análise:

## 1. **gRPC** - Mais Eficiente
**Justificativa:**
- Usa HTTP/2 com multiplexação (múltiplas requisições numa mesma conexão TCP)
- Serialização binária com Protocol Buffers (muito mais compacta que JSON/XML)
- Menor overhead de rede e parsing mais rápido
- Streaming nativo bidirecional
- Conexões persistentes por padrão

## 2. **REST** - Segundo Lugar
**Justificativa:**
- Protocolo stateless simples
- Overhead menor que GraphQL/SOAP
- Cache HTTP fácil de implementar
- Sem overhead de parsing de queries complexas
- Conexões podem ser mantidas com Keep-Alive

## 3. **GraphQL** - Terceiro Lugar  
**Justificativa:**
- Overhead de parsing de queries GraphQL
- Risco de queries complexas que sobrecarregam o servidor
- Over-fetching evitado, mas pode ter under-fetching (múltiplas round trips)
- Respostas tipicamente em JSON (maior que binary protocols)

## 4. **SOAP** - Menos Eficiente
**Justificativa:**
- XML extremamente verboso (muito overhead)
- Parsing de XML é computacionalmente caro
- WSDL e schemas complexos
- Base64 para dados binários aumenta tamanho em ~33%

## **Detalhes Técnicos:**

### gRPC Performance:
```python
# Binary Protocol Buffers vs JSON
JSON: {"id": 1, "title": "Song", "artist": "Artist"}  # ~50 bytes
Protobuf: \x08\x01\x12\x04Song\x1a\x06Artist         # ~15 bytes
```

### REST vs GraphQL:
- **REST**: `GET /tracks` → resposta fixa, cacheável
- **GraphQL**: Parsing de query + resolução dinâmica + overhead

### Cenários de Carga:
- **Alta concorrência**: gRPC > REST > GraphQL > SOAP
- **Largura de banda**: gRPC > GraphQL ≈ REST > SOAP  
- **Processamento CPU**: gRPC > REST > GraphQL > SOAP

**Recomendação para testes:** Comece com gRPC para baseline de performance máxima, depois compare com REST para casos de uso específicos.
