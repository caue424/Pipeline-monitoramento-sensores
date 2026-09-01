# Pipeline-monitoramento-sensores
<img width="1184" height="711" alt="image" src="https://github.com/user-attachments/assets/c1d2bdbc-5341-47e7-8c46-3356b3fad097" />

Este projeto simula um fluxo contínuo (pipeline) de dados, desde a geração das métricas de hardware até a visualização final em um painel interativo. O objetivo é demonstrar a extração, carga e transformação (ETL) de dados utilizando Python, banco de dados relacional e Microsoft Power BI.

**Tecnologias Utilizadas:**
*   **Python:** Bibliotecas `random`, `datetime`, `mysql-connector` (Geração de dados e aplicação de regras de negócio).
*   **MySQL:** Modelagem de tabelas e persistência estruturada dos registros.
*   **Power BI:** Conexão direta com o banco local, tratamento de dados via Power Query e visualização de indicadores.

**Como Funciona:**
1. O script em Python gera valores realistas para sensores de Temperatura, Umidade e Pressão Atmosférica.
2. Uma regra condicional classifica automaticamente o status de cada leitura (ex: NORMAL, TEMP ALTA, PRESSÃO BAIXA).
3. Os registros são injetados diretamente em uma tabela estruturada no MySQL.
4. O Power BI consome esses dados da base relacional, permitindo a análise de variações temporais e a filtragem interativa de alertas no dashboard.
