# Vercel Web Analytics Setup Guide

This guide will help you get started with using Vercel Web Analytics on the Deadhand project, showing you how to enable it, deploy your app to Vercel, and view your data in the dashboard.

## Prerequisites

- A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
- A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
- The Vercel CLI installed. If you don't have it, you can install it using the following command:

```bash
# Using npm
npm i vercel

# Using yarn
yarn add vercel

# Using pnpm
pnpm add vercel

# Using bun
bun add vercel
```

## Setup Instructions

### Step 1: Enable Web Analytics in Vercel

1. Go to your [Vercel dashboard](/dashboard)
2. Select your Deadhand project
3. Click the **Analytics** tab
4. Click **Enable** from the dialog

> **💡 Note:** Enabling Web Analytics will add new routes (scoped at `/_vercel/insights/*`) after your next deployment.

### Step 2: Configure Analytics in Your Templates

For this FastAPI project using Jinja2 templates, the analytics script should be added to your base template or main layout file. 

#### Option A: Add to Base Template (Recommended)

If you're using a base template that extends to other pages, add the analytics script to `app/templates/base.html`:

```html
</head>
<body>
    <!-- Your content here -->
    
    <!-- Vercel Web Analytics -->
    <script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
```

#### Option B: Add to Individual Templates

Add the script to each template file where you want to track analytics:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Deadhand</title>
</head>
<body>
    <!-- Your content here -->
    
    <!-- Vercel Web Analytics -->
    <script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
```

### Step 3: Custom Events (Optional)

To track custom events like button clicks or form submissions, you can use the `window.va` function:

```html
<button onclick="window.va && window.va('event', 'button-click')">
    Click Me
</button>
```

Or in JavaScript:

```javascript
// Track a custom event
if (window.va) {
    window.va('event', 'vault-created', { category: 'engagement' });
}
```

### Step 4: Deploy Your App to Vercel

Deploy your app using the Vercel CLI:

```bash
vercel deploy
```

Or, if you've connected your Git repository:

```bash
git push origin main
```

This will trigger an automatic deployment to Vercel, which will enable the analytics routes.

Once your app is deployed, it will start tracking visitors and page views.

> **💡 Note:** If everything is set up properly, you should be able to see a Fetch/XHR request in your browser's Network tab from `/_vercel/insights/script.js` and `/_vercel/insights/view` when you visit any page.

### Step 5: View Your Data in the Dashboard

Once your app is deployed and users have visited your site:

1. Go to your [Vercel dashboard](/dashboard)
2. Select your Deadhand project
3. Click the **Analytics** tab

After a few days of visitor traffic, you'll be able to start exploring your data by viewing and filtering the analytics panels.

**Pro and Enterprise plans** can also add custom events to track user interactions such as:
- Vault creation
- Seed phrase encryption
- Shard distribution
- Recovery attempts
- Heartbeat check-ins

## Environment Configuration

The Deadhand `vercel.json` file is already configured for Vercel deployment. It includes the necessary settings for Python/FastAPI hosting:

```json
{
    "version": 2,
    "builds": [
        {
            "src": "app/main.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "/app/main.py"
        }
    ]
}
```

## Vercel Speed Insights (Optional)

For additional performance monitoring, you can also enable Vercel Speed Insights:

```html
<script defer src="/_vercel/speed-insights/script.js"></script>
```

This will track Core Web Vitals and other performance metrics.

## Troubleshooting

### Analytics Script Not Loading

If the analytics script isn't loading:

1. Check that you're accessing the site through `https://your-domain.vercel.app`
2. Verify that Analytics is enabled in your Vercel project settings
3. Check browser console for any CORS errors
4. Clear browser cache and reload the page

### No Data Showing in Dashboard

- Wait 24-48 hours for initial data to appear
- Ensure the analytics script is present in your deployed version
- Check that traffic is actually reaching your site

### Custom Events Not Recording

- Verify that `window.va` is defined before calling it
- Check that the event name is a valid string
- Use your browser's console to debug: `console.log(window.va)`

## Best Practices

1. **Use Meaningful Event Names**: Choose descriptive names for custom events
   - ✅ Good: `vault-created`, `seed-encrypted`, `recovery-successful`
   - ❌ Bad: `click`, `event1`, `data`

2. **Track Key User Actions**: Focus on events that matter to your business
   - Vault creation flow completion
   - Shard distribution
   - Recovery success/failure rates
   - Heartbeat check-in responses

3. **Respect User Privacy**: Only track events necessary for understanding user behavior
   - Don't track sensitive data like seed phrases or personal information
   - Follow Vercel's [privacy policy](https://vercel.com/legal/privacy-policy)

4. **Monitor Performance**: Use Speed Insights alongside Web Analytics
   - Track how analytics implementation affects page load times
   - Optimize if needed

## Learn More

For more detailed information about Vercel Web Analytics:

- [Vercel Web Analytics Documentation](https://vercel.com/docs/analytics)
- [Vercel Speed Insights Documentation](https://vercel.com/docs/speed-insights)
- [Privacy and Compliance](https://vercel.com/legal/privacy-policy)

## Next Steps

Now that you have Vercel Web Analytics set up, you can:

1. Monitor user engagement on your site
2. Track vault creation rates and recovery success
3. Identify popular pages and features
4. Optimize user experience based on analytics data
5. Set up custom events for specific business metrics
