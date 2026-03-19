# Qiaomu Mondo Poster Design

English | [简体中文](README.md)

> **One Sentence, Master-Level Design** - No Photoshop, no color theory, no art history? No problem. Just describe what you want in one sentence, and AI automatically selects the perfect artistic style to generate professional-grade posters, covers, and designs.

**Powered by Google Gemini 3 Pro Image** 🎨

## 🚀 Features

✨ **37 Artist Styles** - From Saul Bass to Toulouse-Lautrec, Chip Kidd to Reid Miles
🤖 **AI Auto-Style Selection** - Perfect match for any subject
📱 **Beginner-Friendly** - No design knowledge needed
🎨 **Versatile Formats** - Posters, book covers, album covers, social media graphics
🖼️ **Smart Features** - Comparison mode, image-to-image transformation

## Installation

```bash
npx skills add joeseesun/qiaomu-mondo-poster-design
```

## 📸 Gallery: Real Examples

### IMDB Top 10 Movie Posters

Created with various Mondo techniques:

| The Shawshank Redemption | The Godfather | The Dark Knight |
|:---:|:---:|:---:|
| ![](examples/imdb-01-shawshank.png) | ![](examples/imdb-02-godfather.png) | ![](examples/imdb-03-dark-knight.png) |
| *Negative space - Bird in bars* | *Minimalism - Puppet strings* | *Visual pun - Joker in bat* |

| The Godfather Part II | 12 Angry Men | Return of the King |
|:---:|:---:|:---:|
| ![](examples/imdb-04-godfather-2.png) | ![](examples/imdb-05-12-angry-men.png) | ![](examples/imdb-06-lotr-return.png) |
| *Dual timeline layering* | *12 hands & knife* | *Crown in flames* |

| Schindler's List | Fellowship of the Ring | Pulp Fiction |
|:---:|:---:|:---:|
| ![](examples/imdb-07-schindlers-list.png) | ![](examples/imdb-08-lotr-fellowship.png) | ![](examples/imdb-09-pulp-fiction.png) |
| *Candle of hope* | *Map in ring* | *Briefcase mystery* |

### Master Technique: Figure-Ground Inversion

<p align="center">
  <img src="examples/example-negative-space.png" width="400" alt="Negative Space Example">
  <br>
  <b>Flirting Scholar (唐伯虎点秋香)</b><br>
  <i>Female profile hidden in fan's negative space - Olly Moss technique</i>
</p>

## Quick Start

### Interactive with Claude Code

Simply say:
```
"Create Mondo poster for Blade Runner, compare styles"
"Design 1984 book cover in Saul Bass style"
"Jazz festival poster with vibrant colors"
```

### Command Line

```bash
# Single generation with style
python3 ~/.claude/skills/qiaomu-mondo-poster-design/scripts/generate_mondo_enhanced.py "Blade Runner" movie --style saul-bass

# 3-style comparison
python3 ~/.claude/skills/qiaomu-mondo-poster-design/scripts/generate_mondo_enhanced.py "Akira" movie --compare kilian-eng,saul-bass,jock

# Custom colors
python3 ~/.claude/skills/qiaomu-mondo-poster-design/scripts/generate_mondo_enhanced.py "Jazz Night" event --style milton-glaser --colors "orange, purple, yellow"

# Image-to-image
python3 ~/.claude/skills/qiaomu-mondo-poster-design/scripts/generate_mondo_enhanced.py "noir" movie --input poster.jpg --style saul-bass

# List all styles
python3 ~/.claude/skills/qiaomu-mondo-poster-design/scripts/generate_mondo_enhanced.py --list-styles
```

## 🎨 37 Artist Styles

**Belle Époque (1870s-1900s)**
- jules-cheret, toulouse-lautrec, alphonse-mucha, steinlen

**Modernist (1920s-1960s)**
- saul-bass, cassandre, milton-glaser, josef-muller-brockmann, paul-rand

**Film Legends**
- drew-struzan, olly-moss, tyler-stout, martin-ansin, laurent-durieux

**Contemporary**
- kilian-eng, dan-mccarthy, jock, shepard-fairey, jay-ryan, paula-scher

**Book Cover Designers**
- chip-kidd, peter-mendelsund, coralie-bickford-smith, david-pearson, wang-zhi-hong, jan-tschichold

**Album Cover Designers**
- reid-miles, david-stone-martin, peter-saville

**Chinese Aesthetic Styles**
- wenyi (文艺风), guochao (国潮风), rixi (日系), hanxi (韩系)

**Generic Styles**
- minimal, atmospheric, negative-space

[See full artist guide →](references/artist-styles.md)

## ✨ Features

### 3-Column Comparison
Compare styles side-by-side
```bash
--compare saul-bass,olly-moss,jock
```

### Image-to-Image
Transform existing posters
```bash
--input poster.jpg
```

### Smart Colors
AI suggests or use your own
```bash
--colors "red, blue, cream"
```

## 📋 Mondo Aesthetic

1. **Artistic Reinterpretation** - Conceptual, not literal
2. **Screen Print** - 2-5 colors, flat blocks, halftone
3. **Minimalist Symbolism** - Props over faces
4. **Bold Typography** - Hand-drawn, Art Deco
5. **Retro Colors** - High saturation, bold contrasts

## 💻 Requirements

- Python 3.7+
- `Pillow` (for comparison mode)
- API Key for one of: `TUZI_API_KEY`, `PIPELLM_API_KEY`, `MODELSCOPE_API_KEY`, or `JIMENG_SESSION_ID`

```bash
pip install -r requirements.txt
```

## 📚 Documentation

- [SKILL.md](SKILL.md) - Full guide
- [Artist Styles](references/artist-styles.md) - 37 artists explained
- [Genre Templates](references/genre-templates.md) - Horror, sci-fi, etc.
- [Composition Patterns](references/composition-patterns.md) - Layout strategies

## 🤝 Contributing

Pull requests welcome! Share your Mondo creations.

## 📄 License

MIT

## 📱 Follow

- **X**: [@vista8](https://x.com/vista8)
- **WeChat**: 向阳乔木推荐看

<p align="center">
  <img src="https://github.com/joeseesun/terminal-boost/raw/main/assets/wechat-qr.jpg?raw=true" alt="WeChat QR" width="300">
</p>

---

**Powered by [Claude Code](https://claude.com/claude-code) + Google Gemini 3 Pro Image** 🤖✨
