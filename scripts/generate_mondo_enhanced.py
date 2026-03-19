#!/usr/bin/env python3
"""
Mondo Style Design Generator - Enhanced Version
Features: Claude-generated prompts, 3-column comparison, image-to-image, 37 artist styles
"""

import os
import sys
import argparse
import json
import re
import urllib.request
import urllib.error
import urllib.parse
import mimetypes
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# API Configuration - PipeLLM Gemini
PIPELLM_BASE_URL = 'https://api.pipellm.ai'
DEFAULT_IMAGE_MODEL = 'gemini-3-pro-image-preview'   # 高质量图片模型

# API Configuration - Tu-zi.com Gemini
TUZI_BASE_URL = 'https://api.tu-zi.com'
TUZI_IMAGE_MODEL = 'gemini-3.1-flash-image-preview-2k'

# API Configuration - ModelScope Z-Image
ZIMAGE_BASE_URL = 'https://api-inference.modelscope.cn/'
ZIMAGE_DEFAULT_MODEL = 'Tongyi-MAI/Z-Image-Turbo'
ZIMAGE_POLL_INTERVAL = 5  # seconds

# API Configuration - Jimeng (local Docker)
JIMENG_BASE_URL = 'http://localhost:8000'
JIMENG_DEFAULT_MODEL = 'jimeng-image-4.5'

# Aspect ratio → pixel size mapping (for providers that need explicit dimensions)
ASPECT_RATIO_SIZES = {
    "1:1":  (1024, 1024),
    "16:9": (1280, 720),
    "9:16": (720, 1280),
    "21:9": (1680, 720),
    "3:4":  (768, 1024),
    "4:3":  (1024, 768),
    "2:3":  (682, 1024),
    "3:2":  (1024, 682),
}

# 30+ Design Styles: Poster Artists + Book Cover + Album Cover + Social Media
ARTIST_STYLES = {
    "auto": "let AI choose best style",
    # === Poster Artists (20) ===
    "saul-bass": "Saul Bass minimalist geometric abstraction, 2-3 colors, visual metaphor",
    "olly-moss": "Olly Moss ultra-minimal negative space, clever hidden imagery, 2 colors",
    "tyler-stout": "Tyler Stout maximalist character collage, intricate line work, organized chaos",
    "martin-ansin": "Martin Ansin Art Deco elegance, refined vintage palette, sophisticated",
    "toulouse-lautrec": "Toulouse-Lautrec flat color blocks, Japanese influence, bold silhouettes",
    "alphonse-mucha": "Alphonse Mucha Art Nouveau flowing curves, ornate floral, decorative borders",
    "jules-cheret": "Jules Chéret Belle Époque bright joyful colors, dynamic feminine figures",
    "cassandre": "Cassandre modernist geometry, Cubist planes, dramatic perspective, Art Deco",
    "milton-glaser": "Milton Glaser psychedelic pop art, innovative typography, vibrant colors",
    "drew-struzan": "Drew Struzan painted realism, epic cinematic, warm nostalgic glow",
    "kilian-eng": "Kilian Eng geometric futurism, precise technical lines, cool sci-fi palette",
    "laurent-durieux": "Laurent Durieux visual puns, hidden imagery, mysterious atmospheric",
    "jay-ryan": "Jay Ryan folksy handmade, single focal image, warm textured simple",
    "dan-mccarthy": "Dan McCarthy ultra-flat geometric abstraction, 2-3 solid colors, no gradients",
    "jock": "Jock gritty expressive brushwork, dynamic action, high contrast, raw energy",
    "shepard-fairey": "Shepard Fairey propaganda style, red black cream, halftone, political",
    "steinlen": "Steinlen social realist, expressive lines, cat motifs, high contrast",
    "josef-muller-brockmann": "Josef Müller-Brockmann Swiss grid, Helvetica, mathematical precision",
    "paul-rand": "Paul Rand playful geometry, clever visual puns, witty intelligent",
    "paula-scher": "Paula Scher typographic maximalism, layered text, vibrant expressive letters",
    # === Book Cover Designers (6) ===
    "chip-kidd": "Chip Kidd conceptual book cover, single symbolic object, bold typography, photographic metaphor, witty visual pun, Random House literary aesthetic",
    "peter-mendelsund": "Peter Mendelsund abstract literary cover, deconstructed typography, minimal symbolic elements, intellectual negative space, Knopf literary elegance",
    "coralie-bickford-smith": "Coralie Bickford-Smith Penguin Clothbound Classics, repeating decorative patterns, Art Nouveau foil stamping, jewel-tone palette, ornamental borders, fabric texture",
    "david-pearson": "David Pearson Penguin Great Ideas, bold typographic-only cover, text as visual element, minimal color, intellectual and clean, type-driven design",
    "wang-zhi-hong": "Wang Zhi-Hong East Asian book design, restrained elegant typography, confident negative space, subtle texture, balanced asymmetry, literary sophistication",
    "jan-tschichold": "Jan Tschichold modernist Penguin typography, Swiss precision grid, clean serif fonts, understated elegance, timeless typographic hierarchy",
    # === Album Cover Designers (3) ===
    "reid-miles": "Reid Miles Blue Note Records, bold asymmetric typography, high contrast black and single accent color, jazz photography silhouette, dramatic negative space, vintage vinyl",
    "david-stone-martin": "David Stone Martin Verve Records, single gestural ink brushstroke, minimalist line drawing on cream, fluid calligraphic lines, maximum negative space, improvisational energy",
    "peter-saville": "Peter Saville Factory Records extreme minimalism, single abstract form in vast empty space, monochromatic, no text on cover, conceptual and mysterious, intellectual restraint",
    # === Social Media / Chinese Aesthetic Styles (4) ===
    "wenyi": "文艺风 literary artistic style, soft muted tones, generous white space, delicate serif typography, watercolor texture, poetic atmosphere, refined and contemplative, editorial book review aesthetic",
    "guochao": "国潮风 Chinese contemporary trend, traditional Chinese motifs reimagined modern, bold red and gold palette, ink wash meets graphic design, cultural symbols with street art energy, 新中式",
    "rixi": "日系 Japanese aesthetic, warm film grain, soft natural light, pastel muted palette, clean minimal layout, hand-drawn accents, cozy atmosphere, wabi-sabi imperfection, zakka lifestyle",
    "hanxi": "韩系 Korean aesthetic, clean bright pastel, soft gradient backgrounds, modern sans-serif typography, dreamy ethereal quality, sophisticated minimal, Instagram-worthy composition",
    # === Generic Styles ===
    "minimal": "minimalist, centered single focal point, 2-3 color palette, clean simple",
    "atmospheric": "single strong focal element with atmospheric background, 3-4 colors",
    "negative-space": "figure-ground inversion, negative space reveals hidden element, 2 colors"
}

def get_genai_client():
    """创建 PipeLLM google-genai 客户端"""
    from google import genai
    api_key = os.getenv('PIPELLM_API_KEY')
    if not api_key:
        print("Error: PIPELLM_API_KEY environment variable is required.")
        print("Please set: export PIPELLM_API_KEY=your_key")
        sys.exit(1)
    return genai.Client(
        api_key=api_key,
        http_options={"base_url": PIPELLM_BASE_URL}
    )


def get_format_description(aspect_ratio):
    """Get format description text matching the aspect ratio"""
    ratio_descriptions = {
        "9:16": "vertical 9:16 portrait format, strong central vertical composition",
        "16:9": "horizontal 16:9 landscape format, wide cinematic composition",
        "21:9": "ultra-wide 21:9 panoramic banner format, horizontal landscape",
        "3:4": "vertical 3:4 portrait format, classic poster proportions",
        "4:3": "horizontal 4:3 landscape format",
        "2:3": "vertical 2:3 portrait format, tall elegant proportions",
        "3:2": "horizontal 3:2 landscape format, classic photography proportions",
        "1:1": "square 1:1 format",
    }
    return ratio_descriptions.get(aspect_ratio, f"{aspect_ratio} format")

def generate_prompt(subject, design_type, style="auto", color_hint="", aspect_ratio="9:16"):
    """
    Generate Mondo-style prompt from subject.
    When called by Claude, pass a rich pre-crafted prompt as subject for best results.

    Args:
        subject: The subject matter (or a fully-crafted Mondo prompt from Claude)
        design_type: Type of design ("movie", "book", "album", "event")
        style: Visual style (artist name or preset)
        color_hint: Optional color preferences from user
        aspect_ratio: Aspect ratio for the image

    Returns:
        Generated prompt string
    """
    format_desc = get_format_description(aspect_ratio)

    # Standard template path
    base_elements = "Mondo poster style, screen print aesthetic, limited edition poster art"

    # Get style modifier
    style_desc = ARTIST_STYLES.get(style, ARTIST_STYLES['minimal'])

    # Build prompt based on type
    if design_type == "movie":
        prompt = f"{subject} in {base_elements}, {style_desc}, {format_desc}, clean focused composition, vintage poster aesthetic"
    elif design_type == "book":
        prompt = f"{subject} book cover in {base_elements}, {style_desc}, {format_desc}, clean typography, literary design"
    elif design_type == "album":
        prompt = f"{subject} album cover in {base_elements}, {style_desc}, square 1:1 format, vintage vinyl aesthetic"
    elif design_type == "event":
        prompt = f"{subject} event poster in {base_elements}, {style_desc}, {format_desc}, bold memorable design"
    else:
        prompt = f"{subject} in {base_elements}, {style_desc}, vintage print aesthetic"

    # Add color hint if provided
    if color_hint:
        prompt += f", color palette: {color_hint}"

    return prompt

def get_default_output_path():
    """Generate default output path in knowledge base"""
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    default_dir = os.getenv('MONDO_OUTPUT_DIR', os.path.expanduser("~/乔木新知识库/60-69 素材/61 AI图片/mondo-designs"))
    os.makedirs(default_dir, exist_ok=True)
    return f"{default_dir}/mondo-{timestamp}.png"


def resolve_size(aspect_ratio):
    """Convert aspect ratio string to (width, height) tuple"""
    if aspect_ratio in ASPECT_RATIO_SIZES:
        return ASPECT_RATIO_SIZES[aspect_ratio]
    # Try to parse custom ratio like "5:4"
    parts = aspect_ratio.split(':')
    if len(parts) == 2:
        try:
            w, h = int(parts[0]), int(parts[1])
            # Scale to ~1024px on the longer side
            scale = 1024 / max(w, h)
            return (int(w * scale), int(h * scale))
        except ValueError:
            pass
    return (1024, 1024)  # fallback


def _urllib_request(url, data=None, headers=None, method='GET', timeout=30):
    """Helper: make HTTP request using urllib, return (status_code, body_bytes)"""
    headers = headers or {}
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def generate_image_zimage(prompt, output_path=None, aspect_ratio="9:16"):
    """使用通义万相 Z-Image-Turbo（ModelScope API）生成图片"""
    api_key = os.getenv('MODELSCOPE_API_KEY')
    if not api_key:
        print("⚠ MODELSCOPE_API_KEY not set, skipping z-image provider")
        return None

    width, height = resolve_size(aspect_ratio)
    size_str = f"{width}x{height}"

    print(f"🎨 Generating with Z-Image-Turbo (ModelScope)")
    print(f"📐 Size: {size_str} (from {aspect_ratio})")
    print(f"✍️  Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"✍️  Prompt: {prompt}")
    print("⏳ Please wait...\n")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-ModelScope-Async-Mode": "true",
    }
    payload = json.dumps({
        "model": ZIMAGE_DEFAULT_MODEL,
        "prompt": prompt,
        "size": size_str
    }, ensure_ascii=False).encode('utf-8')

    # Submit task with retry for 429
    task_id = None
    for attempt in range(3):
        try:
            status_code, body = _urllib_request(
                f"{ZIMAGE_BASE_URL}v1/images/generations",
                data=payload, headers=headers, method='POST', timeout=30
            )
            if status_code == 429:
                wait = 2 ** attempt * 10
                print(f"⚠️  Rate limit (429), waiting {wait}s...")
                time.sleep(wait)
                continue
            if status_code >= 400:
                print(f"⚠ HTTP {status_code}: {body[:200]}")
                raise Exception(f"HTTP {status_code}")
            resp_data = json.loads(body)
            if "task_id" in resp_data:
                task_id = resp_data["task_id"]
                print(f"✅ Task submitted: {task_id}")
                break
        except Exception as e:
            print(f"⚠ Attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(5)

    if task_id is None:
        print("❌ Z-Image task submission failed")
        return None

    # Poll for completion
    poll_headers = {
        "Authorization": f"Bearer {api_key}",
        "X-ModelScope-Task-Type": "image_generation",
    }
    max_polls = 120  # 10 minutes max (120 * 5s)
    for poll_count in range(max_polls):
        try:
            status_code, body = _urllib_request(
                f"{ZIMAGE_BASE_URL}v1/tasks/{task_id}",
                headers=poll_headers, timeout=30
            )
            if status_code >= 400:
                print(f"❌ Poll HTTP {status_code}")
                return None
            try:
                data = json.loads(body)
            except (json.JSONDecodeError, TypeError):
                print(f"❌ Invalid JSON response from Z-Image API")
                return None
            status = data.get("task_status")
            if not status:
                print(f"❌ No task_status in response: {str(data)[:200]}")
                return None

            if status == "SUCCEED":
                images = data.get("output_images", [])
                if not images:
                    print("❌ No output images in response")
                    return None
                image_url = images[0]
                print(f"🖼️  Downloading from: {image_url}")

                if not output_path:
                    output_path = get_default_output_path()
                os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
                try:
                    urllib.request.urlretrieve(image_url, output_path)
                except Exception as e:
                    print(f"❌ Download failed: {e}")
                    return None
                print(f"✅ Saved to {output_path}")
                return output_path

            elif status == "FAILED":
                print(f"❌ Z-Image generation failed: {data.get('error', 'Unknown')}")
                return None
            else:
                print(f"   Status: {status}")
                time.sleep(ZIMAGE_POLL_INTERVAL)
        except Exception as e:
            print(f"❌ Polling error: {e}")
            return None

    print(f"❌ Z-Image generation timed out after {max_polls * ZIMAGE_POLL_INTERVAL}s")
    return None


def generate_image_jimeng(prompt, output_path=None, aspect_ratio="9:16"):
    """使用即梦 (Jimeng) 本地 Docker API 生成图片"""
    session_id = os.getenv('JIMENG_SESSION_ID')
    if not session_id:
        print("⚠ JIMENG_SESSION_ID not set, skipping jimeng")
        return None

    width, height = resolve_size(aspect_ratio)

    print(f"🎨 Generating with Jimeng (local Docker)")
    print(f"📐 Size: {width}x{height} (from {aspect_ratio})")
    print(f"✍️  Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"✍️  Prompt: {prompt}")
    print("⏳ Please wait...\n")

    payload = json.dumps({
        "model": JIMENG_DEFAULT_MODEL,
        "prompt": prompt,
        "n": 1,
        "width": width,
        "height": height
    }).encode('utf-8')

    try:
        status_code, body = _urllib_request(
            f"{JIMENG_BASE_URL}/v1/images/generations",
            data=payload, method='POST', timeout=120,
            headers={
                "Authorization": f"Bearer {session_id}",
                "Content-Type": "application/json"
            }
        )
        if status_code >= 400:
            print(f"❌ Jimeng HTTP {status_code}: {body[:200]}")
            return None

        data = json.loads(body)
        images = data.get('data', [])
        if not images:
            print("❌ No images in Jimeng response")
            return None

        image_url = images[0].get('url')
        if not image_url:
            print("❌ No URL in Jimeng image data")
            return None

        # Download
        print(f"🖼️  Downloading from Jimeng...")
        if not output_path:
            output_path = get_default_output_path()
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        urllib.request.urlretrieve(image_url, output_path)
        print(f"✅ Saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Jimeng error: {e}")
        return None


def generate_image_tuzi(prompt, output_path=None, aspect_ratio="9:16", input_image=None):
    """使用 tu-zi.com Gemini Flash Image API 生成图片"""
    urlreq = urllib.request
    jsonlib = json

    api_key = os.getenv('TUZI_API_KEY')
    if not api_key:
        print("⚠ TUZI_API_KEY not set, skipping tuzi provider")
        return None

    model = TUZI_IMAGE_MODEL
    print(f"🎨 Generating with {model} (tu-zi.com)")
    print(f"✍️  Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"✍️  Prompt: {prompt}")
    print("⏳ Please wait...\n")

    parts = [{"text": prompt}]

    # 图生图：添加输入图片
    if input_image and os.path.exists(input_image):
        try:
            import base64
            with open(input_image, 'rb') as f:
                img_bytes = f.read()
            # 检测 mime type
            mime_type = "image/png" if input_image.lower().endswith('.png') else "image/jpeg"
            img_b64 = base64.b64encode(img_bytes).decode()
            parts.append({
                "inline_data": {
                    "mime_type": mime_type,
                    "data": img_b64
                }
            })
            print(f"📷 Using input image: {input_image}")
        except Exception as e:
            print(f"⚠ Could not load input image: {e}, ignoring")

    payload = jsonlib.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE", "TEXT"],
            "imageConfig": {"aspectRatio": aspect_ratio}
        }
    }).encode('utf-8')

    url = f"{TUZI_BASE_URL}/v1beta/models/{model}:generateContent"
    req = urlreq.Request(url, data=payload, headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    })

    try:
        with urlreq.urlopen(req, timeout=120) as resp:
            data = jsonlib.loads(resp.read().decode())

        # 解析响应：返回格式是 markdown 图片链接
        parts_resp = data.get('candidates', [{}])[0].get('content', {}).get('parts', [])
        image_url = None
        for part in parts_resp:
            text = part.get('text', '')
            match = re.search(r'!\[.*?\]\((https?://[^\)]+)\)', text)
            if match:
                image_url = match.group(1)
                break

        if not image_url:
            print("❌ No image URL in response")
            print("Raw response:", jsonlib.dumps(data, ensure_ascii=False)[:500])
            return None

        # 下载图片
        if not output_path:
            output_path = get_default_output_path()

        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        urlreq.urlretrieve(image_url, output_path)
        print(f"✅ Saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def generate_image_pipellm(prompt, output_path=None, model=DEFAULT_IMAGE_MODEL, aspect_ratio="9:16", input_image=None):
    """使用 PipeLLM Gemini API 生成图片"""
    client = get_genai_client()

    print(f"🎨 Generating with {model} (PipeLLM)")
    print(f"✍️  Prompt: {prompt[:80]}..." if len(prompt) > 80 else f"✍️  Prompt: {prompt}")
    print("⏳ Please wait...\n")

    contents = [prompt]

    # 图生图：把输入图片也传给模型
    if input_image and os.path.exists(input_image):
        try:
            from google.genai import types
            with open(input_image, 'rb') as f:
                img_bytes = f.read()
            contents = [
                types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
                f"Transform this image in Mondo poster style: {prompt}"
            ]
            print(f"📷 Using input image: {input_image}")
        except Exception as e:
            print(f"⚠ Could not load input image: {e}, ignoring")

    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
        )

        # 提取图片 part
        image_part = None
        for part in response.parts:
            if part.inline_data is not None:
                image_part = part
                break

        if image_part is None:
            print("❌ No image data in response")
            return None

        if not output_path:
            output_path = get_default_output_path()
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        img = image_part.as_image()
        img.save(output_path)
        print(f"✅ Saved to {output_path}")
        return output_path

    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def generate_image(prompt, output_path=None, model=DEFAULT_IMAGE_MODEL, aspect_ratio="9:16", input_image=None, provider="tuzi"):
    """
    生成图片，支持 4 个 provider:
    - tuzi (默认): Gemini 2.5 Flash Image via tu-zi.com
    - pipellm: Gemini 3 Pro Image via PipeLLM
    - z-image: 通义万相 Z-Image-Turbo via ModelScope
    - jimeng: 即梦 via 本地 Docker API

    tuzi/pipellm 支持图生图 (input_image)，z-image/jimeng 仅支持文生图。
    失败时自动降级：tuzi→pipellm, z-image→jimeng（不跨系列降级）
    """
    if provider == "tuzi":
        result = generate_image_tuzi(prompt, output_path, aspect_ratio, input_image)
        if result is not None:
            return result
        print("\n⚠️  Tu-zi.com failed, auto-fallback to PipeLLM...")
        print("=" * 50)
        return generate_image_pipellm(prompt, output_path, model, aspect_ratio, input_image)

    elif provider == "pipellm":
        return generate_image_pipellm(prompt, output_path, model, aspect_ratio, input_image)

    elif provider == "z-image":
        result = generate_image_zimage(prompt, output_path, aspect_ratio)
        if result is not None:
            return result
        print("\n⚠️  Z-Image failed, auto-fallback to Jimeng...")
        print("=" * 50)
        return generate_image_jimeng(prompt, output_path, aspect_ratio)

    elif provider == "jimeng":
        return generate_image_jimeng(prompt, output_path, aspect_ratio)

    else:
        print(f"❌ Unknown provider: {provider}")
        return None

def feishu_send_image(image_path, target):
    """Upload image to Feishu and send as image message. Returns True on success."""
    app_id = os.getenv('FEISHU_APP_ID')
    app_secret = os.getenv('FEISHU_APP_SECRET')
    if not app_id or not app_secret:
        print("⚠ FEISHU_APP_ID/SECRET not set, skipping Feishu send")
        return False

    base = 'https://open.feishu.cn/open-apis'

    # 1. Get tenant access token
    try:
        tok_data = json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode()
        tok_req = urllib.request.Request(
            f'{base}/auth/v3/tenant_access_token/internal',
            data=tok_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(tok_req, timeout=15) as resp:
            tok_r = json.loads(resp.read())
        token = tok_r.get('tenant_access_token')
        if not token:
            print(f"⚠ Feishu token error: {tok_r}")
            return False
    except Exception as e:
        print(f"⚠ Feishu auth failed: {e}")
        return False

    # 2. Upload image
    try:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        boundary = f'----FsBoundary{int(time.time() * 1000)}'
        filename = os.path.basename(image_path)
        mime = mimetypes.guess_type(filename)[0] or 'image/png'
        body = (
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="image_type"\r\n\r\nmessage\r\n'
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="image"; filename="{filename}"\r\n'
            f'Content-Type: {mime}\r\n\r\n'
        ).encode() + img_data + f'\r\n--{boundary}--\r\n'.encode()
        up_req = urllib.request.Request(
            f'{base}/im/v1/images', data=body, method='POST',
            headers={'Content-Type': f'multipart/form-data; boundary={boundary}',
                     'Authorization': f'Bearer {token}'})
        with urllib.request.urlopen(up_req, timeout=60) as resp:
            up_r = json.loads(resp.read())
        if up_r.get('code', 0) != 0:
            print(f"⚠ Feishu image upload error: {up_r.get('msg')}")
            return False
        image_key = up_r.get('data', {}).get('image_key')
        if not image_key:
            print(f"⚠ No image_key in Feishu response: {up_r}")
            return False
    except Exception as e:
        print(f"⚠ Feishu image upload failed: {e}")
        return False

    # 3. Send image message
    try:
        id_type = 'chat_id' if target.startswith('oc_') else 'open_id'
        send_data = json.dumps({
            'receive_id': target, 'msg_type': 'image',
            'content': json.dumps({'image_key': image_key})
        }).encode()
        send_url = f'{base}/im/v1/messages?receive_id_type={id_type}'
        send_req = urllib.request.Request(
            send_url, data=send_data, method='POST',
            headers={'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'})
        with urllib.request.urlopen(send_req, timeout=15) as resp:
            send_r = json.loads(resp.read())
        if send_r.get('code', 0) != 0:
            print(f"⚠ Feishu send error: {send_r.get('msg')}")
            return False
        print(f"📨 Image sent to Feishu ({target})")
        return True
    except Exception as e:
        print(f"⚠ Feishu send failed: {e}")
        return False


def generate_comparison(subject, design_type, styles, aspect_ratio="9:16", colors=""):
    """
    Generate 3-column comparison of different styles

    Args:
        subject: Subject matter
        design_type: Type of design
        styles: List of 3 style names
        aspect_ratio: Aspect ratio
        colors: Optional color hint

    Returns:
        Path to comparison image
    """
    print(f"\n{'='*80}")
    print(f"🎨 GENERATING 3-STYLE COMPARISON")
    print(f"{'='*80}\n")

    images = []
    labels = []

    for i, style in enumerate(styles, 1):
        print(f"\n[{i}/3] Generating {style} style...")
        prompt = generate_prompt(subject, design_type, style, color_hint=colors, aspect_ratio=aspect_ratio)

        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        default_dir = os.getenv('MONDO_OUTPUT_DIR', os.path.expanduser("~/乔木新知识库/60-69 素材/61 AI图片/mondo-designs"))
        os.makedirs(default_dir, exist_ok=True)
        temp_path = f"{default_dir}/temp-{style}-{timestamp}.png"

        result = generate_image(prompt, temp_path, aspect_ratio=aspect_ratio)
        if result:
            images.append(result)
            labels.append(style)
        else:
            print(f"⚠ Failed to generate {style}, skipping")

    if len(images) < 2:
        print("❌ Not enough images generated for comparison")
        return None

    # Create side-by-side comparison
    try:
        pil_images = [Image.open(img) for img in images]

        # Resize to same height
        target_height = min(img.height for img in pil_images)
        pil_images = [img.resize((int(img.width * target_height / img.height), target_height))
                     for img in pil_images]

        # Create comparison canvas
        total_width = sum(img.width for img in pil_images) + (len(pil_images) - 1) * 20  # 20px spacing
        comparison = Image.new('RGB', (total_width, target_height + 50), 'white')
        draw = ImageDraw.Draw(comparison)

        # Paste images side by side
        x_offset = 0
        for i, (img, label) in enumerate(zip(pil_images, labels)):
            comparison.paste(img, (x_offset, 0))

            # Add label
            label_text = label.upper().replace('-', ' ')
            bbox = draw.textbbox((0, 0), label_text)
            text_width = bbox[2] - bbox[0]
            text_x = x_offset + (img.width - text_width) // 2
            draw.text((text_x, target_height + 15), label_text, fill='black')

            x_offset += img.width + 20

        # Save comparison
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        comparison_path = f"outputs/comparison-{timestamp}.png"
        comparison.save(comparison_path)

        # Clean up temp files
        for img_path in images:
            try:
                os.remove(img_path)
            except:
                pass

        print(f"\n✅ Comparison saved to {comparison_path}")
        return comparison_path

    except Exception as e:
        print(f"❌ Error creating comparison: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Enhanced Mondo Style Design Generator with comparison mode and 37 artist styles',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
🎨 37 Artist Styles Available:
  Poster:  saul-bass, olly-moss, tyler-stout, martin-ansin, toulouse-lautrec, alphonse-mucha,
           jules-cheret, cassandre, milton-glaser, drew-struzan, kilian-eng, laurent-durieux,
           jay-ryan, dan-mccarthy, jock, shepard-fairey, steinlen, josef-muller-brockmann,
           paul-rand, paula-scher
  Book:    chip-kidd, peter-mendelsund, coralie-bickford-smith, david-pearson, wang-zhi-hong, jan-tschichold
  Album:   reid-miles, david-stone-martin, peter-saville
  Chinese: wenyi, guochao, rixi, hanxi
  Generic: minimal, atmospheric, negative-space

Examples:
  # 3-style comparison
  python3 generate_mondo_enhanced.py "Dune" movie --compare saul-bass,olly-moss,kilian-eng

  # Image-to-image transformation
  python3 generate_mondo_enhanced.py "noir thriller" movie --input poster.jpg --style saul-bass

  # With color preferences
  python3 generate_mondo_enhanced.py "Jazz Festival" event --style jules-cheret --colors "vibrant yellow, deep blue, red"

  # Specific artist style
  python3 generate_mondo_enhanced.py "Akira" movie --style kilian-eng
        """
    )

    parser.add_argument('subject', help='Subject matter (e.g., "Blade Runner", "1984 novel")')
    parser.add_argument('type', choices=['movie', 'book', 'album', 'event'],
                       help='Type of design to create')
    parser.add_argument('--style', choices=list(ARTIST_STYLES.keys()), default='auto',
                       help='Artist style (default: auto)')
    parser.add_argument('--compare', type=str,
                       help='Generate 3-style comparison (comma-separated, e.g., "saul-bass,olly-moss,jock")')
    parser.add_argument('--input', type=str,
                       help='Input image for image-to-image transformation')
    parser.add_argument('--colors', type=str, default='',
                       help='Color preferences (e.g., "orange, teal, black")')
    parser.add_argument('--aspect-ratio', '--ratio', dest='aspect_ratio', default='9:16',
                       help='Aspect ratio (default: 9:16)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--model', default=DEFAULT_IMAGE_MODEL, help='Model to use (pipellm only)')
    parser.add_argument('--provider', choices=['tuzi', 'pipellm', 'z-image', 'jimeng'], default='tuzi',
                       help='Image generation provider: tuzi (default, Gemini Flash), pipellm (Gemini Pro), z-image (通义万相), jimeng (即梦)')
    parser.add_argument('--no-generate', action='store_true',
                       help='Only show prompt without generating')
    parser.add_argument('--list-styles', action='store_true',
                       help='List all available artist styles')
    parser.add_argument('--feishu-to', type=str,
                       help='Send generated image to Feishu user (ou_xxx) or group (oc_xxx)')

    args = parser.parse_args()

    # List styles
    if args.list_styles:
        print("\n🎨 37 Artist Styles Available:\n")
        for style, desc in ARTIST_STYLES.items():
            print(f"  {style:25} → {desc}")
        print()
        return

    # Comparison mode
    if args.compare:
        styles = [s.strip() for s in args.compare.split(',')]
        if len(styles) != 3:
            print("❌ Comparison requires exactly 3 styles (e.g., --compare saul-bass,olly-moss,jock)")
            sys.exit(1)

        generate_comparison(args.subject, args.type, styles, args.aspect_ratio, args.colors)
        return

    # Single generation mode
    prompt = generate_prompt(args.subject, args.type, args.style, args.colors, args.aspect_ratio)

    print(f"\n{'='*80}")
    print("🎨 MONDO POSTER PROMPT")
    print(f"{'='*80}")
    print(f"{prompt}")
    print(f"{'='*80}\n")

    if not args.no_generate:
        output_path = generate_image(prompt, args.output, args.model, args.aspect_ratio, args.input, args.provider)
        if not output_path:
            sys.exit(1)
        # Auto-send to Feishu if --feishu-to is set
        feishu_to = getattr(args, 'feishu_to', None)
        if feishu_to and output_path:
            feishu_send_image(output_path, feishu_to)
    else:
        print("✓ Prompt generated. Use without --no-generate to create image.")

if __name__ == '__main__':
    main()
