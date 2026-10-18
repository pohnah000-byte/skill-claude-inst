# Abracadabrax AI Product Photo Generator

Describe a product and get studio-style photos for a store, a marketplace listing or an ad: clean white-background packshots, lifestyle scenes, flat lays, wide hero banners or close-ups. Abracadabrax renders them with the credits of your own Abracadabrax account.

## How a request flows

1. You describe the product: what it is, its material, color and shape.
2. Claude saves a draft with the kind of shot, the setting, the aspect ratio and the image model, and shows its price in credits.
3. You adjust the scene or the format, then ask Claude to render it.
4. Abracadabrax renders the photo and Claude hands you the link to the image.

## Good to know

- **Made by AI.** Every image and video comes from generative AI models that Abracadabrax runs with its model partners. Drafts cost nothing; credits are only used when you confirm a render.
- **Created from a description.** The plugin draws a new product image from text; it does not edit a photo of your real product. Uploading and editing your own photos happens in the Abracadabrax workspace.

## Connection

Endpoint: `https://abracadabrax.app/api/claude/product-photo-generator/mcp` (remote MCP, Streamable HTTP).

Drafting works as a guest. The first time you render something, Claude opens the Abracadabrax sign-in page (OAuth 2.1 with PKCE), where you can also create an account. On clients without MCP Apps, such as Claude Code, the same tools answer with text and links instead of the panel.

## Tool reference

| Tool | Purpose | Credits |
|---|---|---|
| `prepare_product_photo` | Creates a draft from the product description, the kind of shot, the setting and the aspect ratio | none, guest allowed |
| `render_media_widget` | Shows a saved draft again in the panel | none |
| `update_media_project` | Applies the changes made in the panel | none |
| `generate_media` | Starts the render after you confirm | charged, sign-in needed |
| `get_media_job` | Reports progress and returns the file link | none, read-only |

## Try asking

- "White-background product photo of a matte black ceramic coffee mug"
- "Lifestyle shot of a linen tote bag on a sunny beach, 4:3"
- "Hero banner for a citrus-scented soy candle on a marble counter"

## Your data

Abracadabrax receives only what the tools carry: your request, the chosen settings and the ids of your drafts and renders. They are kept in your Abracadabrax account and passed to the model partner that renders the file. Nothing runs locally and the plugin reads nothing else from your conversation.

## Links

- Documentation: https://abracadabrax.app/mcp#product-photo-generator
- Privacy policy: https://abracadabrax.app/privacy
- Terms of service: https://abracadabrax.app/terms
- Help: https://abracadabrax.app/support
