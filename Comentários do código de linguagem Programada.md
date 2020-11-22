# Comentários do código de linguagem Programada;

tODOS OS COMENTÁRIOS ESTÃO TAMBÉM PRESENTES NO CÓDIGO, É BOM CHEGAR PARA VER A PARTE DO CÓDIGO QUE CORRESPONDE O COMENTÁRIO... 

Telegram Bot de Liguangem programada (Menu);

Código em andamento;

há de fazer ainda adaptações e, corrigir alguns pontos que faltam ou inserir novas atualizações, mas está mais perto da proposta final. 

falta integrar o bot de linguagem natual juntamente ao bot de linguagem programada, não sei ainda se coloco junto ao código ou num programa separado e importá - lo.

LINHA DOS COMENTÁRIOS DO CÓDIGO DE LINGUAGEM PROGRAMADA:

L41 para a opção menu não coloquei opções de número e sim strings(fones,chat,outros) para não ter conflito com um submenu já existente numérico(linha 60/61) que responde a opção -> fones e o número retorna a linha do arquivo contatos.txt;

L48 ok está quase do jeito desejado - imprimir todas as opções sem formato de dicionário - corrigir essa bagaça - intenção é trazer do arquivo chat.txt todo o conteúdo, não conseguir ainda no formato desejado;
L49 arquivo chat.txt tem um única linha, não conseguir colocar de forma organizada as linhas como o arquivo contato.txt, pois irá imprimir a primeira linha e não retornará todas elas que é a intenção.

L58 há apenas menu de contatos telefonicos e telegram, quais implementações podem ser adicionais? sugestões para outras formas de atendimento.

L60 problema no posts, se posts for string(é uma string no código, mas nessa parte precisa retornar como int - numero da linha do arquivo para retornar o resultado - acha que é uma gambiarra não sei se é problema) como passar por aki...(essa parte do programa) ou numero fora do intervalo de linhas do arquivo contatos.txt dará erro...a linha não existe que resultado trazer?
L61 (RESOLVIDO - coloquei as opções separadamente como string e convertento - as na parte do código como int), estava pondo um intervalo (posts >= 0 or posts <= 18 limite dos contatos), mas não conseguir converter isso como int;


L75 a 78 é uma parte do código comentada e, sugestão de inserir nessa parte o código de linguagem natural, mas naquela dúvida, misturo o código de lingagem natural e pragramada num mesmo arquivo ou coloco em arq. separados e importo o serviço para rodar ao mesmo tempo.
