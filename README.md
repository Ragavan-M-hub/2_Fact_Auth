# 🔐 Password + OTP Authentication Script

This Python script implements a simple password authentication system with an OTP (One-Time Password) verification step via SMS using Twilio.

## 📋 Features

- Password-based access control
- Sends a randomly generated 5-digit OTP upon correct password entry
- Verifies OTP entered by the user
- Locks user out after 5 incorrect password attempts
- Uses Twilio API for sending OTP via SMS

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- [Twilio](https://www.twilio.com/) account and a verified phone number
- `twilio` Python package
