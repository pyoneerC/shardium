# How Shardium Works

## The Problem: The Trust Paradox

When you die, your crypto dies with you—unless you've shared your seed phrase. But sharing creates risk:

- **Share with family?** They might steal it
- **Use a lawyer?** They don't understand crypto
- **Use a service?** You're trusting them with everything

This is the **Trust Paradox**: You need to share access, but sharing access is dangerous.

## The Solution: Shamir's Secret Sharing

Shardium uses a cryptographic technique called **Shamir's Secret Sharing (SSS)**, invented by Adi Shamir in 1979.

### How SSS Works

Instead of storing your secret as a single piece of data, SSS splits it into multiple "shards" with a **threshold scheme**:

```
Secret → Split into N shards → Need K shards to recover (K ≤ N)
```

Shardium uses a **2-of-3** scheme:
- 3 shards are created
- Any 2 shards can recover the original
- 1 shard alone reveals **zero information**

### Mathematical Guarantee

This isn't just "hard to crack"—it's **information-theoretically secure**:

- With 1 shard, an attacker has infinite possible secrets
- No amount of computing power changes this
- It's not encryption that can be broken—it's math

## The Shardium Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR BROWSER                          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │ Seed Phrase │ -> │ Shamir SSS  │ -> │  3 Shards   │  │
│  │ (plaintext) │    │ (JavaScript)│    │  A, B, C    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         ↓                                    ↓          │
│   Never leaves                         Distributed      │
│   your browser                                          │
└─────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
         ┌─────────┐    ┌─────────┐    ┌─────────┐
         │ Shard A │    │ Shard B │    │ Shard C │
         │   YOU   │    │  HEIR   │    │ SERVER  │
         └─────────┘    └─────────┘    └─────────┘
```

## The Dead Man's Switch

### Heartbeat System

1. **Every 30 days**: Server sends you an email
2. **Click the link**: Confirms you're alive, resets timer
3. **Miss 3 checks**: Switch triggers after 90 days

### What Triggers Release?

```
Day 0    → Vault activated
Day 30   → Email #1 sent
Day 60   → Email #2 sent (if #1 missed)
Day 90   → Email #3 sent (if #2 missed)
Day 91+  → Shard C emailed to beneficiary
```

### Why 90 Days?

- Short enough to be useful
- Long enough to account for vacation, hospital, etc.
- Can be customized in future versions

## Recovery Process

When the switch triggers:

1. Beneficiary receives email with **Shard C**
2. They already have **Shard B** (the printed PDF)
3. They visit Shardium's recovery page
4. They enter both shards
5. Original seed phrase is reconstructed
6. They can now access the wallet

## Trust Model Summary

| Party | What They Have | Can They Steal? |
|-------|---------------|-----------------|
| You | Shard A | No (need 2 shards) |
| Beneficiary | Shard B | No (need 2 shards) |
| Shardium | Shard C | No (need 2 shards) |
| Hacker (server) | Shard C | No (need 2 shards) |
| You + Anyone | A + B or A + C | ✅ Yes (intended) |
| Beneficiary | B + C (after trigger) | ✅ Yes (intended) |

**The only way to recover is with 2 shards—exactly as designed.**
