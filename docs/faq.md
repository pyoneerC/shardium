# FAQ - Frequently Asked Questions

## General

### What is deadhand?

deadhand is a trustless dead man's switch for crypto inheritance. It splits your seed phrase into 3 shards using Shamir's Secret Sharing, ensuring no single party can access your funds.

### Is this safe?

Yes. deadhand uses Shamir's Secret Sharing, which provides **information-theoretic security**. This means:
- 1 shard reveals zero information about your secret
- No amount of computing power can change this
- It's mathematically proven, not just "hard to break"

### Do you ever see my seed phrase?

**No.** Your seed phrase is split entirely in your browser using JavaScript. We only receive Shard C, which is useless on its own.

### What if deadhand gets hacked?

Attackers would only get Shard C values. Without Shard B (which beneficiaries hold physically), they cannot recover any seed phrases.

### What if deadhand shuts down?

If we shut down:
1. You still have Shard A
2. Your beneficiary still has Shard B
3. A + B = full recovery

You don't need us to recover your funds.

---

## Using deadhand

### How often will I receive emails?

Every **30 days**. Just click the link to confirm you're alive.

### What if I'm on vacation?

You have 90 days (3 missed checks) before the switch triggers. Most vacations are shorter than this. If you'll be away longer, click the heartbeat link before you go.

### Can I change my beneficiary?

Currently, you would need to create a new vault. Beneficiary changes are on our roadmap.

### What if my beneficiary dies first?

You should create a new vault with a new beneficiary. Consider having multiple vaults for multiple beneficiaries.

### Can I have multiple beneficiaries?

Currently, one beneficiary per vault. For multiple heirs, create multiple vaults with different portions of your holdings.

---

## Recovery

### How does my beneficiary recover the funds?

1. They receive Shard C via email (when switch triggers)
2. They already have Shard B (the printed PDF you gave them)
3. They visit the deadhand recovery page
4. They enter both shards
5. Original seed phrase is displayed
6. They import it into a wallet

### What if my beneficiary loses Shard B?

This is critical. Without Shard B, they cannot recover even with Shard C. Recommend they:
- Store the printed PDF in a safe
- Make multiple copies
- Store in a bank safety deposit box

### Can I recover my own funds?

Yes! You have Shard A. Combine with:
- Shard B (get it from your beneficiary)

**Note**: Shard C is never released manually. If you lose Shard B while you are alive, we recommend you immediately create a new vault and move your funds to a new seed phrase. If you have lost your seed phrase and Shard B, you must wait for the 90-day switch to trigger.

---

## Security Policy

### Can the team "break" my switch if I lose a shard?

**Never.** The protocol is autonomous. There are zero manual overrides. If you lose a shard, you must wait for the 90-day inactivity trigger. No exceptions. This prevents social engineering and ensures that not even a compromised admin can release your data prematurely.

## Technical

### What cryptographic library do you use?

We use `secrets.js-grempe`, a well-maintained JavaScript implementation of Shamir's Secret Sharing.

### Is the code open source?

Yes! Check our GitHub repository. You can audit the code yourself.

### Can I self-host?

Absolutely. Clone the repo and run your own instance. See the self-hosting documentation.

### What's the threshold scheme?

We use **2-of-3**: 3 shards created, any 2 can recover the secret.

---

## Privacy & Legal

### What data do you store?

- Your email (for heartbeat notifications)
- Beneficiary email (for Shard C delivery)
- Shard C (encrypted)
- Last heartbeat timestamp

We do NOT store:
- Your seed phrase
- Shards A or B
- Wallet addresses
- Any financial information

### Do you comply with GDPR?

Yes. You can request deletion of all your data at any time.

### What happens to my data if I cancel?

All data is deleted within 30 days of cancellation.
