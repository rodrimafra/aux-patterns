#!/usr/bin/env node
/**
 * Fetch published AI-crawler IP ranges and print vercel firewall
 * rules-edit commands. Never publishes. Run monthly.
 *
 * Usage: node tools/sync-ai-bot-allowlist.mjs
 */
const SOURCES = [
  {
    name: "OAI-SearchBot",
    ua: "OAI-SearchBot",
    url: "https://openai.com/searchbot.json",
  },
  {
    name: "ChatGPT-User",
    ua: "ChatGPT-User",
    url: "https://openai.com/chatgpt-user.json",
  },
  {
    name: "PerplexityBot",
    ua: "PerplexityBot",
    url: "https://www.perplexity.ai/perplexitybot.json",
  },
  {
    name: "Claude-SearchBot",
    ua: "Claude-SearchBot",
    url: "https://www.anthropic.com/claude-searchbot.json",
  },
];

function prefixesFrom(json) {
  if (Array.isArray(json?.prefixes)) {
    return json.prefixes
      .map((row) => row.ipv4Prefix || row.ipv6Prefix || row.prefix)
      .filter(Boolean);
  }
  if (Array.isArray(json)) {
    return json
      .map((row) => (typeof row === "string" ? row : row.ipv4Prefix || row.ipv6Prefix || row.prefix))
      .filter(Boolean);
  }
  throw new Error("Unrecognized IP list shape");
}

function shellQuote(value) {
  return "'" + String(value).replace(/'/g, `'"'"'`) + "'";
}

async function main() {
  const results = [];
  for (const src of SOURCES) {
    const res = await fetch(src.url, {
      headers: { Accept: "application/json" },
    });
    if (!res.ok) {
      console.error(`# skip ${src.name}: HTTP ${res.status} ${src.url}`);
      continue;
    }
    const json = await res.json();
    const cidrs = prefixesFrom(json);
    results.push({ ...src, cidrs });
  }

  if (!results.length) {
    console.error("No IP lists fetched. Check URLs.");
    process.exit(1);
  }

  console.log("# Review, then run. Do not auto-publish.");
  console.log("# After edits: vercel firewall diff && vercel firewall publish --yes");
  console.log("");
  for (const row of results) {
    const condUa = JSON.stringify({
      type: "user_agent",
      op: "sub",
      value: row.ua,
    });
    const condIp = JSON.stringify({
      type: "ip_address",
      op: "inc",
      value: row.cidrs,
    });
    const rule = `Allow ${row.name} verified`;
    console.log(`# ${row.name}: ${row.cidrs.length} prefixes from ${row.url}`);
    console.log(
      [
        "vercel firewall rules edit",
        shellQuote(rule),
        "--condition",
        shellQuote(condUa),
        "--condition",
        shellQuote(condIp),
        "--action bypass --yes",
      ].join(" ")
    );
    console.log("");
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
