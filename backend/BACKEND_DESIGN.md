# Backend starter design

This starter supports lossless RGB/RGBA PNG, uncompressed 16-bit PCM WAV, and
UTF-8 text carriers. Every carrier accepts encrypted payload bytes and exposes
`capacity`, `embed`, and `extract` functions.

The application encrypts a UTF-8 message with AES-GCM before embedding it.
`app.crypto` embeds a project magic value, format version, random salt, and
random nonce in the encrypted payload. A passphrase is never stored.

Each carrier stores a four-byte payload length before the encrypted payload and
validates that length during extraction. This is an educational implementation;
the detection, upload validation, APIs, report generation, and web interface
remain future work.
