### Feito Por : Felipe Lamotte Mohacsi
from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

# Artigo em Markdown
article_md = """
# Introdução – escopo do artigo

Esta série de artigos trata do cache no contexto do HTTP. Quando feito corretamente, o cache pode aumentar o desempenho do seu aplicativo em uma ordem de grandeza. Pelo contrário, quando negligenciado ou completamente ignorado, pode levar a alguns efeitos colaterais muito indesejados causados ​​por servidores proxy malcomportados que, na ausência de instruções claras de armazenamento em cache, decidem armazenar em cache de qualquer maneira e servir recursos obsoletos.

...

## Conclusão

Ao longo deste artigo, descrevemos como o cache realmente funciona. Agora seria um bom momento para ativar um servidor de desenvolvimento local e mexer nesses dois cabeçalhos principais: Cache-Control e Vary para vê-los em ação.

Começamos dando uma visão geral de como funciona o cache, ilustrando os quatro caminhos possíveis que uma solicitação pode seguir: o caminho feliz (cache hit) e as 3 maneiras possíveis de ocorrer um cache miss: cache vazio, revalidação com falha e revalidação bem-sucedida. Esta visão geral por si só dá a possibilidade de entender como topologias de cache complexas podem se encaixar.

Em seguida, nos aprofundamos e examinamos todos os cabeçalhos Cache-Control mais úteis e esclarecemos algumas diferenças sutis que são facilmente ignoradas.

Também analisamos o cabeçalho Vary e a diferença fundamental entre recursos e representações, para evitar servir a representação errada ao cliente certo.

Por fim, reservamos algum tempo para revisar tudo sob o ângulo dos equívocos comuns que você pode encontrar e esperamos ajudá-lo a evitá-los.

No próximo artigo, aplicaremos todo esse conhecimento para configurar um ambiente...
"""

# Rota para exibir o artigo em HTML
@app.route('/')
def display_article():
    # Converte o Markdown para HTML
    html_content = markdown.markdown(article_md)
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
