---
title: "Dead Man's Switch: How to Automate Crypto Inheritance"
slug: dead-mans-switch-crypto-inheritance
description: A dead man's switch automatically triggers an action when you stop responding. Learn how this mechanism enables trustless cryptocurrency inheritance.
author: Max Comperatore
date: 2025-12-15
tags: dead mans switch, automation, inheritance, trustless
image: /static/blog/dead-mans-switch.jpg
---

# Dead Man's Switch: How to Automate Crypto Inheritance

**TL;DR:** A dead man's switch is a mechanism that triggers automatically when you stop responding. Combined with Shamir's Secret Sharing, it enables trustless crypto inheritance without giving anyone premature access.

## What Is a Dead Man's Switch?

The term comes from trains. Early locomotives had a pedal the driver had to keep pressed. If the driver had a heart attack, the pedal would release and automatically stop the train.

In the digital world, a dead man's switch is any system that requires periodic confirmation you're alive. If you stop confirming, it assumes something happened and takes action.

## Why Crypto Needs This

The challenge with crypto inheritance is **timing**:
- Too early: Someone could steal your funds while you're alive
- Too late: Your heirs can't find the keys
- Just right: Access transfers exactly when needed

A dead man's switch solves the timing problem automatically.

## How Shardium's Switch Works

### The Timeline

| Day | What Happens |
|-----|--------------|
| 0 | You create a vault and activate the switch |
| 1-29 | Nothing (you're presumably alive) |
| 30 | We send you an email: "Are you still there?" |
| 30-59 | If you click the link, timer resets to Day 0 |
| 60 | Final warning email |
| 90 | If no response, Shard C is sent to your beneficiary |

### Why 90 Days?

We chose 90 days as the default because:
- **Long enough** to handle vacations, hospital stays, or forgetting
- **Short enough** that heirs don't wait forever
- **Multiple reminders** prevent accidental triggers

Some users want shorter windows (30 days) or longer (180 days). We're working on customizable timers for pro users.

## The Trust Model

Here's what makes this trustless:

### What Shardium Has
- Your email address
- Your beneficiary's email
- Shard C (encrypted, useless alone)

### What Shardium Doesn't Have
- Your seed phrase
- Shard A (you keep it)
- Shard B (beneficiary keeps it)
- Any ability to access your funds

Even if we wanted to steal your crypto (we don't), we mathematically can't. Shard C alone reveals nothing.

## Security Considerations

### What if someone hacks Shardium?

They get a database of encrypted Shard C values. Without the corresponding Shard A or B, these are worthless. It's like having one piece of a two-piece puzzle—no picture emerges.

### What if the heartbeat email goes to spam?

We send from a verified domain with proper SPF/DKIM. We also send multiple reminders over 60 days. But we recommend:
1. Adding our email to your contacts
2. Checking your spam folder occasionally
3. Setting a calendar reminder to check in

### What if someone intercepts my heartbeat link?

The link contains a secure, random token. Even if intercepted, clicking it only resets YOUR timer. It doesn't give access to anything.

### What if I die and someone else clicks the link?

This is a risk. If a family member has access to your email and keeps clicking, the switch won't trigger. Solutions:
1. Don't share your email password, or...
2. Create a dedicated email just for Shardium
3. Inform your beneficiary about the 90-day window

## Alternative Approaches

### Google Inactive Account Manager
Google offers a similar feature for your Google account. After N months of inactivity, it can share your data with designated contacts. But it only works for Google services.

### Lawyers and Wills
Traditional estate planning can include crypto instructions. But lawyers can be expensive, slow, and don't understand crypto well.

### Metal Plates in a Safe
Some people stamp their seed phrase on metal and put it in a safe deposit box with instructions. Works, but requires your heirs to find and access the box.

### Multisig with Time Locks
Advanced users can set up Bitcoin transactions with time locks that activate after a certain block height. Very technical and error-prone.

## The Shardium Advantage

We combine the best of all approaches:

✅ **Automated**: No manual action needed when you die
✅ **Trustless**: We can't access your funds
✅ **Simple**: No technical knowledge required
✅ **Secure**: Shamir's math protects against theft
✅ **Reversible**: You can recover with A+B anytime

## Real-World Scenarios

### Scenario 1: You Die
- Day 0-30: Your family is grieving
- Day 30: Email sent (ignored)
- Day 60: Final warning (ignored)
- Day 90: Shard C sent to beneficiary
- Day 91: Beneficiary combines B+C, recovers seed, accesses funds

### Scenario 2: You're Hospitalized
- Day 30: Email sent to your hospital bed
- Day 45: You recover, click the link
- Timer resets, no drama

### Scenario 3: You Forget
- Day 30: Email sent (in spam)
- Day 60: Final warning (you notice!)
- Day 61: You click the link
- Timer resets, crisis averted

## Getting Started

Setting up your dead man's switch takes 5 minutes:

1. Go to [shardium.xyz](https://shardium.xyz)
2. Enter your seed phrase (client-side only)
3. Download/print Shard A and B
4. Enter your email and beneficiary's email
5. Activate the switch

**Cost**: $0 for the first 50 early bird users. We're in public beta and building trust, not just subscriptions.

---

*Questions? Check our [FAQ](/docs/faq) or [contact us](mailto:max.comperatore@gmail.com).*
