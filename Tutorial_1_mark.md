
### Feito Por : Felipe Lamotte Mohacsi
from flask import Flask, render_template_string
import markdown

app = Flask(__name__)

# Conteúdo do artigo em formato Markdown
markdown_content = """
# Cache de API com cabeçalhos HTTP

## O que é cache de API?

Se mais de uma solicitação de API resultar na mesma resposta, podemos armazenar essa resposta em um cache que esteja mais prontamente disponível. Quando um cliente solicita alguns recursos, a solicitação passa primeiro por um cache e depois para o servidor. Se o cache contiver os dados atualizados, a solicitação usará esses dados para satisfazer a solicitação do usuário.

Isso é cache de API e, se feito corretamente, resulta em melhor desempenho e latência, evitando carga excessiva na API. Hoje, as APIs usam extensivamente o cache. Portanto, é essencial que os desenvolvedores entendam como funciona o cache com HTTP.

## Cache de API com cabeçalhos HTTP

Os cabeçalhos de cache HTTP fornecem uma maneira de gerenciar efetivamente o cache de API em aplicativos da web. Eles permitem que o servidor de origem da API comunique estratégias de cache ao cliente. Ao usar cabeçalhos HTTP, um servidor de origem pode especificar o seguinte:

- O recurso pode ser armazenado em cache ou não?
- Por quanto tempo um recurso pode ser armazenado em cache?
- Quem pode armazenar em cache a resposta?
- Quando validar o cache para obter dados atualizados.

Com o uso apropriado desses cabeçalhos, os tempos de resposta podem ser melhorados e a carga do servidor reduzida. Então, sem mais delongas, vamos examinar esses cabeçalhos.

## Controle de cache

O cabeçalho Cache-Control é usado para especificar políticas de cache do navegador tanto nas solicitações do cliente quanto nas respostas do servidor, permitindo que o navegador armazene cópias locais de recursos para recuperação mais rápida. Ele especifica como e por quanto tempo o navegador deve armazenar a resposta em cache.

Para este propósito, o cabeçalho Cache-Control possui múltiplas diretivas. Aqui estão as diretivas mais comumente usadas:

- **idade máxima**
- **privado**
- **público**
- **sem loja**
- **sem cache**
- **deve revalidar**

Vamos examiná-los em detalhes.
"""

@app.route('/')
def home():
    # Renderizando o conteúdo Markdown para HTML
    html_content = markdown.markdown(markdown_content)
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
