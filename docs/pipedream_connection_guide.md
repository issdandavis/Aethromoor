# Pipedream Connection Guide (Local Agent Limitations)

This repository runs in an isolated environment with **no outbound internet access**. That means the local agent cannot connect to Pipedream or accept real API keys. Use the steps below to connect your own Pipedream account safely while keeping secrets out of the repository.

## Quickstart: safe path with your API key
1. **Create a Pipedream API key** in the Pipedream dashboard (`Settings → API Keys`). Treat it like a password.
2. **Do *not* paste the key into chat or commit it.** Store it in Pipedream's Secret Store or as an Environment Variable.
3. **Create a workflow** and add a **HTTP trigger** (or schedule) for your use case. Copy the trigger URL if HTTP-based.
4. **Open the Secrets panel** and add entries like `MY_SERVICE_KEY`, `SHOPIFY_ADMIN_TOKEN`, or `AFFILIATE_FEED_URL`.
5. **Add a Code step** (Node.js or Python) that reads secrets via `process.env.SECRET_NAME` and calls your APIs.
6. **Test in Pipedream** using "Send Test Event" or by hitting the trigger URL with `curl` (example below). Confirm the step exports the values you expect.

> Looking for a full example? See [`docs/pipedream_shopify_affiliate_workflow.md`](./pipedream_shopify_affiliate_workflow.md) for a complete, copy-pastable workflow that pulls products from an affiliate feed and upserts them into Shopify.

### Use it right now (5-minute setup)
If you just want a working workflow to test immediately, follow these exact steps:
1. Go to **Workflows → New** → choose **HTTP / Webhook**.
2. Copy the **Endpoint URL** shown at the top of the trigger step.
3. Click **Secrets** → **+ Add secret** → create `MY_SERVICE_KEY` with your real API key.
4. Add a **Code (Node.js)** step and paste the **Minimal Pipedream code** from below.
5. Click **Deploy**.
6. From your terminal, run the **Trigger test helper** (replace the URL with your endpoint). Your run should appear in **Inspect** with `status` and `items` exports.
7. Replace the placeholder API URL in the code step with your real service and redeploy.

## Sample REST call with your API key
Use `curl` from your machine (not inside this repo) to verify the key works and to list workflows:

```bash
export PIPEDREAM_API_KEY="<your-key>"
curl -H "Authorization: Bearer $PIPEDREAM_API_KEY" \
     https://api.pipedream.com/v1/workflows
```

If you see workflow JSON, the key is valid and your account is reachable.

## End-to-end example: create and test an HTTP-triggered workflow
Follow these concrete steps in the Pipedream UI:
1. **Create workflow → HTTP / Webhook** trigger. Copy the generated URL.
2. Click **+** and choose **Code (Node.js)**.
3. Click **Secrets** (upper right) → **+ Add secret** → create `MY_SERVICE_KEY` with your API key.
4. Paste the code template below, replacing the placeholder URL with your target API.
5. Click **Deploy** and then **Send Test Event** (or run the `curl` command under the trigger URL) to populate sample data.
6. Open the **Inspect** tab → select the latest run → confirm the step **Exports** show the status/data you expect.

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

### Trigger test helper (replace with your trigger URL)
Run this from your terminal to fire the workflow after deployment. It sends a JSON payload you can inspect in **steps.trigger.event**:

```bash
curl -X POST "https://endpoint.m.pipedream.net/your-trigger-id" \
  -H "Content-Type: application/json" \
  -d '{"sample": "hello"}'
```

## What the local agent can and cannot do
- ✅ **Can**: design workflows, draft code steps, and review Pipedream logs you paste here.
- ❌ **Cannot**: call Pipedream APIs directly, create workflows on your account, or accept real API keys inside this environment.

## Next steps
- Decide which trigger you need (HTTP, schedule, new row in Google Sheets, webhook, etc.).
- List the external services you want to call and which credentials each requires.
- Ask for a tailored set of code steps (Node.js/Python) and secret names, and we will draft them for you to paste into Pipedream.
