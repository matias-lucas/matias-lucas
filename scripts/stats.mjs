// Gera o "quadro de atividade" do perfil (stats-{pt,en}-{light,dark}.svg).
// Roda no GitHub Actions (.github/workflows/profile-stats.yml) com o
// GITHUB_TOKEN do próprio workflow: nenhum serviço externo envolvido.
//
// Uso: node scripts/stats.mjs <pasta-de-saida> [--mock]
import fs from "node:fs";
import path from "node:path";

const OUT = process.argv[2] ?? "dist";
const MOCK = process.argv.includes("--mock");
const LOGIN = process.env.GITHUB_LOGIN ?? "matias-lucas";

const QUERY = `query($login: String!) {
  user(login: $login) {
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false) { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}`;

async function fetchUser() {
  if (MOCK) return mockUser();
  const token = process.env.GITHUB_TOKEN;
  if (!token) throw new Error("GITHUB_TOKEN não definido");
  const res = await fetch("https://api.github.com/graphql", {
    method: "POST",
    headers: { Authorization: `bearer ${token}`, "Content-Type": "application/json", "User-Agent": LOGIN },
    body: JSON.stringify({ query: QUERY, variables: { login: LOGIN } }),
  });
  const json = await res.json();
  if (!res.ok || json.errors) throw new Error(`GraphQL: ${res.status} ${JSON.stringify(json.errors ?? json)}`);
  return json.data.user;
}

function mockUser() {
  const weeks = [];
  const start = new Date("2025-10-12T00:00:00Z");
  for (let w = 0; w < 53; w++) {
    const contributionDays = [];
    for (let d = 0; d < 7; d++) {
      const date = new Date(start.getTime() + (w * 7 + d) * 864e5).toISOString().slice(0, 10);
      if (date > "2026-10-14") break;
      contributionDays.push({ date, contributionCount: (w * 7 + d) % 5 === 0 ? 0 : ((w + d) % 4) + 1 });
    }
    weeks.push({ contributionDays });
  }
  return {
    repositories: { totalCount: 5 },
    contributionsCollection: {
      totalCommitContributions: 612,
      totalPullRequestContributions: 18,
      contributionCalendar: { totalContributions: 734, weeks },
    },
  };
}

// Dias com pelo menos uma contribuição e a maior sequência de dias seguidos.
// (A sequência atual ficou de fora: zera a cada dia sem commit e diz pouco.)
function activity(days) {
  let active = 0;
  let longest = 0;
  let run = 0;
  for (const d of days) {
    if (d.contributionCount > 0) active++;
    run = d.contributionCount > 0 ? run + 1 : 0;
    longest = Math.max(longest, run);
  }
  return { active, longest };
}

const THEMES = {
  light: { bg: "#F4F7FB", line: "#C9D5E6", ink: "#14294D", sub: "#5B6F90", accent: "#2E5AD6" },
  dark: { bg: "#0D1D36", line: "#22406B", ink: "#EEF3FB", sub: "#A9BCDB", accent: "#6F95FF" },
};

const COPY = {
  pt: {
    title: "Atividade no GitHub, últimos 12 meses",
    updated: (d) => `atualizado em ${d}`,
    rows: ["Contribuições", "Commits", "Pull requests", "Dias com contribuição", "Maior sequência", "Repositórios públicos"],
    days: (n) => `${n} ${n === 1 ? "dia" : "dias"}`,
    date: (iso) => iso.split("-").reverse().join("/"),
    num: (n) => n.toLocaleString("pt-BR"),
  },
  en: {
    title: "GitHub activity, last 12 months",
    updated: (d) => `updated ${d}`,
    rows: ["Contributions", "Commits", "Pull requests", "Days with contributions", "Longest streak", "Public repositories"],
    days: (n) => `${n} ${n === 1 ? "day" : "days"}`,
    date: (iso) => new Date(`${iso}T12:00:00Z`).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" }),
    num: (n) => n.toLocaleString("en-US"),
  },
};

const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function render(stats, lang, theme) {
  const t = THEMES[theme];
  const c = COPY[lang];
  const W = 1200;
  const HEAD = 64;
  const ROW = 54;
  const H = HEAD + ROW * 3;
  const values = [
    c.num(stats.total),
    c.num(stats.commits),
    c.num(stats.prs),
    c.num(stats.active),
    c.days(stats.longest),
    c.num(stats.repos),
  ];
  const cells = values.map((v, i) => {
    const col = Math.floor(i / 3);
    const row = i % 3;
    const x = col * (W / 2);
    const y = HEAD + row * ROW + ROW / 2 + 7;
    return `<text x="${x + 32}" y="${y}" class="l">${esc(c.rows[i])}</text>` +
      `<text x="${x + W / 2 - 32}" y="${y}" class="v" text-anchor="end">${esc(v)}</text>`;
  });
  const lines = [
    `<path d="M0 ${HEAD}H${W}"/>`,
    `<path d="M0 ${HEAD + ROW}H${W}M0 ${HEAD + ROW * 2}H${W}" stroke-dasharray="2 5"/>`,
    `<path d="M${W / 2} ${HEAD}V${H}"/>`,
  ];
  const alt = `${c.title}: ` + c.rows.map((r, i) => `${r} ${values[i]}`).join(", ");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 ${W + 2} ${H + 2}" width="${W + 2}" height="${H + 2}" role="img" aria-label="${esc(alt)}">
  <title>${esc(alt)}</title>
  <style>
    text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;font-variant-numeric:tabular-nums}
    .h{font-size:21px;font-weight:650;fill:${t.ink}}
    .u{font-size:17px;fill:${t.sub}}
    .l{font-size:20px;fill:${t.sub}}
    .v{font-size:22px;font-weight:650;fill:${t.ink}}
  </style>
  <rect width="${W}" height="${H}" rx="14" fill="${t.bg}" stroke="${t.line}" stroke-width="1.2"/>
  <circle cx="34" cy="${HEAD / 2}" r="6" fill="${t.accent}"/>
  <text x="52" y="${HEAD / 2 + 7}" class="h">${esc(c.title)}</text>
  <text x="${W - 32}" y="${HEAD / 2 + 6}" class="u" text-anchor="end">${esc(c.updated(c.date(stats.today)))}</text>
  <g stroke="${t.line}" stroke-width="1.2" fill="none">${lines.join("")}</g>
  ${cells.join("\n  ")}
</svg>
`;
}

const user = await fetchUser();
const cc = user.contributionsCollection;
const days = cc.contributionCalendar.weeks.flatMap((w) => w.contributionDays);
const stats = {
  total: cc.contributionCalendar.totalContributions,
  commits: cc.totalCommitContributions,
  prs: cc.totalPullRequestContributions,
  repos: user.repositories.totalCount,
  today: days.at(-1)?.date ?? new Date().toISOString().slice(0, 10),
  ...activity(days),
};

fs.mkdirSync(OUT, { recursive: true });
for (const lang of Object.keys(COPY)) {
  for (const theme of Object.keys(THEMES)) {
    fs.writeFileSync(path.join(OUT, `stats-${lang}-${theme}.svg`), render(stats, lang, theme));
  }
}
console.log(JSON.stringify(stats));
