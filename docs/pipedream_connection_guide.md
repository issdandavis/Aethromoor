# Pipedream Connection Guide (Local Agent Limitations)

This repository runs in an isolated environment with **no outbound internet access**. That means the local agent cannot connect to Pipedream or accept real API keys. Use the steps below to connect your own Pipedream account safely while keeping secrets out of the repository.

## How to connect using your API key (safe path)
1. **Create a Pipedream API key** in the Pipedream dashboard (`Settings -> API Keys`). Treat it like a password.
2. **Do *not* paste the key into chat or commit it.** Store it in Pipedream's Secret Store or as an Environment Variable.
3. **Create a workflow** in Pipedream and add a **HTTP trigger** (or schedule) for your use case.
4. **Add code steps** (Node.js or Python) that call external services. Keep all credentials in secrets (e.g., `process.env.MY_API_KEY`).
5. **Test in Pipedream** using the "Send Test Event" button or by hitting the public trigger URL from your terminal.

> Looking for a full example? See [`docs/pipedream_shopify_affiliate_workflow.md`](./pipedream_shopify_affiliate_workflow.md) for a complete, copy-pastable workflow that pulls products from an affiliate feed and upserts them into Shopify.

## Sample REST call with your API key
Use `curl` from your machine (not inside this repo) to verify the key works and to list workflows:

```bash
export PIPEDREAM_API_KEY="<your-key>"
curl -H "Authorization: Bearer $PIPEDREAM_API_KEY" \
     https://api.pipedream.com/v1/workflows
```

If you see workflow JSON, the key is valid and your account is reachable.

## Adding secrets to a Pipedream workflow
1. In the workflow editor, open **Secrets** and add entries like `SHOPIFY_ADMIN_TOKEN` or `AFFILIATE_FEED_URL`.
2. Reference them in code steps via `process.env.SECRET_NAME`.
3. Keep secrets out of logs by avoiding `console.log(process.env.SECRET_NAME)`.

## Minimal Pipedream code step template (Node.js)
Paste this into a **Code** step to call an external API using a secret:

```javascript
import axios from "axios";

export default defineComponent({
  async run({ steps, $ }) {
    const apiKey = process.env.MY_SERVICE_KEY; // stored in Secrets
    const res = await axios.get("https://api.example.com/v1/resource", {
      headers: { Authorization: `Bearer ${apiKey}` },
    });

    $.export("status", res.status);
    $.export("items", res.data?.items || []);
  },
});
```

## What the local agent can and cannot do
- ✅ **Can**: design workflows, draft code steps, and review Pipedream logs you paste here.
- ❌ **Cannot**: call Pipedream APIs directly, create workflows on your account, or accept real API keys inside this environment.

## Next steps
- Decide which trigger you need (HTTP, schedule, new row in Google Sheets, webhook, etc.).
- List the external services you want to call and which credentials each requires.
- Ask for a tailored set of code steps (Node.js/Python) and secret names, and we will draft them for you to paste into Pipedream.
