---
name: qiaomu-mondo-poster-design
description: 一句话生成大师级海报、书籍封面、专辑封面和各类设计作品。无需懂PS、配色或艺术史，AI自动选择最佳风格（基于37位传奇设计师）。支持多平台多比例：公众号封面(21:9)、小红书配图(3:4)、文章配图(16:9)、书籍封面(9:16)、专辑封面(1:1)、电影海报(9:16)。包含风格对比、图生图转换功能。触发词："Mondo风格"、"书籍封面设计"、"专辑封面"、"海报设计"、"读书笔记配图"、"公众号封面"、"小红书配图"、"文章配图"。One-sentence generation of master-level posters, book covers, album covers and designs. 37 legendary designer styles with multi-platform aspect ratio support (21:9, 16:9, 3:4, 1:1, 9:16).
---

# Mondo Style Design Generator

Generate AI image prompts AND create actual designs in Mondo's distinctive alternative aesthetic - known for limited-edition screen-printed posters, book covers, and album art with bold colors, minimalist compositions, and symbolic storytelling.

**This skill can:**
- Generate detailed Mondo-style prompts for any subject
- Create actual images directly via AI Gateway API
- Design movie posters, book covers, album art, event posters
- Provide genre-specific and format-specific templates

## Core Mondo Aesthetic

Mondo posters are characterized by:

1. **Artistic Reinterpretation** - Not literal film scenes, but conceptual visual distillations
2. **Screen Print Aesthetics** - Limited color palettes (2-5 colors), flat color blocks, halftone textures
3. **Minimalist Symbolism** - Key props, silhouettes, negative space over character faces
4. **Bold Vintage Typography** - Hand-drawn lettering, condensed sans-serifs, Art Deco influences
5. **Retro Color Palettes** - High saturation, vintage duotones, bold contrasts (orange/teal, red/cream, etc.)

## Prompt Structure

When generating Mondo-style prompts, use this template:

```
[SUBJECT] in Mondo poster style, [COMPOSITION], [COLOR PALETTE],
screen print aesthetic, limited edition poster art, [KEY VISUAL ELEMENTS],
[TEXTURE/FINISH], minimalist design, vintage movie poster, [MOOD/TONE]
```

### Essential Components

**Style Anchors** (always include):
- "Mondo poster style" or "alternative movie poster"
- "screen print aesthetic" or "silkscreen print"
- "limited edition poster art"
- "vintage [decade] movie poster" (60s/70s/80s)

**Composition Techniques** (choose 1-2):
- Centered symmetrical composition
- Silhouette against [color] background
- Negative space storytelling
- Geometric framing (circles, triangles, arches)
- Layered depth with foreground/midground/background

**Color Strategy** (specify clearly):
- Limited palette: "3-color screen print: [color 1], [color 2], [color 3]"
- Duotone: "[warm color] and [cool color] duotone"
- Vintage scheme: "70s palette: burnt orange, mustard yellow, brown"
- High contrast: "bold [color] on [color] background"

**Visual Elements** (symbolic, not literal):
- Key prop or object (weapon, vehicle, iconic item)
- Silhouettes over detailed faces
- Geometric shapes hiding imagery
- Environmental mood (fog, rain, shadows)
- Symbolic animals or nature elements

**Texture & Finish** (adds authenticity):
- "halftone dot texture"
- "risograph printing effect"
- "paper texture grain"
- "slight misalignment between color layers"
- "vintage print imperfections"

## Artist-Specific Variations

For different Mondo artist styles, see [references/artist-styles.md](references/artist-styles.md).

**Quick reference:**
- **Tyler Stout style**: Dense character collages, intricate details, maximal composition
- **Olly Moss style**: Ultra-minimal, clever negative space, 1-2 colors
- **Martin Ansin style**: Art Deco influence, elegant line work, muted vintage tones

## Example Prompts (Optimized for Clean Design)

### Film Noir (Minimal)
```
Detective silhouette in fedora in Mondo poster style, vertical 9:16 portrait,
single centered figure, 3-color screen print: deep blue, cream, red accent,
clean minimalist composition, halftone texture, vintage 1940s aesthetic
```

### Sci-Fi (Minimalist Eye Window)
```
Astronaut helmet visor reflecting alien planet in Mondo poster style, vertical 9:16,
centered circular composition, 3-color screen print: orange, teal, black, single
focal element, negative space storytelling, clean retro 1970s sci-fi aesthetic
```

### Horror (Symbolic Architecture)
```
Victorian mansion single lit window in Mondo poster style, vertical 9:16 portrait,
centered Gothic silhouette, 3-color screen print: black, burgundy, cream, single
focal point, clean simple composition, vintage 1970s horror aesthetic
```

## Advanced Negative Space Techniques

Master-level Mondo designs use **figure-ground inversion** - where the negative space (area without ink) forms meaningful shapes. This creates dual-layered visual experiences with hidden surprises.

### Technique 1: Clever Visual Puns (Olly Moss Style)
**One element serves double duty:**
- Silhouette CONTAINS another scene within negative space
- Background shape IS the story element
- What's NOT shown tells as much as what IS shown

**Example structure:**
```
[Subject silhouette] in Mondo poster style, vertical 9:16, negative space WITHIN
silhouette reveals [hidden element], Olly Moss figure-ground inversion, 2-color
duotone: [color 1] and [color 2], clever dual imagery, what's missing tells the story
```

**Real-world inspiration:**
- Darth Vader silhouette with AT-ST battle scene in negative space
- Detective hat where negative space forms city skyline
- Knife blade reflecting villain's silhouette

### Technique 2: Scale Contrast Drama
**Tiny vs. Massive creates emotional impact:**
- Small human figure + giant object/creature
- Emphasizes isolation, wonder, or threat
- Uses 70% negative space for breathing room

**Example structure:**
```
Tiny [subject] with massive [object] looming in Mondo poster style, vertical 9:16,
dramatic scale contrast, [subject] occupies only bottom 20%, vast negative space
above, 2-3 color screen print, sense of [emotion: awe/isolation/danger]
```

### Technique 3: Single Shape Storytelling
**ONE iconic shape captures entire narrative:**
- No clutter, no multiple elements
- Let one perfect symbol do ALL the work
- 30% graphic, 30% text, 40% empty space (2024 best practice)

**Example structure:**
```
Single [iconic object/symbol] centered in Mondo poster style, vertical 9:16,
ONLY this one element, surrounded by vast negative space, 2-color print:
[color 1] on [color 2] background, Olly Moss ultra-minimal approach, one
image tells complete story
```

## Proven Success Patterns

Based on successful generations, these patterns consistently deliver exceptional results:

### Pattern 1: Single Focal Point (Minimalist Clean)
**Key principles:**
- ONE central element only (eye, object, silhouette)
- Vertical 9:16 format
- 2-3 colors maximum
- Negative space around focal point
- Clean, uncluttered, iconic

**Simplified structure:**
```
[Single element] in Mondo poster style, vertical 9:16, centered single focal point,
3-color screen print: [color 1], [color 2], [color 3], clean minimalist composition,
vintage [decade] aesthetic, simple and iconic
```

### Pattern 2: Atmospheric Single Subject (Clean Layered)
**Key principles:**
- ONE main subject with simple background
- Vertical 9:16 format
- 3-4 colors for atmosphere
- Subject in foreground, simple backdrop
- Clean composition, not cluttered

**Simplified structure:**
```
[Main subject] in Mondo poster style, vertical 9:16, single subject with [simple backdrop],
3-color screen print: [atmospheric colors], clean composition, vintage [decade] aesthetic,
focused and simple
```

## Workflow

1. **Identify the subject** - Film, book, album, band, event, or concept
2. **Choose symbolic element** - What single image captures the essence?
3. **Select composition pattern** - Minimalist symbolic OR layered atmospheric
4. **Select color palette** - 2-4 colors max, high contrast, vintage-inspired
5. **Add texture keywords** - Screen print, halftone, risograph effects
6. **Set the era** - Specify 60s/70s/80s for period-accurate aesthetics

## Tips for Best Results

**Do:**
- Specify exact color names and counts ("3-color: burnt orange, cream, navy")
- Use geometric composition terms (centered, symmetrical, negative space)
- Reference specific decades for vintage accuracy
- Emphasize symbolic over literal elements
- Include texture/printing process keywords

**Don't:**
- Use photorealistic or digital gradient terms
- Request complex facial details (use silhouettes instead)
- Mix too many styles (keep it focused on screen print aesthetic)
- Forget the vintage era context (60s-80s is key)
- Overlook negative space opportunities

## Advanced: Format-Specific Approaches

For detailed format and genre-specific templates:
- [references/genre-templates.md](references/genre-templates.md) - Horror, Sci-Fi, Western, Noir, etc.
- [references/composition-patterns.md](references/composition-patterns.md) - Layout strategies and visual hierarchy
- [references/book-covers.md](references/book-covers.md) - Book cover design patterns and best practices
- [references/artist-styles.md](references/artist-styles.md) - Tyler Stout, Olly Moss, Martin Ansin, etc.

## 🚀 Enhanced Features

### 1. Three-Column Style Comparison

Generate 3 different styles side-by-side to choose the best:

```bash
python3 scripts/generate_mondo_enhanced.py "Dune" movie --compare saul-bass,olly-moss,kilian-eng
```

**Perfect for:**
- Exploring different artistic approaches
- Client presentations
- Finding the best style for your subject

### 2. Image-to-Image Transformation

Transform existing posters into Mondo style:

```bash
python3 scripts/generate_mondo_enhanced.py "noir thriller" movie --input original_poster.jpg --style saul-bass
```

**Use cases:**
- Convert photographic posters to illustrated style
- Apply Mondo aesthetic to existing designs
- Reimagine classic posters

### 3. 37 Artist Styles

Now includes 37 artist styles across 7 categories:

**Belle Époque Pioneers:**
- `jules-cheret` - Bright joyful colors, dynamic feminine figures
- `toulouse-lautrec` - Flat blocks, Japanese influence, bold silhouettes
- `alphonse-mucha` - Art Nouveau flowing curves, ornate floral
- `steinlen` - Social realist, expressive lines, cat motifs

**Modernist Masters:**
- `saul-bass` - Minimalist geometric abstraction, visual metaphors
- `cassandre` - Cubist planes, dramatic perspective, Art Deco
- `milton-glaser` - Psychedelic pop art, innovative typography
- `josef-muller-brockmann` - Swiss grid, mathematical precision
- `paul-rand` - Playful geometry, clever visual puns

**Film Legends:**
- `drew-struzan` - Painted realism, epic cinematic, nostalgic glow
- `olly-moss` - Ultra-minimal negative space, hidden imagery
- `tyler-stout` - Maximalist collages, intricate details
- `martin-ansin` - Art Deco elegance, refined vintage
- `laurent-durieux` - Visual puns, mysterious atmospheric

**Contemporary:**
- `kilian-eng` - Geometric futurism, precise technical lines
- `dan-mccarthy` - Ultra-flat geometric abstraction
- `jock` - Gritty expressive brushwork, dynamic action
- `shepard-fairey` - Propaganda style, halftone, political
- `jay-ryan` - Folksy handmade, warm textured simple
- `paula-scher` - Typographic maximalism, layered text

**Book Cover Designers:**
- `chip-kidd` - Conceptual, single symbolic object, bold typography
- `peter-mendelsund` - Abstract literary, deconstructed typography
- `coralie-bickford-smith` - Penguin Clothbound Classics, decorative patterns
- `david-pearson` - Bold typographic-only, text as visual element
- `wang-zhi-hong` - East Asian design, restrained elegant typography
- `jan-tschichold` - Modernist Penguin, Swiss precision grid

**Album Cover Designers:**
- `reid-miles` - Blue Note Records, bold asymmetric typography
- `david-stone-martin` - Verve Records, gestural ink brushstroke
- `peter-saville` - Factory Records, extreme minimalism

**Chinese Aesthetic Styles:**
- `wenyi` - 文艺风, soft muted tones, poetic atmosphere
- `guochao` - 国潮风, traditional motifs reimagined modern
- `rixi` - 日系, warm film grain, pastel minimal
- `hanxi` - 韩系, clean bright pastel, dreamy ethereal

**Generic Styles:**
- `minimal` - Centered single focal point, 2-3 colors
- `atmospheric` - Strong focal element with atmospheric background
- `negative-space` - Figure-ground inversion, hidden elements

**View all styles:**
```bash
python3 scripts/generate_mondo_enhanced.py --list-styles
```

### 4. Smart Color Suggestions

AI suggests complementary colors, but you can override:

```bash
# Let AI suggest colors
python3 scripts/generate_mondo_enhanced.py "Jazz Festival" event --style jules-cheret

# Or specify your own
python3 scripts/generate_mondo_enhanced.py "Jazz Festival" event --style jules-cheret --colors "vibrant yellow, deep blue, red"
```

## Interactive Usage with Claude

When using this skill through Claude Code, I can guide you interactively:

**I'll ask you simple questions like:**
1. "What's your subject?" (movie/book/album title)
2. "Which style feels right?" (show 3-4 options with previews)
3. "Any color preferences?" (or let AI suggest)
4. "Want to see comparisons?" (generate 3 versions)

This makes it easy even if you're unfamiliar with Mondo aesthetics!

---

## Direct Image Generation

This skill can generate actual images directly using the bundled scripts:

### Enhanced Version (Recommended)

**Full feature set:** comparisons, image-to-image, 37 artist styles

```bash
python3 scripts/generate_mondo_enhanced.py "subject" "type" [options]
```

**Enhanced Parameters:**
- `subject`: What to design
- `type`: Design type - "movie", "book", "album", "event"
- `--style`: Artist style (37 options, see --list-styles)
- `--provider`: Image generation provider (see below)
- `--compare`: Generate 3-style comparison (e.g., "saul-bass,olly-moss,jock")
- `--input`: Input image for image-to-image transformation (tuzi/pipellm only)
- `--colors`: Color preferences (e.g., "orange, teal, black")
- `--aspect-ratio`: Aspect ratio (default: 9:16)
- `--output`: Custom output path
- `--no-generate`: Only show prompt

**Image Providers (`--provider`):**

| Provider | Model | Features | Env Var |
|----------|-------|----------|---------|
| `tuzi` (default) | Gemini 3.1 Flash Image 2K | Fast, supports image-to-image | `TUZI_API_KEY` |
| `pipellm` | Gemini 3 Pro Image | High quality, supports image-to-image | `PIPELLM_API_KEY` |
| `z-image` | 通义万相 Z-Image-Turbo | Chinese art styles, LoRA support | `MODELSCOPE_API_KEY` |
| `jimeng` | 即梦 jimeng-image-4.5 | Chinese style, free quota (66/day) | `JIMENG_SESSION_ID` |

**Fallback chain:** tuzi→pipellm, z-image→jimeng (stays within same provider family)

**Enhanced Examples:**

3-style comparison:
```bash
python3 scripts/generate_mondo_enhanced.py "Akira" movie --compare kilian-eng,saul-bass,jock
```

Image-to-image with specific artist:
```bash
python3 scripts/generate_mondo_enhanced.py "cyberpunk noir" movie --input poster.jpg --style saul-bass
```

With color preferences:
```bash
python3 scripts/generate_mondo_enhanced.py "Jazz Night" event --style milton-glaser --colors "psychedelic orange, purple, yellow"
```

Use Z-Image (通义万相) provider:
```bash
python3 scripts/generate_mondo_enhanced.py "Akira" movie --style kilian-eng --provider z-image
```

Use Jimeng (即梦) provider:
```bash
python3 scripts/generate_mondo_enhanced.py "Chinese ink landscape" book --style wang-zhi-hong --provider jimeng
```

List all 37 artist styles:
```bash
python3 scripts/generate_mondo_enhanced.py --list-styles
```

### Manual Generation

If you prefer to generate prompts manually and use other image generation tools:

1. Use this skill to generate the Mondo-style prompt
2. Pass the prompt to:
   - `/generate-image` - AI Gateway API (recommended)
   - `/ai-image-generation` - FLUX, Gemini, and other models
   - `/qiaomu-image-generator` - For article/content illustrations

**Recommended settings:**
- Model: `google/gemini-3.1-flash-image-preview` (best quality/speed balance)
- Resolution: 2K or higher for print quality
- Format: PNG with transparency support

## 🚀 Feishu / 飞书图片自动投递

**⚠️ 强制规则：在飞书/OpenClaw 对话中生成图片时，必须使用 `--feishu-to` 参数，让脚本自动上传并发送图片到飞书聊天！**

### 使用方式（一条命令搞定）

生成脚本已内置飞书图片上传和发送功能，只需在生成命令中加 `--feishu-to` 参数：

```bash
# Enhanced 版本（推荐）
python3 scripts/generate_mondo_enhanced.py "Blade Runner" movie --style saul-bass --feishu-to <chat_id_or_open_id>

# Basic 版本
python3 scripts/generate_mondo.py "Akira" movie --feishu-to <chat_id_or_open_id>
```

**参数说明**：
- `--feishu-to`：目标用户 `open_id`（`ou_xxx`）或群聊 `chat_id`（`oc_xxx`），从当前对话上下文获取

### 使用示例

```bash
# 发送到用户私聊
python3 scripts/generate_mondo_enhanced.py "Jazz Night" event --style milton-glaser \
  --feishu-to ou_b3101397cd3c2bdea667b26f6f169afe

# 发送到群聊
python3 scripts/generate_mondo_enhanced.py "Dune" movie --style kilian-eng \
  --feishu-to oc_0bdbbb25dd1951b9373708f43b159cef
```

### 注意事项

- 需要环境变量 `FEISHU_APP_ID` 和 `FEISHU_APP_SECRET`（launchd plist 中已配置）
- 如果环境变量未设置，会跳过飞书发送，只保存到本地
- 支持格式：JPEG, PNG, WEBP, GIF, BMP, TIFF
- 飞书图片大小限制：10MB
