<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-pt-dark.svg">
  <img alt="Lucas Matias: estudante de Engenharia de Software no IFG e escrevente de cartório em Goiás" src="assets/banner-pt-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://linkedin.com/in/matiaslucas"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-14294D?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMC40NDcgMjAuNDUyaC0zLjU1NHYtNS41NjljMC0xLjMyOC0uMDI3LTMuMDM3LTEuODUyLTMuMDM3Yy0xLjg1MyAwLTIuMTM2IDEuNDQ1LTIuMTM2IDIuOTM5djUuNjY3SDkuMzUxVjloMy40MTR2MS41NjFoLjA0NmMuNDc3LS45IDEuNjM3LTEuODUgMy4zNy0xLjg1YzMuNjAxIDAgNC4yNjcgMi4zNyA0LjI2NyA1LjQ1NXY2LjI4NnpNNS4zMzcgNy40MzNhMi4wNiAyLjA2IDAgMCAxLTIuMDYzLTIuMDY1YTIuMDY0IDIuMDY0IDAgMSAxIDIuMDYzIDIuMDY1bTEuNzgyIDEzLjAxOUgzLjU1NVY5aDMuNTY0ek0yMi4yMjUgMEgxLjc3MUMuNzkyIDAgMCAuNzc0IDAgMS43Mjl2MjAuNTQyQzAgMjMuMjI3Ljc5MiAyNCAxLjc3MSAyNGgyMC40NTFDMjMuMiAyNCAyNCAyMy4yMjcgMjQgMjIuMjcxVjEuNzI5QzI0IC43NzQgMjMuMiAwIDIyLjIyMiAweiIvPjwvc3ZnPg%3D%3D"></a>
  <a href="mailto:lucasmatiias2208@gmail.com"><img alt="E-mail" src="https://img.shields.io/badge/E--mail-14294D?style=flat&logo=gmail&logoColor=white"></a>
  <a href="mailto:matias.lucas@estudantes.ifg.edu.br"><img alt="E-mail acadêmico (IFG)" src="https://img.shields.io/badge/E--mail_IFG-14294D?style=flat&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDcgNDQ3Ij48Y2lyY2xlIGN4PSIxMjIiIGN5PSIxMjQiIHI9IjkyIiBmaWxsPSIjQzkwQzBGIi8%2BPHJlY3QgeD0iMjQzIiB5PSI0NiIgd2lkdGg9IjE2NiIgaGVpZ2h0PSIxNTYiIHJ4PSIyNCIgZmlsbD0iIzM1OTgzMCIvPjxyZWN0IHg9IjQwIiB5PSIyMzciIHdpZHRoPSIxNjYiIGhlaWdodD0iMTU2IiByeD0iMjQiIGZpbGw9IiMzNTk4MzAiLz48cmVjdCB4PSIyNDMiIHk9IjIzNyIgd2lkdGg9IjE2NiIgaGVpZ2h0PSIxNTgiIHJ4PSIyNCIgZmlsbD0iIzM1OTgzMCIvPjwvc3ZnPg%3D%3D"></a>
  <a href="https://instagram.com/lucasmatias.ll"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-14294D?style=flat&logo=instagram&logoColor=white"></a>
</p>

<p align="center"><b>Português</b> | <a href="https://github.com/matias-lucas/matias-lucas/blob/main/README.en.md">English</a></p>

## Sobre mim

Estudo Engenharia de Software no **Instituto Federal de Goiás (IFG)**, hoje no 4º período. Também trabalho como **escrevente extrajudicial** em cartório e na **gestão financeira de dois loteamentos**.

É dessa rotina que saem os meus projetos: quando um processo é repetitivo, confuso ou fácil de errar, tento transformá-lo em software. O Classdays nasceu para organizar a agenda da minha turma; a automação de boletos, para acabar com as baixas manuais nos loteamentos.

Uso IA (Claude Code) no meu dia a dia de desenvolvimento. Ela acelera a escrita do código. A minha parte é entender o problema, definir as regras de negócio, revisar o que entra e testar antes de publicar.

**Estou procurando estágio em desenvolvimento web.** Se a sua equipe tem uma vaga, vamos conversar.

## Projeto em destaque: Classdays

O **[Classdays](https://classdays.net)** é o calendário acadêmico da turma em um link público: aulas da semana, provas, entregas e cancelamentos, fáceis de ler no celular. Quem cadastra não precisa preencher formulário: escreve uma frase, como *"na próxima terça não haverá aula de banco de dados"*, e o sistema transforma em evento.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/classdays-demo-pt-dark.gif">
  <img alt="Demonstração do Classdays: no painel, o representante digita 'na próxima terça não haverá aula de banco de dados', o sistema mostra o cancelamento já preenchido para revisão e, depois de salvo, a grade da semana seguinte aparece com a aula cancelada" src="assets/classdays-demo-pt-light.gif" width="100%">
</picture>

- **Linguagem natural:** a frase vai para a API do Claude com *structured outputs*, e o schema garante o formato da resposta. Sem chave configurada, um parser de regras em português assume.
- **Nada entra sem revisão:** todo evento passa por um preview editável antes de chegar ao banco.
- **Feito para a turma:** sem login para consultar, tema claro e escuro, contraste AA, navegação por teclado e alvos de toque de 44 px.
- **245 testes automatizados** cobrindo datas relativas, cancelamentos, feriados e o parser.

**Stack:** Next.js 16, React 19, TypeScript, Supabase (Postgres com RLS), API do Claude e Vercel.

**[Abrir o Classdays](https://classdays.net)** | [Ver o código](https://github.com/matias-lucas/Classdays)

## Outros projetos

**[Site da Matias Imóveis](https://github.com/matias-lucas/matiasimoveis-site)** *(em desenvolvimento)*<br>
Site de uma imobiliária de Itaberaí (GO): busca de imóveis com filtros, contato direto pelo WhatsApp já com o imóvel na mensagem e painel para os corretores cadastrarem fotos e vídeos. Next.js, TypeScript e Supabase.

**Automação de baixa de boletos** *(em uso, repositório privado)*<br>
Programa para Windows usado nos dois loteamentos: lê o extrato do banco, calcula juros e multa e dá baixa no sistema de cobrança, sempre com uma conferência na tela antes de confirmar. Foi desenvolvido com IA a partir das regras de negócio que levantei no trabalho.

**[proj_algb](https://github.com/matias-lucas/proj_algb)** *(projeto acadêmico, descontinuado)*<br>
Trabalho em dupla da disciplina de Álgebra Linear, em C: lê, resolve e classifica sistemas lineares (SPD, SPI ou SI) e guarda os sistemas em arquivo.

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Stack: Next.js, React, TypeScript, JavaScript, HTML, CSS, Supabase, PostgreSQL, API do Claude, Vercel, Git e C" src="assets/stack-light.svg" width="100%">
</picture>

## Atividade

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/stats-pt-dark.svg">
  <img alt="Atividade no GitHub nos últimos 12 meses: contribuições, commits, pull requests, sequências e repositórios públicos" src="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/stats-pt-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/snake-dark.svg">
  <img alt="Animação do gráfico de contribuições do último ano" src="https://raw.githubusercontent.com/matias-lucas/matias-lucas/output/snake-light.svg" width="100%">
</picture>

<sub>Os dois quadros são gerados todo dia por uma [GitHub Action](https://github.com/matias-lucas/matias-lucas/blob/main/.github/workflows/profile-stats.yml) neste repositório, sem depender de serviços externos.</sub>

---

<p align="center">Procurando estágio em desenvolvimento web e aberto a conversar sobre automação e software para problemas reais.<br>
O jeito mais rápido de falar comigo é pelo <a href="https://linkedin.com/in/matiaslucas">LinkedIn</a> ou por <a href="mailto:lucasmatiias2208@gmail.com">e-mail</a>.</p>
