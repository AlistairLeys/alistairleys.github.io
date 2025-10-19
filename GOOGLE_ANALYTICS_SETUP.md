# Google Analytics 4 Setup Instructions

## 🎯 Quick Setup (5 minutes)

### Step 1: Create GA4 Property
1. Go to [Google Analytics](https://analytics.google.com/)
2. Click **Admin** (gear icon, bottom left)
3. Click **Create Property**
4. Enter property details:
   - **Property name:** Alistair Leys Portfolio
   - **Reporting timezone:** Your timezone
   - **Currency:** Your currency
5. Click **Next** → Select industry and business size → Click **Create**

### Step 2: Get Your Measurement ID
1. In Admin → Property column → Click **Data Streams**
2. Click **Add stream** → Select **Web**
3. Enter:
   - **Website URL:** `https://alistairleys.github.io`
   - **Stream name:** Portfolio Website
4. Click **Create stream**
5. Copy your **Measurement ID** (format: `G-XXXXXXXXXX`)

### Step 3: Activate Tracking Code
1. Open `_layouts/default.html` in VS Code
2. Find the commented Google Analytics section (around line 10)
3. **Replace** `G-XXXXXXXXXX` with your actual Measurement ID in **both** places:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-YOUR-ID-HERE"></script>
   <script>
       window.dataLayer = window.dataLayer || [];
       function gtag(){dataLayer.push(arguments);}
       gtag('js', new Date());
       gtag('config', 'G-YOUR-ID-HERE');
   </script>
   ```
4. **Uncomment** the entire script block (remove `<!--` and `-->`)
5. Save, commit, and push to GitHub:
   ```bash
   git add _layouts/default.html
   git commit -m "Activate Google Analytics tracking"
   git push origin main
   ```

### Step 4: Verify It's Working
1. Visit your portfolio: https://alistairleys.github.io
2. Go back to Google Analytics
3. Click **Reports** → **Realtime**
4. You should see yourself as an active user! 🎉

---

## 📊 Useful Reports to Set Up

### Event Tracking (Optional)
Add custom events to track specific actions:
- Project views
- Button clicks
- Contact link clicks

### Goals to Configure
1. **Time on Page:** Track engagement (>2 minutes = engaged visitor)
2. **Project Views:** Track which projects get the most attention
3. **External Links:** Track LinkedIn/Email clicks

---

## 🔧 Troubleshooting

**Not seeing data?**
- Wait 24-48 hours for initial data collection
- Check that you uncommented the script block
- Verify your Measurement ID is correct
- Make sure you pushed changes to GitHub

**Want to test immediately?**
Use the [GA4 DebugView](https://support.google.com/analytics/answer/7201382):
1. Install [Google Analytics Debugger](https://chrome.google.com/webstore) Chrome extension
2. Enable it
3. Visit your site
4. Check Admin → DebugView in GA4

---

## 📈 Privacy & GDPR Compliance

Your site is currently **privacy-friendly** (no cookie consent needed in many jurisdictions) because:
- No personally identifiable information (PII) collected
- No third-party advertising cookies
- Anonymous traffic data only

**Optional:** Add a privacy policy page mentioning GA4 usage.

---

**Ready to activate?** Just follow Steps 1-3 above! 🚀
