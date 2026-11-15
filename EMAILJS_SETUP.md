# EmailJS Setup Guide for FedID

## Step 1: Create Free Account
1. Go to https://www.emailjs.com/
2. Sign up (free — 200 emails/month)

## Step 2: Add Email Service
1. Go to "Email Services" → "Add New Service"
2. Choose "Gmail" (or any provider)
3. Click "Connect Account" → authorize your Gmail
4. Note down the **Service ID** (e.g., `service_abc123`)

## Step 3: Create Email Template
1. Go to "Email Templates" → "Create New Template"
2. Set the template content:

**Subject:** `FedID Secure OTP: {{otp_code}}`

**Body:**
```
🛡️ FedID — National Identity Infrastructure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your One-Time Password (OTP) for secure authentication:

🔐 OTP CODE: {{otp_code}}

This code expires in 3 minutes.
Do not share this code with anyone.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sent to: {{to_email}}
Timestamp: {{timestamp}}
Request ID: {{request_id}}

⚠️ If you did not request this code, please ignore this email.

— FedID Security Division
   National Identity Infrastructure | Powered by ZKP + AES-256
```

3. Set "To Email" field to: `{{to_email}}`
4. Note down the **Template ID** (e.g., `template_xyz789`)

## Step 4: Get Public Key
1. Go to "Account" → "General"
2. Copy your **Public Key** (e.g., `user_abc123...`)

## Step 5: Update the code
Replace the placeholder values in `Login.jsx` and `IssueToken.jsx`:
- `YOUR_SERVICE_ID` → your Service ID
- `YOUR_TEMPLATE_ID` → your Template ID  
- `YOUR_PUBLIC_KEY` → your Public Key
