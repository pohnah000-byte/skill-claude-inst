# Abracadabrax Album Cover Art Maker

Give Claude the title of your album, single, EP, mixtape or playlist, the artist name, the genre and the mood, and get square cover art that still reads as a small thumbnail on streaming platforms, with the title (and the artist) set into the artwork or no text at all. Abracadabrax renders it with the credits of your own Abracadabrax account.

## How a request flows

1. You tell Claude the title, the artist and the kind of music.
2. Claude saves a square draft with the mood, the visual style, the lettering and the image model, and shows its price in credits.
3. You change the style or the wording, then ask Claude to render it.
4. Abracadabrax renders the cover and Claude hands you the link to the image.

## Good to know

- **Made by AI.** Every image and video comes from generative AI models that Abracadabrax runs with its model partners. Drafts cost nothing; credits are only used when you confirm a render.
- **Covers from text.** Putting your own photo or band logo on the cover needs an upload, which happens in the Abracadabrax workspace, not in this plugin.

## Connection

Endpoint: `https://abracadabrax.app/api/claude/album-cover-maker/mcp` (remote MCP, Streamable HTTP).

Drafting works as a guest. The first time you render something, Claude opens the Abracadabrax sign-in page (OAuth 2.1 with PKCE), where you can also create an account. On clients without MCP Apps, such as Claude Code, the same tools answer with text and links instead of the panel.

## Tool reference

| Tool | Purpose | Credits |
|---|---|---|
| `prepare_album_cover` | Creates a square draft from the title, the artist, the genre, the mood, the visual style and the lettering | none, guest allowed |
| `render_media_widget` | Shows a saved draft again in the panel | none |
| `update_media_project` | Applies the changes made in the panel | none |
| `generate_media` | Starts the render after you confirm | charged, sign-in needed |
| `get_media_job` | Reports progress and returns the file link | none, read-only |

## Try asking

- "Cover art for my synthwave single "Midnight Static" by The Paper Moons, neon city at night"
- "An EP cover for a dreamy indie folk record called "Blue Hour", no text on the art"
- "A playlist cover for "Sunday Morning Jazz", warm film photo of a coffee table"

## Your data

Abracadabrax receives only what the tools carry: your request, the chosen settings and the ids of your drafts and renders. They are kept in your Abracadabrax account and passed to the model partner that renders the file. Nothing runs locally and the plugin reads nothing else from your conversation.

## Links

- Documentation: https://abracadabrax.app/mcp#album-cover-maker
- Privacy policy: https://abracadabrax.app/privacy
- Terms of service: https://abracadabrax.app/terms
- Help: https://abracadabrax.app/support
