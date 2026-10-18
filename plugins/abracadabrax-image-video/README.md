# Abracadabrax AI Image & Video Generator

Turn a text prompt into an AI image or a short AI video without leaving Claude. You set the model, the format and the length together with Claude, and Abracadabrax renders the result with the credits of your own Abracadabrax account.

## How a request flows

1. You describe the picture or the clip you have in mind.
2. Claude saves it as a draft and opens a panel with the model (Nano Banana 2, GPT Image 2, Kling 3.0 Pro and others), the aspect ratio, the duration and the price in credits.
3. You adjust anything you like, then ask Claude to go ahead.
4. Abracadabrax renders the media and Claude hands you the link to the finished file.

## Good to know

- **Made by AI.** Every image and video comes from generative AI models that Abracadabrax runs with its model partners. Drafts cost nothing; credits are only used when you confirm a generation.
- **Prompt only.** Editing an uploaded photo, removing a background or animating an existing image happens in the Abracadabrax workspace, not in this plugin.

## Connection

Endpoint: `https://abracadabrax.app/api/claude/media/mcp` (remote MCP, Streamable HTTP).

Drafting works as a guest. The first time you generate, Claude opens the Abracadabrax sign-in page (OAuth 2.1 with PKCE), where you can also create an account. On clients without MCP Apps, such as Claude Code, the same tools answer with text and links instead of the panel.

## Tool reference

| Tool | Purpose | Credits |
|---|---|---|
| `prepare_media_project` | Creates a draft with prompt, model, ratio and duration | none, guest allowed |
| `render_media_widget` | Shows a saved draft again in the panel | none |
| `update_media_project` | Applies the changes made in the panel | none |
| `generate_media` | Starts the render after you confirm | charged, sign-in needed |
| `get_media_job` | Reports progress and returns the file link | none, read-only |

## Try asking

- "Design a poster-style image of a lighthouse in a storm, portrait format"
- "Give me a 5-second clip of a hummingbird drinking from a red flower, slow motion"
- "Draw a flat illustration of a coffee shop storefront for my website header, 16:9"

## Your data

Abracadabrax receives only what the tools carry: the prompt, the chosen settings and the ids of your drafts and renders. They are kept in your Abracadabrax account and passed to the model partner that renders the file. Nothing runs locally and the plugin reads nothing else from your conversation.

## Links

- Documentation: https://abracadabrax.app/mcp#media
- Privacy policy: https://abracadabrax.app/privacy
- Terms of service: https://abracadabrax.app/terms
- Help: https://abracadabrax.app/support
