---
title: "Shamir's Secret Sharing Explained: The Math Behind Crypto Inheritance"
slug: shamirs-secret-sharing-explained
description: Learn how Shamir's Secret Sharing algorithm works and why it's the perfect solution for cryptocurrency inheritance. No trust required - just math.
author: Max Comperatore
date: 2024-12-19
tags: shamir, cryptography, secret sharing, security
image: /static/blog/shamir-math.jpg
---

# Shamir's Secret Sharing Explained: The Math Behind Crypto Inheritance

**TL;DR:** Shamir's Secret Sharing lets you split a secret into pieces where you need K pieces to reconstruct it, but K-1 pieces reveal absolutely nothing. It's the mathematical foundation for trustless crypto inheritance.

## The Problem With Secrets

Let's say you have a Bitcoin seed phrase worth $1 million. You want to:
1. Ensure your family can access it if you die
2. Prevent any single person from stealing it while you're alive
3. Not trust any third party with the full secret

This seems impossible. If you split the seed phrase in half and give each half to different people, they could collude. If you give the full phrase to a lawyer, they could steal it.

## Enter Adi Shamir

In 1979, Israeli cryptographer **Adi Shamir** (the "S" in RSA encryption) invented a brilliant solution. His algorithm, called **Shamir's Secret Sharing**, solves this exact problem.

## How It Works (Simplified)

Imagine your secret is a single number: **42**.

### The Key Insight: Polynomials

A line (1st degree polynomial) is defined by 2 points. If I give you just one point, there are infinite lines that could pass through it. But give someone two points, and there's exactly one line.

Similarly:
- A parabola (2nd degree) needs 3 points
- A cubic (3rd degree) needs 4 points
- And so on...

### Creating Shares

For a **2-of-3** scheme (need any 2 shares to recover):

1. Your secret (42) becomes the y-intercept of a line
2. We generate a random slope (say, 5)
3. The line equation is: `y = 5x + 42`
4. We pick 3 points on this line:
   - Share 1: (1, 47)
   - Share 2: (2, 52)
   - Share 3: (3, 57)

### Recovering the Secret

Give me any two points, and I can solve for the line equation:
- Points (1, 47) and (2, 52)
- Slope = (52-47)/(2-1) = 5
- y-intercept = 47 - 5(1) = 42 ✓

But with just ONE point? There are infinite lines passing through (1, 47). The secret could be anything.

## Information-Theoretic Security

This is the beautiful part: **it's not just hard to crack with one share—it's mathematically impossible**.

Unlike password encryption that could theoretically be brute-forced with enough computing power, Shamir's scheme provides *information-theoretic security*. One share reveals literally zero information about the secret.

A quantum computer can't break it. A time-traveling alien can't break it. The math simply doesn't allow it.

## Why This Matters for Crypto

Your 24-word seed phrase can be converted to a number (or more precisely, a series of numbers). Shamir's algorithm can split this into N shares where any K shares reconstruct the original.

Common configurations:
- **2-of-3**: Good for inheritance (you, beneficiary, service)
- **3-of-5**: Good for business treasuries
- **2-of-2**: Simple backup (you have both, but stored separately)

## How Shardium Uses This

[Shardium](https://shardium.maxcomperatore.com) implements 2-of-3 Shamir sharing:

| Shard | Holder | Purpose |
|-------|--------|---------|
| A | You | Your master backup |
| B | Beneficiary | Recovery after death |
| C | Shardium | Released by dead man's switch |

**Key security properties:**
- Shardium only has Shard C (useless alone)
- Your beneficiary only has Shard B (useless alone)
- You can always recover with A + B
- Beneficiary recovers with B + C (after switch triggers)

## Implementation Details

Under the hood, we use [secrets.js-grempe](https://github.com/grempe/secrets.js), a well-audited JavaScript implementation of Shamir's scheme.

The splitting happens **entirely in your browser**:
1. You enter your seed phrase
2. JavaScript converts it to hexadecimal
3. Shamir's algorithm creates 3 shares
4. Only Shard C is sent to our server
5. Your original seed phrase is never transmitted

## Common Questions

### Can Shardium steal my crypto?
No. We only have Shard C. Without Shard A or B, it's mathematically useless.

### What if someone gets 2 shards?
They can recover the seed phrase. That's why you should:
- Keep Shard A very secure (safe, password manager)
- Only give Shard B to a trusted beneficiary
- The dead man's switch protects against premature release of Shard C

### Is this better than a multisig?
Different use cases. Multisig requires all signers to be available for each transaction. Shamir's is better for inheritance where you want one-time recovery after death.

## Try It Yourself

The math is beautiful, but you don't need to understand polynomials to use it. [Create your vault](https://shardium.maxcomperatore.com/app) in 5 minutes.

---

*Further reading: [Shamir, Adi. "How to share a secret." Communications of the ACM 22.11 (1979): 612-613.](https://dl.acm.org/doi/10.1145/359168.359176)*
