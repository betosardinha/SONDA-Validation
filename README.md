# SONDA-Validation

# Projeto-SONDA
=============

O projeto SONDA tem como principal objetivo implementar uma infraestrutura física e de recursos humanos destinada à montagem e melhoramento da base de dados de superfície necessária ao levantamento dos recursos de energia solar e eólica no Brasil e consequente planejamento de seu uso.

De acordo com o levantamento extensivo realizado pelo INPE e publicado no relatório “Solar and Wind Energy Resource Assessment” (Pereira ISBN 85-17-00002-1 de novembro de 2000), a base de dados de superfície necessária a validação desses modelos é extremamente deficiente no Brasil e em toda a América Latina. Como exemplo, temos a rede solarimétrica nacional, que contava com 24 piranômetros distribuídos nacionalmente, hoje se encontra totalmente desativada.

Atualmente, o projeto SONDA encontra-se totalmente implementado e conta com um total de 18 estações, sendo 13 delas próprias e outras 5 de empresas ou instituições parceiras. Todas as informações como os dados, posição, altitude e outras estão disponibilizadas na página de internet do projeto (http://sonda.ccst.inpe.br). Além da disponibilidade dessas informações , o SONDA conta com uma série de critérios de validação dessas informações seguindo os mais rigorosos testes como o da Baseline Solar Radiation Network (BSRN), World Meteorological Organization (WMO) e outros desenvolvidos pela experiência do grupo de Energias Renováveis do Centro de Ciências do Sistema Terrestre (CCST). 

O processo de validação aplicado nos dados é constituído hoje de 3 níveis: no primeiro nível, são testados os limites fisicamente possíveis, onde são esperados valores dentro de um intervalo já conhecido. No segundo nível, são filtrados os eventos extremamente raros. No terceiro nível, as variáveis são comparadas com outras da mesma estação, onde são esperados valores dentro de certos limites e cada variável medida tem contribuição no valor da outra. Embora esses testes eliminem grande parte dos erros, alguns dados ainda se mostram suspeitos. Assim, torna-se necessário implementar outro nível, o nível 4, onde a radiação global, direta e difusa são comparadas com o modelo de céu claro proposto por Iqbal (1983), chamado de Parametrization Model C.

# Este Código

Este código é uma reestruturação em Python 3.7 do processo de validação dos dados SONDA feito por Rafael Carvalho Chagas (2012 - 2014) utilizando a linguagem Java.
