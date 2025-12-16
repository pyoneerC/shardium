# Getting Started

## What is Shardium?

Shardium is a trustless dead man's switch for crypto inheritance. It uses **Shamir's Secret Sharing** to split your seed phrase into 3 shards, ensuring no single party can access your funds.

## Prerequisites

- A crypto wallet seed phrase (12 or 24 words)
- An email address for heartbeat notifications
- A beneficiary's email address

## Quick Start (5 minutes)

### Step 1: Enter Your Seed Phrase

1. Visit the Shardium app
2. **Disconnect from the internet** (for maximum security)
3. Enter your 12 or 24 word seed phrase
4. Click "Encrypt & Split Key"

### Step 2: Save Your Shards

After splitting, you'll receive 3 shards:

| Shard | Who Keeps It | Purpose |
|-------|--------------|---------|
| **Shard A** | You | Master backup - store in password manager or safe |
| **Shard B** | Beneficiary | Give to your heir (printed PDF recommended) |
| **Shard C** | Shardium Server | Released to beneficiary when switch triggers |

### Step 3: Activate the Switch

1. Enter your email address
2. Enter your beneficiary's email
3. Click "Activate Shardium"

That's it! You'll receive heartbeat emails every 30 days.

## What Happens Next?

- **Every 30 days**: You receive an email asking "Are you alive?"
- **If you respond**: Timer resets, nothing happens
- **If you miss 3 checks (90 days)**: Shard C is emailed to your beneficiary
- **Beneficiary combines B + C**: They can recover your seed phrase

## Security Tips

1. ✅ Split your seed phrase while **offline**
2. ✅ Store Shard A in **multiple secure locations**
3. ✅ Give Shard B to beneficiary in **physical form** (printed)
4. ✅ Use a **dedicated email** for heartbeat notifications
5. ❌ Never store your full seed phrase digitally
