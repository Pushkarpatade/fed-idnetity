# FEDID - Federal Identity System

A decentralized identity verification platform using React.js, Node.js, Express, MongoDB, and Zero-Knowledge Proof (ZKP) simulation via Ethereum Smart Contracts.

## Project Structure
- **/frontend**: React + Vite application (Tailwind CSS)
- **/backend**: Node.js REST API + MongoDB
- **/contracts**: Solidity Smart Contract source code

## 1. Prerequisites
- Node.js (v18+)
- MongoDB (Running locally on default port `27017`)
- Ganache (Optional: For local blockchain testing via `HTTP://127.0.0.1:7545`)
- Remix IDE (For contract deployment)

## 2. Setup Database & Backend
1. Ensure MongoDB is running.
2. Navigate to `backend` directory.
3. Install dependencies:
   ```bash
   cd backend
   npm install
   ```
4. Configure `.env` (already provided):
   Make sure `MONGODB_URI` points to your DB. If using a deployed contract, update `CONTRACT_ADDRESS`.
5. Start the backend:
   ```bash
   node server.js
   # Server will run on http://localhost:5000
   ```

## 3. Setup Frontend
1. Open a new terminal. Navigate to `frontend`.
2. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   # App will run on http://localhost:5173
   ```

## 4. Smart Contract Deployment (Blockchain Simulation)
The system uses simulated ZKP by creating a hash of user details. If you want to connect to a real or local blockchain:
1. Open [Remix IDE](https://remix.ethereum.org/).
2. Create a file `FedIDIdentity.sol` from `contracts/FedIDIdentity.sol`.
3. Compile the contract using Solidity Compiler ^0.8.19.
4. Open Ganache. Note the RPC URL (e.g., `http://127.0.0.1:7545`).
5. In Remix, switch Environment to `Dev - Ganache Provider` or `Injected Provider` (MetaMask).
6. Deploy the `FedIDIdentity` contract.
7. Copy the Deployed Contract Address, paste it into `backend/.env` under `CONTRACT_ADDRESS`.
8. The backend will automatically switch from Simulation Mode to Blockchain Mode.

## 5. Demo Flow
1. **Register as Citizen**: Go to `http://localhost:5173/register` and select `Citizen`.
2. **Citizen Dashboard**: You'll see "Unregistered". Fill out the Identity form to generate a secure Hash payload.
3. **Register as Agency**: Open an Incognito window, go to `/register` and select `Agency`.
4. **Request Access**: The Agency searches for your Citizen username and clicks "Request".
5. **Approval**: Go back to the Citizen window. You will see a Pending Request. Click "Approve". 
6. **ZKP Result**: Go to the Agency window. The result updates to display the `ZKP Validated` badge and the Citizen's Trust Score—without any raw PII (Name/DOB/SSN) being transferred!
