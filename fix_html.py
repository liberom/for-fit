import re
import os

filepath = r'd:\Code\sandbox\_html\for-fit\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all occurrences exactly
def rep(old, new):
    global html
    if old not in html:
        print("COULD NOT FIND:\n", old)
    html = html.replace(old, new)

rep('''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
          target="_blank" class="btn btn-primary cta-header" data-pt="Vem treinar" data-es="Ven a entrenar">Vem
          treinar</a>''',
'''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
          target="_blank" class="btn btn-primary cta-header">
          <span lang="pt">Vem treinar</span>
          <span lang="es">Ven a entrenar</span>
        </a>''')

rep('''<h1 class="hero-title" style="margin-left: auto; margin-right: auto;"
        data-pt="Chegou em Ciudad del Este e não sabe onde treinar?"
        data-es="¿Llegaste a Ciudad del Este y no sabes dónde entrenar?">
        Chegou em Ciudad del Este e não sabe onde treinar?
      </h1>''',
'''<h1 class="hero-title" style="margin-left: auto; margin-right: auto;">
        <span lang="pt">Chegou em Ciudad del Este e não sabe onde treinar?</span>
        <span lang="es">¿Llegaste a Ciudad del Este y no sabes dónde entrenar?</span>
      </h1>''')

rep('''<span data-pt="Conheça a academia For Fit." data-es="Conoce el gimnasio For Fit.">Conheça a academia For
          Fit.</span>''',
'''<span class="d-inline-group">
          <span lang="pt">Conheça a academia For Fit.</span>
          <span lang="es">Conoce el gimnasio For Fit.</span>
        </span>''')

rep('''<strong class="highlight" data-pt="Vem treinar conosco!" data-es="¡Ven a entrenar con nosotros!">Vem treinar
          conosco!</strong>''',
'''<strong class="highlight">
          <span lang="pt">Vem treinar conosco!</span>
          <span lang="es">¡Ven a entrenar con nosotros!</span>
        </strong>''')

rep('''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
        target="_blank" class="btn btn-primary btn-large mt-4" data-pt="Quero Me Matricular"
        data-es="Quiero Inscribirme">Quero Me Matricular</a>''',
'''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
        target="_blank" class="btn btn-primary btn-large mt-4">
        <span lang="pt">Quero Me Matricular</span>
        <span lang="es">Quiero Inscribirme</span>
      </a>''')

rep('''<h2 class="section-title text-center" data-pt="BENEFÍCIOS DE SE MATRICULAR NA FOR FIT"
        data-es="BENEFICIOS DE INSCRIBIRSE EN FOR FIT">BENEFÍCIOS DE SE MATRICULAR NA FOR FIT</h2>''',
'''<h2 class="section-title text-center">
        <span lang="pt">BENEFÍCIOS DE SE MATRICULAR NA FOR FIT</span>
        <span lang="es">BENEFICIOS DE INSCRIBIRSE EN FOR FIT</span>
      </h2>''')

rep('''<p data-pt="1ª Avaliação física gratuita" data-es="1ª Evaluación física gratuita">1ª Avaliação física gratuita
          </p>''',
'''<p>
            <span lang="pt">1ª Avaliação física gratuita</span>
            <span lang="es">1ª Evaluación física gratuita</span>
          </p>''')

rep('''<p data-pt="Treino individualizado" data-es="Entrenamiento individualizado">Treino individualizado</p>''',
'''<p>
            <span lang="pt">Treino individualizado</span>
            <span lang="es">Entrenamiento individualizado</span>
          </p>''')

rep('''<p data-pt="Aplicativo exclusivo para alunos" data-es="Aplicación exclusiva para alumnos">Aplicativo exclusivo
            para alunos</p>''',
'''<p>
            <span lang="pt">Aplicativo exclusivo para alunos</span>
            <span lang="es">Aplicación exclusiva para alumnos</span>
          </p>''')

rep('''<p data-pt="Professores em sala para auxiliar" data-es="Profesores en sala para guiarte">Professores em sala
            para auxiliar</p>''',
'''<p>
            <span lang="pt">Professores em sala para auxiliar</span>
            <span lang="es">Profesores en sala para guiarte</span>
          </p>''')

rep('''<p data-pt="Sorteio todo mês com brindes de até R$ 200"
            data-es="Sorteo todos los meses con premios de hasta R$ 200">Sorteio todo mês com brindes de até R$ 200</p>''',
'''<p>
            <span lang="pt">Sorteio todo mês com brindes de até R$ 200</span>
            <span lang="es">Sorteo todos los meses con premios de hasta R$ 200</span>
          </p>''')

rep('''<h2 class="section-title text-center" data-pt="NÃO É APENAS SOBRE SER FITNESS"
        data-es="NO SE TRATA SOLO DE SER FITNESS">NÃO É APENAS SOBRE SER FITNESS</h2>''',
'''<h2 class="section-title text-center">
        <span lang="pt">NÃO É APENAS SOBRE SER FITNESS</span>
        <span lang="es">NO SE TRATA SOLO DE SER FITNESS</span>
      </h2>''')

rep('''<span data-pt="É TERAPIA" data-es="ES TERAPIA">É TERAPIA</span>''',
'''<span class="d-inline-group"><span lang="pt">É TERAPIA</span><span lang="es">ES TERAPIA</span></span>''')

rep('''<span data-pt="É REMÉDIO" data-es="ES MEDICINA">É REMÉDIO</span>''',
'''<span class="d-inline-group"><span lang="pt">É REMÉDIO</span><span lang="es">ES MEDICINA</span></span>''')

rep('''<span data-pt="É PAZ EM MOVIMENTO" data-es="ES PAZ EN MOVIMIENTO">É PAZ EM
                MOVIMENTO</span>''',
'''<span class="d-inline-group"><span lang="pt">É PAZ EM MOVIMENTO</span><span lang="es">ES PAZ EN MOVIMIENTO</span></span>''')

rep('''<span data-pt="É FORÇA MENTAL" data-es="ES FUERZA MENTAL">É FORÇA
                MENTAL</span>''',
'''<span class="d-inline-group"><span lang="pt">É FORÇA MENTAL</span><span lang="es">ES FUERZA MENTAL</span></span>''')

rep('''<span data-pt="É SAÚDE MENTAL" data-es="ES SALUD MENTAL">É SAÚDE
                MENTAL</span>''',
'''<span class="d-inline-group"><span lang="pt">É SAÚDE MENTAL</span><span lang="es">ES SALUD MENTAL</span></span>''')

rep('''<span data-pt="É AUTOCUIDADO" data-es="ES AUTOCUIDADO">É AUTOCUIDADO</span>''',
'''<span class="d-inline-group"><span lang="pt">É AUTOCUIDADO</span><span lang="es">ES AUTOCUIDADO</span></span>''')

rep('''<span data-pt="É AUTOCONFIANÇA" data-es="ES AUTOCONFIANZA">É
                AUTOCONFIANÇA</span>''',
'''<span class="d-inline-group"><span lang="pt">É AUTOCONFIANÇA</span><span lang="es">ES AUTOCONFIANZA</span></span>''')

rep('''<p class="therapy-conclusion highlight-text mt-4"
            data-pt="É SIMPLES: O CRESCIMENTO PESSOAL COMEÇA NA SUA TRANSFORMAÇÃO FÍSICA"
            data-es="ES SIMPLE: EL CRECIMIENTO PERSONAL COMIENZA EN TU TRANSFORMACIÓN FÍSICA">
            É SIMPLES: O CRESCIMENTO PESSOAL COMEÇA NA SUA TRANSFORMAÇÃO FÍSICA
          </p>''',
'''<p class="therapy-conclusion highlight-text mt-4">
            <span lang="pt">É SIMPLES: O CRESCIMENTO PESSOAL COMEÇA NA SUA TRANSFORMAÇÃO FÍSICA</span>
            <span lang="es">ES SIMPLE: EL CRECIMIENTO PERSONAL COMIENZA EN TU TRANSFORMACIÓN FÍSICA</span>
          </p>''')

rep('''<h2 data-pt="Quer ter resultados de verdade?" data-es="¿Quieres resultados de verdad?">Quer ter resultados de
          verdade?</h2>''',
'''<h2>
          <span lang="pt">Quer ter resultados de verdade?</span>
          <span lang="es">¿Quieres resultados de verdad?</span>
        </h2>''')

rep('''<h3 class="highlight-text" data-pt="VEM PRO NOSSO TIME!" data-es="¡ÚNETE A NUESTRO EQUIPO!">VEM PRO NOSSO TIME!
        </h3>''',
'''<h3 class="highlight-text">
          <span lang="pt">VEM PRO NOSSO TIME!</span>
          <span lang="es">¡ÚNETE A NUESTRO EQUIPO!</span>
        </h3>''')

rep('''<h2 data-pt="Transforme seu Corpo e Mente" data-es="Transforma tu Cuerpo y Mente">Transforme seu Corpo e Mente
        </h2>''',
'''<h2>
          <span lang="pt">Transforme seu Corpo e Mente</span>
          <span lang="es">Transforma tu Cuerpo y Mente</span>
        </h2>''')

rep('''<h3 class="highlight-text" data-pt="FOCO TOTAL" data-es="ENFOQUE TOTAL">FOCO TOTAL</h3>''',
'''<h3 class="highlight-text">
          <span lang="pt">FOCO TOTAL</span>
          <span lang="es">ENFOQUE TOTAL</span>
        </h3>''')

rep('''<blockquote data-pt="Ir pra academia é muito mais sobre constância do que altas cargas"
        data-es="Ir al gimnasio tiene mucho más que ver con la constancia que con cargas altas">
        "Ir pra academia é muito mais sobre constância do que altas cargas"
      </blockquote>''',
'''<blockquote>
        <span lang="pt">"Ir pra academia é muito mais sobre constância do que altas cargas"</span>
        <span lang="es">"Ir al gimnasio tiene mucho más que ver con la constancia que con cargas altas"</span>
      </blockquote>''')

rep('''<h2 class="section-title text-center" data-pt="Onde Estamos" data-es="Dónde Estamos">Onde Estamos</h2>''',
'''<h2 class="section-title text-center">
        <span lang="pt">Onde Estamos</span>
        <span lang="es">Dónde Estamos</span>
      </h2>''')

rep('''<span class="logo-part-for" data-pt="For" data-es="For">FOR</span><span class="logo-part-fit"
                data-pt="Fit" data-es="Fit">Fit</span>
              <span class="logo-part-academia" data-pt="Academia" data-es="Gimnasio">Academia</span>''',
'''<span class="logo-part-for">FOR</span><span class="logo-part-fit">Fit</span>
              <span class="logo-part-academia">
                <span lang="pt">Academia</span>
                <span lang="es">Gimnasio</span>
              </span>''')

rep('''<p data-pt="Km 7, Ciudad del Este - Paraguai" data-es="Km 7, Ciudad del Este - Paraguay">Km 7, Ciudad del
              Este - Paraguai</p>''',
'''<p>
              <span lang="pt">Km 7, Ciudad del Este - Paraguai</span>
              <span lang="es">Km 7, Ciudad del Este - Paraguay</span>
            </p>''')

rep('''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
              target="_blank" class="btn btn-primary w-full mt-4" data-pt="Chamar no WhatsApp"
              data-es="Hablar por WhatsApp">
              <span class="whatsapp-icon">💬</span> Chamar no WhatsApp
            </a>''',
'''<a href="https://wa.me/554796951904?text=Olá,%20vim%20do%20site%20e%20tenho%20interesse%20em%20fazer%20parte%20do%20time%21"
              target="_blank" class="btn btn-primary w-full mt-4">
              <span lang="pt"><span class="whatsapp-icon">💬</span> Chamar no WhatsApp</span>
              <span lang="es"><span class="whatsapp-icon">💬</span> Hablar por WhatsApp</span>
            </a>''')

rep('''<a href="https://www.instagram.com/forfit.cde/" target="_blank" class="btn btn-outline w-full mt-2"
              data-pt="Acessar Instagram" data-es="Acceder a Instagram">
              📸 Acessar Instagram
            </a>''',
'''<a href="https://www.instagram.com/forfit.cde/" target="_blank" class="btn btn-outline w-full mt-2">
              <span lang="pt">📸 Acessar Instagram</span>
              <span lang="es">📸 Acceder a Instagram</span>
            </a>''')

rep('''<p class="mt-4" data-pt="&copy; 2024 For Fit Academia. Todos os direitos reservados."
        data-es="&copy; 2024 Gimnasio For Fit. Todos los derechos reservados.">&copy; 2024 For Fit Academia. Todos os
        direitos reservados.</p>''',
'''<p class="mt-4">
        <span lang="pt">&copy; 2024 For Fit Academia. Todos os direitos reservados.</span>
        <span lang="es">&copy; 2024 Gimnasio For Fit. Todos los derechos reservados.</span>
      </p>''')

rep('''<p class="mt-2" style="font-size: 0.9rem; color: var(--text-muted);" data-pt="Feito por" data-es="Hecho por">
        Feito por <a href="https://liberom.github.io/vynix-sys" target="_blank" class="link-yellow">Vynix</a>
      </p>''',
'''<p class="mt-2" style="font-size: 0.9rem; color: var(--text-muted);">
        <span lang="pt">Feito por </span>
        <span lang="es">Hecho por </span>
        <a href="https://liberom.github.io/vynix-sys" target="_blank" class="link-yellow">Vynix</a>
      </p>''')

js_old = '''// Swap text for elements with data attributes
      const elements = document.querySelectorAll('[data-pt]');
      elements.forEach(el => {
        const text = el.getAttribute(`data-${currentLang}`);
        if (text) {
          if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
            el.placeholder = text;
          } else if (el.tagName === 'META') {
            el.content = text;
          } else {
            // Preserve inner HTML like strong elements if needed, but doing simple textContent for most
            if (el.children.length > 0 && el.innerHTML.includes('<strong')) {
              // this is tricky, let's keep it simple: direct text update for simple tags
            }
            el.textContent = text;
          }
        }
      });

      // Re-bind complex HTML element explicitly if necessary (Hero subtitle has strong tag inside)
      const heroSubtitleHighlight = document.querySelector('.hero-subtitle .highlight');
      if (heroSubtitleHighlight) heroSubtitleHighlight.textContent = heroSubtitleHighlight.getAttribute(`data-${currentLang}`);
      const heroSubtitleSpan = document.querySelector('.hero-subtitle span');
      if (heroSubtitleSpan) heroSubtitleSpan.textContent = heroSubtitleSpan.getAttribute(`data-${currentLang}`);'''

rep(js_old, '// Language switching is now handled by CSS leveraging html[lang]')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")
