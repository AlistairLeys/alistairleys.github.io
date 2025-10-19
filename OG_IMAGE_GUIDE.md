# Open Graph Image Creation Guide

## 🎨 Quick Guide: Create Your Social Sharing Image

When someone shares your portfolio on LinkedIn, Twitter, or Facebook, this image appears as the preview. Make it count!

---

## 📐 Specifications

- **Dimensions:** 1200 x 630 pixels (required for best display)
- **Format:** PNG or JPG
- **File size:** Under 1MB (smaller = faster loading)
- **Safe zone:** Keep important content within 1200 x 600px (Facebook crops top/bottom slightly)

---

## 🎨 Design Recommendations

### Option 1: Simple Text-Based (Easiest)
**Tools:** Canva (free), Figma, or Photoshop

**Design Elements:**
```
┌─────────────────────────────────────┐
│                                     │
│    ALISTAIR LEYS                    │ <- Large, bold text
│    Data Scientist                   │ <- Subtitle
│                                     │
│    • Machine Learning               │
│    • Healthcare Analytics           │ <- Key skills (3-4 bullets)
│    • Statistical Modeling           │
│                                     │
│    alistairleys.github.io          │ <- Website URL
│                                     │
└─────────────────────────────────────┘
```

**Color Scheme:** Use your portfolio colors
- Background: `#0a0a0a` (dark)
- Text: `#ffffff` (white)
- Accent: `#00d4ff` (cyan/blue gradient)

### Option 2: Data Visualization Showcase (Advanced)
Include a small version of your best visualization:
- Diabetes risk stratification chart
- Cyclistic usage heatmap
- Add overlay text with your name and title

### Option 3: Professional Photo + Text (Personal)
- Professional headshot (if you have one)
- Name and title
- Key achievement metrics (e.g., "56% Variance Explained | 442 Patient Analysis")

---

## 🛠️ Quick Creation Methods

### Method 1: Canva (Recommended - No Design Skills Needed)
1. Go to [Canva.com](https://www.canva.com/)
2. Create account (free)
3. Search for **"Open Graph Image"** or **"Twitter Header"** template
4. Customize with your information
5. Download as PNG (1200x630px)

### Method 2: Figma (For Designers)
1. Create 1200x630px frame
2. Design using your portfolio's color scheme
3. Export as PNG (2x resolution recommended)

### Method 3: Simple Online Tool
- [OG Image Generator](https://og-image-generator.vercel.app/) - Quick text-based generator
- [Bannerbear](https://www.bannerbear.com/demos/open-graph-image-generator/) - Free template

### Method 4: AI-Assisted (Quick!)
Use ChatGPT with DALL-E or Midjourney:
```
"Create a professional Open Graph image for a data scientist portfolio.
Dark background (#0a0a0a), cyan accent color (#00d4ff).
Text: 'Alistair Leys - Data Scientist'
Include abstract data visualization elements.
1200x630px, modern minimal design."
```

---

## 💾 Save & Deploy

### Step 1: Save Your Image
- **Filename:** `og-image.png`
- **Location:** `assets/img/og-image.png`

### Step 2: Add to Repository
```bash
# Create directory if it doesn't exist
mkdir -p assets/img

# Add your image
# (Copy og-image.png to assets/img/)

git add assets/img/og-image.png
git commit -m "Add Open Graph social sharing image"
git push origin main
```

### Step 3: Verify It Works
Use these tools to test:
1. **LinkedIn Post Inspector:** https://www.linkedin.com/post-inspector/
   - Enter: `https://alistairleys.github.io`
   - Click **Inspect**
   - See your image preview!

2. **Twitter Card Validator:** https://cards-dev.twitter.com/validator
   - Enter your URL
   - Preview how it looks on Twitter

3. **Facebook Sharing Debugger:** https://developers.facebook.com/tools/debug/
   - Enter your URL
   - Click **Debug**
   - See Facebook preview

**Note:** It may take 1-2 hours for social platforms to pick up the new image. You can use the validators to force a refresh.

---

## ✨ Pro Tips

1. **Keep text large:** Aim for 50-60pt minimum for main headline
2. **High contrast:** Ensure text is easily readable at small sizes
3. **Test at multiple sizes:** It'll be viewed on desktop, mobile, and tablets
4. **Brand consistency:** Use colors from your portfolio
5. **No text cutoff:** Keep important content 50px from edges

---

## 🎯 Current Setup

Your meta tags are already configured in `_layouts/default.html`:
```html
<meta property="og:image" content="https://alistairleys.github.io/assets/img/og-image.png">
```

Once you add the image file, it will automatically work! 🚀

---

## 📸 Example Text for Your Image

### Option A: Skills-Focused
```
ALISTAIR LEYS
Business-Focused Data Scientist

✓ Machine Learning & Predictive Modeling
✓ Healthcare Analytics (R² = 0.56)
✓ Statistical Analysis & A/B Testing
✓ Python • SQL • scikit-learn

alistairleys.github.io
```

### Option B: Project-Focused
```
ALISTAIR LEYS
Data Science Portfolio

🏥 Diabetes Progression Analysis
   442 Patients | 56% Variance Explained

🚴 Bike-Share User Behavior
   499K Trips | $4.3M Revenue Potential

View Projects →
```

### Option C: Minimalist
```
ALISTAIR LEYS

Data Scientist
Turning Data Into Decisions

View Portfolio →
alistairleys.github.io
```

---

**Ready to create?** Pick a method above and create your image in under 10 minutes! 🎨
