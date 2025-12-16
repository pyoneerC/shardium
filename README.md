<p align="center">
  <img src="app/static/banner.jpg" alt="Shardium Banner" width="100%">
</p>

# Shardium

### 🔐 Trustless dead man's switch for crypto inheritance using Shamir's Secret Sharing

## The "Trustless Dead Man's Switch"

Shardium is a SaaS concept that uses **Shamir's Secret Sharing** to split a crypto seed phrase into 3 shards. It ensures that no single entity (including the server) has the full key, solving the "Trust Paradox."

### Architecture

1.  **Client-Side Split**: User enters seed in browser. JS splits it into 3 shards (A, B, C).
2.  **Shard Distribution**:
    *   **Shard A**: User keeps (Master Backup).
    *   **Shard B**: User gives to Beneficiary (Printed/PDF).
    *   **Shard C**: Sent to Server.
3.  **Heartbeat**: Server emails user every 30 days. If user misses 3 checks (90 days), Shard C is emailed to Beneficiary.
4.  **Recovery**: Beneficiary combines Shard B (held physically) + Shard C (emailed) to reconstruct seed.

### Tech Stack

*   **Backend**: FastAPI, SQLite, SQLAlchemy
*   **Frontend**: HTML, TailwindCSS, HTMX
*   **Cryptography**: `secrets.js` (Shamir's Secret Sharing) running in browser.

### How to Run

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the server:
    ```bash
    python -m uvicorn app.main:app --reload --port 8000
    ```

3.  Visit `http://localhost:8000`

### Security Note

This is an MVP/Proof of Concept. In a real production environment:
*   Use HTTPS.
*   Audit the `secrets.js` library.
*   Ensure the database is secure.
*   Use a real email provider (SendGrid/AWS SES) instead of the mock logger.
