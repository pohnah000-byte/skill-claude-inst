# Abracadabrax AI Background Music Generator

Describe a mood and get an original instrumental track to sit under a video, a podcast, an ad, a game, a livestream or a study session. Abracadabrax produces it with the credits of your own Abracadabrax account.

## How a request flows

1. You tell Claude the mood and what the music is for.
2. Claude saves an instrumental draft with the genre, the tempo, the length and the model, and shows its price in credits.
3. You adjust it, then ask Claude to produce it.
4. Abracadabrax renders the track and Claude hands you the link to the audio file.

## Good to know

- **Made by AI.** Vocals and music come from generative AI music models that Abracadabrax runs with its model partners. Drafts cost nothing; credits are only used when you confirm a render.
- **New tracks only.** Remixing, extending or splitting an existing recording needs an upload, which happens in the Abracadabrax music studio, not in this plugin.

## Connection

Endpoint: `https://abracadabrax.app/api/claude/background-music-generator/mcp` (remote MCP, Streamable HTTP).

Drafting works as a guest. The first time you produce something, Claude opens the Abracadabrax sign-in page (OAuth 2.1 with PKCE), where you can also create an account. On clients without MCP Apps, such as Claude Code, the same tools answer with text and links instead of the panel.

## Tool reference

| Tool | Purpose | Credits |
|---|---|---|
| `prepare_background_music` | Creates an instrumental draft from the mood, the use, the genre, the tempo and the length | none, guest allowed |
| `render_song_widget` | Shows a saved draft again in the panel | none |
| `update_song_project` | Applies the changes made in the panel | none |
| `generate_song` | Starts the render after you confirm | charged, sign-in needed |
| `get_song_job` | Reports progress and returns the audio link | none, read-only |

## Try asking

- "Calm lo-fi background music for studying, 2 minutes"
- "Upbeat corporate acoustic track for a product demo video, 60 seconds"
- "Dark ambient loop for a horror game menu screen"

## Your data

Abracadabrax receives only what the tools carry: your request, the chosen settings and the ids of your drafts and renders. They are kept in your Abracadabrax account and passed to the model partner that renders the file. Nothing runs locally and the plugin reads nothing else from your conversation.

## Links

- Documentation: https://abracadabrax.app/mcp#background-music-generator
- Privacy policy: https://abracadabrax.app/privacy
- Terms of service: https://abracadabrax.app/terms
- Help: https://abracadabrax.app/support
